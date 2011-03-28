import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_120to280/QCD6j_120to280/patTuple_1_1_4U1.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_120to280/QCD6j_120to280/patTuple_5_1_y1e.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_120to280/QCD6j_120to280/patTuple_3_1_aMr.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_120to280/QCD6j_120to280/patTuple_4_0_gce.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_120to280/QCD6j_120to280/patTuple_2_1_yDs.root",
]);
