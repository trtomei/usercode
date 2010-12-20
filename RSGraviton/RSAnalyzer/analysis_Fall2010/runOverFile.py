#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################

##################
# Basic services #
##################
# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.Services_cff')

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:selectedHBHEAndTrigger.root'
    )
)
