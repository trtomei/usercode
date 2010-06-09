import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W5Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/F46A789A-4247-DF11-8563-0030487E54B5.root',
       '/store/mc/Spring10/W5Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/AC5220EC-1247-DF11-87F3-003048D4DF80.root',
       '/store/mc/Spring10/W5Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/607ABD7D-0D47-DF11-9DDF-003048C6930E.root',
       '/store/mc/Spring10/W5Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/4A3C8AFA-1747-DF11-9AC6-003048D4DEA6.root',
       '/store/mc/Spring10/W5Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0024/1ED467D7-0F47-DF11-B8DC-0030487F929F.root' ] );


secFiles.extend( [
               ] )

