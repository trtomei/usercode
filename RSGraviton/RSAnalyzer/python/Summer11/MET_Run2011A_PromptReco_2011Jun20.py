import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_172_1_oKs.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_80_1_zKh.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_171_1_RXM.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_56_1_ZMJ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_81_1_zJv.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_55_1_y3D.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_129_1_du4.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_151_1_fOS.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_128_1_bk6.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_31_1_ZJD.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_154_1_k70.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_92_1_zAI.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_39_1_hsn.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_40_1_0ac.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_32_1_9Tv.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_131_1_ChD.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_170_1_WEr.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_87_1_y4F.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_133_1_r0Z.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_82_1_RQJ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_79_1_dbt.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_35_1_z7X.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_148_1_GLc.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_88_1_xWu.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_152_1_BR2.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_54_1_AZo.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_43_1_8PX.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_49_1_VtB.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_52_1_a5c.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_41_1_iXP.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_45_1_piG.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_169_1_oMP.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_53_1_bCz.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_38_1_7El.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_57_1_G7e.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_58_1_RXk.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_47_1_gxj.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_132_1_hz1.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_78_1_8dN.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_147_1_psg.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_48_1_TSx.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_42_1_Trh.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_85_1_ZyB.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_37_1_Fwx.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_91_1_csB.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_89_1_Mtn.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_34_1_DLO.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_84_1_K86.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_150_1_GdA.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_33_1_q49.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_51_1_hx6.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_36_1_xRf.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_95_1_SpK.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_46_1_UEd.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_130_1_YTz.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_83_1_lP6.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_50_1_GBr.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_149_1_Wns.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_93_1_0LP.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_86_1_Ypv.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_44_1_DHS.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_94_1_EeP.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_90_1_Yre.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_153_1_Oh1.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_13_1_Sz4.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_114_1_EY4.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_145_1_gsW.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_8_1_HO2.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_117_1_6DS.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_118_1_gs7.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_1_1_GGl.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_100_1_Tj8.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_113_1_pyB.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_119_1_Hnb.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_10_1_k8p.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_112_1_0Hz.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_105_1_ZAm.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_107_1_UsP.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_64_1_BnB.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_12_1_wQw.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_24_1_0yV.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_102_1_RwJ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_115_1_SQr.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_141_1_TLS.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_138_1_KBz.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_108_1_Rne.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_11_1_Y6J.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_111_1_hCi.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_124_1_Twv.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_110_1_QjX.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_139_1_wCh.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_106_1_8M3.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_123_1_NT3.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_121_1_TuK.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_134_1_9MW.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_143_1_dRL.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_120_1_FWO.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_14_1_gsY.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_109_1_VfU.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_104_1_c3N.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_168_1_V5S.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_17_1_Sk5.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_127_1_t2n.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_142_1_5sz.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_125_1_FDz.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_122_1_1a6.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_158_1_JFj.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_167_1_wqb.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_136_1_49G.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_116_1_obG.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_3_1_L9O.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_161_1_92E.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_166_1_dZO.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_164_1_LPY.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_165_1_808.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_144_1_ivj.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_162_1_0U4.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_26_1_L1z.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_137_1_clP.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_6_1_ygh.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_59_1_pUL.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_5_1_aMz.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_63_1_n6h.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_27_1_SZd.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_15_1_PUX.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_21_1_3Kp.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_18_1_0yQ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_4_1_BMg.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_30_1_6DB.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_155_1_ISh.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_156_1_Gnw.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_16_1_Xkm.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_157_1_4hP.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_126_1_v3B.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_159_1_VyL.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_72_1_XeN.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_73_1_Bws.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_103_1_RRR.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_76_1_YGC.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_75_1_3Gw.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_61_1_8Sm.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_28_1_Ahg.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_23_1_SVp.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_60_1_fS8.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_29_1_ILJ.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_140_1_9Qo.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_101_1_il4.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_96_1_KTo.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_97_1_iDL.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_9_1_PXm.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_65_1_RIb.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_25_1_CXo.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_67_1_zJh.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_20_1_kwa.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_77_1_Kwe.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_68_1_ygd.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_7_1_tx9.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_74_1_PRD.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_69_1_xft.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_22_1_8jw.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_71_1_MbN.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_98_1_gu3.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_66_1_tv3.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_160_1_emO.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_135_1_dl3.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_62_1_6iC.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_163_1_pI7.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_99_1_PRq.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_146_1_IQf.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_2_1_AHe.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_19_1_T02.root",
"/store/user/tomei/MET_Run2011A-PromptReco_2011Jun20/skim_70_1_0yP.root"]);
