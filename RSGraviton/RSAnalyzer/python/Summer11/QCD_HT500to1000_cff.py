import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_59_1_OkF.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_41_1_Ftz.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_106_1_pLu.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_15_1_90g.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_84_1_w5h.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_63_1_xIh.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_93_1_eOe.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_25_1_wHW.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_47_1_l0B.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_29_1_08w.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_49_1_ZGS.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_73_1_gRD.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_65_1_UVR.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_57_1_XbE.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_27_1_oAC.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_64_1_prM.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_68_1_mpO.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_23_1_owQ.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_60_1_RKB.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_13_1_Py7.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_88_1_uX3.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_55_1_g7C.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_26_1_WC2.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_58_1_vo2.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_38_1_qQz.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_97_1_UmX.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_52_1_efI.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_31_1_T2Z.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_20_1_j0W.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_42_1_AUW.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_61_1_jQd.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_46_1_tB9.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_83_1_Wq4.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_77_1_Heo.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_62_1_7Cf.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_50_1_qAy.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_92_1_AZK.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_10_1_mHe.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_24_1_x2w.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_2_1_Bwu.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_51_1_inU.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_3_1_eUY.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_56_1_XoN.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_33_1_Dqm.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_94_1_Kjy.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_5_1_6I1.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_16_1_etc.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_11_1_949.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_102_1_9Qn.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_37_1_KIX.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_44_1_5dZ.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_17_1_lKU.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_21_1_nLv.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_34_1_CqY.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_39_1_ZGu.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_81_1_iVP.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_54_1_ydc.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_67_1_A79.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_48_1_p5c.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_18_1_3M0.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_74_1_Ihv.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_87_1_Qbn.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_12_1_rfE.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_75_1_MbC.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_30_1_vO9.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_53_1_pRX.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_82_1_mN8.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_103_1_Uhy.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_90_1_CdG.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_99_1_iIX.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_19_1_NXN.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_72_1_KdE.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_22_1_1el.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_98_1_aEJ.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_89_1_x3x.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_100_1_I6F.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_6_1_y9M.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_105_1_dpN.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_32_1_oMN.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_70_1_SAR.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_78_1_Qns.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_4_1_gdO.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_40_1_ISo.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_91_1_5JY.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_95_1_NS9.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_104_1_vUP.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_71_1_bdB.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_85_1_re6.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_7_1_VoO.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_79_1_sYm.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_76_1_Haw.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_14_1_7fO.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_8_1_43v.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_45_1_bW0.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_1_1_1VL.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_9_1_yEp.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_35_1_i7E.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_101_1_6cw.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_28_1_Yad.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_96_1_bhN.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_43_1_6Mz.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_36_1_1vo.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_69_1_Lfe.root",
"/store/user/tomei/QCD_TuneZ2_HT-500to1000_7TeV-madgraph/skim_80_1_Xkh.root"
]);
