#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("CHECK")

###########################
# Basic process controls. #
###########################

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.EventContent.EventContent_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')


readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
#readFiles.extend( [
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/F4A840A8-6CCC-DF11-A218-A4BADB3D00FF.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/9A07F077-3DCD-DF11-A190-003048C9CA8E.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/62AC2F3D-68CC-DF11-99A1-001E682F8738.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/4C699E75-3CCD-DF11-B294-0030487CAA5D.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/2A6004A3-3DCD-DF11-B959-00238BBDEAF7.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/1A64EBE3-72CC-DF11-BA19-E0CB4E29C4DB.root' ] );

readFiles.extend(['file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/selectedHBHEAndTrigger.root'])

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output.root')
)

from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

##########
# Jet ID #
##########
process.jetIdCut = cms.EDFilter("RSJetIdSelector",
                                jets = cms.InputTag("ak7CaloJets"),
                                jetID = cms.InputTag("ak7JetID"),
                                threshold = cms.double(30.0),
                                filter = cms.bool(False),
                                tightQuality = cms.bool(False)
                                )

###############
# Corrections #
###############
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.ak7CaloL2Relative.useCondDB = False
process.ak7CaloL3Absolute.useCondDB = False
process.ak7CaloResidual.useCondDB = False
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('ak7CaloL2L3')
                                             )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

##################
# Kinematic cuts #
##################
process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDFilter("LargestPtCaloJetSelector",
                                     src = cms.InputTag("oneJetAboveZero"),
                                     maxNumber = cms.uint32(1)
                                     )

process.etaCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("(eta > 0.0) & (eta < 0.5)"),
                              minNumber = cms.int32(1),
                              )

process.EMFCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("(emEnergyFraction > 0.1) & (emEnergyFraction < 0.9)"),
                              minNumber = cms.int32(1),
                              )

process.normalRegion = cms.EDFilter("JetConfigurableSelector",
                                    src = cms.InputTag("getLargestJet"),
                                    theCut = cms.string("(phi > -2.3562) & (phi < 0)"),
                                    minNumber = cms.int32(1),
                                    )

process.hotRegion = cms.EDFilter("JetConfigurableSelector",
                                    src = cms.InputTag("getLargestJet"),
                                    theCut = cms.string("phi < -2.3562"),
                                    minNumber = cms.int32(1),
                                    )
                              
process.normalRegionCuts = cms.Sequence(process.oneJetAboveZero + process.getLargestJet + process.etaCut + process.EMFCut + process.normalRegion)
process.hotRegionCuts    = cms.Sequence(process.oneJetAboveZero + process.getLargestJet + process.etaCut + process.EMFCut + process.hotRegion)

process.plotNormalJets = cms.EDAnalyzer("CaloJetHistoAnalyzer",
                                        src = cms.InputTag("getLargestJet"),
                                        histograms = jethistos
                                        )
process.plotHotJets = cms.EDAnalyzer("CaloJetHistoAnalyzer",
                                     src = cms.InputTag("getLargestJet"),
                                     histograms = jethistos
                                     )
process.deepNormalJets = cms.EDAnalyzer("RSJetIdAnalyzer",
                                        jet = cms.InputTag("getLargestJet"),
                                        originalJets = cms.InputTag("ak7CaloJets"),
                                        jetID = cms.InputTag("ak7JetID")
                                        )
process.deepHotJets = cms.EDAnalyzer("RSJetIdAnalyzer",
                                     jet = cms.InputTag("getLargestJet"),
                                     originalJets = cms.InputTag("ak7CaloJets"),
                                     jetID = cms.InputTag("ak7JetID")
                                     )
                                        
# Path
process.p1 = cms.Path(
    process.jetIdCut +
    process.myCorrections +
    process.normalRegionCuts +
    process.plotNormalJets +
    process.deepNormalJets
    )
process.p2 = cms.Path(
    process.jetIdCut +
    process.myCorrections +
    process.hotRegionCuts +
    process.plotHotJets +
    process.deepHotJets
    )
