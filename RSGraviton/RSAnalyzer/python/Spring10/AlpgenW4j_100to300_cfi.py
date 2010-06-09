import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W4Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/4209453C-1A47-DF11-9AC8-003048C68A9C.root',
       '/store/mc/Spring10/W4Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/BABD4B20-0847-DF11-B5FE-003048D4363C.root',
       '/store/mc/Spring10/W4Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/B2CEB8F9-1747-DF11-B8D7-0030487E55BB.root',
       '/store/mc/Spring10/W4Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/6808E703-1847-DF11-AD83-0030487F1A3D.root' ] );


secFiles.extend( [
               ] )

