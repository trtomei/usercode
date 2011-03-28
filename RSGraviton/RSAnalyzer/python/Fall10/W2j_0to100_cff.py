import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_14_0_m7Y.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_20_0_5si.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_17_0_AuJ.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_15_0_QrD.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_16_0_Fxm.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_19_0_rMu.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_9_0_VXo.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_21_0_Oqi.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_13_0_c7D.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_8_0_vhg.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_12_0_73T.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_10_0_p8i.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_18_0_LU7.root",
"/store/user/tomei/Fall2010Backgrounds/W2j_0to100/W2j_0to100/patTuple_11_0_zsw.root",
]);
