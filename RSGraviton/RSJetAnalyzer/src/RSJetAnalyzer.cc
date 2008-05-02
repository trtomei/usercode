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

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
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
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  // ----------member data ---------------------------
  TH1F*     h_dR;
  TH1F*     h_dPhi;
  TH2F*     h_EtCorrelation; 
  TH2F*     h_EtaCorrelation;  
  TH2F*     h_PhiCorrelation;  
  TH2F*     h_MassCorrelation; 
  TH1F*     h_Jet1_NumParticles;
  TH1F*     h_Jet2_NumParticles;
  TH1F*     h_Jet1_dRTwoParticles;
  TH1F*     h_Jet1_dRJetParticle;
  TH1F*     h_Jet2_dRTwoParticles;
  TH1F*     h_Jet2_dRJetParticle;
  TProfile* p_Jet1_FracxRadius;
  TProfile* p_Jet2_FracxRadius;
  TProfile* p_Jet1_Density;
  TProfile* p_Jet2_Density;
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
  h_Jet1_dRTwoParticles = fs->make<TH1F>( "Jet1dRTwoParticles", "Jet1dRTwoParticles", 70, 0., 0.7);
  h_Jet1_dRJetParticle  = fs->make<TH1F>( "Jet1dRJetParticle", "Jet1dRJetParticle", 70, 0., 0.7);
  h_Jet2_dRTwoParticles = fs->make<TH1F>( "Jet2dRTwoParticles", "Jet2dRTwoParticles", 70, 0., 0.7);
  h_Jet2_dRJetParticle  = fs->make<TH1F>( "Jet2dRJetParticle", "Jet2dRJetParticle", 70, 0., 0.7);
  p_Jet1_FracxRadius    = fs->make<TProfile>( "jet1Etprofile"  , "jet1Etprofile", 66,  0.045, 0.705);
  p_Jet2_FracxRadius    = fs->make<TProfile>( "jet2Etprofile"  , "jet2Etprofile", 66,  0.045, 0.705);
  p_Jet1_Density        = fs->make<TProfile>( "jet1Density", "jet1Density", 66, 0.045, 0.705);
  p_Jet2_Density        = fs->make<TProfile>( "jet2Density", "jet2Density", 66, 0.045, 0.705);
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
  Handle<CandidateCollection> particlesHandle;
  iEvent.getByLabel("twoJets",jetsHandle);
  iEvent.getByLabel("genParticlesAllStable", particlesHandle);
  
  // For now, this class only analyzes a collection of two jets.
  const Candidate & Jet1 = (* jetsHandle)[0];
  const Candidate & Jet2 = (* jetsHandle)[1];

  // Fills basic histos about these two jets.
  double dR = deltaR(Jet1.eta(), Jet1.phi(), Jet2.eta(), Jet2.phi());
  double dphi = fabs(deltaPhi(Jet1.phi(), Jet2.phi()));
  h_dR->Fill(dR);
  h_dPhi->Fill(dphi);
  
  h_EtCorrelation->Fill(Jet1.et(), Jet2.et());
  h_EtaCorrelation->Fill(Jet1.eta(), Jet2.eta());
  h_PhiCorrelation->Fill(Jet1.phi(), Jet2.phi());
  h_MassCorrelation->Fill(Jet1.mass(), Jet2.mass());

  double minradius = 0.05;
  double maxradius = 0.705;
  double step = 0.01;
  // 66 steps: steps = (maxradius - minradius)/step + 1

  // Calculates for each subradius the sumEt/JetEt of
  // particles inside, for each jet, and fills a TProfile.
  // Also normalizing to the radius square.
  for(double radius = minradius; radius < maxradius; radius += step) {
    //    math::GlobalVector subJet1;
    //    math::GlobalVector subJet2;
    double sumEtJet1 = 0.;
    double sumEtJet2 = 0.;
    
    for(CandidateCollection::const_iterator piter = particlesHandle->begin();
	piter != particlesHandle->end(); ++piter) {
      // Check if the particle is inside of the jets.
      double dRJet1Particle = deltaR(Jet1.eta(),Jet1.phi(),piter->eta(),piter->phi());
      double dRJet2Particle = deltaR(Jet2.eta(),Jet2.phi(),piter->eta(),piter->phi());
      if(dRJet1Particle < radius) {
	//	math::GlobalVector particle(piter->px(),piter->py(),piter->pz());
	//	subJet1 += particle;
	sumEtJet1 += piter->et();
      }
      if(dRJet2Particle < radius) {
	//	math::GlobalVector particle(piter->px(),piter->py(),piter->pz());
	//	subJet2 += particle;
	sumEtJet2 += piter->et();
      }
    }
    //    p_Jet1_FracxRadius->Fill(sqrt(radius,subJet1.perp2())/Jet1.et());
    //    p_Jet2_FracxRadius->Fill(sqrt(radius,subJet2.perp2())/Jet2.et());
    p_Jet1_FracxRadius->Fill(radius,sumEtJet1/Jet1.et());
    p_Jet2_FracxRadius->Fill(radius,sumEtJet2/Jet2.et());
    p_Jet1_Density->Fill(radius,(sumEtJet1/Jet1.et())/(radius*radius));
    p_Jet2_Density->Fill(radius,(sumEtJet2/Jet2.et())/(radius*radius));
  }

  // Calculates, for each jet, the number of particles inside.
  // Also, find the two most energetic particles inside the jet
  // and calculate their mutual distance and distance of the first to the jet axis.
  std::vector<LeafCandidate> Jet1Particles;
  std::vector<LeafCandidate> Jet2Particles;
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

  // For the first jet
  double firstMaxPt = 0.;
  double secondMaxPt = 0.;
  int firstParticle = 0;
  int secondParticle = 0;
  for(int i = 0; i != nParticlesJet1; ++i) {
    if(Jet1Particles.at(i).pt() > firstMaxPt) {
      secondParticle = firstParticle;
      secondMaxPt = firstMaxPt;
      firstParticle = i;
      firstMaxPt = Jet1Particles.at(i).pt();
    }
    else if(Jet1Particles.at(i).pt() > secondMaxPt) {
      secondParticle = i;
      secondMaxPt = Jet1Particles.at(i).pt();
    }
  }

  double dRTwoParticles = deltaR(Jet1Particles.at(firstParticle).eta(), Jet1Particles.at(firstParticle).phi(),  
				 Jet1Particles.at(secondParticle).eta(), Jet1Particles.at(secondParticle).phi());
  double dRJetParticle = deltaR(Jet1Particles.at(firstParticle).eta(), Jet1Particles.at(firstParticle).phi(),  
				Jet1.eta(), Jet1.phi());
  h_Jet1_dRTwoParticles->Fill(dRTwoParticles);
  h_Jet1_dRJetParticle->Fill(dRJetParticle);

  // For the second jet
  firstMaxPt = 0.;
  secondMaxPt = 0.;
  firstParticle = 0;
  secondParticle = 0;
  for(int i = 0; i != nParticlesJet2; ++i) {
    if(Jet2Particles.at(i).pt() > firstMaxPt) {
      secondParticle = firstParticle;
      secondMaxPt = firstMaxPt;
      firstParticle = i;
      firstMaxPt = Jet2Particles.at(i).pt();
    }
    else if(Jet2Particles.at(i).pt() > secondMaxPt) {
      secondParticle = i;
      secondMaxPt = Jet2Particles.at(i).pt();
    }
  }

  dRTwoParticles = deltaR(Jet2Particles.at(firstParticle).eta(), Jet2Particles.at(firstParticle).phi(),  
				 Jet2Particles.at(secondParticle).eta(), Jet2Particles.at(secondParticle).phi());
  dRJetParticle = deltaR(Jet2Particles.at(firstParticle).eta(), Jet2Particles.at(firstParticle).phi(),  
				Jet2.eta(), Jet2.phi());
  h_Jet2_dRTwoParticles->Fill(dRTwoParticles);
  h_Jet2_dRJetParticle->Fill(dRJetParticle);

  
  h_Jet1_NumParticles->Fill(nParticlesJet1);
  h_Jet2_NumParticles->Fill(nParticlesJet2);
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
