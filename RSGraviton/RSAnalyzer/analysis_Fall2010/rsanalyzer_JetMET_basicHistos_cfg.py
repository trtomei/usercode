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
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:skimmedFiles/skim_11_1_aFn.root',
    'file:skimmedFiles/skim_12_2_mq8.root',
    'file:skimmedFiles/skim_13_2_b4b.root',
    'file:skimmedFiles/skim_14_2_fqv.root',
    'file:skimmedFiles/skim_15_2_beN.root',
    'file:skimmedFiles/skim_16_2_gSy.root',
    'file:skimmedFiles/skim_17_2_xsM.root',
    'file:skimmedFiles/skim_18_2_FbO.root',
    'file:skimmedFiles/skim_19_1_Xkc.root',
    'file:skimmedFiles/skim_1_1_nKs.root',
    'file:skimmedFiles/skim_20_2_YfY.root',
    'file:skimmedFiles/skim_21_1_3zL.root',
    'file:skimmedFiles/skim_22_1_tKH.root',
    'file:skimmedFiles/skim_23_2_Tvs.root',
    'file:skimmedFiles/skim_24_2_16Q.root',
    'file:skimmedFiles/skim_26_1_Ici.root',
    'file:skimmedFiles/skim_27_2_m9b.root',
    'file:skimmedFiles/skim_28_2_Pgl.root',
    'file:skimmedFiles/skim_29_2_Jqf.root',
    'file:skimmedFiles/skim_2_1_2Jz.root',
    'file:skimmedFiles/skim_30_2_GpX.root',
    'file:skimmedFiles/skim_31_2_dyf.root',
    'file:skimmedFiles/skim_32_1_msv.root',
    'file:skimmedFiles/skim_33_2_3nm.root',
    'file:skimmedFiles/skim_34_2_rrj.root',
    'file:skimmedFiles/skim_36_2_tVQ.root',
    'file:skimmedFiles/skim_37_2_MAF.root',
    'file:skimmedFiles/skim_38_2_oHj.root',
    'file:skimmedFiles/skim_39_1_Pds.root',
    'file:skimmedFiles/skim_3_1_uFy.root',
    'file:skimmedFiles/skim_40_1_NK0.root',
    'file:skimmedFiles/skim_41_1_vYn.root',
    'file:skimmedFiles/skim_42_1_Pm5.root',
    'file:skimmedFiles/skim_43_2_AfL.root',
    'file:skimmedFiles/skim_44_1_qiF.root',
    'file:skimmedFiles/skim_45_1_5U2.root',
    'file:skimmedFiles/skim_46_1_ROj.root',
    'file:skimmedFiles/skim_47_1_vZx.root',
    'file:skimmedFiles/skim_48_1_Dgs.root',
    'file:skimmedFiles/skim_49_1_2rF.root',
    'file:skimmedFiles/skim_4_1_Pu3.root',
    'file:skimmedFiles/skim_50_2_qZO.root',
    'file:skimmedFiles/skim_51_2_buD.root',
    'file:skimmedFiles/skim_52_1_fOk.root',
    'file:skimmedFiles/skim_53_1_lgu.root',
    'file:skimmedFiles/skim_54_2_s3z.root',
    'file:skimmedFiles/skim_55_2_sxg.root',
    'file:skimmedFiles/skim_56_1_ud8.root',
    'file:skimmedFiles/skim_57_2_DOx.root',
    'file:skimmedFiles/skim_58_1_yiN.root',
    'file:skimmedFiles/skim_5_3_46G.root',
    'file:skimmedFiles/skim_60_1_u1z.root',
    'file:skimmedFiles/skim_61_1_33Z.root',
    'file:skimmedFiles/skim_62_2_FET.root',
    'file:skimmedFiles/skim_63_2_CBQ.root',
    'file:skimmedFiles/skim_64_1_n61.root',
    'file:skimmedFiles/skim_65_2_Y1R.root',
    'file:skimmedFiles/skim_66_1_I4w.root',
    'file:skimmedFiles/skim_67_1_mM2.root',
    'file:skimmedFiles/skim_68_1_5Pm.root',
    'file:skimmedFiles/skim_69_2_beL.root',
    'file:skimmedFiles/skim_70_1_vc2.root',
    'file:skimmedFiles/skim_71_2_0wb.root',
    'file:skimmedFiles/skim_72_1_ZZ3.root',
    'file:skimmedFiles/skim_73_2_PeR.root',
    'file:skimmedFiles/skim_74_2_6yg.root',
    'file:skimmedFiles/skim_76_2_q7J.root',
    'file:skimmedFiles/skim_77_2_jSa.root',
    'file:skimmedFiles/skim_79_1_31s.root',
    'file:skimmedFiles/skim_7_1_J9t.root',
    'file:skimmedFiles/skim_80_1_aKS.root',
    'file:skimmedFiles/skim_81_1_6UE.root',
    'file:skimmedFiles/skim_82_2_kut.root',
    'file:skimmedFiles/skim_83_1_knC.root',
    'file:skimmedFiles/skim_84_1_rdb.root',
    'file:skimmedFiles/skim_85_1_JM1.root',
    'file:skimmedFiles/skim_86_1_Va2.root',
    'file:skimmedFiles/skim_87_2_LeU.root',
    'file:skimmedFiles/skim_88_1_0Pw.root',
    'file:skimmedFiles/skim_89_2_Gxf.root',
    'file:skimmedFiles/skim_8_1_QGZ.root',
    'file:skimmedFiles/skim_90_1_H4n.root',
    'file:skimmedFiles/skim_91_1_L5Y.root',
    'file:skimmedFiles/skim_9_1_krj.root'
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
process.p1 = cms.Path(process.HBHENoiseFilter * (
                          process.triggerSelection +     
                          process.jetIdCut +
                          process.myCorrections +
                          process.jetCuts + process.METCut +    
                          process.differentPtCut +
                          process.getHardJets +
                          process.plotMET +
                          process.plotJetsGeneral)
                      )

#process.load('HLTrigger.HLTcore.triggerSummaryAnalyzerAOD_cfi')
#process.load('HLTrigger.HLTcore.hltEventAnalyzerAOD_cfi')
#process.p2 = cms.Path(process.triggerSummaryAnalyzerAOD + process.hltEventAnalyzerAOD)
