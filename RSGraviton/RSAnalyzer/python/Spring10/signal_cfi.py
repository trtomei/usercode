import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       'file:/storage/trtomei/data/Pythia_800GeV_kmpl005_CMSSW358_RECO.root' ] );
secFiles.extend( [
               ] )

