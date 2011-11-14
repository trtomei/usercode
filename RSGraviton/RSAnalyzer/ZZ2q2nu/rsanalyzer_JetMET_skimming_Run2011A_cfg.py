#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("SKIM")

###########################
# Basic process controls. #
###########################

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.EventContent.EventContent_cff')
#process.load("Configuration.StandardSequences.Geometry_cff")
#process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery=1000
# Summary
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FED96BE1-859A-E011-836E-001A92971B56.root',
#    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/F6EA2A82-A77E-E011-92D8-0026189437F2.root',
    )
                            )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(10000)
        )

### The output
#process.TFileService = cms.Service("TFileService",
#                                   fileName = cms.string('output.root')
#                                   )

#process.Tracer = cms.Service("Tracer")

# Global tag
#process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_R_42_V14::All'

###########
# Trigger #
###########
process.triggerSelection = cms.EDFilter("TriggerResultsFilter",
                                        triggerConditions = cms.vstring('HLT_CentralJet80_MET100_v*', # Defeat this so it becomes smaller
                                                                        'HLT_CentralJet80_MET160_v*',
                                                                        ),
                                        hltResults = cms.InputTag( "TriggerResults" , "", "HLT"),
                                        l1tResults = cms.InputTag( "" ),
                                        l1tIgnoreMask = cms.bool( True ),
                                        l1techIgnorePrescales = cms.bool( False ),
                                        daqPartitions = cms.uint32( 1 ),
                                        throw = cms.bool( False )
                                        )

process.load( "HLTrigger.HLTcore.hltEventAnalyzerAOD_cfi" )

process.pathSelection = cms.Path(process.triggerSelection)

process.skimOut = cms.OutputModule("PoolOutputModule",
                                   fileName = cms.untracked.string('skim.root'),
                                   outputCommands = process.RECOSIMEventContent.outputCommands,
                                   dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO'),
                                                                filterName = cms.untracked.string('SKIMMING')),
                                   SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('pathSelection')
                                                                     )
                                   )

process.e = cms.EndPath(process.skimOut)
