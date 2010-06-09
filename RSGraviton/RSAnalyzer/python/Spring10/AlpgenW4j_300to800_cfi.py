import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W4Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/BA67F9BE-2047-DF11-B873-0030487E5179.root',
       '/store/mc/Spring10/W4Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/582213FE-1947-DF11-9829-0030487F4B8B.root',
       '/store/mc/Spring10/W4Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/9A3444EE-1247-DF11-9265-0030487DE53B.root',
       '/store/mc/Spring10/W4Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/1C1C4952-1847-DF11-8427-0030487D5EA7.root' ] );


secFiles.extend( [
               ] )

