import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/TTbar4Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0013/2A9182F5-D74A-DF11-96AF-003048D438EA.root',
       '/store/mc/Spring10/TTbar4Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0013/28156C9D-1F4A-DF11-8444-0030487F1655.root',
       '/store/mc/Spring10/TTbar4Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0012/C82F11F3-1E4A-DF11-90AA-0030487FA60D.root',
       '/store/mc/Spring10/TTbar4Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0012/A098DEAA-174A-DF11-B08E-003048C692E2.root',
       '/store/mc/Spring10/TTbar4Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0012/96BACBE6-174A-DF11-89FF-003048C693E8.root',
       '/store/mc/Spring10/TTbar4Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0012/92AA68BD-084A-DF11-938D-0030487E4D11.root',
       '/store/mc/Spring10/TTbar4Jets_40GeVthreshold-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0012/8CA44AA3-1F4A-DF11-AB60-003048D4396E.root' ] );


secFiles.extend( [
               ] )

