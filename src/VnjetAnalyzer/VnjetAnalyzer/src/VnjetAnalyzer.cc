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
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Oct 10 09:35:38 CEST 2007
// $Id$
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
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/Common/interface/Ref.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "TFile.h"
#include "TH1.h"
#include "PhysicsTools/CandUtils/interface/AddFourMomenta.h"
#include "DataFormats/Math/interface/deltaPhi.h"

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

  InputTag jets_;
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

const int maxnumjets = 9;
const int maxnummu = 3;
const double barrellimit = 1.3;
const double endcaplimit = 3.0;
const double Zwindowlow = 70.0;
const double Zwindowhigh = 110.0;
const double Ztruemass = 91.1876;
//
// static data member definitions
//

//
// constructors and destructor
//
VnjetAnalyzer::VnjetAnalyzer(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<InputTag>("Jets") ),
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
  hOutputFile->mkdir("Wjets");
  hOutputFile->mkdir("Zjets");
  hOutputFile->mkdir("ttjets");
 
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
     throw cms::Exception("AlpgenProcessID") << "Invalid AlpgenProcessID = " << alpgen;

   LogDebug("Trace") << "Got AlpgenProcessID";
   LogDebug("Values") << "destination = " << destination;

   Handle<double> weightHandle;
   iEvent.getByLabel ("weight","weight", weightHandle);
   double weight = * weightHandle;
   
   LogDebug("Values") << "weight is " << weight;

   Handle<CandidateCollection> jets;
   Handle<CandidateCollection> muons;
   Handle<CandidateCollection> particles;
   Handle<CaloMETCollection> met_handle;
   
   iEvent.getByLabel(jets_, jets);
   iEvent.getByLabel(muons_,muons);
   iEvent.getByLabel(particles_, particles);
   iEvent.getByLabel(MET_, met_handle);
   
   Handle<CandidateCollection> highestjets;
   iEvent.getByLabel("highestJets", highestjets);

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
     
     // We search for the top. A top event contains W boson, 
     // so W events must be treated as subset of top events.
     if(abs_id == tid) 
       foundt = true;
     
     // We search for the W (+ or -) or Z from the hard interaction.
     if( ((temp_id == wpid) || (temp_id == wmid) || (temp_id == zid)) 
	 && (temp_status == hard) ) {
       
       if((temp_id == wpid) || (temp_id == wmid)) {
	 foundw = true;
	 foundwp = (temp_id == wpid);
	 foundwm = (temp_id == wmid);
	 vpt = temp_pt;
	 veta = temp_eta;
       }
       else {
	 foundz = true;
	 vpt = temp_pt;
       }
       
       // BE SURE THAT IT WAS A GENERATOR LEVEL MUON DECAY
       for(size_t bb=0; bb!=piter->numberOfDaughters(); ++bb) {
	 int dau_id = abs(piter->daughter(bb)->pdgId());
	 int dau_status = piter->daughter(bb)->status();
	 if( (dau_id == 13 || dau_id == 14) && dau_status == hard)
	   mudecay = true;
       }
     } // Not treating a W/Z anymore.
     
     // If it is a W, find the neutrino pt.
     if(abs_id == wpid) {
       for(size_t bb=0; bb!=piter->numberOfDaughters(); ++bb) {
	 int temp_id = abs(piter->daughter(bb)->pdgId());
	 int temp_status = piter->daughter(bb)->status();
	 if( (temp_id == 12 || temp_id == 14 || temp_id == 16) && temp_status==hard)
	   nupt = piter->daughter(bb)->pt();
       }
     }    
   
   } // Exiting the particles loop.
   // Back at the main code.
   
   LogDebug("Values") << "vpt = " << vpt;
   LogDebug("Values") << "nupt = " << nupt;
   
   // Safeguards.
   if( !(foundw || foundz) && !ttbarevent ) {
     throw cms::Exception("AlpgenProcessID") << "Didn't find W/Z in a W/Z event.";
     LogError("ALARMING Error") << "Didn't find W/Z in a W/Z event.";
   }
   if( !foundt && ttbarevent ) {
     throw cms::Exception("AlpgenProcessID") << "Didn't find ttbar in a ttbar event.";
     LogError("ALARMING Error") << "Didn't find ttbar in a ttbar event.";
   }
   
   // Care only about muons.
   if(!mudecay && !ttbarevent)
     return;

   if(foundwp && !ttbarevent)
     H_etaWplus->Fill(veta, weight);
   if(foundwm && !ttbarevent)
     H_etaWminus->Fill(veta, weight);
   
   // At this point, at the jets code, I will be safe to use only
   // the AlpgenProcessID information!
   
   // ************ 
   // PART 2: JETS
   // ************

   int njets = 0;
   int nbarrel = 0;
   int nendcap = 0;
   double sum_px_jet = 0.;
   double sum_py_jet = 0.;
   double vptj = 0.;

   njets = jets->size();
   
   for( CandidateCollection::const_iterator jiter = jets->begin();
	jiter != jets->end();
	++jiter) {
     
     double pt_jet = jiter->pt();
     double eta_jet = fabs(jiter->eta());
     LogDebug("Values") << "eta_jet = " << eta_jet;
     LogDebug("Values") << "pt_jet = " << pt_jet;

     if(eta_jet < barrellimit)
       nbarrel++;
     else if( barrellimit < eta_jet && eta_jet < endcaplimit)
       nendcap++;
          
     double px_jet = jiter->px();
     double py_jet = jiter->py();
     
     // Sum of momenta of all jets in the event.
     sum_px_jet += px_jet;
     sum_py_jet += py_jet;
   } // Exiting the jets loop.
   // Back at the main code.
   
   // *************
   // PART 3: MUONS
   // *************

   // THIS COLLECTION MUST HAVE BEEN SORTED IN THE .cfg FILE!!!

   int nmuons = 0;
   nmuons = muons->size();
   double leadingmupt = 0.;
   double secondmupt = 0.;
   double leadingmueta = 0.;
   double secondmueta = 0.;
   {
     int cnt = 0;
     for( CandidateCollection::const_iterator miter = muons->begin();
	  miter != muons->end();
	  ++miter) {
       
       double pt_mu = miter->pt();
       double eta_mu = miter->eta();
       
       if(cnt == 0) {
	 leadingmupt = pt_mu;
	 leadingmueta = eta_mu;
       }
       if(cnt == 1) {
	 secondmupt = pt_mu;
	 secondmueta = eta_mu;
       }

       ++cnt;
       LogDebug("Values") << "Muon pt = " << pt_mu;
     }
   } //Scope the cnt;
  
   // ****************** 
   // PART 4: MET
   // ******************

   // Simply get the MET status.

   const CaloMETCollection *metcol = met_handle.product();
   const CaloMET met = metcol->front();
      
   double met_pt = met.pt();
   
   LogDebug("Values") << "MET pt = " << met_pt;

   // ****************** 
   // PART 5: HISTOGRAMS
   // ******************
   
   // Now we must act based on wether we are dealing with W+jets,
   // Z+jets or ttbar+jets. This we got previously from
   // AlpgenProcessID.

   LogDebug("Values") << "njets = " << njets;
   LogDebug("Values") << "nbarrel = " << nbarrel;
   LogDebug("Values") << "nendcap = " << nendcap;
   LogDebug("Values") << "nmuons = " << nmuons;
   
   // Using the ternary operator... ugly, but compact.
   double perc_barrel = (njets == 0) ? (-1.) :((double)nbarrel/ (double)njets);
   double perc_endcap = (njets == 0) ? (-1.) :((double)nendcap/ (double)njets);

   switch(destination) {
   case 1:

     // Histogram number of jets.
     H_tnumJets_W->Fill(njets, weight);
     if(njets!=0) {
       H_tbarrel_W->Fill(perc_barrel, weight);
       H_tendcap_W->Fill(perc_endcap, weight);
     }
     
     // Histogram mass, calc mass, pt, Et, eta, phi of all jets.
     for( CandidateCollection::const_iterator jiter = jets->begin();
	  jiter != jets->end();
	  ++jiter) {

       double E_jet = jiter->energy();
       double px_jet = jiter->px();
       double py_jet = jiter->py();
       double pz_jet = jiter->pz();
       double m_jet = jiter->mass();
                  
       double mcalc_jet = 0;
       double mcalc_jetsq = E_jet*E_jet - (px_jet*px_jet +
					 py_jet*py_jet +
					 pz_jet*pz_jet);
       
       if(mcalc_jetsq > 0)
	 mcalc_jet = sqrt(mcalc_jetsq);
       else {
         LogWarning("DomainError") << "Jet with negative calculated m^2. Mcalc set to -0.5";
	 mcalc_jet = -0.5;
       }
       
       double Et_jet = jiter->et();
       double pt_jet = jiter->pt();
       double eta_jet = jiter->eta();
       double phi_jet = jiter->phi();
       
       H_m_tJets_W->Fill(m_jet, weight);
       H_mcalc_tJets_W->Fill(mcalc_jet, weight);
       H_Et_tJets_W->Fill(Et_jet, weight);
       H_pt_tJets_W->Fill(pt_jet, weight);
       H_eta_tJets_W->Fill(eta_jet, weight);
       H_phi_tJets_W->Fill(phi_jet, weight);

       double abs_eta = fabs(eta_jet);
       if(abs_eta < barrellimit) {
	 H_Etjets_barrel_W->Fill(Et_jet, weight);
	 H_etajets_barrel_W->Fill(eta_jet, weight);
	 H_phijets_barrel_W->Fill(phi_jet, weight);
       }
       else if(abs_eta < endcaplimit) {
	 H_Etjets_endcap_W->Fill(Et_jet, weight);
	 H_etajets_endcap_W->Fill(eta_jet, weight);
	 H_phijets_endcap_W->Fill(phi_jet, weight);
       }
     } // End loop in normal jets.
     
     // Let's check if the leading jet is in the barrel or in the
     // endcap. If we run in the baseline sample, it should be
     // ALL in the barrel - or else, the previous modules didn't
     // work.
     {
       int cnt = 0;
       for( CandidateCollection::const_iterator jiter = highestjets->begin();
	    jiter != highestjets->end();
	    ++jiter) {
	 
	 double Et_jet = jiter->et();
	 double eta_jet = jiter->eta();
	 double phi_jet = jiter->phi();
	 
	 if(cnt==0) {
	   double abs_eta = fabs(eta_jet);
	   if(abs_eta < barrellimit)
	     H_eff_W->Fill(barrel, weight);
	   else if(abs_eta < endcaplimit)
	     H_eff_W->Fill(endcap, weight);
	   else
	     H_eff_W->Fill(forward, weight);
	 }
	 
	 H_Etjets_W[cnt]->Fill(Et_jet, weight);
	 H_etajets_W[cnt]->Fill(eta_jet, weight);
	 H_phijets_W[cnt]->Fill(phi_jet, weight);
	 ++cnt;
	 
       } // Close loop of 7 highest jets.
     } // Scope the int cnt;

     // Calculate pt of the V from jets.
     
     vptj = sqrt( (sum_px_jet)*(sum_px_jet)+(sum_py_jet)*(sum_py_jet) );
     LogDebug("Values") << "vptj = " << vptj; 
     
     if(njets>=1) {
       H_ptV_jets_1j_W->Fill(vptj, weight);
       H_ptV_dir_1j_W->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_1j_W->Fill(leadingmupt, weight);
	 H_eta1stmu_1j_W->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_1j_W->Fill(secondmupt, weight);
	 H_eta2ndmu_1j_W->Fill(secondmueta, weight);
       }
     }
     if(njets>=2) {
       H_ptV_jets_2j_W->Fill(vptj, weight);
       H_ptV_dir_2j_W->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_2j_W->Fill(leadingmupt, weight);
	 H_eta1stmu_2j_W->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_2j_W->Fill(secondmupt, weight);
	 H_eta2ndmu_2j_W->Fill(secondmueta, weight);
       }
     }
     if(njets>=3) {
       H_ptV_jets_3j_W->Fill(vptj, weight);
       H_ptV_dir_3j_W->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_3j_W->Fill(leadingmupt, weight);
	 H_eta1stmu_3j_W->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_3j_W->Fill(secondmupt, weight);
	 H_eta2ndmu_3j_W->Fill(secondmueta, weight);
       }
     }
     if(njets>=4) {
       H_ptV_jets_4j_W->Fill(vptj, weight);
       H_ptV_dir_4j_W->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_4j_W->Fill(leadingmupt, weight);
	 H_eta1stmu_4j_W->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_4j_W->Fill(secondmupt, weight);
	 H_eta2ndmu_4j_W->Fill(secondmueta, weight);
       }
     }
   
     // Calculate pt of the V from muons and/or MET.
     // This part really depends on if we have found 1, 2 or more muons.
     if(nmuons >= 1) {
     
       // Will reconstruct as a W.
       // Will use the most energetic muon for that.
       const CandidateCollection* muoncol = muons.product();
       const Candidate& muoncand = muoncol->front();
       CompositeCandidate Wcand;

       Wcand.addDaughter(muoncand);
       Wcand.addDaughter(met);
       AddFourMomenta addP4;
       addP4.set(Wcand);

       double met_phi = met.phi();
       double muon_phi = muoncand.phi();
       double muon_pt = muoncand.pt();
       double dphi = deltaPhi(met_phi, muon_phi);
       
       double W_pt = Wcand.pt();
       double W_mass = Wcand.mass();
       double tmsq = 2*muon_pt*met_pt*(1-cos(dphi));
       double transv_mass = sqrt(tmsq);
       
       LogDebug("Values") << "Reco as W: (muon + MET) W_pt = " << W_pt;
       LogDebug("Values") << "Reco as W: (muon + MET) W_mass = " << W_mass;

       H_ptV_mumet_W->Fill(W_pt, weight);
       H_invmass_mumet_W->Fill(W_mass, weight);

       if(njets>=1)	
	 H_transvmass_1j_W->Fill(transv_mass, weight);
       if(njets>=2)
	 H_transvmass_2j_W->Fill(transv_mass, weight);
       if(njets>=3)
	 H_transvmass_3j_W->Fill(transv_mass, weight);
       if(njets>=4)
	 H_transvmass_4j_W->Fill(transv_mass, weight);
              
       // Since we have only ONE muon, we could try to calculate the
       // neutrino pt from jets and muon.
       double nupx = sum_px_jet + muoncand.px();
       double nupy = sum_py_jet + muoncand.py();
       double nupt_jlep = sqrt(nupx*nupx + nupy*nupy);
	 
       H_ptnu_jlep_W->Fill(nupt_jlep, weight);
       H_ptnu_dirl_W->Fill(nupt, weight);
	 
     } // Closes if(nmuons == 1)
     
     if(nmuons >= 2) {
       // Will reconstruct as a Z.
       // Will use the two most energetic muons.
       
       const CandidateCollection *muoncol = muons.product();
       CandidateCollection::const_iterator outmiter=muoncol->begin(); 
       const Candidate& muoncand1 = *outmiter;
       outmiter++;
       const Candidate& muoncand2 = *outmiter;
       CompositeCandidate Zcand;
       
       Zcand.addDaughter(muoncand1);
       Zcand.addDaughter(muoncand2);
       AddFourMomenta addP4;
       addP4.set(Zcand);
       
       double Z_pt = Zcand.pt();
       double Z_mass = Zcand.mass();
       
       LogDebug("Values") << "Reco as Z: (muon + MET) Z_pt = " << Z_pt;
       LogDebug("Values") << "Reco as Z: (muon + MET) Z_mass = " << Z_mass;
       
       if( (Z_mass>Zwindowlow) && (Z_mass<Zwindowhigh) ) {
	 H_invmass_2mu_W->Fill(Z_mass, weight);
	 
	 // Since we got AT LEAST two muons, let's check what happens to V
	 // pt when I ask for at least 1, 2, 3, 4 jets.
	 if(njets>=1) {
	   H_ptV_mu_1j_W->Fill(Z_pt, weight);
	   H_ptV_dirmu_1j_W->Fill(vpt, weight);
	 }
	 if(njets>=2) {
	   H_ptV_mu_2j_W->Fill(Z_pt, weight);
	   H_ptV_dirmu_2j_W->Fill(vpt, weight);
	 }
	 if(njets>=3) {
	   H_ptV_mu_3j_W->Fill(Z_pt, weight);
	   H_ptV_dirmu_3j_W->Fill(vpt, weight);
	 }
	 if(njets>=4) {
	   H_ptV_mu_4j_W->Fill(Z_pt, weight);
	   H_ptV_dirmu_4j_W->Fill(vpt, weight);
	 }
       }

     } // Closes if(nmuons >= 2)
       
     if(nmuons > 2) {
       
       const CandidateCollection *muoncol = muons.product();
       CandidateCollection::const_iterator outmiter=muoncol->begin(); 
       CandidateCollection::const_iterator endmiter=muoncol->end(); 

       // Potentially unsafe...
       const Candidate& muoncand1 = *outmiter;
       outmiter++;
       const Candidate& muoncand2 = *outmiter;
       outmiter++;
       const Candidate& muoncand3 = *outmiter;

       CompositeCandidate Zcand12;
       CompositeCandidate Zcand13;
       CompositeCandidate Zcand23;

       Zcand12.addDaughter(muoncand1);
       Zcand12.addDaughter(muoncand2);
       Zcand13.addDaughter(muoncand1);
       Zcand13.addDaughter(muoncand3);
       Zcand23.addDaughter(muoncand2);
       Zcand23.addDaughter(muoncand3);
       AddFourMomenta addP4;
       addP4.set(Zcand12);
       addP4.set(Zcand13);
       addP4.set(Zcand23);

       double muphi1 = muoncand1.phi();
       double muphi2 = muoncand2.phi();
       double muphi3 = muoncand3.phi();
       
       double Z_m12 = Zcand12.mass();
       double Z_m13 = Zcand13.mass();
       double Z_m23 = Zcand23.mass();
	 
       double dphi12 = deltaPhi(muphi1, muphi2);
       double dphi13 = deltaPhi(muphi1, muphi3);
       double dphi23 = deltaPhi(muphi2, muphi3);
       
       H_invmass_mu12_W->Fill(Z_m12, weight);
       H_invmass_mu13_W->Fill(Z_m13, weight);
       H_invmass_mu23_W->Fill(Z_m23, weight);
       H_dphi_mu12_W->Fill(dphi12, weight);
       H_dphi_mu13_W->Fill(dphi13, weight);
       H_dphi_mu23_W->Fill(dphi23, weight);
	 
     } // Closes if(nmuons > 2)
     
     // Finally, compare neutrino pt true with MET.
     H_ptnu_direct_W->Fill(nupt, weight);
     H_pt_met_W->Fill(met_pt, weight);  
       
     break;
     // *******************************************

   case 2:
     
     // Histogram number of jets.
     H_tnumJets_Z->Fill(njets, weight);
     if(njets!=0) {
       H_tbarrel_Z->Fill(perc_barrel, weight);
       H_tendcap_Z->Fill(perc_endcap, weight);
     }

     // Histogram mass, calc mass, pt, Et, eta, phi of all jets.
     for( CandidateCollection::const_iterator jiter = jets->begin();
	  jiter != jets->end();
	  ++jiter) {

       double E_jet = jiter->energy();
       double px_jet = jiter->px();
       double py_jet = jiter->py();
       double pz_jet = jiter->pz();
       double m_jet = jiter->mass();
                  
       double mcalc_jet = 0;
       double mcalc_jetsq = E_jet*E_jet - (px_jet*px_jet +
					 py_jet*py_jet +
					 pz_jet*pz_jet);
       
       if(mcalc_jetsq > 0)
	 mcalc_jet = sqrt(mcalc_jetsq);
       else {
         LogWarning("DomainError") << "Jet with negative calculated m^2. Mcalc set to -0.5";
	 mcalc_jet = -0.5;
       }
       
       double Et_jet = jiter->et();
       double pt_jet = jiter->pt();
       double eta_jet = jiter->eta();
       double phi_jet = jiter->phi();
       
       H_m_tJets_Z->Fill(m_jet, weight);
       H_mcalc_tJets_Z->Fill(mcalc_jet, weight);
       H_Et_tJets_Z->Fill(Et_jet, weight);
       H_pt_tJets_Z->Fill(pt_jet, weight);
       H_eta_tJets_Z->Fill(eta_jet, weight);
       H_phi_tJets_Z->Fill(phi_jet, weight);

       double abs_eta = fabs(eta_jet);
       if(abs_eta < barrellimit) {
	 H_Etjets_barrel_Z->Fill(Et_jet, weight);
	 H_etajets_barrel_Z->Fill(eta_jet, weight);
	 H_phijets_barrel_Z->Fill(phi_jet, weight);
       }
       else if(abs_eta < endcaplimit) {
	 H_Etjets_endcap_Z->Fill(Et_jet, weight);
	 H_etajets_endcap_Z->Fill(eta_jet, weight);
	 H_phijets_endcap_Z->Fill(phi_jet, weight);
       }
     } // End loop in normal jets.
     
     // Let's check if the leading jet is in the barrel or in the
     // endcap. If we run in the baseline sample, it should be
     // ALL in the barrel - or else, the previous modules didn't
     // work.
     {
       int cnt = 0;
       for( CandidateCollection::const_iterator jiter = highestjets->begin();
	    jiter != highestjets->end();
	    ++jiter) {
	 
	 double Et_jet = jiter->et();
	 double eta_jet = jiter->eta();
	 double phi_jet = jiter->phi();
	 
	 if(cnt==0) {
	   double abs_eta = fabs(eta_jet);
	   if(abs_eta < barrellimit)
	     H_eff_Z->Fill(barrel, weight);
	   else if(abs_eta < endcaplimit)
	     H_eff_Z->Fill(endcap, weight);
	   else
	     H_eff_Z->Fill(forward, weight);
	 }
	 
	 H_Etjets_Z[cnt]->Fill(Et_jet, weight);
	 H_etajets_Z[cnt]->Fill(eta_jet, weight);
	 H_phijets_Z[cnt]->Fill(phi_jet, weight);
	 ++cnt;
	 
       } // Close loop of 7 highest jets.
     } // Scope the int cnt;

     // Calculate pt of the V from jets.
     
     vptj = sqrt( (sum_px_jet)*(sum_px_jet)+(sum_py_jet)*(sum_py_jet) );
     LogDebug("Values") << "vptj = " << vptj; 
     
     if(njets>=1) {
       H_ptV_jets_1j_Z->Fill(vptj, weight);
       H_ptV_dir_1j_Z->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_1j_Z->Fill(leadingmupt, weight);
	 H_eta1stmu_1j_Z->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_1j_Z->Fill(secondmupt, weight);
	 H_eta2ndmu_1j_Z->Fill(secondmueta, weight);
       }
     }
     if(njets>=2) {
       H_ptV_jets_2j_Z->Fill(vptj, weight);
       H_ptV_dir_2j_Z->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_2j_Z->Fill(leadingmupt, weight);
	 H_eta1stmu_2j_Z->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_2j_Z->Fill(secondmupt, weight);
	 H_eta2ndmu_2j_Z->Fill(secondmueta, weight);
       }
     }
     if(njets>=3) {
       H_ptV_jets_3j_Z->Fill(vptj, weight);
       H_ptV_dir_3j_Z->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_3j_Z->Fill(leadingmupt, weight);
	 H_eta1stmu_3j_Z->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_3j_Z->Fill(secondmupt, weight);
	 H_eta2ndmu_3j_Z->Fill(secondmueta, weight);
       }
     }
     if(njets>=4) {
       H_ptV_jets_4j_Z->Fill(vptj, weight);
       H_ptV_dir_4j_Z->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_4j_Z->Fill(leadingmupt, weight);
	 H_eta1stmu_4j_Z->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_4j_Z->Fill(secondmupt, weight);
	 H_eta2ndmu_4j_Z->Fill(secondmueta, weight);
       }
     }
     
     // Calculate pt of the V from muons and/or MET.
     // This part really depends on if we have found 1, 2 or more muons.
     if(nmuons >= 1) {

       // Will reconstruct as a W.
       // Will use the most energetic muon for that.
       const CandidateCollection* muoncol = muons.product();
       const Candidate& muoncand = muoncol->front();
       CompositeCandidate Wcand;

       Wcand.addDaughter(muoncand);
       Wcand.addDaughter(met);
       AddFourMomenta addP4;
       addP4.set(Wcand);

       double met_phi = met.phi();
       double muon_phi = muoncand.phi();
       double muon_pt = muoncand.pt();
       double dphi = deltaPhi(met_phi, muon_phi);
       
       double W_pt = Wcand.pt();
       double W_mass = Wcand.mass();
       double tmsq = 2*muon_pt*met_pt*(1-cos(dphi));
       double transv_mass = sqrt(tmsq);
       
       LogDebug("Values") << "Reco as W: (muon + MET) W_pt = " << W_pt;
       LogDebug("Values") << "Reco as W: (muon + MET) W_mass = " << W_mass;

       H_ptV_mumet_Z->Fill(W_pt, weight);
       H_invmass_mumet_Z->Fill(W_mass, weight);

       if(njets>=1)	
	 H_transvmass_1j_Z->Fill(transv_mass, weight);
       if(njets>=2)
	 H_transvmass_2j_Z->Fill(transv_mass, weight);
       if(njets>=3)
	 H_transvmass_3j_Z->Fill(transv_mass, weight);
       if(njets>=4)
	 H_transvmass_4j_Z->Fill(transv_mass, weight);
              
       // Since we have only ONE muon, we could try to calculate the
       // neutrino pt from jets and muon.
       double nupx = sum_px_jet + muoncand.px();
       double nupy = sum_py_jet + muoncand.py();
       double nupt_jlep = sqrt(nupx*nupx + nupy*nupy);
	 
       H_ptnu_jlep_Z->Fill(nupt_jlep, weight);
       H_ptnu_dirl_Z->Fill(nupt, weight);
	 
     } // Closes if(nmuons == 1)
     
     if(nmuons >= 2) {
       // Will reconstruct as a Z.
       // Will use the two most energetic muons.
       
       const CandidateCollection *muoncol = muons.product();
       CandidateCollection::const_iterator outmiter=muoncol->begin(); 
       const Candidate& muoncand1 = *outmiter;
       outmiter++;
       const Candidate& muoncand2 = *outmiter;
       CompositeCandidate Zcand;
       
       Zcand.addDaughter(muoncand1);
       Zcand.addDaughter(muoncand2);
       AddFourMomenta addP4;
       addP4.set(Zcand);
       
       double Z_pt = Zcand.pt();
       double Z_mass = Zcand.mass();
       
       LogDebug("Values") << "Reco as Z: (muon + MET) Z_pt = " << Z_pt;
       LogDebug("Values") << "Reco as Z: (muon + MET) Z_mass = " << Z_mass;
       
       if( (Z_mass>Zwindowlow) && (Z_mass<Zwindowhigh) ) {
	 H_invmass_2mu_Z->Fill(Z_mass, weight);
	 
	 // Since we got AT LEAST two muons, let's check what happens to V
	 // pt when I ask for at least 1, 2, 3, 4 jets.
	 if(njets>=1) {
	   H_ptV_mu_1j_Z->Fill(Z_pt, weight);
	   H_ptV_dirmu_1j_Z->Fill(vpt, weight);
	 }
	 if(njets>=2) {
	   H_ptV_mu_2j_Z->Fill(Z_pt, weight);
	   H_ptV_dirmu_2j_Z->Fill(vpt, weight);
	 }
	 if(njets>=3) {
	   H_ptV_mu_3j_Z->Fill(Z_pt, weight);
	   H_ptV_dirmu_3j_Z->Fill(vpt, weight);
	 }
	 if(njets>=4) {
	   H_ptV_mu_4j_Z->Fill(Z_pt, weight);
	   H_ptV_dirmu_4j_Z->Fill(vpt, weight);
	 }
       }

     } // Closes if(nmuons >= 2)
       
     if(nmuons > 2) {
       
       const CandidateCollection *muoncol = muons.product();
       CandidateCollection::const_iterator outmiter=muoncol->begin(); 
       CandidateCollection::const_iterator endmiter=muoncol->end(); 

       // Potentially unsafe...
       const Candidate& muoncand1 = *outmiter;
       outmiter++;
       const Candidate& muoncand2 = *outmiter;
       outmiter++;
       const Candidate& muoncand3 = *outmiter;

       CompositeCandidate Zcand12;
       CompositeCandidate Zcand13;
       CompositeCandidate Zcand23;

       Zcand12.addDaughter(muoncand1);
       Zcand12.addDaughter(muoncand2);
       Zcand13.addDaughter(muoncand1);
       Zcand13.addDaughter(muoncand3);
       Zcand23.addDaughter(muoncand2);
       Zcand23.addDaughter(muoncand3);
       AddFourMomenta addP4;
       addP4.set(Zcand12);
       addP4.set(Zcand13);
       addP4.set(Zcand23);

       double muphi1 = muoncand1.phi();
       double muphi2 = muoncand2.phi();
       double muphi3 = muoncand3.phi();
       
       double Z_m12 = Zcand12.mass();
       double Z_m13 = Zcand13.mass();
       double Z_m23 = Zcand23.mass();
	 
       double dphi12 = deltaPhi(muphi1, muphi2);
       double dphi13 = deltaPhi(muphi1, muphi3);
       double dphi23 = deltaPhi(muphi2, muphi3);
       
       H_invmass_mu12_Z->Fill(Z_m12, weight);
       H_invmass_mu13_Z->Fill(Z_m13, weight);
       H_invmass_mu23_Z->Fill(Z_m23, weight);
       H_dphi_mu12_Z->Fill(dphi12, weight);
       H_dphi_mu13_Z->Fill(dphi13, weight);
       H_dphi_mu23_Z->Fill(dphi23, weight);
	 
     } // Closes if(nmuons > 2)
     
     // Finally, compare neutrino pt true with MET.
     H_ptnu_direct_Z->Fill(nupt, weight);
     H_pt_met_Z->Fill(met_pt, weight); 

     break;
     // *******************************************
     
   case 3:
     
     // Histogram number of jets.
     H_tnumJets_tt->Fill(njets, weight);
     if(njets!=0) {
       H_tbarrel_tt->Fill(perc_barrel, weight);
       H_tendcap_tt->Fill(perc_endcap, weight);
     }

     // Histogram mass, calc mass, pt, Et, eta, phi of all jets.
     for( CandidateCollection::const_iterator jiter = jets->begin();
	  jiter != jets->end();
	  ++jiter) {

       double E_jet = jiter->energy();
       double px_jet = jiter->px();
       double py_jet = jiter->py();
       double pz_jet = jiter->pz();
       double m_jet = jiter->mass();
                  
       double mcalc_jet = 0;
       double mcalc_jetsq = E_jet*E_jet - (px_jet*px_jet +
					 py_jet*py_jet +
					 pz_jet*pz_jet);
       
       if(mcalc_jetsq > 0)
	 mcalc_jet = sqrt(mcalc_jetsq);
       else {
         LogWarning("DomainError") << "Jet with negative calculated m^2. Mcalc set to -0.5";
	 mcalc_jet = -0.5;
       }
       
       double Et_jet = jiter->et();
       double pt_jet = jiter->pt();
       double eta_jet = jiter->eta();
       double phi_jet = jiter->phi();
       
       H_m_tJets_tt->Fill(m_jet, weight);
       H_mcalc_tJets_tt->Fill(mcalc_jet, weight);
       H_Et_tJets_tt->Fill(Et_jet, weight);
       H_pt_tJets_tt->Fill(pt_jet, weight);
       H_eta_tJets_tt->Fill(eta_jet, weight);
       H_phi_tJets_tt->Fill(phi_jet, weight);

       double abs_eta = fabs(eta_jet);
       if(abs_eta < barrellimit) {
	 H_Etjets_barrel_tt->Fill(Et_jet, weight);
	 H_etajets_barrel_tt->Fill(eta_jet, weight);
	 H_phijets_barrel_tt->Fill(phi_jet, weight);
       }
       else if(abs_eta < endcaplimit) {
	 H_Etjets_endcap_tt->Fill(Et_jet, weight);
	 H_etajets_endcap_tt->Fill(eta_jet, weight);
	 H_phijets_endcap_tt->Fill(phi_jet, weight);
       }
     } // End loop in normal jets.
     
     // Let's check if the leading jet is in the barrel or in the
     // endcap. If we run in the baseline sample, it should be
     // ALL in the barrel - or else, the previous modules didn't
     // work.
     {
       int cnt = 0;
       for( CandidateCollection::const_iterator jiter = highestjets->begin();
	    jiter != highestjets->end();
	    ++jiter) {
	 
	 double Et_jet = jiter->et();
	 double eta_jet = jiter->eta();
	 double phi_jet = jiter->phi();
	 
	 if(cnt==0) {
	   double abs_eta = fabs(eta_jet);
	   if(abs_eta < barrellimit)
	     H_eff_tt->Fill(barrel, weight);
	   else if(abs_eta < endcaplimit)
	     H_eff_tt->Fill(endcap, weight);
	   else
	     H_eff_tt->Fill(forward, weight);
	 }
	 
	 H_Etjets_tt[cnt]->Fill(Et_jet, weight);
	 H_etajets_tt[cnt]->Fill(eta_jet, weight);
	 H_phijets_tt[cnt]->Fill(phi_jet, weight);
	 ++cnt;
	 
       } // Close loop of 7 highest jets.
     } // Scope the int cnt;

     // Calculate pt of the V from jets.
     
     vptj = sqrt( (sum_px_jet)*(sum_px_jet)+(sum_py_jet)*(sum_py_jet) );
     LogDebug("Values") << "vptj = " << vptj; 
     
     if(njets>=1) {
       H_ptV_jets_1j_tt->Fill(vptj, weight);
       H_ptV_dir_1j_tt->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_1j_tt->Fill(leadingmupt, weight);
	 H_eta1stmu_1j_tt->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_1j_tt->Fill(secondmupt, weight);
	 H_eta2ndmu_1j_tt->Fill(secondmueta, weight);
       }
     }
     if(njets>=2) {
       H_ptV_jets_2j_tt->Fill(vptj, weight);
       H_ptV_dir_2j_tt->Fill(vpt, weight);
       if(nmuons > 0) {
       H_pt1stmu_2j_tt->Fill(leadingmupt, weight);
       H_eta1stmu_2j_tt->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_2j_tt->Fill(secondmupt, weight);
	 H_eta2ndmu_2j_tt->Fill(secondmueta, weight);
       }
     }
     if(njets>=3) {
       H_ptV_jets_3j_tt->Fill(vptj, weight);
       H_ptV_dir_3j_tt->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_3j_tt->Fill(leadingmupt, weight);
	 H_eta1stmu_3j_tt->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_3j_tt->Fill(secondmupt, weight);
	 H_eta2ndmu_3j_tt->Fill(secondmueta, weight);
       }
     }
     if(njets>=4) {
       H_ptV_jets_4j_tt->Fill(vptj, weight);
       H_ptV_dir_4j_tt->Fill(vpt, weight);
       if(nmuons > 0) {
	 H_pt1stmu_4j_tt->Fill(leadingmupt, weight);
	 H_eta1stmu_4j_tt->Fill(leadingmueta, weight);
       }
       if(nmuons > 1) {
	 H_pt2ndmu_4j_tt->Fill(secondmupt, weight);
	 H_eta2ndmu_4j_tt->Fill(secondmueta, weight);
       }
     }
     
     // Calculate pt of the V from muons and/or MET.
     // This part really depends on if we have found 1, 2 or more muons.
     if(nmuons >= 1) {

       // Will reconstruct as a W.
       // Will use the most energetic muon for that.
       const CandidateCollection* muoncol = muons.product();
       const Candidate& muoncand = muoncol->front();
       CompositeCandidate Wcand;

       Wcand.addDaughter(muoncand);
       Wcand.addDaughter(met);
       AddFourMomenta addP4;
       addP4.set(Wcand);

       double met_phi = met.phi();
       double muon_phi = muoncand.phi();
       double muon_pt = muoncand.pt();
       double dphi = deltaPhi(met_phi, muon_phi);
       
       double W_pt = Wcand.pt();
       double W_mass = Wcand.mass();
       double tmsq = 2*muon_pt*met_pt*(1-cos(dphi));
       double transv_mass = sqrt(tmsq);
       
       LogDebug("Values") << "Reco as W: (muon + MET) W_pt = " << W_pt;
       LogDebug("Values") << "Reco as W: (muon + MET) W_mass = " << W_mass;

       H_ptV_mumet_tt->Fill(W_pt, weight);
       H_invmass_mumet_tt->Fill(W_mass, weight);
      
       if(njets>=1)	
	 H_transvmass_1j_tt->Fill(transv_mass, weight);
       if(njets>=2)
	 H_transvmass_2j_tt->Fill(transv_mass, weight);
       if(njets>=3)
	 H_transvmass_3j_tt->Fill(transv_mass, weight);
       if(njets>=4)
	 H_transvmass_4j_tt->Fill(transv_mass, weight);

       // Since we have only ONE muon, we could try to calculate the
       // neutrino pt from jets and muon.
       double nupx = sum_px_jet + muoncand.px();
       double nupy = sum_py_jet + muoncand.py();
       double nupt_jlep = sqrt(nupx*nupx + nupy*nupy);
	 
       H_ptnu_jlep_tt->Fill(nupt_jlep, weight);
       H_ptnu_dirl_tt->Fill(nupt, weight);
	 
     } // Closes if(nmuons == 1)
     
     if(nmuons >= 2) {
       // Will reconstruct as a Z.
       // Will use the two most energetic muons.
       
       const CandidateCollection *muoncol = muons.product();
       CandidateCollection::const_iterator outmiter=muoncol->begin(); 
       const Candidate& muoncand1 = *outmiter;
       outmiter++;
       const Candidate& muoncand2 = *outmiter;
       CompositeCandidate Zcand;
       
       Zcand.addDaughter(muoncand1);
       Zcand.addDaughter(muoncand2);
       AddFourMomenta addP4;
       addP4.set(Zcand);
       
       double Z_pt = Zcand.pt();
       double Z_mass = Zcand.mass();
       
       LogDebug("Values") << "Reco as Z: (muon + MET) Z_pt = " << Z_pt;
       LogDebug("Values") << "Reco as Z: (muon + MET) Z_mass = " << Z_mass;
       
       if( (Z_mass>Zwindowlow) && (Z_mass<Zwindowhigh) ) {
	 H_invmass_2mu_tt->Fill(Z_mass, weight);
	 
	 // Since we got AT LEAST two muons, let's check what happens to V
	 // pt when I ask for at least 1, 2, 3, 4 jets.
	 if(njets>=1) {
	   H_ptV_mu_1j_tt->Fill(Z_pt, weight);
	   H_ptV_dirmu_1j_tt->Fill(vpt, weight);
	 }
	 if(njets>=2) {
	   H_ptV_mu_2j_tt->Fill(Z_pt, weight);
	   H_ptV_dirmu_2j_tt->Fill(vpt, weight);
	 }
	 if(njets>=3) {
	   H_ptV_mu_3j_tt->Fill(Z_pt, weight);
	   H_ptV_dirmu_3j_tt->Fill(vpt, weight);
	 }
	 if(njets>=4) {
	   H_ptV_mu_4j_tt->Fill(Z_pt, weight);
	   H_ptV_dirmu_4j_tt->Fill(vpt, weight);
	 }
       }

     } // Closes if(nmuons >= 2)
       
     if(nmuons > 2) {
       
       const CandidateCollection *muoncol = muons.product();
       CandidateCollection::const_iterator outmiter=muoncol->begin(); 
       CandidateCollection::const_iterator endmiter=muoncol->end(); 

       // Potentially unsafe...
       const Candidate& muoncand1 = *outmiter;
       outmiter++;
       const Candidate& muoncand2 = *outmiter;
       outmiter++;
       const Candidate& muoncand3 = *outmiter;

       CompositeCandidate Zcand12;
       CompositeCandidate Zcand13;
       CompositeCandidate Zcand23;

       Zcand12.addDaughter(muoncand1);
       Zcand12.addDaughter(muoncand2);
       Zcand13.addDaughter(muoncand1);
       Zcand13.addDaughter(muoncand3);
       Zcand23.addDaughter(muoncand2);
       Zcand23.addDaughter(muoncand3);
       AddFourMomenta addP4;
       addP4.set(Zcand12);
       addP4.set(Zcand13);
       addP4.set(Zcand23);

       double muphi1 = muoncand1.phi();
       double muphi2 = muoncand2.phi();
       double muphi3 = muoncand3.phi();
       
       double Z_m12 = Zcand12.mass();
       double Z_m13 = Zcand13.mass();
       double Z_m23 = Zcand23.mass();
	 
       double dphi12 = deltaPhi(muphi1, muphi2);
       double dphi13 = deltaPhi(muphi1, muphi3);
       double dphi23 = deltaPhi(muphi2, muphi3);
       
       H_invmass_mu12_tt->Fill(Z_m12, weight);
       H_invmass_mu13_tt->Fill(Z_m13, weight);
       H_invmass_mu23_tt->Fill(Z_m23, weight);
       H_dphi_mu12_tt->Fill(dphi12, weight);
       H_dphi_mu13_tt->Fill(dphi13, weight);
       H_dphi_mu23_tt->Fill(dphi23, weight);
	 
     } // Closes if(nmuons > 2)
     
     // Finally, compare neutrino pt true with MET.
     H_ptnu_direct_tt->Fill(nupt, weight);
     H_pt_met_tt->Fill(met_pt, weight); 
     
     break;
     // *******************************************

   } // Closes the switch.

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

//define this as a plug-in
DEFINE_FWK_MODULE(VnjetAnalyzer);
