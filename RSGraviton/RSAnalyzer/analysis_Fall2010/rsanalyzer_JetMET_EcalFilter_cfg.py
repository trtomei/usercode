#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("CHECK")

###########################
# Basic process controls. #
###########################

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.EventContent.EventContent_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles, noEventSort = cms.untracked.bool(True))
readFiles.extend(['/store/user/tomei/METFwd_Run2010B-Dec22ReReco_v1/skim_59_1_wJp.root'])

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('filterTest.root')
                                   )

##################
# The global tag #
##################
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'FT_R_39X_V4A::All'

# The filter
#For BE filter
from PhysicsTools.EcalAnomalousEventFilter.ecalanomalouseventfilter_cfi import *
process.ecalAnomalousFilter = EcalAnomalousEventFilter.clone(
    EBRecHitsLabel = cms.untracked.InputTag("reducedEcalRecHitsEB"),
    EERecHitsLabel = cms.untracked.InputTag("reducedEcalRecHitsEE"),
    limitDeadCellToChannelStatusEB = cms.vint32(12,14),
    limitDeadCellToChannelStatusEE = cms.vint32(12,14)
    )

#For TP filter
from UserCode.EcalDeadCellEventFilter.EcalDeadCellEventFilter_cfi import *
process.ecalDeadCellFilter = EcalDeadCellEventFilter.clone(
    tpDigiCollection = cms.InputTag("ecalTPSkim"),
    ecalAnomalousFilterTag = cms.InputTag("ecalAnomalousFilter","anomalousECALVariables")
    )
#process.load("UserCode.EcalDeadCellEventFilter.RA2EcalDeadCell_cff")

from RSGraviton.RSAnalyzer.METhistos_cff import histograms as METhistos
process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("corMetGlobalMuons"),
                                 histograms = METhistos
                                 )

process.plotMETnormal = process.plotMET.clone()
process.plotMETanomalous = process.plotMET.clone()

process.pnormal = cms.Path(
    process.ecalAnomalousFilter +
    process.ecalDeadCellFilter +
    process.plotMETnormal
    )

#process.panomalous = cms.Path(
#    ~process.EcalAnomalousEventFilter +
#    process.plotMETanomalous
#    )
