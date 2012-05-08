import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_39_2_Op9.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_31_2_tBf.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_18_2_vVx.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_25_2_OeL.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_46_2_8So.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_13_2_b9H.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_37_2_93y.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_24_2_hWJ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_20_3_7S9.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_42_4_f6Q.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_45_4_tJt.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_49_4_90K.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_34_4_qx2.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_3_4_ObK.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_32_4_M50.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_26_4_CAY.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_6_4_6k5.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_5_4_8lF.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_43_5_vqw.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_22_5_lwU.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_35_5_8mN.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_44_5_gHQ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_23_5_TLb.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_15_5_C5D.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_21_5_Hao.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_14_5_VSe.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_16_5_4np.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_28_1_eJ6.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_4_1_yJU.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_10_1_fad.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_50_1_ype.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_11_1_Irj.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_48_1_mud.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_17_1_5hZ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_9_1_2OG.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_47_1_VDl.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_51_1_gyq.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_12_1_ICn.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_27_1_Yp9.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_30_1_tAt.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_8_1_vAM.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_40_1_rDE.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_19_1_rku.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_29_1_Cwm.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_1_1_AK2.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_33_1_AEW.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_38_1_MFF.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_41_1_ACw.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_2_1_iZV.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part1/skim_7_1_5CX.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_43_3_CjT.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_1_3_aJw.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_41_4_w7I.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_1_6_0O7.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_6_7_eRm.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_25_6_sZV.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_28_7_gGr.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_34_7_hkc.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_13_6_YWi.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_24_1_2IY.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_47_1_wav.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_15_1_euw.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_26_1_e7F.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_19_1_sk4.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_20_1_W7w.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_46_1_PN4.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_7_1_PRK.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_22_1_RTY.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_36_1_6jK.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_11_1_86C.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_35_1_F65.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_3_1_MmC.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_44_1_jTJ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_10_1_jMf.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_8_1_N1H.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_14_1_xpE.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_27_1_AEt.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_38_1_CIp.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_39_1_GG5.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_45_1_PO0.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_18_1_c3J.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_12_1_7wF.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_2_1_5li.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_37_1_iMV.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_17_1_P2Z.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_40_1_dCI.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_16_1_b18.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_32_1_8L4.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_42_1_Fpl.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_31_1_tn9.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_5_1_H3L.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_33_1_5w6.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_21_2_5uJ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_9_2_J1s.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_23_2_UHF.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_30_2_8vz.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_4_2_aSf.root",
"/store/user/tomei/MET_Run2011A-PromptReco_v5_part2/skim_29_2_QxA.root",
]);