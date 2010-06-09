import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/FA760094-8D4A-DF11-BF50-0017A4771000.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/F0D9C418-8C4A-DF11-912E-002264984988.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/CACD3335-8D4A-DF11-AE0C-001E0B4A0EFC.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/BA5CA29C-8D4A-DF11-B21C-00237DA1680E.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/B4EA44FD-8E4A-DF11-A639-00237DA1680E.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/AE5A1AE9-8B4A-DF11-8EDA-0017A4770014.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/88E24C80-8D4A-DF11-9560-0017A4770414.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/86EE930C-8D4A-DF11-8371-0017A4770828.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/6A26D022-8D4A-DF11-8CD7-0017A4770014.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/62F38E97-8F4A-DF11-93E9-0017A4770418.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/5CFB0E95-8D4A-DF11-9C0D-0017A4771034.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/5A6DDFD6-8D4A-DF11-A630-0017A4770C10.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/363C97CD-A24A-DF11-AA3C-00237DA12CA0.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/2CA042FD-8B4A-DF11-96FE-0017A477100C.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/24E485B9-8C4A-DF11-84DF-002481A8A782.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/063D688C-8D4A-DF11-8336-00237DA13FB6.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/F6A35F6D-864A-DF11-A8C4-0017A4770C2C.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/EC436F91-8A4A-DF11-8A94-0017A4770428.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/DE137227-8A4A-DF11-B789-001CC4164B40.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/DC5E0191-894A-DF11-B498-0017A4770C14.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/DA0F1D41-824A-DF11-AACA-0017A4770030.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/D477DC8F-8A4A-DF11-B160-0017A4770C24.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/D2D6EB32-8A4A-DF11-A945-001E0B48E92A.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/CCC65351-884A-DF11-B0DE-0017A4770C14.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/CC6A4040-864A-DF11-99AA-001E0B4A0EFC.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/B88C3F6D-884A-DF11-85DC-0017A4771004.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/B0D530B2-894A-DF11-9274-0017A4770434.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/AE01A598-824A-DF11-9E08-0017A4770C2C.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/AA0E0187-844A-DF11-BB49-00237DA41368.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/A450E39F-844A-DF11-9D87-0017A477000C.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/A243128F-894A-DF11-89E2-0017A4770818.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/9A95A5C0-8E4A-DF11-B247-002481A8A782.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/948D7471-864A-DF11-85D7-0022649C40A8.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/9291FB1A-8B4A-DF11-9D0D-0017A4770C04.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/8EC77E75-8A4A-DF11-BF8A-0017A477000C.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/84429D10-8D4A-DF11-BF98-0017A4770C14.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/82D5FAF8-834A-DF11-ADF5-0017A4770004.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/7C985BA4-834A-DF11-B283-0022649C40A8.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/725C7276-8B4A-DF11-A6BF-0017A4770410.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/6A50E30B-854A-DF11-991F-001B78E2A8C8.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/66F571C9-834A-DF11-9E3C-0017A4770424.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/640664DF-854A-DF11-8353-00237DA15C66.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/5CDE446C-844A-DF11-8D6F-0017A4770C0C.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/5CC2F7FB-854A-DF11-91C9-0022649C40A8.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/4EECEECA-854A-DF11-95A1-0017A4771020.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/422E0916-864A-DF11-BE09-0017A4770020.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/3A7BE355-8B4A-DF11-8E3A-001E0B5F3148.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/3444F919-8A4A-DF11-88A5-0017A4771034.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/32F50206-864A-DF11-A8A5-0017A477002C.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/2C786411-884A-DF11-8F1F-0017A477042C.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/2AE2B876-894A-DF11-B0F6-0017A4770410.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/2680CCF1-834A-DF11-960C-001E0B5FA5A8.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/1E71BCAB-8C4A-DF11-8414-0017A4770428.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/0A85D010-874A-DF11-8A80-0017A4771014.root',
       '/store/mc/Spring10/QCD6Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0064/0A17D68A-844A-DF11-81D4-00237DA1CD8E.root' ] );


secFiles.extend( [
               ] )

