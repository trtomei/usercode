import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_13_1_lY0.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_17_1_z4u.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_9_1_FNs.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_2_1_xxS.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_5_1_cz5.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_15_1_lVN.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_11_1_CmO.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_8_1_J0a.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_1_1_7zZ.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_16_1_v7Z.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_7_1_sjA.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_12_1_t4o.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_6_1_xVb.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_3_1_aCG.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_10_1_8Kc.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_4_1_4Ho.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_0to100/W3j_0to100/patTuple_14_1_Qdk.root",
]);
