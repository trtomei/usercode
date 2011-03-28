import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_14_2_jwY.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_3_2_GiQ.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_13_2_EqF.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_6_2_mNy.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_1_2_6n0.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_11_2_lRC.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_8_2_bWw.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_15_2_Qcl.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_5_2_RR3.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_10_2_Phb.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_7_2_tsh.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_2_2_Qjd.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_19_2_h7Z.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_9_2_kpE.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_4_2_TTC.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_16_2_Qz4.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_18_2_AEq.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_17_2_1z1.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_20_2_fpx.root",
"/store/user/tomei/Fall2010Backgrounds/W1j_0to100/W1j_0to100/patTuple_12_2_RBp.root",
]);
