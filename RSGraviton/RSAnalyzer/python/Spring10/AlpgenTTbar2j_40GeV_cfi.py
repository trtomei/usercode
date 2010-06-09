import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0012/3E4CDFFA-D548-DF11-BBAF-0024E87663BA.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/FE4FDFF2-7448-DF11-B5AD-0015178C6B54.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/A0048A50-7048-DF11-9F44-00151796D6C4.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/9EEB0AA0-7948-DF11-A3A1-0024E876A889.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/9091FB52-7048-DF11-B877-0015178C4A78.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/8836F99A-7948-DF11-8CDD-0015178C1980.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/60E12286-7D48-DF11-A499-0015178C4BF0.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/4E6F1156-7048-DF11-9C50-001D0967DAAD.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/4E08FB41-8E48-DF11-8DCE-0015178C48E4.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/22B2A72D-7848-DF11-8274-00151796C1E8.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/16A7180E-6648-DF11-8A6B-0024E876842C.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/149E179D-7948-DF11-B4FF-0015178C66B0.root',
       '/store/mc/Spring10/TTbar2Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0009/12BBC041-7548-DF11-A357-0024E876A807.root' ] );


secFiles.extend( [
               ] )

