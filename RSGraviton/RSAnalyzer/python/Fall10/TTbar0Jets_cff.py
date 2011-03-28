import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_18_1_Uz8.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_27_1_ZiB.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_25_1_tsK.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_10_1_Mqc.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_30_1_QN4.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_26_0_i3m.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_15_0_AzG.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_11_0_jqI.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_24_1_uDc.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_8_1_5Jv.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_17_1_T9B.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_6_1_Aby.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_20_1_vHG.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_7_1_6fO.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_29_1_AJ9.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_4_1_hoM.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_23_1_SLV.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_16_1_Q3f.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_1_1_5V9.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_14_0_zL6.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_19_1_ge7.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_5_1_38h.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_22_1_TCB.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_13_0_aOF.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_2_1_qkr.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_21_1_zNF.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_28_1_LC1.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_3_1_617.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_12_0_A0B.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar0Jets/TTbar0Jets/patTuple_9_1_dCv.root",
]);
