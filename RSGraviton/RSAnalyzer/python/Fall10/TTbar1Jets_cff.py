import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ 
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_7_0_rC3.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_10_0_K2g.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_12_1_ZaK.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_6_0_b60.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_13_0_zBS.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_9_0_zRP.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_2_1_R8l.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_11_0_Syd.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_8_0_7IB.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_3_0_bEK.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_1_1_OYc.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_4_0_CbC.root",
"/store/user/tomei/Fall2010BackGrounds_try3/TTbar1Jets/TTbar1Jets/patTuple_5_0_a9t.root",
]);
