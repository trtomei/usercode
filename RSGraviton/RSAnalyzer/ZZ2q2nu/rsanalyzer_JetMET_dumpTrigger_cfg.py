#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("ANALYSIS")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.Services_cff')

# Other statements
myOptions = sys.argv
if 'input' in myOptions:
    setupInputFileName = myOptions[myOptions.index('input')+1]
else:
    setupInputFileName = ''

if 'suffix' in myOptions:
    setupSuffix = myOptions[myOptions.index('suffix')+1]
else:
    setupSuffix = ''

if 'numEvents' in myOptions:
    setupNumEvents = int(myOptions[myOptions.index('numEvents')+1])
else:
    setupNumEvents = -1


fileList = cms.untracked.vstring(setupInputFileName,)
process.source = cms.Source("PoolSource",fileNames = fileList)

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(setupNumEvents)
        )

process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True)
        )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

### The output
#process.TFileService = cms.Service("TFileService",
#                                   fileName = cms.string('output_'+setupSuffix+'.root')
#)

process.hltEventAnalyzerAOD = cms.EDAnalyzer("HLTEventAnalyzerAOD",
                                             processName = cms.string("HLT"),
                                             triggerName = cms.string("@"),
                                             triggerResults = cms.InputTag("TriggerResults","","HLT"),
                                             triggerEvent   = cms.InputTag("hltTriggerSummaryAOD","","HLT")
                                             )

process.triggerSelection = cms.EDFilter("TriggerResultsFilter",
                                        triggerConditions = cms.vstring('HLT_MET65_CenJet50U_v*',),
                                        hltResults = cms.InputTag( "TriggerResults" , "", "HLT"),
                                        l1tResults = cms.InputTag( "" ),
                                        l1tIgnoreMask = cms.bool( True ),
                                        l1techIgnorePrescales = cms.bool( False ),
                                        daqPartitions = cms.uint32( 1 ),
                                        throw = cms.bool( False )
                                        )

process.p1 = cms.Path(
    process.hltEventAnalyzerAOD
    )
