// -*- C++ -*-
//
// Package:    RSFlowAnalyzer
// Class:      RSFlowAnalyzer
// 
/**\class RSFlowAnalyzer RSFlowAnalyzer.cc RSGraviton/RSFlowAnalyzer/src/RSFlowAnalyzer.cc

 Description: Class to analyze the flow of energy inside jets, using tracks.

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  
//         Created:  Thu Jan 15 18:14:18 BRST 2009
// $Id: RSFlowAnalyzer.cc,v 1.1 2009/01/16 12:16:32 tomei Exp $
//
//


// system include files
#include <memory>
#include <vector>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/InputTag.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "PhysicsTools/Utilities/interface/deltaR.h"
#include "RSGraviton/RSFlowAnalyzer/interface/Flow.hh"
#include "PhysicsTools/Utilities/interface/Parameter.h"
#include "PhysicsTools/Utilities/interface/RootMinuit.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"

//
// class decleration
//

class RSFlowAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSFlowAnalyzer(const edm::ParameterSet&);
  ~RSFlowAnalyzer();
  
  
private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  // ----------member data ---------------------------
  TH1F* h_flow;
  edm::InputTag tracks_;
  edm::InputTag jets_;
  double maxDeltaR_;
  int jetNumber_;
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
RSFlowAnalyzer::RSFlowAnalyzer(const edm::ParameterSet& iConfig)

{
  tracks_ = iConfig.getParameter<edm::InputTag>("tracks");
  jets_ = iConfig.getParameter<edm::InputTag>("jets");
  maxDeltaR_ = iConfig.getParameter<double>("maxDeltaR");
  jetNumber_ = iConfig.getParameter<int>("jetNumber");
  edm::Service<TFileService> fs;
  h_flow = fs->make<TH1F>("flow", "Jet Transverse Flow", 100, 0., 1.);
}


RSFlowAnalyzer::~RSFlowAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSFlowAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   Handle<reco::TrackCollection> tracksHandle;
   iEvent.getByLabel(tracks_,tracksHandle);
   Handle<reco::CaloJetCollection> jetsHandle;
   iEvent.getByLabel(jets_,jetsHandle);

   // Get the jet vector.
   math::XYZVector jetVector;
   jetVector = jetsHandle->at(jetNumber_).momentum();

   // Create a vector for the XYZVectors from the tracks.
   // But ONLY for those tracks inside the cone of the jet.
   std::vector<math::XYZVector> trackVectors;
   trackVectors.reserve(tracksHandle->size());
   for(reco::TrackCollection::const_iterator i = tracksHandle->begin();
       i != tracksHandle->end(); ++i) {
     if(reco::deltaR(i->eta(),i->phi(),jetVector.eta(),jetVector.phi()) < maxDeltaR_)
	trackVectors.push_back(i->momentum());
   }

   // Do the flow.
   funct::Parameter phi("Phi",0.7);
   Flow f(jetVector,trackVectors,phi);
   fit::RootMinuit<Flow> minuit(f, false);
   minuit.addParameter(phi, 0.1, 0.0, M_PI_2);
   minuit.minimize();
   minuit.migrad();
   h_flow->Fill(-minuit.minValue());
}


// ------------ method called once each job just before starting event loop  ------------
void 
RSFlowAnalyzer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSFlowAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSFlowAnalyzer);
