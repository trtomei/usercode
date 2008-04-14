// -*- C++ -*-
//
// Package:    RSAnalyzer
// Class:      RSAnalyzer
// 
/**\class RSAnalyzer RSAnalyzer.cc RSGraviton/RSAnalyzer/src/RSAnalyzer.cc

Description: Thiago's class for analyzing G*->ZZ->2j + nunu and
                                          G*->ZZ->4j events. 

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Feb 13 15:08:56 CET 2008
// $Id: RSAnalyzer.cc,v 1.1 2008/03/20 11:45:59 tomei Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "PhysicsTools/CandUtils/interface/AddFourMomenta.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile.h" 
//
// class decleration
//
bool compare(const reco::GenParticle& x, const reco::GenParticle& y);

class RSAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSAnalyzer(const edm::ParameterSet&);
  ~RSAnalyzer();
  
private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  // ----------member data ---------------------------
  TH1F* h_1stZ_pt;
  TH1F* h_1stZ_eta; 
  TH1F* h_1stZ_phi;
  TH1F* h_2ndZ_pt; 
  TH1F* h_2ndZ_eta; 
  TH1F* h_2ndZ_phi;
  TH1F* h_grav_pt;
  TH1F* h_grav_eta; 
  TH1F* h_grav_phi;
  TH1F* h_numjets;
  TH1F* h_1stjet_Et;
  TH1F* h_1stjet_eta;
  TH1F* h_1stjet_phi;
  TH1F* h_1stjet_mass;
  TH1F* h_2ndjet_Et;
  TH1F* h_2ndjet_eta;
  TH1F* h_2ndjet_phi;
  TH1F* h_2ndjet_mass;
  TH1F* h_3rdjet_Et;
  TH1F* h_3rdjet_eta;
  TH1F* h_3rdjet_phi;
  TH1F* h_3rdjet_mass;
  TH1F* h_4thjet_Et;
  TH1F* h_4thjet_eta;
  TH1F* h_4thjet_phi;
  TH1F* h_4thjet_mass;
//   TH1F* h_dRoneparton;
//   TH1F* h_dRotherparton;
//   TH1F* h_dRtwopartons;
//   TH1F* h_dRZ;
  TH1F* h_MET;
  TH1F* h_recoZ_mass;
  TH1F* h_2ndrecoZ_mass;
  TH1F* h_num_const_1stjet;
  TH1F* h_num_const_2ndjet;
  TH1F* h_num_const_3rdjet;
  TH1F* h_num_const_4thjet;
  TH2F* h_nc_mass_1stjet;
  TH2F* h_nc_mass_2ndjet;
  TH2F* h_nc_mass_3rdjet;
  TH2F* h_nc_mass_4thjet;
  //  TProfile* p_jet_mass_pt;
};

//
// constants, enums and typedefs
//
const int Z_id = 23;
const int grav_id = 5000039;
const double conesize = 0.5;
//
// static data member definitions
//

//
// constructors and destructor
//
RSAnalyzer::RSAnalyzer(const edm::ParameterSet& iConfig)

{
  edm::Service<TFileService> fs;
  h_1stZ_pt    = fs->make<TH1F>( "Z_1st_pt"  , "p_{t}", 100,  0., 1000.);
  h_1stZ_eta   = fs->make<TH1F>( "Z_1st_eta"  , "#eta", 50,  -5., 5.);
  h_1stZ_phi   = fs->make<TH1F>( "Z_1st_phi"  , "#phi", 72,  -M_PI, M_PI );
  h_2ndZ_pt    = fs->make<TH1F>( "Z_2nd_pt"  , "p_{t}", 100,  0., 1000.);
  h_2ndZ_eta   = fs->make<TH1F>( "Z_2nd_eta"  , "#eta", 50,  -5., 5.);
  h_2ndZ_phi   = fs->make<TH1F>( "Z_2nd_phi"  , "#phi", 50,  -M_PI, M_PI );
  h_grav_pt    = fs->make<TH1F>( "grav_pt"  , "p_{t}", 100,  0., 1000.);
  h_grav_eta   = fs->make<TH1F>( "grav_eta"  , "#eta", 50,  -5., 5.);
  h_grav_phi   = fs->make<TH1F>( "grav_phi"  , "#phi", 72,  -M_PI, M_PI );
  h_numjets    = fs->make<TH1F>( "numjets", "number of jets", 10, -0.5, 9.5);
  h_1stjet_Et  = fs->make<TH1F>( "jet_1st_Et" , "E_{t}", 100, 0., 1000.);
  h_1stjet_eta  = fs->make<TH1F>( "jet_1st_eta" , "eta", 50, -5., 5.);
  h_1stjet_phi  = fs->make<TH1F>( "jet_1st_phi" , "phi", 72, -M_PI, M_PI );
  h_1stjet_mass = fs->make<TH1F>( "jet_1st_mass", "mass", 200, 0., 200.);
  h_2ndjet_Et  = fs->make<TH1F>( "jet_2nd_Et" , "E_{t}", 100, 0., 1000.);
  h_2ndjet_eta  = fs->make<TH1F>( "jet_2nd_eta" , "eta", 50, -5., 5.);
  h_2ndjet_phi  = fs->make<TH1F>( "jet_2nd_phi" , "phi", 72, -M_PI, M_PI );
  h_2ndjet_mass = fs->make<TH1F>( "jet_2nd_mass", "mass", 200, 0., 200.);
  h_3rdjet_Et  = fs->make<TH1F>( "jet_3rd_Et" , "E_{t}", 100, 0., 1000.);
  h_3rdjet_eta  = fs->make<TH1F>( "jet_3rd_eta" , "eta", 50, -5., 5.);
  h_3rdjet_phi  = fs->make<TH1F>( "jet_3rd_phi" , "phi", 72, -M_PI, M_PI );
  h_3rdjet_mass = fs->make<TH1F>( "jet_3rd_mass", "mass", 200, 0., 200.);
  h_4thjet_Et  = fs->make<TH1F>( "jet_4th_Et" , "E_{t}", 100, 0., 1000.);
  h_4thjet_eta  = fs->make<TH1F>( "jet_4th_eta" , "eta", 50, -5., 5.);
  h_4thjet_phi  = fs->make<TH1F>( "jet_4th_phi" , "phi", 72, -M_PI, M_PI );
  h_4thjet_mass = fs->make<TH1F>( "jet_4th_mass", "mass", 200, 0., 200.);
//   h_dRoneparton = fs->make<TH1F>( "dR_oneparton", "dR", 50, 0., 5.);
//   h_dRotherparton = fs->make<TH1F>( "dR_otherparton", "dR", 50, 0., 5.);
//   h_dRZ = fs->make<TH1F>( "dRZ", "dR", 50, 0., 5.);
//   h_dRtwopartons = fs->make<TH1F>( "dR_twopartons", "dR", 50, 0., 5.);
  h_MET = fs->make<TH1F>( "MET", "MET", 100, 0., 1000.);
  h_recoZ_mass = fs->make<TH1F>("recoZ_mass", "mass of reconstructed Z", 1000, 0., 5000.); 
  h_2ndrecoZ_mass = fs->make<TH1F>("recoZ2_mass", "mass of reconstructed Z", 200, 0., 1000.);
  h_num_const_1stjet = fs->make<TH1F>("jet_1st_numconst", "Number of particles", 100, 0., 100.);
  h_num_const_2ndjet = fs->make<TH1F>("jet_2nd_numconst", "Number of particles", 100, 0., 100.);
  h_num_const_3rdjet = fs->make<TH1F>("jet_3rd_numconst", "Number of particles", 100, 0., 100.);
  h_num_const_4thjet = fs->make<TH1F>("jet_4th_numconst", "Number of particles", 100, 0., 100.);
  //  p_jet_mass_pt = fs->make<TProfile>("jet_mass_pt", "jet mass X pt", 50, 0., 500.); 
  h_nc_mass_1stjet = fs->make<TH2F>("jet_1st_ncXmass", "Num. particles X mass", 100, 0., 100., 200, 0., 200.);
  h_nc_mass_2ndjet = fs->make<TH2F>("jet_2nd_ncXmass", "Num. particles X mass", 100, 0., 100., 200, 0., 200.);
  h_nc_mass_3rdjet = fs->make<TH2F>("jet_3rd_ncXmass", "Num. particles X mass", 100, 0., 100., 200, 0., 200.);
  h_nc_mass_4thjet = fs->make<TH2F>("jet_4th_ncXmass", "Num. particles X mass", 100, 0., 100., 200, 0., 200.);

}


RSAnalyzer::~RSAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;

  Handle<GenParticleCollection> genParticles;
  iEvent.getByLabel("genParticles", genParticles);

  Handle<CandidateCollection> stables_handle;
  iEvent.getByLabel("genParticlesAllStableNoNuBSM", stables_handle);
  const CandidateCollection stables = *stables_handle.product();

  Handle<CandidateCollection> partons_handle;
  iEvent.getByLabel("partons", partons_handle);
  const CandidateCollection* partons = partons_handle.product();

  Handle<CandidateCollection> candJets;
  iEvent.getByLabel("candJets", candJets);

  Handle<CandidateCollection> highestJets_handle;
  iEvent.getByLabel("highestJets", highestJets_handle);
  const CandidateCollection* highestJets = highestJets_handle.product();

  Handle<CandidateCollection> met_handle;
  iEvent.getByLabel("genMet", met_handle);

  // PART 1: GenParticles
  // cout << "  // PART 1: GenParticles" << endl;
  GenParticleCollection Zs;
  GenParticle graviton;

  for(GenParticleCollection::const_iterator iter = genParticles->begin(); 
      iter != genParticles->end();
      ++ iter) {
    int id = iter->pdgId();
    int st = iter->status();  
    if(id == Z_id && st == 2) {
      GenParticle thisZ = *iter;
      Zs.push_back(thisZ);
    }
    if(id == grav_id && st == 2)
      graviton = *iter;
  }
  // Ok, got the Zs and the graviton.


  sort(Zs.begin(), Zs.end(), compare);
  reverse(Zs.begin(), Zs.end());

  const GenParticle& firstZ = Zs.at(0);
  const GenParticle& secondZ = Zs.at(1);

  h_1stZ_pt->Fill(firstZ.pt());
  h_1stZ_eta->Fill(firstZ.eta());
  h_1stZ_phi->Fill(firstZ.phi());
  h_2ndZ_pt->Fill(secondZ.pt());
  h_2ndZ_eta->Fill(secondZ.eta());
  h_2ndZ_phi->Fill(secondZ.phi());
  h_grav_pt->Fill(graviton.pt());
  h_grav_eta->Fill(graviton.eta());
  h_grav_phi->Fill(graviton.phi());

  // PART 2: CandJets
  // cout << "  // PART 2: CandJets" << endl;
  int numjets = candJets->size();
  int numhighjets = highestJets->size();
  h_numjets->Fill(numjets);

  // cout << "numjets = " << numjets << endl;
  // cout << "numhighjets = " << numhighjets << endl;
  const Candidate* firstjet = 0; 
  const Candidate* secondjet = 0;
  const Candidate* thirdjet = 0;
  const Candidate* fourthjet = 0;

  int num = 0; 
  if(numhighjets > 0) {
    firstjet = &(*highestJets)[0];
    
    // Get number of constituents
//     int num = countconstituents(firstjet, stables, conesize);
    h_num_const_1stjet->Fill(num);
    
    h_1stjet_Et->Fill(firstjet->et());
    h_1stjet_eta->Fill(firstjet->eta());
    h_1stjet_phi->Fill(firstjet->phi());
    h_1stjet_mass->Fill(firstjet->mass());
    h_nc_mass_1stjet->Fill(num, firstjet->mass());
  }  
  if(numhighjets > 1) {
    // cout << "secondjet" << endl;
    secondjet = &(*highestJets)[1];

//     int num =  countconstituents(secondjet, stables, conesize);
    h_num_const_2ndjet->Fill(num);
    // cout << "the second jet candidate is at" << &(*highestJets)[1] << endl;
    // cout << "secondjet pointer is " << &*secondjet << endl;
    h_2ndjet_Et->Fill(secondjet->et());
    h_2ndjet_eta->Fill(secondjet->eta());
    h_2ndjet_phi->Fill(secondjet->phi());
    h_2ndjet_mass->Fill(secondjet->mass());
    h_nc_mass_2ndjet->Fill(num, secondjet->mass());
  }
  if(numhighjets > 2) {
    // cout << "thirdjet" << endl;
    thirdjet = &(*highestJets)[2];

//     int num = countconstituents(thirdjet, stables, conesize);
    h_num_const_3rdjet->Fill(num);
    // cout << "the third jet candidate is at" << &(*highestJets)[2] << endl;
    // cout << "thirdjet pointer is " << &*thirdjet << endl;
    h_3rdjet_Et->Fill(thirdjet->et());
    h_3rdjet_eta->Fill(thirdjet->eta());
    h_3rdjet_phi->Fill(thirdjet->phi());
    h_3rdjet_mass->Fill(thirdjet->mass());
    h_nc_mass_3rdjet->Fill(num, thirdjet->mass());
  }
  if(numhighjets > 3) {
    // cout << "fourthjet" << endl;
    fourthjet = &(*highestJets)[3];

//     int num = countconstituents(fourthjet, stables, conesize);
    h_num_const_4thjet->Fill(num);
    h_4thjet_Et->Fill(fourthjet->et());
    h_4thjet_eta->Fill(fourthjet->eta());
    h_4thjet_phi->Fill(fourthjet->phi());
    h_4thjet_mass->Fill(fourthjet->mass());
    h_nc_mass_4thjet->Fill(num, fourthjet->mass());
  }

  // cout << "  // PART 3: Matching" << endl;

  // PART 3: Matching
  // This should be reimplemented.
//   const Candidate& oneparton = (*partons)[0];
//   const Candidate& otherparton = (*partons)[1];

//   double dr2p = deltaR(otherparton.eta(), otherparton.phi(),
// 		       oneparton.eta(), oneparton.phi());
//   h_dRtwopartons->Fill(dr2p);
  
//   if(firstjet != 0) {
//     double dr1 = deltaR(firstjet->eta(), firstjet->phi(),
// 			oneparton.eta(), oneparton.phi());
//     double dr2 = deltaR(firstjet->eta(), firstjet->phi(),
// 			otherparton.eta(), otherparton.phi());
//     double drZ1 = deltaR(firstjet->eta(), firstjet->phi(),
// 			 firstZ.eta(), firstZ.phi());
//     double drZ2 = deltaR(firstjet->eta(), firstjet->phi(),
// 			 secondZ.eta(), secondZ.phi());
//     double drZ = min(drZ1, drZ2);

//     h_dRoneparton->Fill(dr1);
//     h_dRotherparton->Fill(dr2);
//     h_dRZ->Fill(drZ);
//   }
  
  // PART 4: MET
  // cout << "PART 4: MET" << endl;
  const CandidateCollection *metcol = met_handle.product();
  const Candidate* met = &metcol->front();
  
  double met_pt = met->pt();
  
  h_MET->Fill(met_pt);

  // PART 5: Reconstructing the Z.
  // cout << "PART 5: Reconstructing the Z" << endl;
  if(numhighjets > 1) {
    CompositeCandidate recoZ;
    recoZ.addDaughter(*firstjet);
    recoZ.addDaughter(*secondjet);
    AddFourMomenta addP4;
    addP4.set(recoZ);
    h_recoZ_mass->Fill(recoZ.mass());
  }
  
  if(numhighjets > 3) {
    CompositeCandidate recoZ;
    recoZ.addDaughter(*thirdjet);
    recoZ.addDaughter(*fourthjet);
    AddFourMomenta addP4;
    addP4.set(recoZ);
    h_2ndrecoZ_mass->Fill(recoZ.mass());
  }

  // cout << "C'est fini!" << endl;
  // PART 6: Jet masses

  //  if(numhighjets > 0)
  //    p_jet_mass_pt->Fill(firstjet->pt(), firstjet->mass());
}

bool compare(const reco::GenParticle& x, const reco::GenParticle& y)
{
  return x.pt() < y.pt();
}

// int RSAnalyzer::countconstituents(const Candidate* jet, const CandidateCollection& particles, double conesize) 
// {
//   int result = 0;
  
//   for(CandidateCollection::const_iterator iter = particles.begin(); 
//       iter != particles.end();
//       ++ iter) {
//     double dr = deltaR(jet->eta(), jet->phi(), iter->eta(), iter->phi());
//     if(dr < conesize)
//       ++result;
//   }
//   return result;
// }

// ------------ method called once each job just before starting event loop  ------------
void 
RSAnalyzer::beginJob(const edm::EventSetup&)
{
  
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSAnalyzer::endJob() {

}

//define this as a plug-in
DEFINE_FWK_MODULE(RSAnalyzer);
