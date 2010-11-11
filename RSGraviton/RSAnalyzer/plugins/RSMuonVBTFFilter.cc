// Shamelessly copied from WMuNuSelector

#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"

class RSMuonVBTFFilter : public edm::EDFilter {
public:
  RSMuonVBTFFilter (const edm::ParameterSet &);
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void beginJob();
  virtual void endJob();
private:
  edm::InputTag muonTag_;
  edm::InputTag jetTag_;
  double ptThrForZ1_;
  double ptThrForZ2_;
  bool vetoSecondMuonEvents_;
  double eJetMin_;
  int nJetMax_;
  double ptCut_;
  double etaCut_;
  bool isRelativeIso_;
  bool isCombinedIso_;
  double isoCut03_;

  double dxyCut_;
  double normalizedChi2Cut_;
  int trackerHitsCut_;
  int pixelHitsCut_;    
  int muonHitsCut_;
  bool isAlsoTrackerMuon_;
  int nMatchesCut_;

  bool filter_;

};
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/Common/interface/Handle.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

#include "DataFormats/JetReco/interface/Jet.h"

#include "DataFormats/GeometryVector/interface/Phi.h"

#include "DataFormats/Common/interface/View.h"

using namespace edm;
using namespace std;
using namespace reco;

RSMuonVBTFFilter::RSMuonVBTFFilter( const ParameterSet & cfg ) :
      
      // Input collections
      muonTag_(cfg.getUntrackedParameter<edm::InputTag> ("MuonTag", edm::InputTag("muons"))),
      jetTag_(cfg.getUntrackedParameter<edm::InputTag> ("JetTag", edm::InputTag(""))),

      // Preselection cuts 
      ptThrForZ1_(cfg.getUntrackedParameter<double>("PtThrForZ1", 20.)),
      ptThrForZ2_(cfg.getUntrackedParameter<double>("PtThrForZ2", 10.)),
      
      eJetMin_(cfg.getUntrackedParameter<double>("EJetMin", 999999.)),
      nJetMax_(cfg.getUntrackedParameter<int>("NJetMax", 999999)),

      // Main cuts 
      ptCut_(cfg.getUntrackedParameter<double>("PtCut", 20.)),
      etaCut_(cfg.getUntrackedParameter<double>("EtaCut", 2.1)),
      isRelativeIso_(cfg.getUntrackedParameter<bool>("IsRelativeIso", true)),
      isCombinedIso_(cfg.getUntrackedParameter<bool>("IsCombinedIso", true)),
      isoCut03_(cfg.getUntrackedParameter<double>("IsoCut03", 0.15)),

      // Muon quality cuts
      dxyCut_(cfg.getUntrackedParameter<double>("DxyCut", 0.2)),   // dxy < 0.2 cm 
      normalizedChi2Cut_(cfg.getUntrackedParameter<double>("NormalizedChi2Cut", 10.)), // chi2/ndof (of global fit) <10.0
      trackerHitsCut_(cfg.getUntrackedParameter<int>("TrackerHitsCut", 11)),  // Tracker Hits >10 
      pixelHitsCut_(cfg.getUntrackedParameter<int>("PixelHitsCut", 1)), // Pixel Hits >0
      muonHitsCut_(cfg.getUntrackedParameter<int>("MuonHitsCut", 1)),  // Valid Muon Hits >0 
      isAlsoTrackerMuon_(cfg.getUntrackedParameter<bool>("IsAlsoTrackerMuon", true)),
      nMatchesCut_(cfg.getUntrackedParameter<int>("NMatchesCut", 2)), // At least 2 Chambers with matches 
      
      // To filter or not?
      filter_(cfg.getUntrackedParameter<bool>("filter",false))
{
  produces< reco::MuonCollection >
    ("selectedVBTFMuons").setBranchAlias("selectedVBTFMuons");
  produces < int >
    ("muonVBTFStatus").setBranchAlias("muonVBTFStatus");
}

void RSMuonVBTFFilter::beginJob() {
}

void RSMuonVBTFFilter::endJob() {
}

