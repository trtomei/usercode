import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-1750-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/F202DB64-3DB0-E011-825A-485B39800B98.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-1750-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/E6B9DD41-F4AF-E011-9D78-485B39800B73.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-1750-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/AE459415-EEAF-E011-BA56-001A4BA900B8.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-1750-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/90809583-F8AF-E011-9392-001EC9D87221.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_kMpl-005_M-1750-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/6E1211C7-4BB0-E011-9C28-E0CB4E29C4D8.root' ] );
