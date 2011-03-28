import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_4_1_Uqm.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_9_1_vhI.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_10_1_8PA.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_15_1_P00.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_7_1_rLs.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_6_1_Dl0.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_11_1_PcN.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_2_1_UPm.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_1_1_mTP.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_19_1_GJB.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_8_1_zvf.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_14_1_luG.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_13_1_3RF.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_18_1_yVA.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_3_1_D5x.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_17_1_C4Y.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_16_1_EkE.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_5_1_TmZ.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_300to800/W2j_300to800/patTuple_12_1_OvC.root",
]);