bool RSMuonVBTFFilter::filter (Event & ev, const EventSetup &) {
  // Repeat Pre-Selection Cuts just in case...
  
  // Muon collection
  Handle<View<Muon> > muonCollection;
  ev.getByLabel(muonTag_, muonCollection);
  unsigned int muonCollectionSize = muonCollection->size();
 
  bool weGotMuons = true;
  if(muonCollectionSize == 0) {
    // Ok, there are no muons in the event...
    weGotMuons = false;
  }

  // Loop to reject/control Z->mumu is done separately
  unsigned int nmuonsForZ1 = 0;
  unsigned int nmuonsForZ2 = 0;
  unsigned int leadingMuonIndex = 0;
  double leadingMuonPt = 0.0;
  for (unsigned int i=0; i<muonCollectionSize; i++) {
    const Muon& mu = muonCollection->at(i);
    if (!mu.isGlobalMuon()) continue;
    double pt = mu.pt();
    if (pt>ptThrForZ1_) nmuonsForZ1++;
    if (pt>ptThrForZ2_) nmuonsForZ2++;
    if(pt > leadingMuonPt) {
      leadingMuonPt = pt;
      leadingMuonIndex = i;
    }
  }
  
  // Jet collection
  Handle<View<Jet> > jetCollection;
  ev.getByLabel(jetTag_, jetCollection);
  unsigned int jetCollectionSize = jetCollection->size();
  int njets = 0;
  for (unsigned int i=0; i<jetCollectionSize; i++) {
    const Jet& jet = jetCollection->at(i);
    if (jet.et()>eJetMin_) njets++;
  }
  
  // Beam spot
  Handle<reco::BeamSpot> beamSpotHandle;
  ev.getByLabel(InputTag("offlineBeamSpot"), beamSpotHandle);
  
  // Get the flags ready.
  bool preselection = true; // Leading muon passes preselection
  bool isGlobal     = true; // Leading muon is global
  bool kinematic    = true; // Leading muon passes kinematics
  bool quality      = true; // Leading muon passes quality
  bool iso          = true; // Leading muon passes isolation

  // Get the collections ready
  auto_ptr<reco::MuonCollection> 
     selectedVBTFMuons(new reco::MuonCollection);
  auto_ptr<int> muonVBTFStatus(new int);
  
  if(weGotMuons) {
    // Ok, get the muon itself and pray.
    const reco::Muon & mu = muonCollection->at(leadingMuonIndex);
    // Shove the guy into the collection already.
    reco::Muon theChosenMuon = *(mu.clone()); 
    selectedVBTFMuons->push_back(theChosenMuon);
    
    // Preselection cuts
    if (nmuonsForZ2>1 && vetoSecondMuonEvents_) // Oops, Z candidate
      preselection = false;
    if (njets>nJetMax_) // Oops, too many jets
      preselection = false;

    // Want a global muon.
    isGlobal = mu.isGlobalMuon();
    
    // Kinematic cuts
    if(!isGlobal) kinematic = false; // Don't even continue, we already failed the global muon cut...
    if(isGlobal) {double pt = mu.pt();
      double eta = mu.eta();
      if (pt<ptCut_) kinematic=false;
      if (fabs(eta)>etaCut_) kinematic=false;
    }
    
    // Quality cuts
    if(!kinematic) quality = false; // Don't even continue, we already failed the kinematic cuts...
    if(kinematic) {
      reco::TrackRef gm = mu.globalTrack();
      reco::TrackRef tk = mu.innerTrack();
      double dxy = gm->dxy(beamSpotHandle->position());
      double normalizedChi2 = gm->normalizedChi2(); 
      int trackerHits = tk->hitPattern().numberOfValidTrackerHits();
      int pixelHits = tk->hitPattern().numberOfValidPixelHits();
      int muonHits = gm->hitPattern().numberOfValidMuonHits();
      int nMatches = mu.numberOfMatches(); 
      
      if (fabs(dxy)>dxyCut_) {quality = false;}
      if (normalizedChi2>normalizedChi2Cut_) {quality=false;}
      if (trackerHits<trackerHitsCut_) {quality=false;}
      if (pixelHits<pixelHitsCut_) {quality=false;}
      if (muonHits<muonHitsCut_) {quality=false;}
      if (!mu.isTrackerMuon()) {quality=false;}
      if (nMatches<nMatchesCut_) {quality=false;}
    }
    
    // Isolation cuts
    if(!quality) iso = false; // Don't even continue, we already failed the quality cuts...
    if(quality) {
      double pt = mu.pt();
      double SumPt = mu.isolationR03().sumPt; double isovar=SumPt;
      double Cal   = mu.isolationR03().emEt + mu.isolationR03().hadEt; 
      if (isCombinedIso_) isovar += Cal;
      if (isRelativeIso_) isovar /= pt;
      iso = (isovar<=isoCut03_);
    }
  }

  bool theFilterResult = (weGotMuons && isGlobal && kinematic && quality && iso); 
  if(theFilterResult == true)
    *muonVBTFStatus = 1;
  else
    *muonVBTFStatus = 0;

  ev.put( selectedVBTFMuons, "selectedVBTFMuons");
  ev.put( muonVBTFStatus, "muonVBTFStatus");
  
  // choose your destiny
  if(filter_ == true)
    return theFilterResult;
  else
    return true;
}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(RSMuonVBTFFilter);
