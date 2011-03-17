import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-750_7TeV-pythia6/AODSIM/START38_V12-v1/0013/64037CA1-72CC-DF11-9821-E0CB4E19F9A4.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-750_7TeV-pythia6/AODSIM/START38_V12-v1/0013/4834BE6F-17CB-DF11-AC9A-E0CB4E4408D3.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-750_7TeV-pythia6/AODSIM/START38_V12-v1/0013/2A2849A9-6CCC-DF11-A228-003048678A44.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-750_7TeV-pythia6/AODSIM/START38_V12-v1/0012/AA69E339-FBC9-DF11-87A9-E0CB4E1A119A.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-750_7TeV-pythia6/AODSIM/START38_V12-v1/0012/9091DD0E-FBC9-DF11-B3F1-0030487CB568.root' ] );


secFiles.extend( [
                   ] )

