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

### Global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_R_38X_V15::All'

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_10_1_lQt.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_11_1_4rU.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_12_1_met.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_13_1_2iE.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_14_1_dAP.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_15_1_NaY.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_16_1_Y1S.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_17_1_W4N.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_18_1_ncG.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_19_1_byh.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_1_1_Q7R.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_20_1_XR7.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_21_1_kWd.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_22_1_LJC.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_23_1_V73.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_24_1_3dN.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_25_1_g19.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_26_1_9GN.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_27_1_p1C.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_28_1_oX6.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_29_1_EkQ.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_2_1_9iP.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_30_1_wCG.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_31_1_Hln.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_32_1_I3z.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_33_1_QZ0.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_34_1_NHb.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_35_1_wA4.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_36_1_3Re.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_37_1_fUB.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_38_1_xVd.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_39_1_xV4.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_3_1_O8n.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_40_1_zYf.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_41_1_55r.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_42_1_FBQ.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_43_1_IDD.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_44_1_SlF.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_45_1_EuN.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_46_1_Mw8.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_47_1_BSA.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_48_1_nNJ.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_49_1_Wf0.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_4_1_4b1.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_50_1_Smh.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_51_1_yn3.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_52_1_pFD.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_53_1_c94.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_54_1_E4D.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_55_1_PAc.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_56_1_elR.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_57_1_a1C.root',
'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_58_1_wwL.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_59_1_0Sm.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_5_1_uHL.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_60_1_bbh.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_61_1_T85.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_62_1_Ha8.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_63_1_7lQ.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_64_1_wdc.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_65_1_deK.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_66_1_7M3.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_67_1_HVV.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_68_1_IYm.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_69_1_Neg.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_6_1_eqh.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_70_1_B7g.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_71_1_gQR.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_72_1_gZ3.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_73_1_AFB.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_74_1_Y9B.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_75_1_DU0.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_76_1_JsK.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_77_1_89P.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_78_1_DW7.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_79_1_q9h.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_7_1_vTH.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_80_1_xUX.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_81_1_Y5b.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_82_1_xQu.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_83_1_Rx4.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_84_1_F76.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_85_1_vrj.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_8_1_Oj9.root',
# 'file:/home/fladias/CMSSW_3_8_6_patch2/src/RSGraviton/RSAnalyzer/analysis_Fall2010/Skims/skim_9_1_5tx.root'
#    "file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/selectedHBHEAndTrigger.root"
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
from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as basicjethistos

##################
# Mandatory cuts #
##################
# Good vertices, no scraping
process.primaryVertexFilter = cms.EDFilter("VertexSelector",
                                           src = cms.InputTag("offlinePrimaryVertices"),
                                           cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
                                           filter = cms.bool(True),
                                           )

process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )

process.vertexScraping = cms.Sequence(process.primaryVertexFilter + process.noscraping)

##########
# Jet ID #
##########
process.jetIdCut = cms.EDFilter("RSPFJetIdSelector",
                                jets = cms.InputTag("ak7PFJets"),
                                threshold = cms.double(30.0),
                                filter = cms.bool(True)
                                )

###############
# Corrections #
###############
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.myL2L3CorJetAK7PF= cms.EDProducer('PFJetCorrectionProducer',
                                          src        = cms.InputTag('jetIdCut'),
                                          correctors = cms.vstring('ak7PFL2L3')
                                          )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7PF)

###########
# Trigger #
###########
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskAlgoTrigConfig_cff')
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
process.load('HLTrigger.HLTfilters.hltLevel1GTSeed_cfi')
process.load('HLTrigger.special.hltPhysicsDeclared_cfi')
process.hltPhysicsDeclared.L1GtReadoutRecordTag = 'gtDigis'

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
thiagoJetPtCut = 80.0
thiagoJetEtaCut = 3.0
thiagoJetMassCut = 0.0
thiagoMETCut = 80.0

### For Path 1 - FAT jet from Z.
process.oneJetAboveZero = cms.EDFilter("PFJetConfigurableSelector",
                                       src = cms.InputTag("myL2L3CorJetAK7PF"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDFilter("LargestPtPFJetSelector",
                                     src = cms.InputTag("oneJetAboveZero"),
                                     maxNumber = cms.uint32(1)
                                     )

# Jet pt, eta cut
process.ptCut = cms.EDFilter("PFJetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > "+str(thiagoJetPtCut)),
                             minNumber = cms.int32(1),
                             )
process.etaCut = cms.EDFilter("PFJetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("abs(eta) < "+str(thiagoJetEtaCut)),
                              minNumber = cms.int32(1),
                              )
process.jetCuts = cms.Sequence(process.oneJetAboveZero + process.getLargestJet + process.ptCut + process.etaCut)

# MET cut
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("pfMet"),
                              ptMin = cms.double(thiagoMETCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

process.differentPtCut = cms.EDFilter("PFJetConfigurableSelector",
                                      src = cms.InputTag("myL2L3CorJetAK7PF"),
                                      theCut = cms.string("(pt > 25.0) && (abs(eta) < 5.0)"),
                                      minNumber = cms.int32(1)                                       
                                      )

process.getHardJets = cms.EDFilter("LargestPtPFJetSelector",
                                   src = cms.InputTag("differentPtCut"),
                                   maxNumber = cms.uint32(9999)
                                   )

process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')

# Other cuts
#
# EMF cut
process.EMFCut = cms.EDFilter("RSJetConfigurableSelector",
                              src = cms.InputTag("getHardJets"),
                              theCut = cms.string("(emEnergyFraction > 0.1) && (emEnergyFraction < 0.9)"),
                              minNumber = cms.int32(-1)
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
                                 src = cms.InputTag("pfMet"),
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

process.plotJetsGeneral = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                         src = cms.InputTag("getHardJets"),
                                         histograms = basicjethistos
                                         )

process.deepJetAnalyzer = cms.EDAnalyzer("RSJetAnalyzerV2",
                                         jets = cms.InputTag("getLargestJet"),
                                         numberInCollection = cms.uint32(0)
                                         )
# Path
process.p1 = cms.Path(
    process.HBHENoiseFilter +
    process.vertexScraping + 
#    process.hltPhysicsDeclared +
#    process.triggerSelection +
    process.jetIdCut +
    process.myCorrections +
    process.jetCuts + process.METCut +    
    process.differentPtCut +
    process.getHardJets +
#    process.EMFCut +
#    process.TIVCut +
#    process.multiJetCut +
    process.plotMET +
    process.plotJetsGeneral +
    process.deepJetAnalyzer
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
