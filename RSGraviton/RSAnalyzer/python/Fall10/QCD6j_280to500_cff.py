import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_280to500/QCD6j_280to500/patTuple_4_1_Ap6.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_280to500/QCD6j_280to500/patTuple_5_1_Y2A.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_280to500/QCD6j_280to500/patTuple_2_1_7RA.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_280to500/QCD6j_280to500/patTuple_3_0_kCM.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_280to500/QCD6j_280to500/patTuple_1_1_E6l.root",
]);
