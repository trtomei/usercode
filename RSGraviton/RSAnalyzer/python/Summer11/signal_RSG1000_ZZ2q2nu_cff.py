import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/C6362019-1393-E011-A4FD-00215E22214E.root',
    '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/BC9ED7D8-1093-E011-B467-00215E22214E.root',
    '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/4AC9B24A-1093-E011-B4DC-E41F131815AC.root',
    '/store/mc/Summer11/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/08449EAF-1393-E011-AB13-00215E221B48.root' ] );

secFiles.extend( [
                   ] )
