import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( ['file:/hdacs/shared/BeamCommissioning09_MinimumBias_Feb9ReReco_v2.root'
                  ]
                  );

secFiles.extend( [
                   ] )

