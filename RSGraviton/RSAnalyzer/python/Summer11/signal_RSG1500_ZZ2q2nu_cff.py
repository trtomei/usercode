import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-1500-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/58887E8F-F2AF-E011-92A3-485B39800C13.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-1500-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/4CA620EC-F5AF-E011-9422-485B39800B65.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-1500-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/1A24E2A2-F0AF-E011-BBED-E0CB4E0ED8C0.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-1500-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/0A4640C8-37B0-E011-B999-E0CB4E19F9A0.root' ] );
