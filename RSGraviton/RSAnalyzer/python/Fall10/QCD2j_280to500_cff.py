import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_280to500/QCD2j_280to500/patTuple_7_1_hcu.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_280to500/QCD2j_280to500/patTuple_2_1_De3.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_280to500/QCD2j_280to500/patTuple_4_1_NyT.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_280to500/QCD2j_280to500/patTuple_3_1_g0B.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_280to500/QCD2j_280to500/patTuple_1_1_8dn.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_280to500/QCD2j_280to500/patTuple_6_0_r89.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_280to500/QCD2j_280to500/patTuple_5_0_Lz9.root",
]);
