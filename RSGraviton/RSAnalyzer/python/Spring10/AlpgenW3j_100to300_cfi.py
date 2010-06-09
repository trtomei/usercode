import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0070/E438FBCE-E74A-DF11-BF4F-0017A477082C.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0070/E411981B-E94A-DF11-8B14-00237D9F2120.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0070/B6BE78D6-E74A-DF11-A5B7-0017A4770430.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0070/9466A007-E64A-DF11-8484-00237DA15C66.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0070/3271BC93-EA4A-DF11-B370-0017A4770C24.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0070/1A904D0A-E64A-DF11-8BCB-002481A60370.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0070/04EC84EA-E74A-DF11-8397-00237DA1ED1C.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/D66FC418-E34A-DF11-8DAE-0017A4770838.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/C22A9112-E44A-DF11-8306-0017A4771008.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/BA38B900-E14A-DF11-9518-0017A4770420.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/B4C21C17-E34A-DF11-A77E-00237DA15C66.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/9C3E6BFD-E04A-DF11-927A-0017A4770820.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/6E8289FB-E04A-DF11-9C0F-0017A477082C.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/56FB43DC-DF4A-DF11-8C01-0017A4770C08.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/4276660E-DE4A-DF11-94EA-0017A4770C34.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/40D78F4D-DF4A-DF11-B4BF-0017A477100C.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/208D5BFD-E14A-DF11-80EA-0017A4770C04.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/16A80D1B-E34A-DF11-A5A9-0017A4770800.root',
       '/store/mc/Spring10/W3Jets_Pt100to300-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0069/06CAF8E8-E04A-DF11-86B8-00237DA10D06.root' ] );


secFiles.extend( [
               ] )

