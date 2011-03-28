import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_500to5000/QCD2j_500to5000/patTuple_2_1_lxx.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_500to5000/QCD2j_500to5000/patTuple_4_0_I6v.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_500to5000/QCD2j_500to5000/patTuple_6_0_hH4.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_500to5000/QCD2j_500to5000/patTuple_3_0_JMG.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_500to5000/QCD2j_500to5000/patTuple_5_1_rfi.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD2j_500to5000/QCD2j_500to5000/patTuple_1_1_eZy.root",
]);
