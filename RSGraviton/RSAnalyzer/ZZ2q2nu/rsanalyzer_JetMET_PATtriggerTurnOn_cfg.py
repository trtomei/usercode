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

#fileList = cms.untracked.vstring('file:'+setupInputFileName,)
fileList = cms.untracked.vstring([
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_0/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_1/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_10/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_11/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_12/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_13/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_14/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_15/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_16/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_17/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_18/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_19/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_2/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_20/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_3/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_4/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_5/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_6/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_7/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_8/output.root",
"file:condor_dataPattuples_2011May10ReReco_triggerStudies_9/output.root",
])
process.source = cms.Source("PoolSource",fileNames = fileList)

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(setupNumEvents)
        )

process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True)
        )

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output_'+setupSuffix+'.root')
)

# Jet
process.cutOnJet = cms.EDFilter("CandViewSelector",
                                src = cms.InputTag("goodPatJetsPFlow"),
                                cut = cms.string("(pt > 300.0) && (abs(eta) < 2.4)"),
                                minNumber = cms.int32(1),
                                filter = cms.bool(True)
                                )

process.getLargestJet = cms.EDFilter("LargestPtCandViewSelector",
                                     src = cms.InputTag("goodPatJetsPFlow"),
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
                                        triggerConditions = cms.vstring('HLT_CentralJet80_MET80_v*',),
                                        hltResults = cms.InputTag( "TriggerResults" , "", "HLT"),
                                        l1tResults = cms.InputTag( "" ),
                                        l1tIgnoreMask = cms.bool( True ),
                                        l1techIgnorePrescales = cms.bool( False ),
                                        daqPartitions = cms.uint32( 1 ),
                                        throw = cms.bool( False )
                                        )

process.p1 = cms.Path(
    process.cutOnJet +
    process.plotMET
    )

process.p2 = cms.Path(
    process.triggerSelection +
    process.cutOnJet +
    process.plotMETwithTrigger
    )
