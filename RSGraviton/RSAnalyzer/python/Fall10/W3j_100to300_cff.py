import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W3j_100to300/W3j_100to300/patTuple_4_1_6XO.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_100to300/W3j_100to300/patTuple_8_1_eKF.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_100to300/W3j_100to300/patTuple_6_1_J1r.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_100to300/W3j_100to300/patTuple_9_1_tvK.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_100to300/W3j_100to300/patTuple_3_1_xfV.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_100to300/W3j_100to300/patTuple_2_1_9r7.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_100to300/W3j_100to300/patTuple_5_1_8B6.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_100to300/W3j_100to300/patTuple_7_1_uiQ.root",
"/store/user/tomei/Fall2010Backgrounds/W3j_100to300/W3j_100to300/patTuple_1_1_qgJ.root",
]);
