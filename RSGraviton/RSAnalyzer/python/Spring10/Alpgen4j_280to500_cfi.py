import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0008/349CF02F-0448-DF11-8B79-001D0967D0A3.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/FCA8900D-CB47-DF11-B375-0024E8766408.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/E27FD001-CB47-DF11-A754-0024E876635F.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/DE76E008-CB47-DF11-BF68-0024E8768D4E.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/C6FA6B54-C947-DF11-ACAB-0024E86E8D18.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/BE2D6EF5-C847-DF11-BBFF-0024E87699E7.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/BAF6F62C-C647-DF11-AFE7-0024E87699C0.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/A84394DE-C847-DF11-8195-0024E8769B60.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/A64F61DF-C847-DF11-BE16-0015178C6744.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/9450C0B9-CD47-DF11-81D8-0024E8768446.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/84FC6110-CB47-DF11-8D4D-0024E876803E.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/60BC18E3-C847-DF11-B334-001D0967DEEF.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/5246E20E-CB47-DF11-A74D-0024E8768224.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/48D8D609-D147-DF11-AEEB-00151796D9EC.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/44D6C4E8-C847-DF11-AB79-00151796D4E8.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/38F5E50C-C647-DF11-93DA-0024E8768D1A.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/38702EE2-C847-DF11-B5A0-001D0967DEA4.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/362D73DD-C847-DF11-8E1D-0015178C6A5C.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/2AAA2D52-C947-DF11-95D4-0024E876839D.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/22903DDD-C847-DF11-8E49-001D0967DFCB.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/1AFE83B8-CD47-DF11-9EC2-0024E8767D2B.root',
       '/store/mc/Spring10/QCD4Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0007/12A02AFD-CA47-DF11-A091-0024E8767D1E.root' ] );


secFiles.extend( [
               ] )

