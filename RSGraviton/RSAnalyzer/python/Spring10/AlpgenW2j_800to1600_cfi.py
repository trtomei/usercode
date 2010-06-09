import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/W2Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0028/6AD1B548-4248-DF11-BA91-0024E87663E1.root',
       '/store/mc/Spring10/W2Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/C0EFCAF8-F447-DF11-9044-0024E8768C57.root',
       '/store/mc/Spring10/W2Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/C01FE85E-D347-DF11-8CCE-0024E876823E.root',
       '/store/mc/Spring10/W2Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/B6006D3B-FF47-DF11-B2F5-00151796D884.root',
       '/store/mc/Spring10/W2Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/8C67362D-CB47-DF11-8887-0024E87680C0.root',
       '/store/mc/Spring10/W2Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/66720BF7-EC47-DF11-B1D3-0015178C6BD8.root',
       '/store/mc/Spring10/W2Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/5E22521B-CB47-DF11-B72E-0024E8768C09.root',
       '/store/mc/Spring10/W2Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0027/163CECAE-A847-DF11-8CAB-0024E8767D6C.root',
       '/store/mc/Spring10/W2Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/5472E8B5-9A47-DF11-8395-0015178C69F8.root',
       '/store/mc/Spring10/W2Jets_Pt800to1600-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/324402E2-9F47-DF11-BA37-001D0967D3D2.root' ] );


secFiles.extend( [
               ] )

