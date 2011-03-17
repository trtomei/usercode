// -*- C++ -*-
//
// Package:    PFJetConfigurableSelector
// Class:      PFJetConfigurableSelector
// 
/**\class PFJetConfigurableSelector PFJetConfigurableSelector.cc RSGraviton/PFJetConfigurableSelector/src/PFJetConfigurableSelector.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Thiago Tomei
//         Created:  Thu Mar  4 16:26:36 BRT 2010
// $Id: PFJetConfigurableSelector.cc,v 1.4 2010/12/23 16:14:24 tomei Exp $
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
#include "CommonTools/UtilAlgos/interface/StringCutObjectSelector.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"

//
// class declaration
//

class PFJetConfigurableSelector : public edm::EDFilter {
   public:
      explicit PFJetConfigurableSelector(const edm::ParameterSet&);
      ~PFJetConfigurableSelector();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
  edm::InputTag src_;
  std::string theCut_;
  int minNumber_;
  char buffer[1024];
  typedef StringCutObjectSelector<reco::PFJet> JetStringFilterFunctor;
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
PFJetConfigurableSelector::PFJetConfigurableSelector(const edm::ParameterSet& iConfig) :
  src_(iConfig.getParameter<edm::InputTag>("src")),
  theCut_(iConfig.getParameter<std::string>("theCut")),
  minNumber_(iConfig.getParameter<int>("minNumber"))
{
  produces<reco::PFJetCollection>();
  strcpy(buffer,theCut_.c_str());
}


PFJetConfigurableSelector::~PFJetConfigurableSelector()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
PFJetConfigurableSelector::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<reco::PFJetCollection> jetsHandle;
  iEvent.getByLabel(src_,jetsHandle);

  std::auto_ptr<reco::PFJetCollection> passingJets(new reco::PFJetCollection);
  const int size = jetsHandle->size();
  passingJets->reserve( size );

  JetStringFilterFunctor theFilter(buffer);

  for(reco::PFJetCollection::const_iterator ijet = jetsHandle->begin();
      ijet != jetsHandle->end();
      ++ijet)  {    

    bool pass = theFilter(*ijet);
    if(pass) {
      reco::PFJet jetClone = *(ijet->clone());
      passingJets->push_back(jetClone);
    }

  }

  bool minimumAchieved = false;

  // If minNumber = -1, the conditions for minimumAchieved are that ALL jets must pass...
  if(minNumber_ > 0)
    minimumAchieved = ( passingJets->size() >= size_t(minNumber_));
  else if(minNumber_ < 0)
    minimumAchieved = ( passingJets->size() == size_t(minNumber_));
  
  iEvent.put(passingJets);

  return minimumAchieved;
}

// ------------ method called once each job just before starting event loop  ------------
void 
PFJetConfigurableSelector::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PFJetConfigurableSelector::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(PFJetConfigurableSelector);
