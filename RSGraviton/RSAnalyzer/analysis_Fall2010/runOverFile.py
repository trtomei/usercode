#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("CONSOLIDATION")

###########################
# Basic process controls. #
###########################

##################
# Basic services #
##################
# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(20)
            )


readFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles)
readFiles.extend( ["file:data_selectedMuons.root",])

process.preselectionOut = cms.OutputModule("PoolOutputModule",
                                           fileName = cms.untracked.string('forViewing.root'),
                                           outputCommands = process.RECOEventContent.outputCommands,
                                           dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO'),
                                                                        filterName = cms.untracked.string('CONSOLIDATION'))
                                           )

process.e = cms.EndPath(process.preselectionOut)
