#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("SANITY")

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

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    "file:selectedHBHEAndTrigger.root"
    )
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
process.jetIdCut = cms.EDProducer("RSJetIdSelector",
                                  jets = cms.InputTag("ak7CaloJets"),
                                  jetID = cms.InputTag("ak7JetID")
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
                                        hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
                                        l1tResults = cms.InputTag( "" ),
                                        l1tIgnoreMask = cms.bool( True ),
                                        l1techIgnorePrescales = cms.bool( False ),
                                        daqPartitions = cms.uint32( 1 ),
                                        throw = cms.bool( False )
                                        )

##################
# Kinematic cuts #
##################
thiagoJetPtCut = 0.0
thiagoJetEtaCut = 9999.0
thiagoJetMassCut = 0.0
thiagoMETCut = 0.0

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

# Jet pt, eta cut
process.ptCut = cms.EDFilter("JetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > "+str(thiagoJetPtCut)),
                             minNumber = cms.int32(1),
                             )
process.etaCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("abs(eta) < "+str(thiagoJetEtaCut)),
                              minNumber = cms.int32(1),
                              )
process.jetCuts = cms.Sequence(process.oneJetAboveZero + process.getLargestJet + process.ptCut + process.etaCut)

# MET cut
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("corMetGlobalMuons"),
                              ptMin = cms.double(thiagoMETCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

process.differentPtCut = cms.EDFilter("JetConfigurableSelector",
                                      src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                      theCut = cms.string("(pt > 25.0) && (abs(eta) < 5.0)"),
                                      minNumber = cms.int32(1)                                       
                                      )

process.getHardJets = cms.EDFilter("LargestPtCaloJetSelector",
                                   src = cms.InputTag("differentPtCut"),
                                   maxNumber = cms.uint32(9999)
                                   )

process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')

# Other cuts
#
# EMF cut
process.EMFCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("(emEnergyFraction > 0.1) && (emEnergyFraction < 0.9)"),
                              minNumber = cms.int32(1)
                              )

# TIV cut
process.TIVCut = cms.EDFilter("RSTrackerIndirectVetoFilter",
                              src = cms.InputTag("generalTracks"),
                              trackMinPt = cms.double(1.0),
                              seedTrackMinPt = cms.double(10.0),
                              trackMaxEta = cms.double(2.4),
                              minCone = cms.double(0.02),
                              maxCone = cms.double(0.3),
                              minAcceptableTIV = cms.double(0.1), # 10%, has no effect if filter is False
                              pixelHits = cms.int32(1),
                              trackerHits = cms.int32(5),
                              highPurityRequired = cms.bool(True),
                              filter = cms.bool(True)
                              )

# Multijets cut
process.multiJetCut = cms.EDFilter("RSEventDeltaPhiFilter",
                                   jets = cms.InputTag("getHardJets"),
                                   maxValue = cms.double(0.94)
                                   )

#########
# PLOTS #
#########

process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("corMetGlobalMuons"),
                                 histograms = cms.VPSet(
                                     cms.PSet(nbins = cms.untracked.int32(500),
                                              description = cms.untracked.string('MET'),
                                              plotquantity = cms.untracked.string('et'),
                                              min = cms.untracked.double(0.0),
                                              max = cms.untracked.double(1000.0),
                                              name = cms.untracked.string('MET')
                                              ),
                                     cms.PSet(nbins = cms.untracked.int32(500),
                                              description = cms.untracked.string('METpt'),
                                              plotquantity = cms.untracked.string('pt'),
                                              min = cms.untracked.double(0.0),
                                              max = cms.untracked.double(1000.0),
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

process.plotJetsGeneral = cms.EDAnalyzer("CaloJetHistoAnalyzer",
                                         src = cms.InputTag("getHardJets"),
                                         histograms = jethistos
                                         )

process.deepJetAnalyzer = cms.EDAnalyzer("RSJetAnalyzerV2",
                                         jets = cms.InputTag("getLargestJet"),
                                         numberInCollection = cms.uint32(0)
                                         )
# Path
process.p1 = cms.Path(process.HBHENoiseFilter *
                      (
                          process.triggerSelection +
                          process.jetIdCut +
                          process.myCorrections +
                          process.jetCuts + process.METCut +    
#                          process.differentPtCut +
#                          process.getHardJets +
#                          process.EMFCut +
#                          process.TIVCut +
#                          process.multiJetCut +
#                          process.plotMET +
#                          process.plotJetsGeneral)
                          process.deepJetAnalyzer
                      )
)
#process.load('HLTrigger.HLTcore.triggerSummaryAnalyzerAOD_cfi')
#process.load('HLTrigger.HLTcore.hltEventAnalyzerAOD_cfi')
#process.p2 = cms.Path(process.triggerSummaryAnalyzerAOD + process.hltEventAnalyzerAOD)

#myoutput  = process.RECOEventContent.outputCommands
#myoutput.append('keep *_getHardJets_*_*')
#print myoutput

#process.skimOut = cms.OutputModule("PoolOutputModule",
#                                   fileName = cms.untracked.string('selectedHBHEAndTrigger.root'),
#                                   outputCommands = myoutput,
#                                   dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO'),
#                                                                filterName = cms.untracked.string('SKIMMING')),
#                                   SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p1')
#                                                                     )
#                                   )
#process.e = cms.EndPath(process.skimOut)
