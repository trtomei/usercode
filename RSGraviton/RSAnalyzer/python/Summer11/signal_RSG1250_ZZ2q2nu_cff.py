import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-1250_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/FE00BA09-0C90-E011-A159-00215E222808.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-1250_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/7001108D-1090-E011-A7A6-00215E21D6D8.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-1250_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/623878C0-1490-E011-A58E-00215E93EFB8.root',
           '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-1250_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/26930C6F-2190-E011-A36D-00215E21DD32.root' ] );

secFiles.extend( [
    ] )
