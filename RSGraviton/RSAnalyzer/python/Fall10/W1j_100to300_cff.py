import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_20_1_jLf.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_17_1_cTo.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_18_1_Xu1.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_13_1_rwr.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_19_1_lK3.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_12_1_BwL.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_1_1_Q5A.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_4_1_0Ws.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_15_1_axv.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_16_1_wVm.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_9_1_V91.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_11_1_Adz.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_3_1_nYm.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_5_1_L0Y.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_14_1_I8w.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_8_1_8uh.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_10_1_B7Z.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_2_1_y6r.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_6_1_yB7.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_100to300/W1j_100to300/patTuple_7_1_Fs7.root",
]);
