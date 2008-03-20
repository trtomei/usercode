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
// $Id$
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
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "TFile.h"
#include "TH1.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Utilities/interface/Exception.h"

using namespace std;
using namespace reco;
using namespace edm;
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
  InputTag src_;
  string fOutputFileName_;

  TFile* hOutputFile;
  TH1D* H_W_numjets;
  TH1D* H_Z_numjets;
  TH1D* H_tt_numjets;
  vector<TH1D*> H_W;
  vector<TH1D*> H_Z;
  vector<TH1D*> H_tt;

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
  src_(iConfig.getParameter<InputTag>("src") ),
  fOutputFileName_(iConfig.getUntrackedParameter<string>("HistOutFile", "output.root") )
{
  //now do what ever initialization is needed
  hOutputFile   = new TFile(fOutputFileName_.c_str(), "RECREATE" );
  char name_W[256];
  char name_Z[256];
  char name_tt[256];

  H_W_numjets = new TH1D("numjets_W_total", "Number of jets", 10, 0., 10.);
  H_Z_numjets = new TH1D("numjets_Z_total", "Number of jets", 10, 0., 10.);
  H_tt_numjets = new TH1D("numjets_tt_total", "Number of jets", 10, 0., 10.);

  H_W.resize(6);
  H_Z.resize(6);
  H_tt.resize(6);

  for (int i=0; i!=6; ++i) {
    sprintf(name_W, "numjets_%ip_W", i);
    sprintf(name_Z, "numjets_%ip_Z", i);
    sprintf(name_tt, "numjets_%ip_tt", i);
    H_W[i]  = new TH1D(name_W, "Number of jets", 10, 0., 10.);
    H_Z[i]  = new TH1D(name_Z, "Number of jets", 10, 0., 10.);
    H_tt[i] = new TH1D(name_tt, "Number of jets", 10, 0., 10.);
  }  
  
}

JetCounter::~JetCounter()
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
JetCounter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace std;
  using namespace edm;

   // CSA07 weights.
  Handle<double> weightHandle;
  iEvent.getByLabel ("weight","weight", weightHandle);
  double weight = * weightHandle;
   
  LogDebug("Values") << "weight is " << weight;

  bool wevent = false;
  bool zevent = false;
  bool ttbarevent = false;
  int multiplier = 0;
  int numpartons = 0;

  // Code to decide if I am dealing with:
  // 1- ttbar event.
  // 2- w+jets event.
  // 3- z+jets event.
  Handle<int> ALPGENHandle;
  iEvent.getByLabel ("weight","AlpgenProcessID", ALPGENHandle);
  int alpgen = * ALPGENHandle;

  if( (alpgen >= 1000) && (alpgen < 2000) ){
    wevent = true;
    multiplier = 1;
  }
  else if( (alpgen >= 2000) && (alpgen < 3000) ){
    zevent = true;
    multiplier = 2;
  }
  else if( (alpgen >= 3000) && (alpgen < 4000) ){ 
    ttbarevent = true;
    multiplier = 3;
  }
  
  numpartons = alpgen - (multiplier*1000);

  LogDebug("Values") << "numpartons = " << numpartons;

  if(numpartons > 5) {
    throw cms::Exception("RangeError") << "Too many (" << numpartons << ") hard partons";
    LogError("ERROR") << "Too many (" << numpartons << ") hard partons";
  }
  
  Handle<CandidateCollection> src;
  iEvent.getByLabel(src_, src);
  int njets = src->size();
  
  if(wevent)
    H_W_numjets->Fill(njets, weight);
  if(zevent)
    H_Z_numjets->Fill(njets, weight);
  if(ttbarevent)
    H_tt_numjets->Fill(njets, weight);
  
  switch(multiplier) {
  case 1: 
    {
      (H_W.at(numpartons))->Fill(njets, weight);
    }
    break;

  case 2: 
    {
      (H_Z.at(numpartons))->Fill(njets, weight);
    }
    break;

  case 3:
    {
      (H_tt.at(numpartons))->Fill(njets, weight);
    }
    break;
    
  } // Closes switch;  


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
