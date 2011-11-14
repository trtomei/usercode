import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_17_1_Pcm.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_12_1_N8U.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_4_1_EqK.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_28_1_nfB.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_29_1_X2U.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_6_1_R7m.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_5_1_HOx.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_3_1_KBg.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_9_1_pkx.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_10_1_rEJ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_16_1_emi.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_24_1_GTH.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_2_1_hDd.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_13_1_HOa.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_1_1_az4.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_25_1_gWE.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_26_1_wnF.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_20_1_h6F.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_27_1_mZg.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_7_1_gVz.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_11_1_D8v.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_22_1_l3c.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_19_1_ZtT.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_15_1_tC8.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_23_1_uBF.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_18_1_L5p.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_21_1_ZRS.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_30_1_bAa.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_8_1_bsy.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_31_1_Wdc.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v6_2011Set30_try3/skim_14_1_mUj.root",
]);
