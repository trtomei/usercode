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
#                            fileNames = cms.untracked.vstring("file:/home/trtomei/storage/data/Pythia_GZZjjmumu_700GeV_kmpl005_CMSSW358_RECO.root")
                            fileNames = cms.untracked.vstring("file:/home/trtomei/hdacs/CMSSW_3_6_3_patch2/src/RSGraviton/RSAnalyzer/analysis_Summer2010/hadronicChannel/test/W1Jets_pt300to800-alpgen.root")
                            )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("output.root")
                                   )
#process.Tracer = cms.Service("Tracer")

# Global tag
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START3X_V25::All'

##################
# Mandatory cuts #
##################

# The "select collisions" trigger ...
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskAlgoTrigConfig_cff')
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
process.load('HLTrigger/HLTfilters/hltLevel1GTSeed_cfi')

process.L1T1coll=process.hltLevel1GTSeed.clone()
process.L1T1coll.L1TechTriggerSeeding = cms.bool(True)
#process.L1T1coll.L1SeedsLogicalExpression = cms.string('0 AND (40 OR 41) AND NOT (36 OR 37 OR 38 OR 39)')
process.L1T1coll.L1SeedsLogicalExpression = cms.string('(40 OR 41) AND NOT (36 OR 37 OR 38 OR 39)')
# Don't ask for bit 0 in the MC.
#process.l1tcollpath = cms.Path(process.L1T1coll)

# The PhysicsDeclared HLT
process.hltHighLevel = cms.EDFilter("HLTHighLevel",
                                    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                    HLTPaths = cms.vstring('HLT_PhysicsDeclared'),# provide list of HLT paths (or patterns) you want
                                    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                                    andOr = cms.bool(True), # how to deal with multiple triggers: True: accept if ANY is true, False:accept if ALL are true
                                    throw = cms.bool(True)  # throw exception on unknown path names
                                    )

