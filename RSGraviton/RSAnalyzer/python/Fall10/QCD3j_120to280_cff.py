import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_120to280/QCD3j_120to280/patTuple_1_1_oWG.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_120to280/QCD3j_120to280/patTuple_5_0_Mzi.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_120to280/QCD3j_120to280/patTuple_4_0_61X.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_120to280/QCD3j_120to280/patTuple_2_0_OLv.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_120to280/QCD3j_120to280/patTuple_8_1_fnz.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_120to280/QCD3j_120to280/patTuple_7_1_qNT.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_120to280/QCD3j_120to280/patTuple_3_0_X4R.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD3j_120to280/QCD3j_120to280/patTuple_6_1_c3c.root",
]);
