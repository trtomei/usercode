// -*- C++ -*-
//
// Package:    RSJetAnalyzerV2
// Class:      RSJetAnalyzerV2
// 
/**\class RSJetIdAnalyzer RSJetIdAnalyzer.cc RSGraviton/RSJetIdAnalyzer/src/RSJetIdAnalyzer.cc

Description: Class to select jets based on JetID in RS->jets events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSJetIdAnalyzer.cc,v 1.3 2010/12/23 16:14:24 tomei Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/JetReco/interface/JetID.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "JetMETCorrections/Objects/interface/JetCorrector.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
//
// class decleration
//

class RSJetIdAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSJetIdAnalyzer(const edm::ParameterSet&);
  ~RSJetIdAnalyzer();

private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag jet_;
  edm::InputTag jetID_;
  edm::InputTag originalJets_;
  TH1F* h_fHPD;
  TH1F* h_fRBX;
  TH1F* h_n90;
  TH1F* h_nECAL;
  TH1F* h_nHCAL;
  TH1F* h_fEB;
  TH1F* h_fEE;
  TH1F* h_fHB;
  TH1F* h_fHE;
  TH1F* h_fHO;
  TH1F* h_fLong;
  TH1F* h_fShort;
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
RSJetIdAnalyzer::RSJetIdAnalyzer(const edm::ParameterSet& iConfig) :
  jet_(iConfig.getParameter<edm::InputTag>("jet") ),
  jetID_(iConfig.getParameter<edm::InputTag>("jetID") ),
  originalJets_(iConfig.getParameter<edm::InputTag>("originalJets") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_fHPD = fs->make<TH1F>("h_fHPD","h_fHPD",50,0.0,1.0);
  h_fRBX = fs->make<TH1F>("h_fRBX","h_fRBX",50,0.0,1.0);
  h_n90 = fs->make<TH1F>("h_n90","h_n90",100,-0.5,99.5);
  h_nECAL = fs->make<TH1F>("h_nECAL","h_nECAL",100,-0.5,99.5);
  h_nHCAL = fs->make<TH1F>("h_nHCAL","h_nHCAL",100,-0.5,99.5);
  h_fEB = fs->make<TH1F>("h_fEB","h_fEB",50,0.0,1.0);
  h_fEE = fs->make<TH1F>("h_fEE","h_fEE",50,0.0,1.0);
  h_fHB = fs->make<TH1F>("h_fHB","h_fHB",50,0.0,1.0);
  h_fHE = fs->make<TH1F>("h_fHE","h_fHE",50,0.0,1.0);
  h_fHO = fs->make<TH1F>("h_fHO","h_fHO",50,0.0,1.0);
  h_fLong = fs->make<TH1F>("h_fLong","h_fLong",50,0.0,1.0);
  h_fShort = fs->make<TH1F>("h_fShort","h_fShort",50,0.0,1.0);
}


RSJetIdAnalyzer::~RSJetIdAnalyzer()
{
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSJetIdAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  // jet ID handle
  edm::Handle<reco::JetIDValueMap> hJetIDMap;
  iEvent.getByLabel(jetID_, hJetIDMap );

  // original jets
  edm::Handle<edm::View< reco::CaloJet > > hJet;
  iEvent.getByLabel(jet_, hJet );
  // selected jets
  edm::Handle<edm::View< reco::CaloJet > > hOriginalJets;
  iEvent.getByLabel(originalJets_, hOriginalJets );
  
  edm::RefToBase<reco::CaloJet> jetRef = hJet->refAt(0);
  std::cout << "Found our jet" << std::endl;
  const reco::CaloJet* theJet = jetRef.get();
  std::cout << "Has eta, phi = " << theJet->eta() << ", "
	    << theJet->phi() << std::endl;

  // Ugly deltaR matching
  double bestDeltaR = 9999.9;
  unsigned int matchingIDX = 999;

  for ( edm::View<reco::CaloJet>::const_iterator ibegin = hOriginalJets->begin(),
	  iend = hOriginalJets->end(), ijet = ibegin;
	ijet != iend; ++ijet ) {

    unsigned int idx = ijet - ibegin;
    edm::RefToBase<reco::CaloJet> thisJetRef = hOriginalJets->refAt(idx);
    double thisEta = thisJetRef->eta();
    double thisPhi = thisJetRef->phi();
    double thisDeltaR = deltaR(theJet->eta(),theJet->phi(),thisEta,thisPhi);
    if(thisDeltaR < bestDeltaR) {
      bestDeltaR = thisDeltaR;
      matchingIDX = idx;
    }
  }

  edm::RefToBase<reco::CaloJet> originalJetRef = hOriginalJets->refAt(matchingIDX);
  std::cout << "Hola que tal" << std::endl;
  
  reco::JetID theJetId = (*hJetIDMap)[ originalJetRef ];
  std::cout << "Hola que tal2" << std::endl;

  reco::CaloJet theNewJet = (*jetRef);
  std::cout << "Hola que tal3" << std::endl;
 
  h_fHPD->Fill(theJetId.fHPD);
  h_fRBX->Fill(theJetId.fRBX);
  h_n90->Fill(theJetId.n90Hits);
  h_nECAL->Fill(theJetId.nECALTowers);
  h_nHCAL->Fill(theJetId.nHCALTowers);
  h_fEB->Fill(theJetId.fEB);
  h_fEE->Fill(theJetId.fEE);
  h_fHB->Fill(theJetId.fHB);
  h_fHE->Fill(theJetId.fHE);
  h_fHO->Fill(theJetId.fHO);
  h_fLong->Fill(theJetId.fLong);
  h_fShort->Fill(theJetId.fShort);
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSJetIdAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSJetIdAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSJetIdAnalyzer);
