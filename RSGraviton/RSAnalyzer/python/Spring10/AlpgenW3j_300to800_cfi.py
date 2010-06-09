import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/9AEFAF3E-2347-DF11-876F-0030487F1A3D.root',
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/5CCDF453-2447-DF11-B4CE-003048C693EE.root',
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/368F8EFB-3247-DF11-A782-003048D436D2.root',
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/B0874F3B-1A47-DF11-B4E0-0030487F8E69.root',
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/9622D1F0-2547-DF11-8E10-003048C68A7C.root',
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/8AD67FBB-1D47-DF11-8369-003048D3C886.root',
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/8894E8BE-1D47-DF11-B122-003048D43986.root',
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/64B2A6C5-1D47-DF11-878E-003048D47976.root',
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/58C4EAF0-2547-DF11-B5CB-003048D436BE.root',
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/48DD44F2-2547-DF11-91E5-0030487F1655.root',
       '/store/mc/Spring10/W3Jets_Pt300to800-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0025/10686A3A-1A47-DF11-9705-003048D47976.root' ] );


secFiles.extend( [
               ] )

