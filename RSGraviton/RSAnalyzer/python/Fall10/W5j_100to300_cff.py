import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W5j_100to300/W5j_100to300/patTuple_1_3_PNZ.root",
"/store/user/tomei/Fall2010Backgrounds/W5j_100to300/W5j_100to300/patTuple_5_3_XbT.root",
"/store/user/tomei/Fall2010Backgrounds/W5j_100to300/W5j_100to300/patTuple_2_3_fgi.root",
"/store/user/tomei/Fall2010Backgrounds/W5j_100to300/W5j_100to300/patTuple_4_3_asn.root",
"/store/user/tomei/Fall2010Backgrounds/W5j_100to300/W5j_100to300/patTuple_3_3_8JD.root",
]);
