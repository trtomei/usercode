import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_10_1_vVv.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_18_1_zsx.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_21_1_YBD.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_20_1_fr4.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_7_1_HHe.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_3_1_zd5.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_4_1_Qvy.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_15_1_Yyy.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_24_1_p0j.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_14_1_2TZ.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_26_1_IN3.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_16_1_L6h.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_19_1_g1u.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_27_1_iYd.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_17_1_uMq.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_25_1_uTs.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_1_1_4hp.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_6_1_pOV.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_23_1_JmT.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_12_1_stf.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_22_1_tWN.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_13_1_NFC.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_8_1_b7Z.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_11_1_TTt.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_9_1_t4u.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_5_1_eT4.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_100to300/W2j_100to300/patTuple_2_1_8Xg.root",
]);
