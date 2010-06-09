import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0035/2EF76E55-B647-DF11-BC96-001E0B471C92.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0034/FEE34D83-E346-DF11-83B6-001B78CE74FE.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0034/EAEFBDC2-E146-DF11-8708-0017A4770810.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0034/D2F550C6-DF46-DF11-A970-0017A4770420.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0034/C64C4004-E046-DF11-8ABA-0017A4770434.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0034/BEFDB578-E346-DF11-9C6F-0017A477042C.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0034/86A3782E-DF46-DF11-B4DC-0017A4770834.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0034/84CA0037-E346-DF11-8382-0017A4771010.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0034/78BF0689-E346-DF11-B8FB-0017A4770018.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0034/649FDB2B-E146-DF11-9CC6-0017A4771038.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0034/624E8404-E046-DF11-9446-0017A4770C10.root',
       '/store/mc/Spring10/TTbar3Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0033/84493E50-E046-DF11-A762-0017A4770830.root' ] );


secFiles.extend( [
               ] )

