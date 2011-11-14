import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-750_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/EEBA6EB3-0F93-E011-A84F-00215E221812.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-750_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/968526CF-1493-E011-86AA-00215E2221AE.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-750_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/867E1A6E-1193-E011-AE5D-00215E22053A.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-750_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/50D14494-1293-E011-9A22-00215E221B48.root' ] );


secFiles.extend( [
    ] )
