import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W5Jets_Pt0to100-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/9E91DB05-A847-DF11-8AAD-90E6BA19A23C.root',
       '/store/mc/Spring10/W5Jets_Pt0to100-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/30789E8B-8247-DF11-81FE-001A4BA98720.root',
       '/store/mc/Spring10/W5Jets_Pt0to100-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/F088003D-4447-DF11-9AF0-E0CB4E1A1189.root',
       '/store/mc/Spring10/W5Jets_Pt0to100-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/262529CA-1B47-DF11-9C09-00163E010495.root',
       '/store/mc/Spring10/W5Jets_Pt0to100-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/10E10DE9-1747-DF11-BC78-90E6BA0D09B3.root' ] );


secFiles.extend( [
               ] )

