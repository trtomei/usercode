#####################################
# CMSSW configuration file - Python #
#####################################

import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################

fileLabel = 'RS750ZZ'
# Source
process.load('RSGraviton.RSAnalyzer.Summer08_'+fileLabel+'_JetMET_cfi')

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('results_'+fileLabel+'_withFlow.root')
)

# process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

##################
# Kinematic cuts #
##################

process.twoJetsAboveThirty = cms.EDFilter("EtMinCaloJetCountFilter",
    src = cms.InputTag("sisCone7CaloJets"),
    minNumber = cms.uint32(2),
    etMin = cms.double(30.0)
)                           

process.twoJetsAboveHundred = cms.EDFilter("EtMinCaloJetCountFilter",
    src = cms.InputTag("sisCone7CaloJets"),
    minNumber = cms.uint32(2),
    etMin = cms.double(100.0)
)

process.getTwoJetsAboveHundred = cms.EDProducer("LargestEtCaloJetSelector",
    src = cms.InputTag("sisCone7CaloJets"),
    maxNumber = cms.uint32(2)
)

process.massRangeJets = cms.EDProducer("MassRangeCaloJetSelector",
    massMin = cms.double(60.0),
    massMax = cms.double(100.0),                                   
    src = cms.InputTag("getTwoJetsAboveHundred")
)

process.twoJetsAfterCuts = cms.EDFilter("CaloJetCountFilter",
    src = cms.InputTag("massRangeJets"),
    minNumber = cms.uint32(2)
)

###########################
# Graviton Reconstruction #
###########################

process.directGravitons = cms.EDFilter("CandViewCombiner",
    cut = cms.string('600.0 < mass < 99999.0'),
    decay = cms.string('massRangeJets massRangeJets')
)

#########
# Plots #
#########

process.plotJetsBeforeCuts = cms.EDAnalyzer("CaloJetHistoAnalyzer",
    src = cms.InputTag("sisCone7CaloJets"),
    histograms = jethistos
)

process.plotJetsAfterCuts = cms.EDAnalyzer("CaloJetHistoAnalyzer",
    src = cms.InputTag("massRangeJets"),
    histograms = jethistos
)

process.plotDirectGravitons = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("directGravitons"),
    histograms = Ghistos
)

process.plotFlowJet1 = cms.EDAnalyzer("RSFlowAnalyzer",
                                      tracks = cms.InputTag("generalTracks"),
                                      jets = cms.InputTag("getTwoJetsAboveHundred"),
                                      maxDeltaR = cms.double(0.7),
                                      jetNumber = cms.int32(0)
)

process.plotFlowJet2 = cms.EDAnalyzer("RSFlowAnalyzer",
                                      tracks = cms.InputTag("generalTracks"),
                                      jets = cms.InputTag("getTwoJetsAboveHundred"),
                                      maxDeltaR = cms.double(0.7),
                                      jetNumber = cms.int32(1)
)

#########
# Paths #
#########

# Path before all cuts.
process.p1 = cms.Path(process.twoJetsAboveThirty * process.plotJetsBeforeCuts)

# Path after all cuts.
process.theCuts = cms.Sequence(process.twoJetsAboveHundred * process.getTwoJetsAboveHundred *
                               process.massRangeJets *
                               process.twoJetsAfterCuts * process.directGravitons)

# Flow path.
process.theFlow = cms.Sequence(process.plotFlowJet1 + process.plotFlowJet2)

process.p2 = cms.Path(process.theCuts * (process.plotJetsAfterCuts +
                                         process.theFlow +
                                         process.plotDirectGravitons) )
