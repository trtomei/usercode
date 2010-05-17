import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process('USER')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.threshold = 'WARNING'
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('lala.root')
                                   )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:allData/Pythia_800GeV_kmpl005_RECO.root')
                            )

process.getXSec = cms.EDAnalyzer("GenEventAnalyzer",
                                 min = cms.untracked.double(0.0),
                                 max = cms.untracked.double(1000.0),
                                 nbins = cms.untracked.int32(200),
                                 description = cms.untracked.string("pthat"),
                                 name = cms.untracked.string("pthat"),
                                 plotquantity = cms.untracked.string("binningValues.front")
                                 )

process.p1 = cms.Path(process.getXSec)
