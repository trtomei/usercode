// -*- C++ -*-
//
// Package:    VnjetAnalyzer
// Class:      VnjetAnalyzer
// 
/**\class VnjetAnalyzer VnjetAnalyzer.cc VnjetAnalyzer/VnjetAnalyzer/src/VnjetAnalyzer.cc

Description: Thiago Tomei package for vector boson + jets analysis.

Implementation:
<Notes on implementation>
*/
//s
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Oct 10 09:35:38 CEST 2007
// $Id: VnjetAnalyzer.cc,v 1.3 2008/03/26 18:07:42 tomei Exp $
//
//


// system include files
#include <memory>
#include <cstddef>
#include <algorithm>
#include <sstream>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// My includes
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Common/interface/Ref.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "TFile.h"
#include "TH1.h"
#include "PhysicsTools/CandUtils/interface/AddFourMomenta.h"
#include "DataFormats/GeometryVector/interface/GlobalVector.h"

using namespace std;
using namespace reco;
using namespace edm;
//
// class decleration
//

class VnjetAnalyzer : public edm::EDAnalyzer {
public:
  explicit VnjetAnalyzer(const edm::ParameterSet&);
  ~VnjetAnalyzer();


private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  double transvmass(const Candidate& firstdau, const Candidate& seconddau);

  InputTag jets_;
  InputTag highestjets_;
  InputTag MET_;  
  InputTag muons_;
  InputTag particles_;
  bool debugmode_;
  string fOutputFileName_;
    
  // ROOT stuff.

  TFile*      hOutputFile;

  // Include all histograms we want.
#include "histograms.h" 
  // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//
const int wpid = 24; // W+ id
const int wmid = -24; // W- id
const int tid = 6; // top id
const int zid = 23; // Z0 id
const int hard = 3;    // Hard interaction products have status 3.

const double barrellimit = 1.3;
const double endcaplimit = 3.0;
//
// static data member definitions
//

//
// constructors and destructor
//
VnjetAnalyzer::VnjetAnalyzer(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<InputTag>("Jets") ),
  highestjets_(iConfig.getParameter<InputTag>("highestJets") ),
  MET_(iConfig.getParameter<InputTag>("MET") ),
  muons_(iConfig.getParameter<InputTag>("Muons") ),
  particles_(iConfig.getParameter<InputTag>("Particles") ),
  debugmode_(iConfig.getUntrackedParameter<bool>("DebugMode", false) ),
  fOutputFileName_(iConfig.getUntrackedParameter<string>("HistOutFile", "output.root") )
  // The latter name parameters must be given in the .cfg file.
  
{
  // Now do what ever initialization is needed

  // As this is an Analyzer that will write ROOT files, we should book the
  // histograms here.
  hOutputFile   = new TFile(fOutputFileName_.c_str(), "RECREATE" );
 
  // Book histograms.
#include "booking.h"

  return ;
}


VnjetAnalyzer::~VnjetAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  hOutputFile->Write() ;
  hOutputFile->Close() ;
  return;
}

//
// member functions
//


