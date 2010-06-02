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
// $Id: RSTrackerIndirectVetoFilter.cc,v 1.3 2010/05/17 11:27:46 tomei Exp $
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
  double minCone_;
  double maxCone_;
  double maxAcceptableTIV_;
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
  minCone_(iConfig.getParameter<double>("minCone")),
  maxCone_(iConfig.getParameter<double>("maxCone")),
  maxAcceptableTIV_(iConfig.getParameter<double>("maxAcceptableTIV")),
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
  reco::TrackCollection passingTracks;
  //const int size = tracksHandle->size();
  //std::cout << "Starting from " << size << " tracks" << std::endl;
   
  for(reco::TrackCollection::const_iterator itrack = tracksHandle->begin();
      itrack != tracksHandle->end();
      ++itrack)  {    
    //std::cout << "I am in here!" << std::endl;
    bool highPurityCut = true;
    bool trackerHitsCut = true;
    bool pixelHitsCut = true;
    bool trackPtCut = true;
    // We want high purity tracks, if asked.
    if(highPurityRequired_ && !(itrack->quality(reco::Track::highPurity)))
      highPurityCut = false;
    
    // We want at least some hits, as defined in the configuration.
    // Default would be: at least >= 8 total hits, >=0 pixel hits.
    const reco::HitPattern hpattern = itrack->hitPattern();
    if(!(hpattern.numberOfValidTrackerHits() >= trackerHits_))
      trackerHitsCut = false;
    if(!(hpattern.numberOfValidPixelHits() >= pixelHits_))
      pixelHitsCut = false;
    
    // And only those tracks above what is defined in the configuration.
    if(itrack->pt() < trackMinPt_)
      trackPtCut = false;

    bool fullTrackCut = (highPurityCut && trackerHitsCut && pixelHitsCut && trackPtCut);
    // If track is good, select it in.
    if(fullTrackCut) {
      reco::Track selectedTrack = *itrack;
      passingTracks.push_back(selectedTrack);
    }
  }
  std::cout << "We have number of tracks: " << passingTracks.size() << std::endl;

  // Now calculate all the TIV quantities.
  std::vector<double> allTIVs;
  for(reco::TrackCollection::const_iterator itrack = passingTracks.begin();
      itrack != passingTracks.end();
      ++itrack) {
    size_t iThisTrack = 0;
    size_t iMaxTrack = 0;
    double maxPt = -1.0;
    double sumPt = 0;

    for(reco::TrackCollection::const_iterator jtrack = passingTracks.begin();
	jtrack != passingTracks.end();
	++jtrack) {
      ++iThisTrack;
      double dR = deltaR(itrack->eta(),itrack->phi(),jtrack->eta(),jtrack->phi());
      // Must be in hollow cone, as defined in the configuration.
      if(dR < minCone_ || dR > maxCone_) continue;
      // Save if this is the leading track
      if(jtrack->pt()>maxPt) {maxPt = jtrack->pt(); iMaxTrack = iThisTrack;}
      sumPt += jtrack->pt();
    }
    // Now we have both sumPt and maxPt in the hollow cone, for each track
    double TIV = sumPt/maxPt;
    allTIVs.push_back(TIV);
  }
  // Now we have the TIVs for all tracks.
  // Get the largest TIV, and put it into the event.
  std::auto_ptr<double> maxTIV(new double);
  double maxTIVtmp = -1.0;
  if(allTIVs.size()!=0)
    maxTIVtmp = *(std::max_element(allTIVs.begin(),allTIVs.end()));
  *maxTIV = maxTIVtmp;
  iEvent.put(maxTIV);
  
  // Now, do we make a cut?
  if(!filter_) // Don't cut, accept the event.
    return true;
  else {
    if(maxTIVtmp > maxAcceptableTIV_) // Max TIV above the cut, reject the event.
      return false;
    else  // Max TIV below the cut, accept the event.
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
