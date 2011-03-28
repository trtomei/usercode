import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_40to120/QCD6j_40to120/patTuple_1_1_qOb.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_40to120/QCD6j_40to120/patTuple_4_0_UVV.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_40to120/QCD6j_40to120/patTuple_2_1_tpU.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_40to120/QCD6j_40to120/patTuple_3_1_hYc.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD6j_40to120/QCD6j_40to120/patTuple_5_1_ZHX.root",
]);
