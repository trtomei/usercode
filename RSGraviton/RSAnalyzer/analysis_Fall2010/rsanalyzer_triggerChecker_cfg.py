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
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# Summary
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    "/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/F4A840A8-6CCC-DF11-A218-A4BADB3D00FF.root",
    "/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/9A07F077-3DCD-DF11-A190-003048C9CA8E.root",
    "/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/62AC2F3D-68CC-DF11-99A1-001E682F8738.root",
    "/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/4C699E75-3CCD-DF11-B294-0030487CAA5D.root",
    "/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/2A6004A3-3DCD-DF11-B959-00238BBDEAF7.root",
    "/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/1A64EBE3-72CC-DF11-BA19-E0CB4E29C4DB.root"
    )
                            )
process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output.root')
                                   )

#process.Tracer = cms.Service("Tracer")

# Global tag
#process.load('Configuration.StandardSequences.GeometryExtended_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = 'GR_R_39X_V5::All'

###########
# Trigger #
###########
process.triggerSelection = cms.EDFilter("TriggerResultsFilter",
                                        triggerConditions = cms.vstring('HLT_Jet50U AND HLT_MET65',
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
#process.p = cms.Path(process.hltEventAnalyzerAOD)


##########
# Jet ID #
##########
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')

process.skimOut = cms.OutputModule("PoolOutputModule",
                                   fileName = cms.untracked.string('skim.root'),
                                   outputCommands = process.RECOEventContent.outputCommands,
                                   dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO'),
                                                                filterName = cms.untracked.string('SKIMMING')),
                                   SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('pathSelection')
                                                                     )
                                   )

#process.e = cms.EndPath(process.skimOut)
