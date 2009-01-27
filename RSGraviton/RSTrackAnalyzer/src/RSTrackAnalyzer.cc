// -*- C++ -*-
//
// Package:    RSTrackAnalyzer
// Class:      RSTrackAnalyzer
// 
/**\class RSTrackAnalyzer RSTrackAnalyzer.cc RSGraviton/RSTrackAnalyzer/src/RSTrackAnalyzer.cc

 Description: Class to count tracks inside jets.

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Tue May  6 17:17:55 CEST 2008
// $Id: RSTrackAnalyzer.cc,v 1.2 2008/05/17 19:37:41 tomei Exp $
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
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
//
// class decleration
//

class RSTrackAnalyzer : public edm::EDAnalyzer {
   public:
      explicit RSTrackAnalyzer(const edm::ParameterSet&);
      ~RSTrackAnalyzer();


   private:
      virtual void beginJob(const edm::EventSetup&) ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      // ----------member data ---------------------------
  edm::InputTag tracks_;
  edm::InputTag jets_;
  double jetRadius_;

  TH1F* h_tracksJet1;
  TH1F* h_tracksJet2;
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
RSTrackAnalyzer::RSTrackAnalyzer(const edm::ParameterSet& iConfig) :
  tracks_(iConfig.getParameter<edm::InputTag>("tracks") ),
  jets_(iConfig.getParameter<edm::InputTag>("jets") ),
  jetRadius_(iConfig.getParameter<double>("jetRadius") )
{
   //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_tracksJet1  = fs->make<TH1F>( "tracksJet1"  , "tracksJet1", 500,  0.5, 500.5);
  h_tracksJet2  = fs->make<TH1F>( "tracksJet2"  , "tracksJet2", 500,  0.5, 500.5);
}


RSTrackAnalyzer::~RSTrackAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSTrackAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;
   
   Handle<TrackCollection> tracksHandle;
   Handle<CaloJetCollection> jetsHandle;
   
   iEvent.getByLabel(tracks_, tracksHandle);
   iEvent.getByLabel(jets_, jetsHandle);   
   
   // Let us get the two jets
   const Jet & Jet1 = (* jetsHandle)[0];
   const Jet & Jet2 = (* jetsHandle)[1];

   // Find the particles inside, and compare
   // them to the tracks.
   int nTracksJet1 = 0;
   int nTracksJet2 = 0;
   
   for(TrackCollection::const_iterator titer = tracksHandle->begin();
       titer != tracksHandle->end(); ++titer) {
     
     double dR1 = deltaR(Jet1.eta(),Jet1.phi(),titer->eta(),titer->phi());
     double dR2 = deltaR(Jet2.eta(),Jet2.phi(),titer->eta(),titer->phi());
     
     if(dR1 < jetRadius_)
       ++nTracksJet1;
     if(dR2 < jetRadius_)
       ++nTracksJet2;     
   }

   h_tracksJet1->Fill(nTracksJet1);
   h_tracksJet2->Fill(nTracksJet2);
}


// ------------ method called once each job just before starting event loop  ------------
void 
RSTrackAnalyzer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSTrackAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSTrackAnalyzer);
