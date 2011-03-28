import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_280to500/QCD4j_280to500/patTuple_5_1_AnV.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_280to500/QCD4j_280to500/patTuple_2_0_YVt.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_280to500/QCD4j_280to500/patTuple_1_1_o88.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_280to500/QCD4j_280to500/patTuple_3_1_0hE.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_280to500/QCD4j_280to500/patTuple_4_1_4cN.root",
]);
