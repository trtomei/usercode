// -*- C++ -*-
//
// Package:    CandidateComparator
// Class:      CandidateComparator
// 
/**\class CandidateComparator CandidateComparator.cc VnjetAnalyzer/CandidateComparator/src/CandidateComparator.cc

Description: <one line class summary>

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Tue Feb 19 15:47:35 CET 2008
// $Id$
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
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandMatchMap.h"
#include "TFile.h"
#include "TH1.h"
#include "DataFormats/Math/interface/deltaR.h"

using namespace std;
using namespace reco;
using namespace edm;
//
// class decleration
//

class CandidateComparator : public edm::EDAnalyzer {
public:
  explicit CandidateComparator(const edm::ParameterSet&);
  ~CandidateComparator();


private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  InputTag src_;
  InputTag mt_;
  InputTag match_;
  string fOutputFileName_;

  TFile* hOutputFile;

  TH1D* H_num_src_W;
  TH1D* H_num_mt_W;
  TH1D* H_dR_W;
  TH1D* H_num_src_Z;
  TH1D* H_num_mt_Z;
  TH1D* H_dR_Z;
  TH1D* H_num_src_tt;
  TH1D* H_num_mt_tt;
  TH1D* H_dR_tt;
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
CandidateComparator::CandidateComparator(const edm::ParameterSet& iConfig):
  src_(iConfig.getParameter<InputTag>("src") ),
  mt_(iConfig.getParameter<InputTag>("matched") ),
  match_(iConfig.getParameter<InputTag>("map") ),
  fOutputFileName_(iConfig.getUntrackedParameter<string>("HistOutFile", "output.root") )
{
  //now do what ever initialization is needed
  hOutputFile   = new TFile(fOutputFileName_.c_str(), "RECREATE" );
  hOutputFile->mkdir("Wjets");
  hOutputFile->mkdir("Zjets");
  hOutputFile->mkdir("ttjets");
  
  hOutputFile->cd("Wjets");
  H_num_src_W  = new TH1D("num_src_W", "Number of sources", 10, 0., 10.);
  H_num_mt_W   = new TH1D("num_mt_W", "Number of matches", 10, 0., 10.);
  H_dR_W       = new TH1D("dR_W", "deltaR source - matched", 50, 0., 0.5);
  hOutputFile->cd("Zjets");
  H_num_src_Z  = new TH1D("num_src_Z", "Number of sources", 10, 0., 10.);
  H_num_mt_Z   = new TH1D("num_mt_Z", "Number of matches", 10, 0., 10.);
  H_dR_Z       = new TH1D("dR_Z", "deltaR source - matched", 50, 0., 0.5);
  hOutputFile->cd("ttjets");
  H_num_src_tt = new TH1D("num_src_tt", "Number of sources", 10, 0., 10.);
  H_num_mt_tt  = new TH1D("num_mt_tt", "Number of matches", 10, 0., 10.);
  H_dR_tt      = new TH1D("dR_tt", "deltaR source - matched", 50, 0., 0.5);

}


CandidateComparator::~CandidateComparator()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  hOutputFile->Write() ;
  hOutputFile->Close() ;
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
CandidateComparator::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace std;
  using namespace edm;
  
  // CSA07 weights.
  Handle<double> weightHandle;
  iEvent.getByLabel ("weight","weight", weightHandle);
  double weight = * weightHandle;
   
  LogDebug("Values") << "weight is " << weight;

  bool ttbarevent = false;
  bool wevent = false;
  bool zevent = false;
  int destination = 0;
  
  // Code to decide if I am dealing with:
  // 1- ttbar event.
  // 2- w+jets event.
  // 3- z+jets event.
  Handle<int> ALPGENHandle;
  iEvent.getByLabel ("weight","AlpgenProcessID", ALPGENHandle);
  int alpgen = * ALPGENHandle;
  if( (alpgen >= 1000) && (alpgen < 2000) ){
    wevent = true;
    destination = 1;
  }
  else if( (alpgen >= 2000) && (alpgen < 3000) ){
    zevent = true;
    destination = 2;
  }
  else if( (alpgen >= 3000) && (alpgen < 4000) ){ 
    ttbarevent = true;
    destination = 3;
  }
  
  if(destination == 0)
    throw cms::Exception("AlpgenProcessID") 
      << "Invalid AlpgenProcessID = " << alpgen;

  Handle<CandidateCollection> src;
  Handle<CandidateCollection> mt;
  Handle<CandMatchMap> match;
  
  iEvent.getByLabel(src_, src);
  iEvent.getByLabel(mt_, mt);
  iEvent.getByLabel(match_, match );

  switch(destination) {
  case 1:
    {
      // Plot the number of reconstructed jets.
      int num_src = src->size();
      int num_mt  = mt->size();
      
      H_num_src_W->Fill(num_src, weight);
      H_num_mt_W->Fill(num_mt, weight);
      
      // Plot the dR between source and matched jets.
      for(CandMatchMap::const_iterator iter = match->begin();
	  iter != match->end();
	  ++iter) {
	const Candidate* source = &*(iter->key);
	const Candidate* matched = &*(iter->val);
	if(matched != 0) {
	  double dR = deltaR(source->eta(), source->phi(), matched->eta(), matched->phi());
	  H_dR_W->Fill(dR, weight);
	}
      }
    }
    break;

  case 2:
    {
      // Plot the number of reconstructed jets.
      int num_src = src->size();
      int num_mt  = mt->size();

      H_num_src_Z->Fill(num_src, weight);
      H_num_mt_Z->Fill(num_mt, weight);
    
      // Plot the dR between source and matched jets.
      for(CandMatchMap::const_iterator iter = match->begin();
	  iter != match->end();
	  ++iter) {
	const Candidate* source = &*(iter->key);
	const Candidate* matched = &*(iter->val);
	if(matched != 0) {
	  double dR = deltaR(source->eta(), source->phi(), matched->eta(), matched->phi());
	  H_dR_Z->Fill(dR, weight);
	}
      }
    }
    break;

  case 3:
    {
      // Plot the number of reconstructed jets.
      int num_src = src->size();
      int num_mt  = mt->size();

      H_num_src_tt->Fill(num_src, weight);
      H_num_mt_tt->Fill(num_mt, weight);
    
      // Plot the dR between source and matched jets.
      for(CandMatchMap::const_iterator iter = match->begin();
	  iter != match->end();
	  ++iter) {
	const Candidate* source = &*(iter->key);
	const Candidate* matched = &*(iter->val);
	if(matched != 0) {
	  double dR = deltaR(source->eta(), source->phi(), matched->eta(), matched->phi());
	  H_dR_tt->Fill(dR, weight);
	}
      }
    }
    break;

  } // End switch.
}

// ------------ method called once each job just before starting event loop  ------------
void 
CandidateComparator::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CandidateComparator::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(CandidateComparator);
