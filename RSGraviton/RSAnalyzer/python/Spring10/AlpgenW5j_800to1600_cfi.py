import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W5Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/82AFD6E0-B147-DF11-A581-0015178C6924.root',
       '/store/mc/Spring10/W5Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/445AB429-A647-DF11-9B5D-0024E876885A.root',
       '/store/mc/Spring10/W5Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/3801AA88-D447-DF11-9011-0015178C4D70.root',
       '/store/mc/Spring10/W5Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/3025631E-A647-DF11-9D84-0024E87683EB.root',
       '/store/mc/Spring10/W5Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/7EE4C88E-3B47-DF11-8564-00151796C138.root',
       '/store/mc/Spring10/W5Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/26E78C18-0C47-DF11-A8A2-001D0967DF3F.root' ] );


secFiles.extend( [
               ] )

