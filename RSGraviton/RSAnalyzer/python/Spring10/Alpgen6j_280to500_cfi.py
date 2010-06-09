import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/E67BEEE1-9C4A-DF11-AB1A-0017A4770C0C.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/F06C4D12-864A-DF11-B263-0017A477042C.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/C8A542D9-814A-DF11-9C00-0017A4770C1C.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/BEDB61F3-804A-DF11-8A9F-0017A4770414.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/B4144141-844A-DF11-AF94-001A4BE1C5D4.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/AEF9FF14-864A-DF11-B53A-0017A4770434.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/9C6EDA8A-824A-DF11-8089-001CC4AADC6E.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/98FB7584-824A-DF11-AEF5-0017A4770434.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/824CC764-844A-DF11-9946-001E0B48E92A.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/7603F0FE-894A-DF11-9525-0017A477002C.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/62F25A0E-854A-DF11-9E3D-001A4BE1C5D4.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/4AF4C668-844A-DF11-96B9-0017A477041C.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/46709D9C-844A-DF11-83C8-0017A4770C24.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/3858E2B9-844A-DF11-A3A1-001B78CE74FE.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/36241D81-864A-DF11-BE25-0017A4770C0C.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/30108BD4-844A-DF11-8BC4-00237DA1DDFC.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/2C843FBF-844A-DF11-8DFA-0017A4770000.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/100AB7DD-844A-DF11-9D82-001E0BEACAB8.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/083CBD7D-874A-DF11-B1FD-0017A477080C.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/0474221B-884A-DF11-96A8-0017A4770C0C.root',
       '/store/mc/Spring10/QCD6Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/00B0645F-834A-DF11-8544-0017A4770804.root' ] );


secFiles.extend( [
               ] )

