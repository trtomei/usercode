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
                            fileNames = cms.untracked.vstring("file:/home/trtomei/hdacs/CMSSW_3_6_3_patch2/src/RSGraviton/RSAnalyzer/analysis_Summer2010/hadronicChannel/test/W1Jets_pt300to800-alpgen.root")
                            )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output.root')
                                   )
#process.Tracer = cms.Service("Tracer")

# Global tag
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_R_38X_V15::All'

##################
# Mandatory cuts #
##################

process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(24),
                                           maxd0 = cms.double(2)
                                                                                                 )
process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )

##########
# Jet ID #
##########
process.jetIdCut = cms.EDProducer("RSJetIdSelector",
                                  jets = cms.InputTag("ak7CaloJets"),
                                  jetID = cms.InputTag("ak7JetID")
                                  )

###############
# Corrections #
###############
process.load('JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff')

# For Calo jets
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('ak7CaloL2L3')
                                             )

process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

###########
# Trigger #
###########
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskAlgoTrigConfig_cff')
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
process.load('HLTrigger/HLTfilters/hltLevel1GTSeed_cfi')

process.triggerSelection = cms.EDFilter("TriggerResultsFilter",
                                        triggerConditions = cms.vstring(
    'HLT_MET65_CenJet50U_v*',
    'HLT_MET80_CenJet50U_v*',
    ),
                                        hltResults = cms.InputTag( "TriggerResults" , "", "HLT"),
                                        l1tResults = cms.InputTag( "" ),
                                        l1tIgnoreMask = cms.bool( True ),
                                        l1techIgnorePrescales = cms.bool( False ),
                                        daqPartitions = cms.uint32( 1 ),
                                        throw = cms.bool( False )
                                        )
##################
# Kinematic cuts #
##################

jetPtCut = 80.0
jetEtaCut = 3.0
jetMassCut = 0.0
METCut = 80.0

### For Path 1 - FAT jet from Z.
process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDFilter("LargestPtCaloJetSelector",
                                     src = cms.InputTag("oneJetAboveZero"),
                                     maxNumber = cms.uint32(1)
                                     )

process.ptCut = cms.EDFilter("JetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > "+str(jetPtCut)),
                             minNumber = cms.int32(1),
                             )

process.etaCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("abs(eta) < "+str(jetEtaCut)),
                              minNumber = cms.int32(1),
                              )

process.massCut = cms.EDFilter("JetConfigurableSelector",
                               src = cms.InputTag("getLargestJet"),
                               theCut = cms.string("mass > "+str(jetMassCut)),
                               minNumber = cms.int32(1)
                               )

process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("corMetGlobalMuons"),
                              ptMin = cms.double(METCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

############
# Counting #
############
# In case you want to check efficiencies cut by cut.
process.eventCounter = cms.EDAnalyzer("EventCounter")
process.eventCounterTwo = process.eventCounter.clone()
process.eventCounterThree = process.eventCounter.clone()
process.eventCounterFour = process.eventCounter.clone()
process.eventCounterFive = process.eventCounter.clone()

#########
# Paths #
#########

# Summary of cuts.
process.goodVertexSequence = cms.Sequence(process.primaryVertexFilter+process.noscraping)
process.jetId  = cms.Sequence(process.jetIdCut + process.myCorrections)
process.cuts0  = cms.Sequence(process.oneJetAboveZero)
process.cuts1  = cms.Sequence(process.ptCut)
process.cuts2  = cms.Sequence(process.etaCut)
process.cuts3  = cms.Sequence(process.massCut)
process.cuts4  = cms.Sequence(process.METCut)

process.thiagoSelection = cms.Sequence(
    process.eventCounter + process.goodVertexSequence + # Good vertex
    process.eventCounterTwo + process.jetId + process.cuts0 + process.getLargestJet + process.cuts2 + # One jet in eta region
    process.eventCounterThree + process.cuts1 + # Jet must be above pt cut
    process.eventCounterFour + process.cuts4 + # MET must be above MET cut
    process.eventCounterFive
    )

#process.pathSelection = cms.Path(process.thiagoSelection)
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