# Good vertices, no scraping
process.primaryVertexFilter = cms.EDFilter("VertexSelector",
                                           src = cms.InputTag("offlinePrimaryVertices"),
                                           cut = cms.string("!isFake && ndof > 4 && abs(z) <= 15 && position.Rho <= 2"),
                                           filter = cms.bool(True),
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
process.jetIdCut = cms.EDAnalyzer("RSJetIdSelector",
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

##################
# Kinematic cuts #
##################

jetPtCut = 150.0
jetEtaCut = 3.0
jetMassCut = 70.0
METCut = 150.0

### For Path 1 - FAT jet from Z.
process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDProducer("LargestPtCaloJetSelector",
                                       src = cms.InputTag("oneJetAboveZero"),
                                       maxNumber = cms.uint32(1)
                                       )

process.ptCut = cms.EDFilter("JetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > "+str(jetPtCut)),
                             minNumber = cms.int32(1),
                             )


process.differentPtCut = cms.EDFilter("JetConfigurableSelector",
                                      src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                      theCut = cms.string("(pt > 25.0) && (abs(eta) < 5.0)"),
                                      minNumber = cms.int32(1)                                       
                                      )

process.getHardJets = cms.EDProducer("LargestPtCaloJetSelector",
                                     src = cms.InputTag("differentPtCut"),
                                     maxNumber = cms.uint32(9999)
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

process.deltaPhiFilter = cms.EDFilter("RSEventDeltaPhiFilter",
                                      jets = cms.InputTag("getHardJets"),
                                      maxValue = cms.double(0.94)
                                      )

#################
# VBTF electron #
#################
process.load("RSGraviton.RSAnalyzer.simpleEleIdSequence_cff")
process.seqEleId = cms.Sequence(process.simpleEleId80relIso)

process.electronVBTFFilter = cms.EDFilter('RSElectronVBTFFilter',
                                          # cuts
                                          ETCut = cms.untracked.double(20.),
                                          vetoSecondElectronEvents = cms.untracked.bool(True),
                                          ETCut2ndEle = cms.untracked.double(20.),
                                          # trigger here
                                          triggerCollectionTag = cms.untracked.InputTag("TriggerResults","","HLT"),
                                          triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","","HLT"),
                                          hltpath = cms.untracked.string("HLT_Ele15_SW_L1R"),
                                          hltpathFilter = cms.untracked.InputTag("hltL1NonIsoHLTNonIsoSingleElectronEt15PixelMatchFilter"),
                                          electronMatched2HLT = cms.untracked.bool(False),
                                          electronMatched2HLT_DR = cms.untracked.double(0.1),
                                          # electrons
                                          electronCollectionTag = cms.untracked.InputTag("gsfElectrons"),   # Electron collection name
                                          # electron ID
                                          electronIdTag = cms.untracked.InputTag("simpleEleId80relIso"),    # Eletron ID map name
                                          electronIdMin = cms.untracked.int32(7), # Must pass ALL selections
                                          # fiducial definition
                                          BarrelMaxEta = cms.untracked.double(1.4442),
                                          EndCapMinEta = cms.untracked.double(1.566),
                                          EndCapMaxEta = cms.untracked.double(2.5),
                                          )

#############
# VBTF muon #
#############
process.load("ElectroWeakAnalysis.WMuNu.WMuNuSelection_cff")
process.selcorMet.MtMin = cms.untracked.double(-999999.9)
process.selcorMet.plotHistograms = cms.untracked.bool(True)
process.selcorMet.JetTag = cms.untracked.InputTag("ak5CaloJets")

############
# Counting #
############
# In case you want to check efficiencies cut by cut.
process.eventCounter = cms.EDAnalyzer("EventCounter")
process.eventCounterTwo = process.eventCounter.clone()
process.eventCounterThree = process.eventCounter.clone()
process.eventCounterFour = process.eventCounter.clone()
process.eventCounterFive = process.eventCounter.clone()
process.eventCounterSix = process.eventCounter.clone()
process.eventCounterSeven = process.eventCounter.clone()
process.eventCounterEight = process.eventCounter.clone()
process.eventCounterNine = process.eventCounter.clone()
process.eventCounterTen = process.eventCounter.clone()

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
process.doMultiJets = cms.Sequence(process.differentPtCut + process.getHardJets)
process.multiJetVeto = cms.Sequence(process.deltaPhiFilter)
process.VBTFelectron = cms.Sequence(process.simpleEleId80relIso + process.electronVBTFFilter);
process.VBTFmuon = cms.Sequence(process.corMetWMuNus + process.selcorMet)
process.noMuonAndNoElectron = cms.Sequence(process.simpleEleId80relIso + ~process.electronVBTFFilter +
                                           process.corMetWMuNus + ~process.selcorMet)

process.thiagoSelection = cms.Sequence(
    process.eventCounter + process.goodVertexSequence + # Good vertex
    process.eventCounterTwo + process.jetId + process.cuts0 + process.getLargestJet + process.cuts2 + # One jet in eta region
    process.eventCounterThree + process.cuts1 + # Jet must be above 150 GeV
    process.eventCounterFour + process.cuts3 + # Jet must have mass above 70 GeV
    process.eventCounterFive + process.cuts4 + # MET must be above 150 GeV
    process.eventCounterSix + process.doMultiJets + process.multiJetVeto + # The two-jet // multijet veto
    process.eventCounterSeven
    )

process.pathSelection = cms.Path(process.thiagoSelection)
process.pathElectron = cms.Path(process.thiagoSelection + process.VBTFelectron + process.eventCounterEight)
process.pathMuon = cms.Path(process.thiagoSelection + process.VBTFmuon + process.eventCounterNine)
process.pathNoMuonAndNoElectron = cms.Path(process.thiagoSelection + process.noMuonAndNoElectron + process.eventCounterTen)

process.skimOut = cms.OutputModule("PoolOutputModule",
                                   fileName = cms.untracked.string('skim.root'),
                                   outputCommands = process.AODSIMEventContent.outputCommands,
                                   dataset = cms.untracked.PSet(dataTier = cms.untracked.string('AOD-SIM'),
                                                                filterName = cms.untracked.string('SKIMMING')),
                                   SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('pathSelection')
                                                                     )
                                   )

process.e = cms.EndPath(process.skimOut)
