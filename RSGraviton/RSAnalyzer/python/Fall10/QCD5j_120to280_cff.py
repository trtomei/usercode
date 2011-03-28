import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_120to280/QCD5j_120to280/patTuple_5_1_SX2.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_120to280/QCD5j_120to280/patTuple_3_1_dMs.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_120to280/QCD5j_120to280/patTuple_2_0_wjZ.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_120to280/QCD5j_120to280/patTuple_4_1_Uev.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_120to280/QCD5j_120to280/patTuple_1_1_TWk.root",
]);
