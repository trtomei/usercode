import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W4j_300to800/W4j_300to800/patTuple_5_1_gWd.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_300to800/W4j_300to800/patTuple_3_1_bD4.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_300to800/W4j_300to800/patTuple_2_1_vQC.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_300to800/W4j_300to800/patTuple_4_1_hHk.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_300to800/W4j_300to800/patTuple_1_1_kTw.root",
]);
