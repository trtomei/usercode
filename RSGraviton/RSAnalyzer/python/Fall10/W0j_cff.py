import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    "/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_66_1_GCe.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_75_1_vci.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_35_1_xF3.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_70_1_iNI.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_62_1_T0s.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_21_1_HGm.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_37_1_9vQ.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_13_1_p5c.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_58_1_8C6.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_15_1_x1V.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_20_1_0Hw.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_64_1_pZ7.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_67_1_5kK.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_71_1_pTC.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_36_1_QSS.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_18_1_oOR.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_19_1_5UJ.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_32_1_FYR.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_49_1_pLU.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_55_1_U5l.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_68_1_bof.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_7_1_rbd.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_2_1_ngz.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_56_1_5ll.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_24_1_idN.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_29_1_pZm.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_73_1_iyl.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_69_1_yXh.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_54_1_ZYX.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_28_1_mjk.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_61_1_y2A.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_47_1_NkX.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_5_1_5wp.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_8_1_bvB.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_42_1_G1p.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_12_1_cEl.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_22_1_pi7.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_52_1_GcW.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_38_1_wwZ.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_27_1_Di7.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_9_1_j1N.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_26_1_4pC.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_10_1_aBC.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_31_1_WgS.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_33_1_vb5.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_48_1_DmM.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_45_1_7ZR.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_40_1_2zk.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_44_1_W2h.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_14_1_c94.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_4_1_kui.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_63_1_g7G.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_23_1_BzQ.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_72_1_4LP.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_53_1_TGz.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_1_1_Wmd.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_43_1_07P.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_3_1_Xj8.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_39_1_8Aw.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_65_1_703.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_46_1_PjT.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_50_1_Yxs.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_34_1_LOd.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_41_1_mfd.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_60_1_YT9.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_59_1_LU6.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_11_1_Q0u.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_16_1_mqp.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_30_1_A3M.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_57_1_TVu.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_51_1_Vp8.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_74_1_4mM.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_25_1_AI7.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_6_1_5r4.root",
"/store/user/tomei/Fall2010Backgrounds/W0j/W0j/patTuple_17_1_4eS.root",
]);
