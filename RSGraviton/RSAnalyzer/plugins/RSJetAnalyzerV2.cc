// -*- C++ -*-
//
// Package:    RSJetAnalyzerV2
// Class:      RSJetAnalyzerV2
// 
/**\class RSJetAnalyzerV2 RSJetAnalyzerV2.cc RSGraviton/RSJetAnalyzerV2/src/RSJetAnalyzerV2.cc

Description: Class to analyze jets in RS->jets events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSJetAnalyzerV2.cc,v 1.6 2010/12/23 16:14:24 tomei Exp $
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
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
#include "TH2F.h"
//
// class decleration
//

class RSJetAnalyzerV2 : public edm::EDAnalyzer {
public:
  explicit RSJetAnalyzerV2(const edm::ParameterSet&);
  ~RSJetAnalyzerV2();

private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag jets_;
  unsigned int numberInCollection_;
  TH2F*     h_pT_mass;
  TH2F*     h_pT_energy;
  TH2F*     h_energy_mass;
  TH2F*     h_eta_phi; 
  TH1F*     h_ptOverMass;
  TH1F*     h_ptOverEnergy;
  TH1F*     h_massOverEnergy;
  TH1F* h_pt;
  TH1F* h_eta;
  TH1F* h_mass;
  TH1F* h_chf;
  TH1F* h_nhf;
  TH1F* h_cef;
  TH1F* h_nef;
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
RSJetAnalyzerV2::RSJetAnalyzerV2(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets") ),
  numberInCollection_(iConfig.getParameter<unsigned int>("numberInCollection") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_pT_mass       = fs->make<TH2F>( "pT_mass", "pT X mass", 500, 0., 1000., 500, 0., 1000.);
  h_pT_energy     = fs->make<TH2F>( "pT_energy", "pT X energy", 500, 0., 1000., 500, 0., 1000.);
  h_energy_mass   = fs->make<TH2F>( "energy_mass", "energy X mass", 500, 0., 1000., 500, 0., 1000.);
  h_eta_phi       = fs->make<TH2F>( "eta_phi", "eta X phi", 200,-5.0,5.0,72,-3.141592,3.141592);
  h_ptOverMass    = fs->make<TH1F>( "ptOverMass", "pT over mass", 500, 0., 50.);
  h_ptOverEnergy  = fs->make<TH1F>( "ptOverEnergy", "pT over energy", 50, 0., 1.);
  h_massOverEnergy= fs->make<TH1F>( "massOverEnergy", "mass over energy",50,0., 1.);
  h_pt            = fs->make<TH1F>( "pt", "pt",1000, 0., 2000.);
  h_eta           = fs->make<TH1F>( "eta", "eta",80, -4.0, 4.0);
  h_mass          = fs->make<TH1F>( "mass", "mass",100,0., 200.);
  h_chf           = fs->make<TH1F>( "chf", "charged hadron fraction",100,0., 1.);
  h_nhf           = fs->make<TH1F>( "nhf", "neutral hadron fraction",100,0., 1.);
  h_cef           = fs->make<TH1F>( "cef", "charged EM fraction",100,0., 1.);
  h_nef           = fs->make<TH1F>( "nef", "neutral EM fraction",100,0., 1.);
}


RSJetAnalyzerV2::~RSJetAnalyzerV2()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSJetAnalyzerV2::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  Handle<edm::View<pat::Jet> > jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);
  
  // Let us double check that we have the wanted jet available.
  if((numberInCollection_+1)>jetsHandle->size())
    throw cms::Exception("ProductNotFound")
      << "The jet collection does not contain enough jets!\n"
      << "We have only " << jetsHandle->size() << " jets!\n";

  // Choose which jet to analyze.
  const pat::Jet & theJet = (* jetsHandle)[numberInCollection_];
  double theMass = theJet.mass();
  double theEnergy = theJet.energy();
  double thePt = theJet.pt();
  double theEta = theJet.eta();
  double CHF = theJet.chargedHadronEnergyFraction();
  double NHF = theJet.neutralHadronEnergyFraction();
  double CEF = theJet.chargedEmEnergyFraction();
  double NEF = theJet.neutralEmEnergyFraction();  

  // Fill the histograms.
  h_pt->Fill(thePt);
  h_eta->Fill(theEta);
  h_mass->Fill(theMass);
  h_chf->Fill(CHF);
  h_nhf->Fill(NHF);
  h_cef->Fill(CEF);
  h_nef->Fill(NEF);

  h_pT_mass->Fill(thePt, theMass);
  h_pT_energy->Fill(thePt, theEnergy);
  h_energy_mass->Fill(theEnergy, theMass);
  h_eta_phi->Fill(theJet.eta(),theJet.phi());
  h_ptOverMass->Fill(thePt/theMass);
  h_ptOverEnergy->Fill(thePt/theEnergy);
  h_massOverEnergy->Fill(theMass/theEnergy);
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSJetAnalyzerV2::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSJetAnalyzerV2::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSJetAnalyzerV2);
