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
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/F6EA2A82-A77E-E011-92D8-0026189437F2.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/F052F9B8-C27E-E011-A321-002618943833.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/ECC670BB-7E7E-E011-9974-002618FDA208.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/DCB118A9-907E-E011-AF9D-002618943985.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/DC45422A-C57E-E011-B4E8-003048679048.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/B493CE0C-867E-E011-BB3A-00261894386E.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/B45ECD15-BD7E-E011-BD0D-002618943966.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/B08227F8-A67E-E011-A291-001A92810AB8.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/A86A0164-907E-E011-80A8-002618943957.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/A0FE8D0A-A97E-E011-8340-00304867908C.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/9A8AB018-AC7E-E011-83AB-003048679010.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/9668F11D-AA7E-E011-8249-00248C55CC9D.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/8C19A7E4-A47E-E011-B771-001A92971B7E.root',
    '/store/data/Run2011A/METBTag/AOD/May10ReReco-v1/0000/848B019E-307F-E011-9DE2-002618943911.root',
    )
    )
process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
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
                                        triggerConditions = cms.vstring('HLT_CentralJet80_MET100_v*',
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
                                   outputCommands = process.RECOEventContent.outputCommands,
                                   dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO'),
                                                                filterName = cms.untracked.string('SKIMMING')),
                                   SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('pathSelection')
                                                                     )
                                   )

process.e = cms.EndPath(process.skimOut)
