import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_280to500/QCD3j_280to500/patTuple_3_1_YZp.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_280to500/QCD3j_280to500/patTuple_5_0_N5n.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_280to500/QCD3j_280to500/patTuple_1_1_BHE.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_280to500/QCD3j_280to500/patTuple_4_1_JW7.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_280to500/QCD3j_280to500/patTuple_2_1_hs9.root",
]);
