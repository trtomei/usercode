import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_40to120/QCD3j_40to120/patTuple_3_1_Jm1.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_40to120/QCD3j_40to120/patTuple_4_1_f37.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_40to120/QCD3j_40to120/patTuple_5_0_PR7.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_40to120/QCD3j_40to120/patTuple_1_1_8gU.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_40to120/QCD3j_40to120/patTuple_7_1_zh4.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_40to120/QCD3j_40to120/patTuple_2_1_a2M.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_40to120/QCD3j_40to120/patTuple_6_1_rlg.root",
]);
