import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_500to5000/QCD3j_500to5000/patTuple_2_0_XWK.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_500to5000/QCD3j_500to5000/patTuple_3_1_yiG.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_500to5000/QCD3j_500to5000/patTuple_4_1_dla.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_500to5000/QCD3j_500to5000/patTuple_1_1_1F3.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_500to5000/QCD3j_500to5000/patTuple_5_1_FaL.root",
]);
