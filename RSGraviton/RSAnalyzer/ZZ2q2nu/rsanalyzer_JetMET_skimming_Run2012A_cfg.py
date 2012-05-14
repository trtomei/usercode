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
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery=1000
# Summary
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.load("RSGraviton.RSAnalyzer.Run2012.MET_Run2012A-PromptReco-v1_AOD_test")

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

# Good lumis
#import FWCore.PythonUtilities.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#myLumis = LumiList.LumiList(filename = 'file.json').getCMSSWString().split(',')
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#process.source.lumisToProcess.extend(myLumis)

#process.Tracer = cms.Service("Tracer")

###########
# Trigger #
###########
process.triggerSelection = cms.EDFilter("TriggerResultsFilter",
                                        triggerConditions = cms.vstring('HLT_PFMET150_v*',
                                                                        #'HLT_PFMET180_v*'
                                                                        #'HLT_MET200_v*',    
                                                                        #'HLT_MET300_v*',
                                                                        #'HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v*'
                                                                        ),
                                        hltResults = cms.InputTag( "TriggerResults" , "", "HLT"),
                                        l1tResults = cms.InputTag( "" ),
                                        l1tIgnoreMask = cms.bool( True ),
                                        l1techIgnorePrescales = cms.bool( False ),
                                        daqPartitions = cms.uint32( 1 ),
                                        throw = cms.bool( False )
                                        )

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
