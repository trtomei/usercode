import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W3Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0028/C21EE86C-5F48-DF11-894C-0024E876841F.root',
       '/store/mc/Spring10/W3Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/B6376F15-A647-DF11-A8DE-0024E8767D38.root',
       '/store/mc/Spring10/W3Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/84A27565-CB47-DF11-A9F7-0024E8768833.root',
       '/store/mc/Spring10/W3Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/98B0AE71-A047-DF11-861E-001D0967D91D.root',
       '/store/mc/Spring10/W3Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/2A39D596-9947-DF11-98A0-001D0967DAE4.root',
       '/store/mc/Spring10/W3Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/78CD273F-9447-DF11-A487-0024E8768C64.root' ] );


secFiles.extend( [
               ] )

