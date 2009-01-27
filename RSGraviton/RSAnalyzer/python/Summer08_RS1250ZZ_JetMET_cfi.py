import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/00D74CB1-DABB-DD11-81DB-001A64592EFC.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/0E181762-E3BB-DD11-B06F-001E0BC1EEC6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/14EEA270-D6BB-DD11-8187-001E0BC1EEDE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/18FC0098-DABB-DD11-8969-001A6459387A.root',#BROKEN
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/30D28F65-85BC-DD11-AF4D-00163E1124EB.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/3636B0B3-D0BB-DD11-8AFB-001A645931AE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/3E1ABA6C-D6BB-DD11-A26A-001E0BC1E34C.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/4C227E3E-C6BB-DD11-83A6-0018FE28BED0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/4C6B9A65-ACBC-DD11-B92F-001560AC4F10.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/62E02CBB-D5BB-DD11-9C61-001E0BC1EEDE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/8EF0E4CA-99BC-DD11-9673-00163E1124EB.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/A28E006C-D6BB-DD11-9BCC-001E0BC1EEDE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/CC1BD1C1-DFBB-DD11-ACBC-001A6459326E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0000/D2A68E5A-CBBB-DD11-98B2-001E0BC198C0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0002/3A61B25F-EFBF-DD11-9CDD-001E0B479F9C.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0002/9A1C6896-E7BF-DD11-944A-001E0BDBDC04.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1250/GEN-SIM-RECO/IDEAL_V9_v1/0002/A200A792-1AC0-DD11-969A-00163E1124E6.root' ] );


secFiles.extend( [
                   ] )
