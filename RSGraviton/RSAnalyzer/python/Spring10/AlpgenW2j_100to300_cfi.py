import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/D6CF9A14-5547-DF11-9DDC-90E6BA19A22B.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/D665CA8F-5A47-DF11-8B01-00163E010356.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/A2ED0865-5747-DF11-B8AD-E0CB4E1A11A7.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/80C669FB-5847-DF11-88D0-00163E0105DC.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/76A6D911-5747-DF11-9B53-90E6BA442F23.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/CCB4C63C-4447-DF11-8D44-E0CB4E1A1181.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/C627511D-3047-DF11-AD33-0019BB3FD4AA.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/A46C5268-2547-DF11-8156-00261834B59B.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/84B882CB-2947-DF11-A7D8-0030487CD9C8.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/84B49769-2547-DF11-9709-00261834B559.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/7A8719E8-2947-DF11-869E-0030487C6A2C.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/247EC38E-2E47-DF11-9622-90E6BA0D09BB.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/FC404813-2147-DF11-B5AA-E0CB4E1A1187.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/DE2FBD90-2147-DF11-B338-00163E01008B.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/DC79B074-1B47-DF11-B8DD-90E6BA19A24C.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/DADEDC7A-2647-DF11-8501-90E6BA0D09B2.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/D8AF89B4-2047-DF11-B38B-0018FE8A0F18.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/C638A2A2-1B47-DF11-8D14-001A4BA92974.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/C6276CB2-2047-DF11-B454-001A4BA963DE.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/C4C90F82-2647-DF11-8E9F-E0CB4E1A1196.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/B83D75B0-2047-DF11-8D38-E0CB4E1A1195.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/B26FBF7A-2647-DF11-898E-E0CB4E1A1183.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/B26236A3-1B47-DF11-9767-001A4BA92916.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/AC15A37C-1947-DF11-9590-001A4BA660CA.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/A88C068A-2647-DF11-8456-0030487CDAF6.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/8E76F719-1C47-DF11-9FA4-00163E0100D1.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/866A9978-1B47-DF11-82E9-001A4BA55348.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/80FD2EB5-2047-DF11-830C-0030487C6A32.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/7ADDEF9B-2647-DF11-8713-0030487CDAC8.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/7256FFC6-2047-DF11-A374-E0CB4E1A1177.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/6EFCD89F-2647-DF11-8774-003048678948.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/32600C3E-1947-DF11-9ACC-001A4BA54360.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/308A9390-2647-DF11-A50F-0030487CDB2C.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/2E19EF84-2647-DF11-B270-E0CB4E1A1189.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/2C0D4E7B-1B47-DF11-9591-001A4BA6A818.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/268C8A1A-2147-DF11-83B6-0019BB3FD4FC.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/2206587C-2647-DF11-B32C-90E6BA0D09B9.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/1EC7B57F-2647-DF11-8FFF-00261834B579.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/180C831E-2147-DF11-A6B9-001A4BA86F1A.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/0A209317-1C47-DF11-BCD8-00163E0105CC.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/089CD2F9-2047-DF11-9CB3-001A4BA5CB72.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/02B22560-2047-DF11-952D-E0CB4E1A1182.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/0282AC7B-2647-DF11-B54D-90E6BA19A24C.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/F2A32C3E-1847-DF11-B745-90E6BA442F2B.root',
       '/store/mc/Spring10/W2Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/586A9D69-0E47-DF11-A087-E0CB4E1A117F.root' ] );


secFiles.extend( [
               ] )

