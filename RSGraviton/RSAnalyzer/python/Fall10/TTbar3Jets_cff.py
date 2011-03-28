import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar3Jets/TTbar3Jets/patTuple_3_1_STT.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar3Jets/TTbar3Jets/patTuple_4_1_zGg.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar3Jets/TTbar3Jets/patTuple_2_1_H95.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar3Jets/TTbar3Jets/patTuple_1_1_fGG.root",
]);
