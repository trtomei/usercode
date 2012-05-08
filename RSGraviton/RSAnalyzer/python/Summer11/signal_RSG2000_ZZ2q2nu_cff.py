import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-2000-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/FCDA538B-F8AF-E011-AB03-001A4BA80F36.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-2000-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/925E341C-F5AF-E011-867C-0022198F5D7B.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-2000-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/7C310969-F3AF-E011-8732-90E6BA0D09D7.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-2000-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/52D85814-3FB0-E011-8885-E0CB4E19F9A0.root',
           #'/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-2000-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/1A471B9F-A1B0-E011-90C7-E0CB4E19F9A5.root'
           ] );
