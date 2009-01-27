import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/0E896ABC-CEBB-DD11-89F3-001E0BC198A2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/34BC46EF-74BC-DD11-9120-00163E11240B.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/36190C89-C6BB-DD11-B043-001E0B48D104.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/50835B88-C6BB-DD11-821F-0018FE28BF3E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/62B50289-C6BB-DD11-8975-001CC443B7B8.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/769F8A1A-DCBB-DD11-8ADF-001A645933C4.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/78E38887-C6BB-DD11-A90F-0018FE28AFE6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/98382D87-C6BB-DD11-9786-001F2969CD08.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/A4EEC8BC-CEBB-DD11-AB08-001E0BC1E34C.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/B4EAB943-86BC-DD11-8335-00163E1124E0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/C24E1FDC-7ABC-DD11-9797-00163E1124CD.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/C632F988-C6BB-DD11-9FEA-001E0B48A1BE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/FE346F88-C6BB-DD11-984F-001CC416B322.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0002/2CF8849B-52C0-DD11-90F6-001A645CED70.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0002/782C905F-EFBF-DD11-8A36-001E0B49D098.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0002/A223A387-1AC0-DD11-BEA3-00163E1124D7.root' ] );


secFiles.extend( [
                   ] )
