#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

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
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_10_1_u7Z.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_11_1_717.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_1_1_cI4.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_12_1_LvA.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_13_2_qdI.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_14_1_hGZ.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_15_1_ZRy.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_16_1_EDT.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_17_1_6D8.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_18_1_CmZ.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_19_1_paJ.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_20_1_OmU.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_21_1_DYX.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_2_1_kh6.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_22_1_kzs.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_23_1_ctH.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_24_1_OL7.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_25_2_Wlr.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_26_1_Fbl.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_27_1_fAP.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_28_1_sGs.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_29_2_XMW.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_30_1_7Ka.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_31_1_wuL.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_3_1_5bD.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_32_1_Urk.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_33_1_4OP.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_34_1_I2k.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_35_1_cf2.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_36_2_7tC.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_37_1_pIB.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_38_1_B6S.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_39_1_GbP.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_40_2_J5b.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_41_1_d1d.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_4_1_Hx6.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_42_2_5qv.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_43_1_Vp1.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_44_2_8pF.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_45_1_suK.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_46_1_o52.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_47_1_Wir.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_48_1_zHq.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_49_1_EOW.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_50_1_ARV.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_51_1_L2x.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_5_1_nuY.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_52_1_YAO.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_53_1_tD5.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_54_1_3Fy.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_55_2_pWS.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_56_1_mKo.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_57_1_ZC7.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_58_1_lzC.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_59_1_9t1.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_60_1_y1s.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_61_1_qVh.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_6_1_vWb.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_62_1_zD1.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_63_1_Gd0.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_64_1_Cy7.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_65_1_a3t.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_66_1_grI.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_67_1_EhR.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_68_1_tmX.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_69_1_lxh.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_70_1_l4Q.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_71_1_IiX.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_7_1_PFP.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_72_1_etQ.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_73_2_mjN.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_74_1_HOZ.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_75_2_Fws.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_76_1_186.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_77_1_Ids.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_78_2_lpy.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_79_1_3R8.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_80_1_B9k.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_81_1_9BW.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_82_1_aqB.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_8_2_bm7.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_83_1_XeB.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_84_1_xEr.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_85_1_xRV.root',
'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/skim_9_1_oHC.root'
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
thiagoJetPtCut = 150.0
thiagoJetEtaCut = 3.0
thiagoJetMassCut = 0.0
thiagoMETCut = 150.0

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

# Path
process.p1 = cms.Path(process.HBHENoiseFilter *
                      (
                          process.triggerSelection)# +     
#                          process.jetIdCut +
#                          process.myCorrections +
#                          process.jetCuts + process.METCut +    
#                          process.differentPtCut +
#                          process.getHardJets +
#                          process.EMFCut +
#                          process.TIVCut +
#                          process.multiJetCut +
#                          process.plotMET +
#                          process.plotJetsGeneral)
                      )

#process.load('HLTrigger.HLTcore.triggerSummaryAnalyzerAOD_cfi')
#process.load('HLTrigger.HLTcore.hltEventAnalyzerAOD_cfi')
#process.p2 = cms.Path(process.triggerSummaryAnalyzerAOD + process.hltEventAnalyzerAOD)

myoutput  = process.RECOEventContent.outputCommands
#myoutput.append('keep *_getHardJets_*_*')
#print myoutput

process.skimOut = cms.OutputModule("PoolOutputModule",
                                   fileName = cms.untracked.string('selectedHBHEAndTrigger.root'),
                                   outputCommands = myoutput,
                                   dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO'),
                                                                filterName = cms.untracked.string('SKIMMING')),
                                   SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p1')
                                                                     )
                                   )
process.e = cms.EndPath(process.skimOut)
