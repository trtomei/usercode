import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/02456EE3-B1BC-DD11-AD0C-001F29C4D34E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/0620D5BF-B2BC-DD11-ADEB-001E0B482938.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/1E81EB7A-B3BC-DD11-A7A6-00163E1124D4.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/367CE62D-BBBC-DD11-9E29-001E0BC1EEC6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/3E985738-B2BC-DD11-9965-00163E1124E8.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/5082B538-B2BC-DD11-852F-00163E1124DE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/529730BF-B2BC-DD11-8622-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/607A2BEF-AFBC-DD11-ABE0-001E0B5F95B0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/6C63A4BF-B2BC-DD11-AC5E-001E0B48E91C.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/A2165722-BEBC-DD11-9584-001A64593A2A.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/A8095922-BEBC-DD11-BE53-001A64593154.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/B08DC9BD-B2BC-DD11-B68F-001F29C4D34E.root',#BROKEN
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/C04A37A6-BCBC-DD11-BC3C-001E0BC199C2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/C2807FB9-B5BC-DD11-98B0-00163E1124E8.root',#BROKEN
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/C63B9B2E-BBBC-DD11-ADF0-001E0BDBDC04.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/EA3127BE-B2BC-DD11-9CB5-0018FE28BED0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M750/GEN-SIM-RECO/IDEAL_V9_v1/0000/F2D8DF3B-BEBC-DD11-B39F-001A645933C4.root' ] );


secFiles.extend( [
                   ] )