// ------------ method called to for each event  ------------
void
VnjetAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace std;
  using namespace edm;

  int barrel = 0;
  int endcap = 1;
  int forward = 2;

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
    //      wevent = true;
    destination = 1;
  }
  else if( (alpgen >= 2000) && (alpgen < 3000) ){
    //      zevent = true;
    destination = 2;
  }
  else if( (alpgen >= 3000) && (alpgen < 4000) ){ 
    //      ttbarevent = true;
    destination = 3;
  }
  
  if(destination != 3)
    throw cms::Exception("AlpgenProcessID") << "Invalid AlpgenProcessID = " << alpgen;
  
  LogDebug("Trace") << "Got AlpgenProcessID";
  LogDebug("Values") << "destination = " << destination;
  
  Handle<double> weightHandle;
  iEvent.getByLabel ("weight","weight", weightHandle);
  double weight = * weightHandle;
  
  //  double weight = 1.0;
   
  LogDebug("Values") << "weight is " << weight;

  Handle<CandidateCollection> jets;
  Handle<CandidateCollection> highestjets;
  Handle<CandidateCollection> muons;
  Handle<CandidateCollection> particles;
  Handle<CandidateCollection> met_handle;
   
  iEvent.getByLabel(jets_, jets);
  iEvent.getByLabel(highestjets_, highestjets);
  iEvent.getByLabel(muons_,muons);
  iEvent.getByLabel(particles_, particles);
  iEvent.getByLabel(MET_, met_handle);
  
  // ***************** 
  // PART 1: PARTICLES
  // *****************
  
  bool foundw   = false; // Flag for finding W.
  bool foundwp  = false; // Flag for finding W+.
  bool foundwm  = false; // Flag for finding W-.
  bool foundz   = false; // Flag for finding Z.
  bool foundt   = false; // Flag for finding top.
  bool mudecay  = false; // Flag for finding mu.
  double vpt = 0.; // V pt
  double veta = 0.; // V eta
  double nupt = 0.; // Neutrino pt
  
  // We will loop through all particles in the event.
  for( CandidateCollection::const_iterator piter = particles->begin();
       piter != particles->end();
       ++piter) {

    // Statistics of the particle.
    double temp_pt = piter->pt();
    double temp_eta = piter->eta();
    int temp_id = piter->pdgId();
    int abs_id = abs(temp_id);
    int temp_status = piter->status();
    
    // Which particle is it?
    bool iswp = (temp_id == wpid);
    bool iswm = (temp_id == wmid);
    bool isw = (iswp || iswm);
    bool isz = (temp_id == zid);
    bool ist = (abs_id == tid);
    
    // If W or Z from the hard interaction, get the kinematics.
    if( (isw || isz) && (temp_status == hard) ) {
      vpt = temp_pt;
      veta = temp_eta;
      
      // Checking the daughters.
      for(size_t bb=0; bb!=piter->numberOfDaughters(); ++bb) {
	int dau_id = abs(piter->daughter(bb)->pdgId());
	int dau_status = piter->daughter(bb)->status();
	// Check decay in muon.
	if( (dau_id == 13 || dau_id == 14) && dau_status == hard)
	  mudecay = true;
	// Get neutrino kinematics, if there is a neutrino daughter.
	if( (temp_id == 12 || temp_id == 14 || temp_id == 16) && temp_status == hard)
	  nupt = piter->daughter(bb)->pt();
      }

    } // Not treating a W/Z anymore.

    // Let's record that we found a W, Z or top.
    if(isw)
      foundw = true;
    if(iswp)
      foundwp = true;
    if(iswm)
      foundwm = true;
    if(isz)
      foundz = true;
    if(ist)
      foundt = true;
    
  } // Exiting the particles loop.
  // Back at the main code.
   
  // Let's decide what kind of event this is.
  // This would be changed if I had AlpgenProcessID

  // Careful, there are W's in ttbarevents.
  if(foundt)
    ttbarevent = true;
  else {
    if(foundw)
      wevent = true;
    if(foundz)
      zevent = true;
  }
  
  // Safeguards. Should redesign this part.
 //  if(false) {
