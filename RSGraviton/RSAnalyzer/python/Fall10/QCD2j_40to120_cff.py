import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_40to120/QCD2j_40to120/patTuple_2_1_FPi.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_40to120/QCD2j_40to120/patTuple_8_1_dqM.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_40to120/QCD2j_40to120/patTuple_3_1_SUJ.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_40to120/QCD2j_40to120/patTuple_6_1_SXH.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_40to120/QCD2j_40to120/patTuple_1_1_BDr.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_40to120/QCD2j_40to120/patTuple_5_1_GvG.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_40to120/QCD2j_40to120/patTuple_4_1_vF9.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_40to120/QCD2j_40to120/patTuple_7_1_LT4.root",
]);
