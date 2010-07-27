import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.threshold = 'WARNING'
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

#process.source = cms.Source("EmptySource")
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring("file:/storage/trtomei/data/PythiaWjjlnu_800GeV_kmpl005_CMSSW358_RECO.root"))

#process.ZZGenFilter = cms.EDFilter("ZZDecayFilter", verbose=cms.bool(True))

process.getXSec = cms.EDAnalyzer("PythiaXSecAnalyzer",
                                 outFileName = cms.string("xSec.txt"),
                                 massParameter = cms.double(-9.9))

# Path and EndPath definitions
process.p = cms.Path(process.getXSec)