//     throw cms::Exception("AlpgenProcessID") << "Ciao";
//     LogError("ALARMING Error") << "Ciao";
//   }
   
  // Care only about muons.
  if(!mudecay && !ttbarevent)
    return;

  if(foundwp && wevent)
    H_etaWplus->Fill(veta, weight);
  if(foundwm && wevent)
    H_etaWminus->Fill(veta, weight);

  LogDebug("Values") << "wevent is " << wevent;
  LogDebug("Values") << "zevent is " << zevent;
  LogDebug("Values") << "ttbarevent is " << ttbarevent;

  if(wevent || zevent) {
    LogDebug("Values") << "vpt = " << vpt;
    LogDebug("Values") << "veta = " << veta;
    LogDebug("Values") << "nupt = " << nupt;
  }

  // ************ 
  // PART 2: JETS
  // ************

  int njets = jets->size();
  int nhighjets = highestjets->size();
      
  // *************
  // PART 3: MUONS
  // *************

  // THIS COLLECTION MUST HAVE BEEN SORTED IN THE .cfg FILE!!!

  int nmuons = muons->size();
  
  CandidateRef firstmu;
  CandidateRef secondmu;
  
  if(nmuons > 0)
    firstmu = CandidateRef(muons,0);
  if(nmuons > 1)
    secondmu = CandidateRef(muons,1);
  
  // ****************** 
  // PART 4: MET
  // ******************

  // Simply get the MET status.

  CandidateRef met = CandidateRef(met_handle,0);
  
  double met_pt = met->pt();

  LogDebug("Values") << "MET pt = " << met_pt;

  // ****************** 
  // PART 5: HISTOGRAMS
  // ******************
  
  // Reconstruct the vector boson from jets.
  CompositeCandidate vFromJets;
   
  int nbarrel = 0;
  int nendcap = 0;

  // Histogram Et, eta, phi of all jets.
  for( CandidateCollection::const_iterator jiter = jets->begin();
       jiter != jets->end();
       ++jiter) {

    vFromJets.addDaughter(*jiter);
     
    double Et_jet  = jiter->et();
    double eta_jet = jiter->eta();
    double phi_jet = jiter->phi();

    if(eta_jet < barrellimit)
      nbarrel++;
    else if( barrellimit < eta_jet && eta_jet < endcaplimit)
      nendcap++;
    
    H_Et_tJets->Fill(Et_jet, weight);
    H_eta_tJets->Fill(eta_jet, weight);
    H_phi_tJets->Fill(phi_jet, weight);
     
    double abs_eta = fabs(eta_jet);
    if(abs_eta < barrellimit) {
      H_Etjets_barrel->Fill(Et_jet, weight);
      H_etajets_barrel->Fill(eta_jet, weight);
      H_phijets_barrel->Fill(phi_jet, weight);
    }
    else if(abs_eta < endcaplimit) {
      H_Etjets_endcap->Fill(Et_jet, weight);
      H_etajets_endcap->Fill(eta_jet, weight);
      H_phijets_endcap->Fill(phi_jet, weight);
    }
  } // End loop in normal jets.

  AddFourMomenta addjets;
  addjets.set(vFromJets);

  LogDebug("Info") << "Looped over jets.";

  // Using the ternary operator... ugly, but compact. Avoids div. by zero.
  // njets was defined upwards.
  double perc_barrel = (njets == 0) ? (-1.) :((double)nbarrel/ (double)njets);
  double perc_endcap = (njets == 0) ? (-1.) :((double)nendcap/ (double)njets);
  
  LogDebug("Values") << "njets = " << njets;
  LogDebug("Values") << "nhighjets = " << nhighjets;
  LogDebug("Values") << "nbarrel = " << nbarrel;
  LogDebug("Values") << "nendcap = " << nendcap;
  
  // Histogram number of jets and percentage in barrel/endcap. 
  H_tnumJets->Fill(njets, weight);
  if(njets!=0) {
    H_tbarrel->Fill(perc_barrel, weight);
    H_tendcap->Fill(perc_endcap, weight);
  }
  LogDebug("Info") << "Filled jet histograms";
  
  // Let's check if the leading jet is in the barrel or in the
  // endcap. If we run in the baseline or later samples, it should be
  // ALL in the barrel - or else, the previous modules didn't
  // work. Here, we loop in the highestjets collection.
  {
    int cnt = 0;
    for( CandidateCollection::const_iterator jiter = highestjets->begin();
	 jiter != highestjets->end();
	 ++jiter, ++cnt) {
      
      double Et_jet  = jiter->et();
      double eta_jet = jiter->eta();
      double phi_jet = jiter->phi();
      LogDebug("cnt") << "cnt" << cnt;
      LogDebug("Values") << "Et_jet" << Et_jet;
      LogDebug("Values") << "eta_jet" << eta_jet;
      LogDebug("Values") << "phi_jet" << phi_jet;
 
      // For the first jet, fill in the region where it is.
      if(cnt==0) {
	double abs_eta = fabs(eta_jet);
	if(abs_eta < barrellimit)
	  H_eff->Fill(barrel, weight);
	else if(abs_eta < endcaplimit)
	  H_eff->Fill(endcap, weight);
	else
	  H_eff->Fill(forward, weight);
      }
       
      H_Etjets[cnt]->Fill(Et_jet, weight);
      H_etajets[cnt]->Fill(eta_jet, weight);
      H_phijets[cnt]->Fill(phi_jet, weight);
             
    } // Close loop of 7 highest jets.
  }// Scope the cnt;

  LogDebug("Info") << "Looped over highjets";
  // Now, we act based on if we found 1,2,3,4 jets.
  // First, we reconstruct the boson as if it was a W and a Z.

  // Reconstruct as W
  CompositeCandidate Wcand;
  double Wmt = 0.;
  if(nmuons > 0) {
    Wcand.addDaughter(*met);
    Wcand.addDaughter(*firstmu);
    AddFourMomenta addP4;
    addP4.set(Wcand);
    Wmt = transvmass(*firstmu, *met);
  }
  LogDebug("Info") << "Reconstructed W";
  
  // Reconstruct as Z
  CompositeCandidate Zcand;
  if(nmuons > 1) {
    Zcand.addDaughter(*firstmu);
    Zcand.addDaughter(*secondmu);
    AddFourMomenta addP4;
    addP4.set(Zcand);
  }
  LogDebug("Info") << "Reconstructed Z";

  H_tnumMuons->Fill(nmuons, weight);
  
  double leadingmupt =0.;
  double leadingmueta = 0.;
  double secondmupt = 0.;
  double secondmueta = 0.;
  
  if(nmuons > 0) {
    leadingmupt = firstmu->pt();
    leadingmueta = firstmu->eta();
  }
  if(nmuons > 1) {
    secondmupt = secondmu->pt();
    secondmueta = secondmu->eta();
  }

  // Greater or equal than 1 jet.
  if(njets>=1) {
    H_ptV_dir_1j->Fill(vpt, weight);
    H_ptV_jets_1j->Fill(vFromJets.pt(), weight);
    if(nmuons > 0) {
      H_pt1stmu_1j->Fill(leadingmupt, weight);
      H_eta1stmu_1j->Fill(leadingmueta, weight);
      H_ptV_mumet_1j->Fill(Wcand.pt(), weight);
      H_transvmass_1j->Fill(Wmt, weight);
    }
    if(nmuons > 1) {
      H_pt2ndmu_1j->Fill(secondmupt, weight);
      H_eta2ndmu_1j->Fill(secondmueta, weight);
      H_ptV_mu_1j->Fill(Zcand.pt(), weight);
      H_invmass_2mu_1j->Fill(Zcand.mass(), weight);
    }
  }
  LogDebug("Info") << ">= 1jet";

  // Greater or equal than 2 jets.
  if(njets>=2) {
    H_ptV_dir_2j->Fill(vpt, weight);
    H_ptV_jets_2j->Fill(vFromJets.pt(), weight);
    if(nmuons > 0) {
      H_pt1stmu_2j->Fill(leadingmupt, weight);
      H_eta1stmu_2j->Fill(leadingmueta, weight);
      H_ptV_mumet_2j->Fill(Wcand.pt(), weight);
      H_transvmass_2j->Fill(Wmt, weight);
    }
    if(nmuons > 1) {
      H_pt2ndmu_2j->Fill(secondmupt, weight);
      H_eta2ndmu_2j->Fill(secondmueta, weight);
      H_ptV_mu_2j->Fill(Zcand.pt(), weight);
      H_invmass_2mu_2j->Fill(Zcand.mass(), weight);
    }
  }
  LogDebug("Info") << ">= 2jet";

  // Greater or equal than 3 jets.
  if(njets>=3) {
    H_ptV_dir_3j->Fill(vpt, weight);
    H_ptV_jets_3j->Fill(vFromJets.pt(), weight);
    if(nmuons > 0) {
      H_pt1stmu_3j->Fill(leadingmupt, weight);
      H_eta1stmu_3j->Fill(leadingmueta, weight);
      H_ptV_mumet_3j->Fill(Wcand.pt(), weight);
      H_transvmass_3j->Fill(Wmt, weight);
    }
    if(nmuons > 1) {
      H_pt2ndmu_3j->Fill(secondmupt, weight);
      H_eta2ndmu_3j->Fill(secondmueta, weight);
      H_ptV_mu_3j->Fill(Wmt, weight);
      H_invmass_2mu_3j->Fill(Zcand.mass(), weight);
    }
  }
  LogDebug("Info") << ">= 3jet";

  // Greater or equal than 4 jets.
  if(njets>=4) {
    H_ptV_dir_4j->Fill(vpt, weight);
    H_ptV_jets_4j->Fill(vFromJets.pt(), weight);
    if(nmuons > 0) {
      H_pt1stmu_4j->Fill(leadingmupt, weight);
      H_eta1stmu_4j->Fill(leadingmueta, weight);
      H_ptV_mumet_4j->Fill(Wcand.pt(), weight);
      H_transvmass_4j->Fill(Wmt, weight);
    }
    if(nmuons > 1) {
      H_pt2ndmu_4j->Fill(secondmupt, weight);
      H_eta2ndmu_4j->Fill(secondmueta, weight);
      H_ptV_mu_4j->Fill(Zcand.pt(), weight);
      H_invmass_2mu_4j->Fill(Zcand.mass(), weight);
    }
  }
  LogDebug("Info") << ">= 4jet";
  

  // Finally, compare neutrino pt true with MET.
  H_ptnu_direct->Fill(nupt, weight);
  H_pt_met->Fill(met_pt, weight);  
  H_eventcounter->Fill(0.5, weight);

  LogDebug("Info") << "Finished! :)";

} // Closes the analyzer.

// ------------ method called once each job just before starting event loop  ------------
void 
VnjetAnalyzer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
VnjetAnalyzer::endJob()
{
}

double 
VnjetAnalyzer::transvmass(const Candidate& firstdau, const Candidate& seconddau)
{
  double et1 = firstdau.et();
  double et2 = seconddau.et();
  GlobalVector pt1(firstdau.px(), firstdau.py(),0.);
  GlobalVector pt2(seconddau.px(), seconddau.py(),0.);
  double tm = 2*(et1*et2 - pt1.dot(pt2));
  return tm;
}

//define this as a plug-in
DEFINE_FWK_MODULE(VnjetAnalyzer);
