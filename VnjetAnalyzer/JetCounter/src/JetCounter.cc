// -*- C++ -*-
//
// Package:    JetCounter
// Class:      JetCounter
// 
/**\class JetCounter JetCounter.cc VnjetAnalyzer/JetCounter/src/JetCounter.cc

Description: <one line class summary>

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Feb 20 15:48:51 CET 2008
// $Id: JetCounter.cc,v 1.1 2008/03/20 10:17:29 tomei Exp $
//
//


// system include files
#include <memory>
#include <vector>
#include <cstdio>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "TH1F.h"
//
// class decleration
//

class JetCounter : public edm::EDAnalyzer {
public:
  explicit JetCounter(const edm::ParameterSet&);
  ~JetCounter();


private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  edm::InputTag src_;
  TH1F* numjets0p;
  TH1F* numjets1p;
  TH1F* numjets2p;
  TH1F* numjets3p;
  TH1F* numjets4p;
  TH1F* numjets5p;
  // ----------member data ---------------------------
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
JetCounter::JetCounter(const edm::ParameterSet& iConfig):
  src_(iConfig.getParameter<edm::InputTag>("src") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  numjets0p = fs->make<TH1F>("numjets0p", "numjets0p", 15, -0.5, 14.5);
  numjets1p = fs->make<TH1F>("numjets1p", "numjets1p", 15, -0.5, 14.5);
  numjets2p = fs->make<TH1F>("numjets2p", "numjets2p", 15, -0.5, 14.5);
  numjets3p = fs->make<TH1F>("numjets3p", "numjets3p", 15, -0.5, 14.5);
  numjets4p = fs->make<TH1F>("numjets4p", "numjets4p", 15, -0.5, 14.5);
  numjets5p = fs->make<TH1F>("numjets5p", "numjets5p", 15, -0.5, 14.5);
}

JetCounter::~JetCounter()
{
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
JetCounter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

   // CSA07 weights.
  Handle<double> weightHandle;
  Handle<int> processIDHandle;
  iEvent.getByLabel ("weight","weight", weightHandle);
  iEvent.getByLabel ("weight","AlpgenProcessID", processIDHandle);
  double weight = *weightHandle;
  int processID = *processIDHandle;
  
  // Get number of partons from processID - it is the last digit.
  int npartons = processID%10;

  Handle<reco::CandidateView> src;
  iEvent.getByLabel(src_, src);
  int njets = src->size();

  // Stupid code, but... 
  if(npartons == 0)
    numjets0p->Fill(njets, weight);
  if(npartons == 1)
    numjets1p->Fill(njets, weight);
  if(npartons == 2)
    numjets2p->Fill(njets, weight);
  if(npartons == 3)
    numjets3p->Fill(njets, weight);
  if(npartons == 4)
    numjets4p->Fill(njets, weight);
  if(npartons == 5)
    numjets5p->Fill(njets, weight);
}

// ------------ method called once each job just before starting event loop  ------------
void 
JetCounter::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetCounter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetCounter);
