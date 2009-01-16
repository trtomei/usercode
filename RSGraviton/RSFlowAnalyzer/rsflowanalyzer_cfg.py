#####################################
# CMSSW configuration file - Python #
#####################################

import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [ '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/0E896ABC-CEBB-DD11-89F3-001E0BC198A2.root' ] )


secFiles.extend( [
                   ] )

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")
#process.Tracer = cms.Service("Tracer")

##################
# Kinematic cuts #
##################

process.twoJetsAboveThirty = cms.EDFilter("EtMinCaloJetCountFilter",
    src = cms.InputTag("sisCone7CaloJets"),
    minNumber = cms.uint32(2),
    etMin = cms.double(30.0)
)                           

process.getTwoJets = cms.EDProducer("LargestEtCaloJetSelector",
    src = cms.InputTag("sisCone7CaloJets"),
    maxNumber = cms.uint32(2)
)

process.test = cms.EDAnalyzer("RSFlowAnalyzer",
                              tracks = cms.InputTag("generalTracks"),
                              jets = cms.InputTag("getTwoJets"),
                              maxDeltaR = cms.double(0.7),
                              jetNumber = cms.int32(0)
                              )
#########
# Paths #
#########

# Path before all cuts.
process.p1 = cms.Path(process.twoJetsAboveThirty * process.getTwoJets * process.test)
