// -*- C++ -*-
//
// Package:    RSEventAnalyzer
// Class:      RSEventAnalyzer
// 
/**\class RSEventAnalyzer RSEventAnalyzer.cc RSGraviton/RSEventAnalyzer/src/RSEventAnalyzer.cc

Description: Class to analyze jets in RS->jets events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSEventAnalyzer.cc,v 1.6 2009/04/22 18:39:49 tomei Exp $
//
//


// system include files
#include <memory>
#include <cmath>

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
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/CaloMETFwd.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
//
// class decleration
//

class RSEventAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSEventAnalyzer(const edm::ParameterSet&);
  ~RSEventAnalyzer();

private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag jets_;
  edm::InputTag met_;
  TH1F* h_dPhi_jet_MET;
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
RSEventAnalyzer::RSEventAnalyzer(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets") ),
  met_(iConfig.getParameter<edm::InputTag>("met") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_dPhi_jet_MET  = fs->make<TH1F>( "dPhi_jet_MET", "dPhi jet and MET", 72, -M_PI, M_PI);
}

RSEventAnalyzer::~RSEventAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSEventAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;

  Handle<CaloJetCollection> jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);
  Handle<CaloMETCollection> metHandle;
  iEvent.getByLabel(met_, metHandle);
  const CaloMET& theMET = metHandle->front();
  const CaloJet& theJet = (*jetsHandle)[0];

  double phiJet = theJet.phi();
  double phiMET = theMET.phi();
  double diffPhi = deltaPhi(phiJet,phiMET);
  
  // Fill the histograms.
  h_dPhi_jet_MET->Fill(diffPhi);
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSEventAnalyzer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSEventAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSEventAnalyzer);
