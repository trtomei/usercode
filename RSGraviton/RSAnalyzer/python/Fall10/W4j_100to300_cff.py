import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W4j_100to300/W4j_100to300/patTuple_3_2_H8j.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_100to300/W4j_100to300/patTuple_2_2_H1T.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_100to300/W4j_100to300/patTuple_4_2_1GA.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_100to300/W4j_100to300/patTuple_1_2_H0Z.root",
]);
