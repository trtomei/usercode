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
// $Id: RSJetAnalyzer.cc,v 1.4 2008/05/17 16:41:32 tomei Exp $
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
#include "FWCore/ParameterSet/interface/InputTag.h"

#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/Math/interface/deltaR.h"
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
  double getMajor(const reco::Jet&) ;
  double getMinor(const reco::Jet&) ;
  // ----------member data ---------------------------

  edm::InputTag jets_;

  TH1F*     h_dR;
  TH1F*     h_dPhi;
  TH2F*     h_EtCorrelation; 
  TH2F*     h_EtaCorrelation;  
  TH2F*     h_PhiCorrelation;  
  TH2F*     h_MassCorrelation; 
  TH1F*     h_Jet1Major;
  TH1F*     h_Jet2Major;
  TH1F*     h_Jet1Minor;
  TH1F*     h_Jet2Minor;
  TH2F*     h_MajorCorrelation;
  TH2F*     h_MinorCorrelation;
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
RSJetAnalyzer::RSJetAnalyzer(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_dR                  = fs->make<TH1F>( "dR"  , "dR", 200,  0., 20.);
  h_dPhi                = fs->make<TH1F>( "dPhi"  , "dPhi", 144,  0., M_PI);
  h_EtCorrelation       = fs->make<TH2F>( "etCorrelation", "etCorrelation", 400, 0., 1000., 400, 0., 1000.);
  h_EtaCorrelation      = fs->make<TH2F>( "etaCorrelation", "etaCorrelation", 400, -4., 4., 400, -4., 4.);
  h_PhiCorrelation      = fs->make<TH2F>( "phiCorrelation", "phiCorrelation", 144, -M_PI, M_PI, 144, -M_PI, M_PI);
  h_MassCorrelation     = fs->make<TH2F>( "massCorrelation", "massCorrelation", 400, 0., 1000., 400, 0., 1000.); 
  h_Jet1Major           = fs->make<TH1F>( "jet1Major", "jet1Major", 500, 0., 5.);
  h_Jet2Major           = fs->make<TH1F>( "jet2Major", "jet2Major", 500, 0., 5.);
  h_Jet1Minor           = fs->make<TH1F>( "jet1Minor", "jet1Minor", 500, 0., 5.);
  h_Jet2Minor           = fs->make<TH1F>( "jet2Minor", "jet2Minor", 500, 0., 5.);
  h_MajorCorrelation    = fs->make<TH2F>( "majorCorrelation", "majorCorrelation", 500, 0., 5., 500, 0., 5.);
  h_MinorCorrelation    = fs->make<TH2F>( "minorCorrelation", "minorCorrelation", 500, 0., 5., 500, 0., 5.);

}


RSJetAnalyzer::~RSJetAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
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

  Handle<CaloJetCollection> jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);

  // For now, this class only analyzes a collection of two jets.
  const Jet & Jet1 = (* jetsHandle)[0];
  const Jet & Jet2 = (* jetsHandle)[1];
  
  // Fills basic histos about these two jets.
  double dR = deltaR(Jet1.eta(), Jet1.phi(), Jet2.eta(), Jet2.phi());
  double dphi = fabs(deltaPhi(Jet1.phi(), Jet2.phi()));
  h_dR->Fill(dR);
  h_dPhi->Fill(dphi);
  
  h_EtCorrelation->Fill(Jet1.et(), Jet2.et());
  h_EtaCorrelation->Fill(Jet1.eta(), Jet2.eta());
  h_PhiCorrelation->Fill(Jet1.phi(), Jet2.phi());
  h_MassCorrelation->Fill(Jet1.mass(), Jet2.mass());
  
  // Get the jets major and minor.
  double jet1Major = getMajor(Jet1);
  double jet2Major = getMajor(Jet2);
  double jet1Minor = getMinor(Jet1);
  double jet2Minor = getMinor(Jet1);
  h_Jet1Major->Fill(jet1Major);
  h_Jet2Major->Fill(jet2Major);
  h_Jet1Minor->Fill(jet1Minor);
  h_Jet2Minor->Fill(jet2Minor);
  h_MajorCorrelation->Fill(jet1Major,jet2Major);
  h_MinorCorrelation->Fill(jet1Minor,jet2Minor);
}

double
RSJetAnalyzer::getMajor(const reco::Jet& jet) {
  double sEtaEta = 0.;
  double sPhiPhi = 0.;
  double sEtaPhi = 0.;
  sEtaEta = jet.etaetaMoment();
  sPhiPhi = jet.phiphiMoment();
  sEtaPhi = jet.etaphiMoment();
  double major = ( sEtaEta + sPhiPhi
		   + sqrt ((sEtaEta-sPhiPhi)*(sEtaEta-sPhiPhi)+4*sEtaPhi*sEtaPhi))/2.0;
  return major;
}

double
RSJetAnalyzer::getMinor(const reco::Jet& jet) {
  double sEtaEta = 0.;
  double sPhiPhi = 0.;
  double sEtaPhi = 0.;
  sEtaEta = jet.etaetaMoment();
  sPhiPhi = jet.phiphiMoment();
  sEtaPhi = jet.etaphiMoment();
  double minor = ( sEtaEta + sPhiPhi
		   + sqrt ((sEtaEta-sPhiPhi)*(sEtaEta-sPhiPhi)+4*sEtaPhi*sEtaPhi))/2.0;
  return minor;
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
