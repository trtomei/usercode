import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_120to280/QCD2j_120to280/patTuple_6_0_5w1.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_120to280/QCD2j_120to280/patTuple_3_1_1Rc.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_120to280/QCD2j_120to280/patTuple_1_1_u7D.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_120to280/QCD2j_120to280/patTuple_7_1_USG.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_120to280/QCD2j_120to280/patTuple_8_1_W2j.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_120to280/QCD2j_120to280/patTuple_4_0_3pM.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_120to280/QCD2j_120to280/patTuple_2_1_ONI.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_120to280/QCD2j_120to280/patTuple_5_0_TTX.root",
]);
