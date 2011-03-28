import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W4j_0to100/W4j_0to100/patTuple_1_3_3be.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_0to100/W4j_0to100/patTuple_3_3_IQ6.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_0to100/W4j_0to100/patTuple_2_3_38x.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_0to100/W4j_0to100/patTuple_5_3_GX8.root",
"/store/user/tomei/Fall2010Backgrounds/W4j_0to100/W4j_0to100/patTuple_4_3_rPv.root",
]);
