// -*- C++ -*-
//
// Package:    JetConfigurableSelector
// Class:      JetConfigurableSelector
// 
/**\class JetConfigurableSelector JetConfigurableSelector.cc RSGraviton/JetConfigurableSelector/src/JetConfigurableSelector.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Thiago Tomei
//         Created:  Thu Mar  4 16:26:36 BRT 2010
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
//#include "RSGraviton/RSAnalyzer/interface/JetConfigurableSelectionFunctor.h"
#include "PhysicsTools/UtilAlgos/interface/StringCutObjectSelector.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"

//
// class declaration
//

class JetConfigurableSelector : public edm::EDFilter {
   public:
      explicit JetConfigurableSelector(const edm::ParameterSet&);
      ~JetConfigurableSelector();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
  edm::InputTag src_;
  double ptMin_;
  double etaMax_;
  double emfMin_;
  double massMin_;
  int minNumber_;
  typedef StringCutObjectSelector<reco::CaloJet> JetStringFilterFunctor;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
JetConfigurableSelector::JetConfigurableSelector(const edm::ParameterSet& iConfig) :
  src_(iConfig.getParameter<edm::InputTag>("src")),
  ptMin_(iConfig.getParameter<double>("ptMin")),
  etaMax_(iConfig.getParameter<double>("etaMax")),
  emfMin_(iConfig.getParameter<double>("emfMin")),
  massMin_(iConfig.getParameter<double>("massMin")),
  minNumber_(iConfig.getParameter<int>("minNumber"))
{
  produces<reco::CaloJetCollection>();
}


JetConfigurableSelector::~JetConfigurableSelector()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
JetConfigurableSelector::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<reco::CaloJetCollection> jetsHandle;
  iEvent.getByLabel(src_,jetsHandle);

  std::auto_ptr<reco::CaloJetCollection> passingJets(new reco::CaloJetCollection);
  const int size = jetsHandle->size();
  passingJets->reserve( size );

  //  JetConfigurableSelectionFunctor jetCut(ptMin_, etaMax_, emfMin_, massMin_);  
  char buffer[64];
  sprintf(buffer,"abs(eta) < %4.1f | emEnergyFraction > %4.2f",etaMax_,emfMin_);
  JetStringFilterFunctor theFilter(buffer);

  for(reco::CaloJetCollection::const_iterator ijet = jetsHandle->begin();
      ijet != jetsHandle->end();
      ++ijet)  {    

    bool pass = theFilter(*ijet);
    if(pass) {
      reco::CaloJet jetClone = *(ijet->clone());
      passingJets->push_back(jetClone);
    }

  }

  bool minimumAchieved = false;
  minimumAchieved = ( passingJets->size() >= size_t(minNumber_));

  iEvent.put(passingJets);

  return minimumAchieved;
}

// ------------ method called once each job just before starting event loop  ------------
void 
JetConfigurableSelector::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetConfigurableSelector::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetConfigurableSelector);
