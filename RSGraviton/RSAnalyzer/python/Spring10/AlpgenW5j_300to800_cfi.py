import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W5Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/C2E3BFF8-1947-DF11-9F86-0030487D5D67.root',
       '/store/mc/Spring10/W5Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/96BDBAC5-1247-DF11-A4AF-003048C68A9C.root',
       '/store/mc/Spring10/W5Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/6C9F80AA-1947-DF11-9A1E-003048C693F0.root',
       '/store/mc/Spring10/W5Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/6A2BBA05-1447-DF11-8D55-003048D3C7DC.root',
       '/store/mc/Spring10/W5Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/60687DC5-1247-DF11-8F6B-0030487D5D89.root' ] );


secFiles.extend( [
               ] )

