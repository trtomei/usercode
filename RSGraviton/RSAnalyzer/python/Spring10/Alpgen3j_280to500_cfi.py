import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0036/E0F9C3A8-6149-DF11-B92C-003048678A04.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0036/B61E5E41-6149-DF11-9DB3-90E6BA19A241.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0036/B050F875-6149-DF11-A578-90E6BA0D09C2.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0036/AADAB840-6149-DF11-A6C3-90E6BA19A215.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0036/48A4B02F-6349-DF11-8D69-E0CB4E1A1194.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0036/3A4F00AE-6149-DF11-A9B6-90E6BA0D09AC.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0036/30F27F4A-6149-DF11-9567-90E6BA442EF2.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/EA73E77A-3D49-DF11-AF85-90E6BAE8CC08.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/C8DEAC7B-3D49-DF11-B350-E0CB4E19F972.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/C2E91656-3F49-DF11-B72A-90E6BAE8CC37.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/A6741D7E-3D49-DF11-A9EB-E0CB4E1A118F.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/8EAD692A-3D49-DF11-AFD7-90E6BA19A23E.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/74D74956-3F49-DF11-A4E7-90E6BA0D09EC.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/7293592A-3D49-DF11-9FA4-E0CB4E19F96B.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/6C71487C-3D49-DF11-8F33-90E6BA442F11.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/5E0E6F85-3D49-DF11-A48C-E0CB4E1A119E.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/3EAC977F-3D49-DF11-9E23-0030487CD9C8.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/3AD71779-3D49-DF11-B03D-E0CB4E1A1176.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/24A12F56-3F49-DF11-94BF-E0CB4E1A1181.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/20764556-3F49-DF11-AAAD-E0CB4E19F971.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/16CC517D-3D49-DF11-BC15-90E6BA442F23.root',
       '/store/mc/Spring10/QCD3Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0032/101D8156-3F49-DF11-9122-90E6BA0D09B8.root' ] );


secFiles.extend( [
               ] )

