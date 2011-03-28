import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar4Jets/TTbar4Jets/patTuple_2_1_y1A.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar4Jets/TTbar4Jets/patTuple_3_1_OI1.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar4Jets/TTbar4Jets/patTuple_5_1_ASC.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar4Jets/TTbar4Jets/patTuple_4_1_sUn.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar4Jets/TTbar4Jets/patTuple_1_1_fka.root",
]);
