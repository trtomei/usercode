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
// $Id: RSJetAnalyzerV2.cc,v 1.1 2010/04/05 14:23:22 tomei Exp $
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
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include "TH2F.h"
//
// class decleration
//

class RSJetAnalyzerV2 : public edm::EDAnalyzer {
public:
  explicit RSJetAnalyzerV2(const edm::ParameterSet&);
  ~RSJetAnalyzerV2();

private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag jets_;
  unsigned int numberInCollection_;
  TH2F*     h_pT_mass;
  TH2F*     h_pT_energy;
  TH2F*     h_energy_mass;
  TH1F*     h_ptOverMass;
  TH1F*     h_ptOverEnergy;
  TH1F*     h_massOverEnergy;
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
  h_ptOverMass    = fs->make<TH1F>( "ptOverMass", "pT over mass", 500, 0., 50.);
  h_ptOverEnergy  = fs->make<TH1F>( "ptOverEnergy", "pT over energy", 20, 0., 1.);
  h_massOverEnergy= fs->make<TH1F>( "massOverEnergy", "mass over energy",20,0., 1.);
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
  using namespace reco;

  Handle<CaloJetCollection> jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);
  
  // Let us double check that we have the wanted jet available.
  if((numberInCollection_+1)>jetsHandle->size())
    throw cms::Exception("ProductNotFound")
      << "The jet collection does not contain enough events!\n";

  // Choose which jet to analyze.
  const Jet & theJet = (* jetsHandle)[numberInCollection_];
  double theMass = theJet.mass();
  double theEnergy = theJet.energy();
  double thePt = theJet.pt();
  
  // Fill the histograms.
  h_pT_mass->Fill(thePt, theMass);
  h_pT_energy->Fill(thePt, theEnergy);
  h_energy_mass->Fill(theEnergy, theMass);
  h_ptOverMass->Fill(thePt/theMass);
  h_ptOverEnergy->Fill(thePt/theEnergy);
  h_massOverEnergy->Fill(theMass/theEnergy);
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSJetAnalyzerV2::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSJetAnalyzerV2::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSJetAnalyzerV2);
