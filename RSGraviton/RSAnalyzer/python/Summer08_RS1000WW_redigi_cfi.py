import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/3410AA53-2FE6-DD11-B127-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/EAF200CC-12E6-DD11-A13F-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/EAABB69E-12E6-DD11-8457-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/E4AD4DAB-13E6-DD11-99F9-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/E2D93552-14E6-DD11-B27D-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/DEA09720-0DE6-DD11-9AB8-001E0B479CF6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/DE9E8958-1CE6-DD11-9826-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/D49ABE2A-0FE6-DD11-A37D-001E0B4A0EFA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/D2971FE4-12E6-DD11-8F37-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/D0DEA785-12E6-DD11-83B1-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/CC24A532-1CE6-DD11-B0A4-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/BCBADF3D-0FE6-DD11-A6B0-001E0B479CF6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/BA13300B-13E6-DD11-B2A0-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/B6F47C19-0DE6-DD11-8A93-001F29C4C3BC.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/B6F1EB32-14E6-DD11-A413-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/B60C4639-11E6-DD11-BEB6-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/B2D17344-12E6-DD11-AE99-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/ACA19E5C-14E6-DD11-9BBA-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/AC694DAB-0DE6-DD11-9397-001E0B5FA506.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/AA9E4477-0DE6-DD11-BE4F-001E0B5FA506.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/A6A18D75-0DE6-DD11-BFAA-001F296BE5A6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/A6332334-13E6-DD11-8287-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/A4F6FD5C-12E6-DD11-9747-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/A0E8571F-0DE6-DD11-944A-001F29C4D34E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/9A3A3E51-12E6-DD11-96A0-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/9858ED5C-13E6-DD11-B12E-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/96ECA331-0FE6-DD11-92EC-001E0B5F3142.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/90BF81D4-11E6-DD11-9237-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/8CE6FF96-0DE6-DD11-8F85-001F29C4A3A2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/8CDD45F9-1DE6-DD11-A31A-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/8CB3CC80-11E6-DD11-8719-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/8C787350-0DE6-DD11-BF4F-001F296A377E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/86D8324B-0DE6-DD11-94E4-001E0B482938.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/84C35822-1DE6-DD11-8870-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/82735806-1DE6-DD11-BA54-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/7A87AC1A-0DE6-DD11-A5A9-001E0B5F5892.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/783B2ABC-13E6-DD11-84F0-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/76123BF5-12E6-DD11-8BD6-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/6C0C742A-0FE6-DD11-8DE0-001F296B24D0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/689A4D9B-0DE6-DD11-BEDC-001F29C464E0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/64B94B9E-14E6-DD11-8EE4-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/5EF16D4C-0DE6-DD11-8187-001F29C464E0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/5E20C197-0DE6-DD11-9DCB-001E0B5F27AC.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/5C7A1F72-13E6-DD11-B09D-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/5AAB0B21-1CE6-DD11-A75A-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/4EC8713E-14E6-DD11-963E-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/48877D4E-1CE6-DD11-A619-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/4835D19C-0DE6-DD11-BCDC-001F29C4D34E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/4668743A-0FE6-DD11-B9B3-001E0B479CF6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/42EB2BDF-10E6-DD11-A5A0-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/3ABE3EDE-10E6-DD11-901A-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/38D3889D-0DE6-DD11-B1BC-001F296A377E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/38D02050-11E6-DD11-8AEA-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/3611A22D-14E6-DD11-ACD2-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/345EC52A-12E6-DD11-9B96-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/2E3DAE34-0FE6-DD11-AEA6-001E0B5FA5BE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/26B943DE-10E6-DD11-9F2D-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/24673D42-11E6-DD11-B549-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/2202F724-13E6-DD11-A0C6-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/20F3C26F-1CE6-DD11-B0A5-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/0EA27877-0DE6-DD11-8959-001B78E1095C.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/0C457E94-12E6-DD11-BAD6-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/0A97E134-0FE6-DD11-8103-001F29C4D34E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/088901C7-12E6-DD11-A3B5-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/06AC7956-0DE6-DD11-B1AA-001F29C450E2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/04875965-13E6-DD11-81B7-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/02936CF9-11E6-DD11-A651-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/007E7D9F-0DE6-DD11-AF21-001F29C450E2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/F278FA99-08E6-DD11-BFBA-001F29C4C3BC.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/F055D0EC-09E6-DD11-9D87-001F29C464E0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/EE9BFE8F-0DE6-DD11-A819-001F296B7586.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/A63C417E-0BE6-DD11-9E27-001E0B482938.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/7A8CED7B-0BE6-DD11-80A9-001E0B471C7E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/6213778B-0DE6-DD11-92E7-001E0B48A1BE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/50964024-0DE6-DD11-8D02-001F29C424DA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/3EC8A0D2-06E6-DD11-A039-001E0B477F52.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/2C3252B3-0DE6-DD11-A5E6-001E0B479CF6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1000/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/2C1DC91F-0DE6-DD11-8C7B-001F29C450E2.root' ] );


secFiles.extend( [
                   ] )

