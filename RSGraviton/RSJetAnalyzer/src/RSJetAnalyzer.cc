// -*- C++ -*-
//
// Package:    RSJetAnalyzer
// Class:      RSJetAnalyzer
// 
/**\class RSJetAnalyzer RSJetAnalyzer.cc RSGraviton/RSJetAnalyzer/src/RSJetAnalyzer.cc

Description: Class to analyze jets in RS->jets events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSJetAnalyzer.cc,v 1.1 2008/05/02 10:58:19 tomei Exp $
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

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "DataFormats/Candidate/interface/CandMatchMap.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
//
// class decleration
//

class RSJetAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSJetAnalyzer(const edm::ParameterSet&);
  ~RSJetAnalyzer();

private:
  void assignZDaughters(double&, double&, const reco::Candidate&, const reco::Candidate&);
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  // ----------member data ---------------------------
  std::vector<reco::LeafCandidate> Jet1Particles;
  std::vector<reco::LeafCandidate> Jet2Particles;
  std::vector<reco::LeafCandidate> Jet1ZDaughters;
  std::vector<reco::LeafCandidate> Jet2ZDaughters;
  
  TH1F*     h_dR;
  TH1F*     h_dPhi;
  TH2F*     h_EtCorrelation; 
  TH2F*     h_EtaCorrelation;  
  TH2F*     h_PhiCorrelation;  
  TH2F*     h_MassCorrelation; 
  TH1F*     h_Jet1_NumParticles;
  TH1F*     h_Jet2_NumParticles;

  TH2F* h_Jet1_dRZxMass;
  TH2F* h_Jet1_dRZxNumParticles;
  TH2F* h_Jet1_dRZxEt;

  TH2F* h_Jet1_dRDauxMass;
  TH2F* h_Jet1_dRDauxNumParticles;
  TH2F* h_Jet1_dRDauxZpt;

  TH2F* h_MassxNumParticles;
  TH2F* h_Jet1EtxdRDau;
  TH2F* h_Jet1EtxNumParticles;
  TH2F* h_Jet1EtxMass;
  TH2F* h_Jet1EtxEta;
};

//
// constants, enums and typedefs
//
const int Z_id = 23;

//
// static data member definitions
//

//
// constructors and destructor
//
RSJetAnalyzer::RSJetAnalyzer(const edm::ParameterSet& iConfig)
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_dR                  = fs->make<TH1F>( "dR"  , "dR", 200,  0., 20.);
  h_dPhi                = fs->make<TH1F>( "dPhi"  , "dPhi", 144,  0., M_PI);
  h_EtCorrelation       = fs->make<TH2F>( "etCorrelation", "etCorrelation", 400, 0., 1000., 400, 0., 1000.);
  h_EtaCorrelation      = fs->make<TH2F>( "etaCorrelation", "etaCorrelation", 400, -4., 4., 400, -4., 4.);
  h_PhiCorrelation      = fs->make<TH2F>( "phiCorrelation", "phiCorrelation", 144, -M_PI, M_PI, 144, -M_PI, M_PI);
  h_MassCorrelation     = fs->make<TH2F>( "massCorrelation", "massCorrelation", 400, 0., 1000., 400, 0., 1000.); 
  h_Jet1_NumParticles   = fs->make<TH1F>( "jet1Particles", "jet1Particles", 500, 0.5, 500.5);
  h_Jet2_NumParticles   = fs->make<TH1F>( "jet2Particles", "jet2Particles", 500, 0.5, 500.5);

  h_Jet1_dRZxMass         = fs->make<TH2F>( "jet1dRZMass", "jet1dRZMass", 200, 0., 4., 400, 0., 1000.);
  h_Jet1_dRZxNumParticles = fs->make<TH2F>( "jet1dRZParticles", "jet1dRZParticles", 200, 0., 4., 500, 0.5, 500.5);
  h_Jet1_dRZxEt          = fs->make<TH2F>( "jet1dRZEt", "jet1dRZEt", 200, 0., 4., 400, 0., 1000.); 
  
  h_Jet1_dRDauxMass         = fs->make<TH2F>( "jet1dRDauMass", "jet1dRDauMass", 200, 0., 4., 400, 0., 1000.); 
  h_Jet1_dRDauxNumParticles = fs->make<TH2F>( "jet1dRDauParticles", "jet1dRDauParticles", 200, 0., 4., 500, 0.5, 500.5); 
  h_Jet1_dRDauxZpt          = fs->make<TH2F>( "jet1dRDauZPt", "jet1dRDauZPt", 200, 0., 4., 400, 0., 1000.); 
  
  h_MassxNumParticles   = fs->make<TH2F>( "jet1MassParticles", "jet1MassParticles", 400, 0., 1000., 500, 0.5, 500.5); 
  h_Jet1EtxdRDau        = fs->make<TH2F>( "jet1EtdRDau", "jet1EtdRDau", 400, 0., 1000., 400, 0., 4.); 
  h_Jet1EtxNumParticles = fs->make<TH2F>( "jet1EtParticles", "jet1EtParticles", 400, 0., 1000., 500, 0.5, 500.5); 
  h_Jet1EtxMass         = fs->make<TH2F>( "jet1EtMass", "jet1EtMass", 400, 0., 1000., 400, 0., 1000.);
  h_Jet1EtxEta          = fs->make<TH2F>( "jet1EtEta", "jet1EtEta", 400, 0., 1000., 400, -4., 4.); 
}


RSJetAnalyzer::~RSJetAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSJetAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;

  Handle<View<Candidate> > jetsHandle;
  Handle<View<Candidate> > ZsHandle;
  Handle<CandidateCollection> particlesHandle;

  iEvent.getByLabel("twoJets",jetsHandle);
  iEvent.getByLabel("trueZs", ZsHandle);
  iEvent.getByLabel("genParticleCandidates", particlesHandle);
  
  //  std::cout << jetsHandle->size() << " jets" << std::endl;
  //  std::cout << ZsHandle->size() << " Zs" << std::endl;

  // For now, this class only analyzes a collection of two jets and two Zs
  const Candidate & Jet1 = (* jetsHandle)[0];
  const Candidate & Jet2 = (* jetsHandle)[1];
  const Candidate & Z1 = (* ZsHandle)[0];
  const Candidate & Z2 = (* ZsHandle)[1];
  
  // Fills basic histos about these two jets.
  double dR = deltaR(Jet1.eta(), Jet1.phi(), Jet2.eta(), Jet2.phi());
  double dphi = fabs(deltaPhi(Jet1.phi(), Jet2.phi()));
  h_dR->Fill(dR);
  h_dPhi->Fill(dphi);
  
  h_EtCorrelation->Fill(Jet1.et(), Jet2.et());
  h_EtaCorrelation->Fill(Jet1.eta(), Jet2.eta());
  h_PhiCorrelation->Fill(Jet1.phi(), Jet2.phi());
  h_MassCorrelation->Fill(Jet1.mass(), Jet2.mass());
  
  // Find the particles inside, and put them in Jet1Particles
  // and Jet2Particles.
  Jet1Particles.clear();
  Jet2Particles.clear();
  double jetradius=0.7;

  for(CandidateCollection::const_iterator piter = particlesHandle->begin();
      piter != particlesHandle->end(); ++piter) {
    double dR1 = deltaR(Jet1.eta(),Jet1.phi(),piter->eta(),piter->phi());
    double dR2 = deltaR(Jet2.eta(),Jet2.phi(),piter->eta(),piter->phi());
    if(dR1 < jetradius)
      Jet1Particles.push_back
	(LeafCandidate(piter->charge(), piter->p4(), piter->vertex(), piter->pdgId(), piter->status()));
    if(dR2 < jetradius) 
      Jet2Particles.push_back
	(LeafCandidate(piter->charge(), piter->p4(), piter->vertex(), piter->pdgId(), piter->status()));
  }
  int nParticlesJet1 = Jet1Particles.size();
  int nParticlesJet2 = Jet2Particles.size();
  h_Jet1_NumParticles->Fill(nParticlesJet1);
  h_Jet2_NumParticles->Fill(nParticlesJet2);

  // Z X jet analysis.
  // Assign each jet to a Z. "inverse" means Jet1 with Z2, Jet2 with Z1.
  double dRJet1 = 0.;
  double dRJet2 = 0.;
  double dRJet1Z1 = deltaR(Jet1.eta(), Jet1.phi(), Z1.eta(), Z1.phi()); 
  double dRJet1Z2 = deltaR(Jet1.eta(), Jet1.phi(), Z2.eta(), Z2.phi()); 
  double dRJet2Z1 = deltaR(Jet2.eta(), Jet2.phi(), Z1.eta(), Z1.phi()); 
  double dRJet2Z2 = deltaR(Jet2.eta(), Jet2.phi(), Z1.eta(), Z1.phi()); 
  bool inverse = false;
  if(dRJet1Z1 < dRJet1Z2) {
    dRJet1 = dRJet1Z1;
    dRJet2 = dRJet2Z2;
    inverse = false;
  }
  else { 
    dRJet1 = dRJet1Z2;
    dRJet2 = dRJet2Z1;
    inverse = true;
  }

  // Get the Z daughters of each Z associated to each jet.
  
  double Jet1Zpt = 0;
  double Jet2Zpt = 0;
  Jet1ZDaughters.clear();
  Jet2ZDaughters.clear();
  
  if(!inverse)
    this->assignZDaughters(Jet1Zpt, Jet2Zpt, Z1, Z2);
  else
    this->assignZDaughters(Jet1Zpt, Jet2Zpt, Z2, Z1);

  // Calculate the dR in between each Z's daughters, and do some plots. 

  double Jet1dRZDaughters;
  
  Jet1dRZDaughters = deltaR(Jet1ZDaughters.at(0).eta(), Jet1ZDaughters.at(0).phi(),
			    Jet1ZDaughters.at(1).eta(), Jet1ZDaughters.at(1).phi());
  
  h_Jet1_dRZxMass->Fill(dRJet1, Jet1.mass());
  h_Jet1_dRZxNumParticles->Fill(dRJet1, nParticlesJet1);
  h_Jet1_dRZxEt->Fill(dRJet1, Jet1.et());

  h_Jet1_dRDauxMass->Fill(Jet1dRZDaughters, Jet1.mass());
  h_Jet1_dRDauxNumParticles->Fill(Jet1dRZDaughters, nParticlesJet1);
  h_Jet1_dRDauxZpt->Fill(Jet1dRZDaughters, Jet1Zpt);

  h_MassxNumParticles->Fill(Jet1.mass(), nParticlesJet1);
  h_Jet1EtxdRDau->Fill(Jet1.et(),Jet1dRZDaughters);
  h_Jet1EtxNumParticles->Fill(Jet1.et(),nParticlesJet1);
  h_Jet1EtxMass->Fill(Jet1.et(),Jet1.mass());
  h_Jet1EtxEta->Fill(Jet1.et(),Jet1.eta());
}

void
RSJetAnalyzer::assignZDaughters(double& Jet1Zpt, double& Jet2Zpt , const reco::Candidate& Z1, const reco::Candidate& Z2) {
  
  Jet1Zpt = Z1.pt();
  Jet2Zpt = Z2.pt();
  
    // Get the Zdaughters of Jet1;
  for(unsigned int daunum = 0; daunum != Z1.numberOfDaughters(); ++daunum) {
    if(Z1.daughter(daunum)->pdgId() != Z_id)
      Jet1ZDaughters.push_back(reco::LeafCandidate(Z1.daughter(daunum)->charge(), 
						   Z1.daughter(daunum)->p4(), 
						   Z1.daughter(daunum)->vertex(), 
						   Z1.daughter(daunum)->pdgId(), 
						   Z1.daughter(daunum)->status() ) );
  }
  // Get the Zdaughters of Jet2;
  for(unsigned int daunum = 0; daunum != Z2.numberOfDaughters(); ++daunum) {
    if(Z2.daughter(daunum)->pdgId() != Z_id)
      Jet2ZDaughters.push_back(reco::LeafCandidate(Z2.daughter(daunum)->charge(), 
						   Z2.daughter(daunum)->p4(), 
						   Z2.daughter(daunum)->vertex(), 
						   Z2.daughter(daunum)->pdgId(), 
						   Z2.daughter(daunum)->status() ) );
  }
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSJetAnalyzer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSJetAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSJetAnalyzer);
