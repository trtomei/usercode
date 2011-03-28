import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W5j_0to100/W5j_0to100/patTuple_4_1_yaP.root",
"/store/user/tomei/Fall2010Backgrounds/W5j_0to100/W5j_0to100/patTuple_3_1_YEj.root",
"/store/user/tomei/Fall2010Backgrounds/W5j_0to100/W5j_0to100/patTuple_2_1_euY.root",
"/store/user/tomei/Fall2010Backgrounds/W5j_0to100/W5j_0to100/patTuple_1_1_hXb.root",
]);
