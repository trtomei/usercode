import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/QCD6Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/EC7DE69A-9D4A-DF11-AB16-00237DA1A66C.root',
       '/store/mc/Spring10/QCD6Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/E69F8B2B-924A-DF11-BD24-0017A4770430.root',
       '/store/mc/Spring10/QCD6Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/CCA488FE-904A-DF11-8929-00237DA13FB6.root',
       '/store/mc/Spring10/QCD6Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/B80CEDF5-904A-DF11-B631-0017A4770824.root',
       '/store/mc/Spring10/QCD6Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/92AADA20-924A-DF11-8656-0017A4770010.root',
       '/store/mc/Spring10/QCD6Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/8A80AC7F-934A-DF11-8814-002264055CE4.root',
       '/store/mc/Spring10/QCD6Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/64DA6EF5-904A-DF11-84A4-0017A4771028.root',
       '/store/mc/Spring10/QCD6Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/44B0EAF5-904A-DF11-85E9-0017A4770C04.root',
       '/store/mc/Spring10/QCD6Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/2C872DC5-924A-DF11-BE83-0017A4770C24.root',
       '/store/mc/Spring10/QCD6Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0065/18249EF5-904A-DF11-AE89-0017A4770000.root' ] );


secFiles.extend( [
               ] )

