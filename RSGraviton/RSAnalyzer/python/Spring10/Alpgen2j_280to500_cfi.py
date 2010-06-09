import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0026/A879E15A-B448-DF11-A72A-00304867C1BC.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/FE9C4CB9-E547-DF11-A6AA-00304867920C.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/F40A893D-DF47-DF11-86D6-002618943866.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/F23DD40B-E547-DF11-85B1-001A9281171E.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/EC39710F-E547-DF11-8EAE-00248C0BE012.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/E289A8B1-DE47-DF11-AE17-003048678A6C.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/DE5EF764-DE47-DF11-B5EF-003048678AFA.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/D00F399A-D847-DF11-A128-00261894392B.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/CE47B7B2-DE47-DF11-890F-0030486792BA.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/CE2CBF50-E547-DF11-91B5-003048679076.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/C0955802-E547-DF11-8426-0026189438DB.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/BA4D7730-E647-DF11-B669-003048678B72.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/AA49EC6F-E647-DF11-9A9C-003048678B20.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/A6E34153-E547-DF11-B44E-002354EF3BDB.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/9CFD020F-E547-DF11-9B87-00261894393B.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/90EC5114-E547-DF11-980E-002618943924.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/88AA5382-D847-DF11-B226-00261894389A.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/88588841-E647-DF11-B48C-00261894387D.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/80A3E793-D847-DF11-AA20-002618943933.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/7E91F75A-DE47-DF11-8CE5-0026189437F0.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/78582483-E647-DF11-9606-0026189438D2.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/5EA8CA9A-DE47-DF11-B6A1-0026189438B8.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/54D395A4-DE47-DF11-A7FB-00304867C0FC.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/5445D5E2-E447-DF11-94AC-0030486790B8.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/4AA6AB7F-DE47-DF11-A01D-003048678EE2.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/48F7C37A-E547-DF11-A65A-002618943870.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/4882657C-DF47-DF11-AB15-003048679228.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/460E84B4-E547-DF11-8019-0026189438A5.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/4056DE13-E547-DF11-B433-00248C0BE014.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/3C3CF105-E547-DF11-882B-0026189438AA.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/34594F22-E747-DF11-9580-003048678FF6.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/30398D89-DE47-DF11-91B6-003048679012.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/2ED35B12-E547-DF11-83B8-00304867BED8.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/20ACC884-E547-DF11-A7F7-003048678A6C.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/20872CC2-E647-DF11-97D1-003048D15E02.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/14C6B967-E547-DF11-9DB6-001A92971B5E.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/12394CE8-DE47-DF11-8C18-00304867C1B0.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/04395321-DF47-DF11-9CA0-002618943923.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0020/024CD7AA-DE47-DF11-A3DA-003048678FE0.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0019/C8DF2846-D447-DF11-97AA-002618FDA263.root',
       '/store/mc/Spring10/QCD2Jets_Pt280to500-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0019/B4BC06D0-D547-DF11-92A6-001A92971BDA.root' ] );


secFiles.extend( [
               ] )

