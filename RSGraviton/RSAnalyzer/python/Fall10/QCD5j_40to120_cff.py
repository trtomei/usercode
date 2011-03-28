import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_40to120/QCD5j_40to120/patTuple_4_0_zXM.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_40to120/QCD5j_40to120/patTuple_3_1_pM8.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_40to120/QCD5j_40to120/patTuple_1_1_RVG.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_40to120/QCD5j_40to120/patTuple_2_1_LGt.root",
"/store/user/tomei/Fall2010BackGrounds_try3/QCD5j_40to120/QCD5j_40to120/patTuple_5_1_SyE.root",
]);
