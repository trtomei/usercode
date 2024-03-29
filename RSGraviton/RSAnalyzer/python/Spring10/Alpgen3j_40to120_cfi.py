import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0036/20B7F7D6-6149-DF11-AC0A-90E6BA442EF0.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/FE6AB447-6149-DF11-9C24-0030487C73D4.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/E2AF0C49-6149-DF11-A038-90E6BA19A24A.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/CCA2C699-6049-DF11-BC51-90E6BA19A24C.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/BE6A14B4-6149-DF11-96B1-90E6BA0D09D7.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/B4C5676F-6149-DF11-8F05-90E6BA0D0988.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/942AC0E0-6149-DF11-94AC-90E6BA19A20B.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/6E644D4A-6149-DF11-8955-90E6BA19A212.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/1E3B88B6-6049-DF11-9EF9-E0CB4E1A1195.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/12CAB1B3-6149-DF11-8913-00261834B55F.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/06590173-6149-DF11-BE80-0030487CB568.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/0414A345-6149-DF11-8E9F-90E6BA442F30.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/020FEE9D-6049-DF11-84BA-90E6BA442F0D.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/FA11D7FC-4049-DF11-94A5-0030487C6A2C.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/F67270FC-4049-DF11-8C2D-90E6BA19A229.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/E6591956-3F49-DF11-9648-E0CB4E19F958.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/E49974FC-4049-DF11-8F7A-00261834B51E.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/E48A42FC-4049-DF11-BCA2-90E6BA0D09B4.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/E41C3A56-3F49-DF11-9DC1-90E6BA442EF6.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/E2574FFC-4049-DF11-8123-90E6BA0D09BB.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/DCE26FFC-4049-DF11-BFB7-00261834B548.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/D84976FC-4049-DF11-A1F3-90E6BA442F0D.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/D6879EFC-4049-DF11-B7E5-E0CB4E1A1150.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/D2817D56-3F49-DF11-93D5-E0CB4E19F96D.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/D03A8A56-3F49-DF11-B412-90E6BA19A232.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/CED32556-3F49-DF11-9043-90E6BA442F28.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/BEBB4856-3F49-DF11-AFA2-E0CB4E1A1190.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/B80F26FC-4049-DF11-9731-00261834B5A4.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/AA43C009-4149-DF11-A6DD-003048D2910A.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/A2A36BFC-4049-DF11-ADC5-90E6BA442F1F.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/9E84DEFC-4049-DF11-9650-90E6BA442F32.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/9E3349FC-4049-DF11-A953-E0CB4E1A1183.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/98E52EFC-4049-DF11-AAA2-90E6BA442EEB.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/964F2356-3F49-DF11-B096-90E6BA19A210.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/7E2644FC-4049-DF11-8126-90E6BA19A252.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/7207DB55-3F49-DF11-A282-0030487CDA68.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/70692056-3F49-DF11-84C6-E0CB4E1A1198.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/6C1CAD56-3F49-DF11-8E67-90E6BA442F15.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/62A324FC-4049-DF11-8658-90E6BA442F3C.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/60C94356-3F49-DF11-8C9B-90E6BA442F04.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/5AEF3B05-4149-DF11-A69A-0030487CB568.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/4E346856-3F49-DF11-AE0C-90E6BA442F23.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/48783956-3F49-DF11-84D0-90E6BA19A22B.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/3A9465FC-4049-DF11-935C-E0CB4E1A115D.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/3A263F56-3F49-DF11-8AB7-E0CB4E19F972.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/3A13AE07-4149-DF11-A81B-0030487C6A32.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/36F08256-3F49-DF11-B561-E0CB4E1A1169.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/344281FC-4049-DF11-90FF-90E6BA442F41.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/2E3B18FF-4049-DF11-B711-003048678948.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/28EE95FC-4049-DF11-8222-90E6BA0D0998.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/202D5256-3F49-DF11-81CB-90E6BAE8CC13.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/1C5D2156-3F49-DF11-B8FB-E0CB4E1A1176.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/1A5D5F56-3F49-DF11-BCE4-90E6BA19A231.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/18CAA856-3F49-DF11-8FE8-E0CB4E1A119E.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/16C2BAFC-4049-DF11-BEBF-90E6BA0D0988.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/12145B56-3F49-DF11-A04B-90E6BA442F2A.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/0E6E3AFC-4049-DF11-B09B-90E6BA19A215.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/0E002D56-3F49-DF11-97CA-90E6BA19A1F9.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/0CE23D56-3F49-DF11-BC48-90E6BA19A226.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/0CC67256-3F49-DF11-AF18-00261834B53C.root',
       '/store/mc/Spring10/QCD3Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/082782FC-4049-DF11-BB27-90E6BA442F07.root' ] );


secFiles.extend( [
               ] )

