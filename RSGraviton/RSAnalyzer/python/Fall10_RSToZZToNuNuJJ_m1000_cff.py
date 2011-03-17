import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/F4A840A8-6CCC-DF11-A218-A4BADB3D00FF.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/9A07F077-3DCD-DF11-A190-003048C9CA8E.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/62AC2F3D-68CC-DF11-99A1-001E682F8738.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/4C699E75-3CCD-DF11-B294-0030487CAA5D.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/2A6004A3-3DCD-DF11-B959-00238BBDEAF7.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/1A64EBE3-72CC-DF11-BA19-E0CB4E29C4DB.root' ] );


secFiles.extend( [
                   ] )
