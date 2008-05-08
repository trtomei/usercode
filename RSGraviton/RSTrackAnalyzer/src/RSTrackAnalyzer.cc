// -*- C++ -*-
//
// Package:    RSTrackAnalyzer
// Class:      RSTrackAnalyzer
// 
/**\class RSTrackAnalyzer RSTrackAnalyzer.cc RSGraviton/RSTrackAnalyzer/src/RSTrackAnalyzer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Tue May  6 17:17:55 CEST 2008
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
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
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
  TH1F* h_chargedJet1;
  TH1F* h_chargedJet2;
  TH1F* h_tracksJet1;
  TH1F* h_tracksJet2;
  TH1F* h_matchedJet1;
  TH1F* h_matchedJet2;
  TH1F* h_unmatchedJet1;
  TH1F* h_unmatchedJet2;
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
RSTrackAnalyzer::RSTrackAnalyzer(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_chargedJet1  = fs->make<TH1F>( "chargedJet1"  , "chargedJet1", 500,  0.5, 500.5);
  h_chargedJet2  = fs->make<TH1F>( "chargedJet2"  , "chargedJet2", 500,  0.5, 500.5);
  h_tracksJet1  = fs->make<TH1F>( "tracksJet1"  , "tracksJet1", 500,  0.5, 500.5);
  h_tracksJet2  = fs->make<TH1F>( "tracksJet2"  , "tracksJet2", 500,  0.5, 500.5);
  h_matchedJet1  = fs->make<TH1F>( "matchedJet1"  , "matchedJet1", 500,  0.5, 500.5);
  h_matchedJet2  = fs->make<TH1F>( "matchedJet2"  , "matchedJet2", 500,  0.5, 500.5);
  h_unmatchedJet1  = fs->make<TH1F>( "unmatchedJet1"  , "unmatchedJet1", 500,  0.5, 500.5);
  h_unmatchedJet2  = fs->make<TH1F>( "unmatchedJet2"  , "unmatchedJet2", 500,  0.5, 500.5);

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
   Handle<CandidateCollection> particlesHandle;
   Handle<View<Candidate> > jetsHandle;
   
   iEvent.getByLabel("ctfGSWithMaterialTracks", tracksHandle);
   iEvent.getByLabel("genParticlesAllStable", particlesHandle);
   iEvent.getByLabel("twoCaloJets", jetsHandle);   
   
   // Let us get the two jets
   const Candidate & Jet1 = (* jetsHandle)[0];
   const Candidate & Jet2 = (* jetsHandle)[1];

   // Find the particles inside, and compare
   // them to the tracks.
   double jetradius=0.7;
   double matchradius = 0.075; // Is this reasonable?
   int nMatchedJet1 = 0;
   int nUnmatchedJet1 = 0;
   int nChargedJet1 = 0;
   int nMatchedJet2 = 0;
   int nUnmatchedJet2 = 0;
   int nChargedJet2 = 0;

   for(CandidateCollection::const_iterator piter = particlesHandle->begin();
       piter != particlesHandle->end(); ++piter) {
     if(piter->charge() == 0) 
       continue;
     double dR1 = deltaR(Jet1.eta(),Jet1.phi(),piter->eta(),piter->phi());
     double dR2 = deltaR(Jet2.eta(),Jet2.phi(),piter->eta(),piter->phi());
     
     if(dR1 < jetradius) { // Inside jet 1
       ++nChargedJet1;
       double matched = false;
       for(TrackCollection::const_iterator titer = tracksHandle->begin();
	   titer != tracksHandle->end(); ++titer) {
	 double dRPartTrack = deltaR(piter->eta(), piter->phi(), titer->eta(), titer->phi());
	 if(dRPartTrack < matchradius)
	   matched = true;
       }
       if(matched)
	 ++nMatchedJet1;
       else
	 ++nUnmatchedJet1;
     }
     
     if(dR2 < jetradius) { // Inside jet 2
       ++nChargedJet2;
       double matched = false;
       for(TrackCollection::const_iterator titer = tracksHandle->begin();
	   titer != tracksHandle->end(); ++titer) {
	 double dRPartTrack = deltaR(piter->eta(), piter->phi(), titer->eta(), titer->phi());
	 if(dRPartTrack < matchradius)
	   matched = true;
       }
       if(matched)
	 ++nMatchedJet2;
       else
	 ++nUnmatchedJet2;
     }
     
   }

   int nTracksJet1 = 0;
   int nTracksJet2 = 0;
   
   for(TrackCollection::const_iterator titer = tracksHandle->begin();
       titer != tracksHandle->end(); ++titer) {
     
     double dR1 = deltaR(Jet1.eta(),Jet1.phi(),titer->eta(),titer->phi());
     double dR2 = deltaR(Jet2.eta(),Jet2.phi(),titer->eta(),titer->phi());
     
     if(dR1 < jetradius)
       ++nTracksJet1;
     if(dR2 < jetradius)
       ++nTracksJet2;     
   }

   h_chargedJet1->Fill(nChargedJet1);
   h_chargedJet2->Fill(nChargedJet2);
   h_tracksJet1->Fill(nTracksJet1);
   h_tracksJet2->Fill(nTracksJet2);
   h_matchedJet1->Fill(nMatchedJet1);
   h_matchedJet2->Fill(nMatchedJet2);
   h_unmatchedJet1->Fill(nUnmatchedJet1);
   h_unmatchedJet2->Fill(nUnmatchedJet2);
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
