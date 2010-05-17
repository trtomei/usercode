// -*- C++ -*-
//
// Package:    RSJetComparison
// Class:      RSJetComparison
// 
/**\class RSJetComparison RSJetComparison.cc RSGraviton/RSJetComparison/src/RSJetComparison.cc

Description: Class to analyze jets in RS->jets events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSJetComparison.cc,v 1.1 2009/05/13 15:38:08 tomei Exp $
//
//


// system include files
#include <memory>
#include <map>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/InputTag.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
//
// class decleration
//

class RSJetComparison : public edm::EDAnalyzer {
public:
  explicit RSJetComparison(const edm::ParameterSet&);
  ~RSJetComparison();

private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag src_;
  edm::InputTag matched_; 
  TH1F*     h_dR;
  TH1F*     h_deltaEt;
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
RSJetComparison::RSJetComparison(const edm::ParameterSet& iConfig) :
  src_(iConfig.getParameter<edm::InputTag>("src") ),
  matched_(iConfig.getParameter<edm::InputTag>("matched") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_dR                  = fs->make<TH1F>( "dR"  , "dR", 100,  0., 0.25);
  h_deltaEt             = fs->make<TH1F>( "deltaEt"  , "deltaEt", 200,  -10.0, 10.0);
}


RSJetComparison::~RSJetComparison()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSJetComparison::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;

  Handle<CandidateView> srcHandle;
  iEvent.getByLabel(src_,srcHandle);
  Handle<CandidateView> matchedHandle;
  iEvent.getByLabel(matched_,matchedHandle);

  if(matchedHandle->size() != srcHandle->size())
    return;

  std::map<size_t,double> theMap;
  for(size_t i = 0; i != srcHandle->size(); ++i) {
    double minDeltaR = 9999.9;
    double minDeltaEt = 9999.9;
    size_t bestMatch = 30000;
    const Candidate& thisSource =(*srcHandle)[i];
    
    for(size_t j = 0; j != matchedHandle->size(); ++j) {
      const Candidate& thisMatch = (*matchedHandle)[j]; 
      double thisDeltaR = deltaR(thisSource.eta(), thisSource.phi(), thisMatch.eta(), thisMatch.phi());
      if(thisDeltaR < minDeltaR) {
	bestMatch = j;
	minDeltaR = thisDeltaR;
	minDeltaEt = (thisSource.et() - thisMatch.et());
      }
    }
    // Found the best match in deltaR space, fill the histogram.
    h_dR->Fill(minDeltaR);
    h_deltaEt->Fill(minDeltaEt);
   } 

}

// ------------ method called once each job just before starting event loop  ------------
void 
RSJetComparison::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSJetComparison::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSJetComparison);
