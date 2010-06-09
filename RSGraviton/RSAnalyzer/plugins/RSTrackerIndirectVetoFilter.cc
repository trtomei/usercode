// -*- C++ -*-
//
// Package:    RSTrackerIndirectVetoFilter
// Class:      RSTrackerIndirectVetoFilter
// 
/**\class RSTrackerIndirectVetoFilter RSTrackerIndirectVetoFilter.cc RSGraviton/RSTrackerIndirectVetoFilter/src/RSTrackerIndirectVetoFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Thiago Tomei
//         Created:  Thu Mar  4 16:26:36 BRT 2010
// $Id: RSTrackerIndirectVetoFilter.cc,v 1.1 2010/06/02 16:30:44 tomei Exp $
//
//


// system include files
#include <memory>
#include <algorithm>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
//#include "RSGraviton/RSAnalyzer/interface/JetConfigurableSelectionFunctor.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/Vector3D.h"
//#include "CommonTools/UtilAlgos/interface/StringCutObjectSelector.h"

//
// class declaration
//

class RSTrackerIndirectVetoFilter : public edm::EDFilter {
   public:
      explicit RSTrackerIndirectVetoFilter(const edm::ParameterSet&);
      ~RSTrackerIndirectVetoFilter();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
  edm::InputTag src_;
  double trackMinPt_;
  double seedTrackMinPt_;
  double trackMaxEta_;
  double minCone_;
  double maxCone_;
  double minAcceptableTIV_;
  int pixelHits_;
  int trackerHits_;
  bool highPurityRequired_;
  bool filter_;
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
RSTrackerIndirectVetoFilter::RSTrackerIndirectVetoFilter(const edm::ParameterSet& iConfig) :
  src_(iConfig.getParameter<edm::InputTag>("src")),
  trackMinPt_(iConfig.getParameter<double>("trackMinPt")),
  seedTrackMinPt_(iConfig.getParameter<double>("seedTrackMinPt")),
  trackMaxEta_(iConfig.getParameter<double>("trackMaxEta")),
  minCone_(iConfig.getParameter<double>("minCone")),
  maxCone_(iConfig.getParameter<double>("maxCone")),
  minAcceptableTIV_(iConfig.getParameter<double>("minAcceptableTIV")),
  pixelHits_(iConfig.getParameter<int>("pixelHits")),
  trackerHits_(iConfig.getParameter<int>("trackerHits")),
  highPurityRequired_(iConfig.getParameter<bool>("highPurityRequired")),
  filter_(iConfig.getParameter<bool>("filter"))
{
  produces<double>();
}


RSTrackerIndirectVetoFilter::~RSTrackerIndirectVetoFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
RSTrackerIndirectVetoFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<reco::TrackCollection> tracksHandle;
  iEvent.getByLabel(src_,tracksHandle);
  
  // Transient only!!!
  std::vector<math::XYZVector> passingTracks;
  
  //const int size = tracksHandle->size();
  //std::cout << "Starting from " << size << " tracks" << std::endl;
  
  for(reco::TrackCollection::const_iterator itrack = tracksHandle->begin();
      itrack != tracksHandle->end();
      ++itrack)  {    

    bool highPurityCut = true;
    bool trackerHitsCut = true;
    bool pixelHitsCut = true;
    bool trackPtCut = true;
    bool trackEtaCut= true;

    // We want high purity tracks, if asked for in the configuration.
    if(highPurityRequired_ && !(itrack->quality(reco::Track::highPurity))) {
      highPurityCut = false;
    }
    
    // We want at least some hits, as defined in the configuration.
    // Default would be: at least >= 8 total hits, >=0 pixel hits.
    const reco::HitPattern hpattern = itrack->hitPattern();
    if(!(hpattern.numberOfValidTrackerHits() >= trackerHits_)) {
      trackerHitsCut = false;
    }
    if(!(hpattern.numberOfValidPixelHits() >= pixelHits_)) {
      pixelHitsCut = false;
    }

    // And only those tracks with kinematics defined in the configuration.
    if(itrack->pt() < trackMinPt_) {
      trackPtCut = false;
    }
    if(std::abs(itrack->eta()) > trackMaxEta_) {
      trackEtaCut = false;
    }

    bool fullTrackCut = (highPurityCut && trackerHitsCut && pixelHitsCut && trackPtCut && trackEtaCut);
    // If track is good, select it in.
    if(fullTrackCut) {
      math::XYZVector theSelectedTrack;
      theSelectedTrack.SetX(itrack->px());
      theSelectedTrack.SetY(itrack->py());
      theSelectedTrack.SetZ(itrack->pz());
      passingTracks.push_back(theSelectedTrack);
    }
  }
  //std::cout << "We have number of tracks: " << passingTracks.size() << std::endl;

  // Now calculate all the TIV quantities, for all tracks which are high pT enough to be seeds.;
  std::vector<double> allTIVs;
  for(std::vector<math::XYZVector>::const_iterator itrack = passingTracks.begin();
      itrack != passingTracks.end();
      ++itrack) {
    
    // Only make cones around tracks above seedTrackPt
    double seedTrackPt = std::sqrt(itrack->Perp2());
    if(seedTrackPt < seedTrackMinPt_) continue;

    double maxPt = -1.0;
    double sumPt = 0.0;
    for(std::vector<math::XYZVector>::const_iterator jtrack = passingTracks.begin();
	jtrack != passingTracks.end();
	++jtrack) {

      // Must be in hollow cone, as defined in the configuration.
      double dR = deltaR(itrack->eta(),itrack->phi(),jtrack->eta(),jtrack->phi());
      if(dR < minCone_ || dR > maxCone_) continue;
      
      // Save if this is the leading track
      double jtrackPt = std::sqrt(jtrack->Perp2());
      if(jtrackPt > maxPt) maxPt = jtrackPt;
      sumPt += jtrackPt;
    }

    // Now we have both sumPt and maxPt in the hollow cone, for this track.
    // We have some choices on WHAT we put in the denominator:
    // a) max pT in the hollow cone? That is, maxPt?
    // b) max pT in the FULL cone? That is, the largest in between maxPt and seedTrackPt?
    // c) the seeding track pT? That is, seedTrackPt?
    // For now we choose option B.
    double theThingThatWePutInTheDenominator;
    if(maxPt > seedTrackPt)
      theThingThatWePutInTheDenominator = maxPt;
    else
      theThingThatWePutInTheDenominator = seedTrackPt;
    
    double TIV = sumPt/theThingThatWePutInTheDenominator;
    allTIVs.push_back(TIV);
  }

  // Now we have the TIVs for all tracks.
  // Get the smallest TIV, and put it into the event.
  std::auto_ptr<double> minTIV(new double);
  
  // If no TIVs were calculated, something is wrong. Put a negative number to signal it.
  // This means that there are no tracks above seedTrackPtCut...
  double minTIVtmp = -5.0;
  if(allTIVs.size()!=0)
    minTIVtmp = *(std::min_element(allTIVs.begin(),allTIVs.end()));
  *minTIV = minTIVtmp;
  iEvent.put(minTIV);

  // Now, we make a cut if asked for in the configuration.
  if(!filter_) // Don't cut, accept the event.
    return true;
  else {
    if(minTIVtmp < minAcceptableTIV_) // Min TIV below the cut, reject the event.
      return false;
    else  // Min TIV accept the cut, accept the event.
      return true;
  }
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSTrackerIndirectVetoFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSTrackerIndirectVetoFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSTrackerIndirectVetoFilter);
