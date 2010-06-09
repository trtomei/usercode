import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W4Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/D858693F-C147-DF11-8F0F-0024E8769958.root',
       '/store/mc/Spring10/W4Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/C6EC2439-B747-DF11-80E1-001D0967D16B.root',
       '/store/mc/Spring10/W4Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/84B426DC-A047-DF11-94A8-0015178C0224.root',
       '/store/mc/Spring10/W4Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/7876FB7D-A647-DF11-BD49-0015178C6B90.root',
       '/store/mc/Spring10/W4Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/1C44FE69-B447-DF11-98CD-001D0967CEBE.root',
       '/store/mc/Spring10/W4Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/1607DB7A-A047-DF11-A9B6-0024E8768065.root',
       '/store/mc/Spring10/W4Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/6ED5C6B2-4247-DF11-913E-00151796D894.root' ] );


secFiles.extend( [
               ] )

