import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_40to120/QCD4j_40to120/patTuple_5_0_KPJ.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_40to120/QCD4j_40to120/patTuple_3_0_p5T.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_40to120/QCD4j_40to120/patTuple_4_0_ffc.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_40to120/QCD4j_40to120/patTuple_2_0_GJX.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD4j_40to120/QCD4j_40to120/patTuple_1_1_6rw.root",
]);
