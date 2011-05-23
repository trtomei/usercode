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


fileList = cms.untracked.vstring('file:'+setupInputFileName,)
process.source = cms.Source("PoolSource",fileNames = fileList)

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(setupNumEvents)
        )

process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True)
        )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output_'+setupSuffix+'.root')
)

# Jet
process.load("RSGraviton.RSAnalyzer.patCleaning_cfi")
process.load("RSGraviton.RSAnalyzer.pfJetId_cfi")

# MET
process.oneJetAboveZero = cms.EDFilter("CandViewSelector",
                                       src = cms.InputTag("jetIdCut"),
                                       cut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1),
                                       filter = cms.bool(True)
                                       )

process.getLargestJet = cms.EDFilter("LargestPtCandViewSelector",
                                     src = cms.InputTag("oneJetAboveZero"),
                                     maxNumber = cms.uint32(1)
                                     )


process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("patMETsPFlow"),
                                 histograms = cms.VPSet(cms.PSet(nbins = cms.untracked.int32(400),
                                                                 description = cms.untracked.string('MET'),
                                                                 plotquantity = cms.untracked.string('et'),
                                                                 min = cms.untracked.double(0.0),
                                                                 max = cms.untracked.double(2000.0),
                                                                 name = cms.untracked.string('MET')
                                                                 ),
                                                        cms.PSet(nbins = cms.untracked.int32(400),
                                                                 description = cms.untracked.string('METpt'),
                                                                 plotquantity = cms.untracked.string('pt'),
                                                                 min = cms.untracked.double(0.0),
                                                                 max = cms.untracked.double(2000.0),
                                                                 name = cms.untracked.string('METpt')
                                                                 ),
                                                        cms.PSet(nbins = cms.untracked.int32(72),
                                                                 description = cms.untracked.string('MET phi'),
                                                                 plotquantity = cms.untracked.string('phi'),
                                                                 min = cms.untracked.double(-3.141592),
                                                                 max = cms.untracked.double(3.141592),
                                                                 name = cms.untracked.string('MET_phi')
                                                                 )
                                                        )
                                 )

process.plotJet = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("getLargestJet"),
                                 histograms = cms.VPSet(cms.PSet(nbins = cms.untracked.int32(400),
                                                                 description = cms.untracked.string('jet pt'),
                                                                 plotquantity = cms.untracked.string('pt'),
                                                                 min = cms.untracked.double(0.0),
                                                                 max = cms.untracked.double(1000.0),
                                                                 name = cms.untracked.string('jet pt')
                                                                 )
                                                        )
                                 )

process.plotMETwithTrigger = process.plotMET.clone()
process.plotJetwithTrigger = process.plotJet.clone()

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
    process.cleanPatCandidatesPFlow +
    process.jetIdCut +
    process.oneJetAboveZero +
    process.getLargestJet +
    process.plotJet
    )

process.p2 = cms.Path(
    process.triggerSelection + 
    process.cleanPatCandidatesPFlow +
    process.jetIdCut + 
    process.oneJetAboveZero +
    process.getLargestJet +
    process.plotJetwithTrigger
    )
