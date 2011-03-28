import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_500to5000/QCD4j_500to5000/patTuple_5_0_nWc.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_500to5000/QCD4j_500to5000/patTuple_3_1_5ld.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_500to5000/QCD4j_500to5000/patTuple_1_1_suL.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_500to5000/QCD4j_500to5000/patTuple_2_1_1Qo.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_500to5000/QCD4j_500to5000/patTuple_4_1_w7J.root",
]);
