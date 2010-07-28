// -*- C++ -*-
//
// Package:    RSJetAnalyzerV2
// Class:      RSJetAnalyzerV2
// 
/**\class RSJetIdSelector RSJetIdSelector.cc RSGraviton/RSJetIdSelector/src/RSJetIdSelector.cc

Description: Class to select jets based on JetID in RS->jets events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSJetIdSelector.cc,v 1.1 2010/06/09 13:52:52 tomei Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/JetReco/interface/JetID.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
//
// class decleration
//

class RSJetIdSelector : public edm::EDProducer {
public:
  explicit RSJetIdSelector(const edm::ParameterSet&);
  ~RSJetIdSelector();

private:
  virtual void beginJob();
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag jets_;
  edm::InputTag jetID_;
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
RSJetIdSelector::RSJetIdSelector(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets") ),
  jetID_(iConfig.getParameter<edm::InputTag>("jetID") )
{
  //now do what ever initialization is needed
  produces<reco::CaloJetCollection>();
  edm::Service<TFileService> fs;
}


RSJetIdSelector::~RSJetIdSelector()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSJetIdSelector::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  // jet ID handle
  edm::Handle<reco::JetIDValueMap> hJetIDMap;
  iEvent.getByLabel(jetID_, hJetIDMap );

  // jets
  edm::Handle<edm::View< reco::CaloJet > > hJets;
  iEvent.getByLabel(jets_, hJets );
  
  // Implementing loose cuts.
  //* EMF > 0.01 if |eta| < 2.6
  //* n90hits > 1
  //* fHPD < 0.98 
  
  unsigned int idx;
  std::vector<unsigned int> passingIdx;
  std::auto_ptr<reco::CaloJetCollection> passingJets( new reco::CaloJetCollection );
  const int size = hJets->size();
  passingJets->reserve( size );

  for ( edm::View<reco::CaloJet>::const_iterator ibegin = hJets->begin(),
	  iend = hJets->end(), ijet = ibegin;
	ijet != iend; ++ijet ) {

    idx = ijet - ibegin;
    edm::RefToBase<reco::CaloJet> jetRef = hJets->refAt(idx);
    reco::JetID theJetId = (*hJetIDMap)[ jetRef ];
    reco::CaloJet theNewJet = (*jetRef);

    bool emfCut = false;
    bool n90HitsCut = false;
    bool fHPDCut = false;
    if(std::abs(jetRef->eta()) < 2.6 && jetRef->emEnergyFraction() > 0.01)
      emfCut = true;
    if(std::abs(jetRef->eta()) > 2.6)
      emfCut = true;
    if(theJetId.n90Hits > 1)
      n90HitsCut = true;
    if(theJetId.fHPD < 0.98)
      fHPDCut = true;

    if(emfCut && n90HitsCut && fHPDCut) {
      passingIdx.push_back(idx); 
      passingJets->push_back(theNewJet);
    }
  }

  iEvent.put(passingJets);
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSJetIdSelector::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSJetIdSelector::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSJetIdSelector);
