import FWCore.ParameterSet.Config as cms

from PhysicsTools.EcalAnomalousEventFilter.ecalanomalouseventfilter_cfi import *
ecalAnomalousEventFilter = EcalAnomalousEventFilter.clone(
    EBRecHitsLabel = cms.untracked.InputTag("reducedEcalRecHitsEB"),
    EERecHitsLabel = cms.untracked.InputTag("reducedEcalRecHitsEE"),
    limitDeadCellToChannelStatusEB = cms.vint32(12,14),
    limitDeadCellToChannelStatusEE = cms.vint32(12,14)
    )

ecalAnomalousEventFilterSequence = cms.Sequence(ecalAnomalousEventFilter)
