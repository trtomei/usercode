import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_280to500/QCD5j_280to500/patTuple_5_0_WhV.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_280to500/QCD5j_280to500/patTuple_4_0_StB.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_280to500/QCD5j_280to500/patTuple_3_0_iwU.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_280to500/QCD5j_280to500/patTuple_2_0_Kxi.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_280to500/QCD5j_280to500/patTuple_1_1_5uB.root",
]);
