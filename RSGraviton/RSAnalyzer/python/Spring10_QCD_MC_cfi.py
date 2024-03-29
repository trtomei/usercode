import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( ['/store/user/tomei/2010_Mar_29/qcdSkimming_37.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_31.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_59.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_55.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_16.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_17.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_45.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_50.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_41.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_52.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_49.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_28.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_51.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_33.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_4.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_48.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_10.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_26.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_40.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_34.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_47.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_61.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_2.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_23.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_1.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_54.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_20.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_7.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_27.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_11.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_14.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_39.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_53.root',
'/store/user/tomei/2010_Mar_29/qcdSkimming_66.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_65.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_24.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_22.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_57.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_5.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_18.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_56.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_43.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_60.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_13.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_21.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_30.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_38.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_29.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_15.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_44.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_19.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_6.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_62.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_35.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_9.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_3.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_8.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_58.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_12.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_46.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_63.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_36.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_32.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_42.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_25.root',
'/store/user/tomei/2010_Mar_29_v2/qcdSkimming_64.root'
                  ]
                  );

secFiles.extend( [
                   ] )

