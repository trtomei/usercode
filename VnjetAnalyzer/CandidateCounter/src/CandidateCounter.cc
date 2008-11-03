// -*- C++ -*-
//
// Package:    CandidateCounter
// Class:      CandidateCounter
// 
/**\class CandidateCounter CandidateCounter.cc VnjetAnalyzer/CandidateCounter/src/CandidateCounter.cc

Description: <one line class summary>

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Feb 20 15:48:51 CET 2008
// $Id: CandidateCounter.cc,v 1.2 2008/06/23 11:16:01 tomei Exp $
//
//


// system include files
#include <memory>
#include <string>

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

class CandidateCounter : public edm::EDAnalyzer {
public:
  explicit CandidateCounter(const edm::ParameterSet&);
  ~CandidateCounter();


private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  edm::InputTag src_;
  double weight_;
  TH1F* numjets;
  double min;
  double max;
  int nbins;
  std::string description;
  std::string name;
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
CandidateCounter::CandidateCounter(const edm::ParameterSet& iConfig):
  src_(iConfig.getParameter<edm::InputTag>("src") ),
  weight_(iConfig.getParameter<double>("weight") ),
  min(iConfig.getParameter<double>("min") ),
  max(iConfig.getParameter<double>("max") ),
  nbins(iConfig.getParameter<int>("nbins") ),
  description(iConfig.getParameter<std::string>("description") ),
  name(iConfig.getParameter<std::string>("name") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  numjets = fs->make<TH1F>("name", "description", nbins, min, max);
}

CandidateCounter::~CandidateCounter()
{
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
CandidateCounter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  Handle<reco::CandidateView> src;
  iEvent.getByLabel(src_, src);
  int njets = src->size();

  numjets->Fill(njets, weight_);
}

// ------------ method called once each job just before starting event loop  ------------
void 
CandidateCounter::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CandidateCounter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(CandidateCounter);
