import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1250_7TeV-pythia6/AODSIM/START38_V12-v1/0014/944F35C6-D7D5-DF11-9FC4-001E682F8738.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1250_7TeV-pythia6/AODSIM/START38_V12-v1/0014/92C6F60F-B2D5-DF11-B26B-001E682F273A.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1250_7TeV-pythia6/AODSIM/START38_V12-v1/0014/88B105B4-BED5-DF11-87DE-001E68A993A4.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1250_7TeV-pythia6/AODSIM/START38_V12-v1/0014/7034DF5E-C5D5-DF11-85E9-003048D3E450.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1250_7TeV-pythia6/AODSIM/START38_V12-v1/0014/50C941DD-D8D5-DF11-9631-003048D3E454.root',
                  '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1250_7TeV-pythia6/AODSIM/START38_V12-v1/0014/428BCB82-AAD5-DF11-A391-001E682F84DE.root' ] );


secFiles.extend( [
                   ] )
