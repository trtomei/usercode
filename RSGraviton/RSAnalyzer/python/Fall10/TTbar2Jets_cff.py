import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar2Jets/TTbar2Jets/patTuple_1_1_Lvo.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar2Jets/TTbar2Jets/patTuple_4_1_xW7.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar2Jets/TTbar2Jets/patTuple_2_1_G32.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar2Jets/TTbar2Jets/patTuple_3_1_AwQ.root",
]);
