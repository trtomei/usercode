import FWCore.ParameterSet.Config as cms

TIVCut = cms.EDFilter("RSPATTrackerIndirectVetoFilter",
                      src = cms.InputTag("generalTracks"),
                      excludeTracks = cms.bool(False),
                      tracksToExclude = cms.InputTag(""), # Has no effect if excludeTracks is false
                      trackMinPt = cms.double(1.0),
                      seedTrackMinPt = cms.double(10.0),
                      trackMaxEta = cms.double(2.4),
                      minCone = cms.double(0.02),
                      maxCone = cms.double(0.3),
                      minAcceptableTIV = cms.double(0.1), # 10%, has no effect if filter is False
                      pixelHits = cms.int32(1),
                      trackerHits = cms.int32(5),
                      highPurityRequired = cms.bool(True),
                      filter = cms.bool(True)
                      )
