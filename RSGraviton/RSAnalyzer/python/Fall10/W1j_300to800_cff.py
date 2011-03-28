import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_16_1_iNU.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_9_1_zdj.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_13_1_Nd5.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_15_1_nhk.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_11_1_AKH.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_12_1_rzI.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_19_1_7mU.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_2_1_LmU.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_10_1_FAi.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_21_1_CnD.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_6_1_Gee.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_14_1_jow.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_18_1_DC5.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_4_1_hHd.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_20_1_Vyp.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_8_1_6Mj.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_7_1_Maz.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_3_1_pHI.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_17_1_obV.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_5_1_tN4.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_300to800/W1j_300to800/patTuple_1_1_qDT.root",
]);
