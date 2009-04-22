#####################################
# CMSSW configuration file - Python #
#####################################

import FWCore.ParameterSet.Config as cms
import datetime

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################
today = str(datetime.date.today())
fileLabel = 'RS750ZZ_'

# Source
process.load('RSGraviton.RSAnalyzer.Summer08_'+fileLabel+'JetMET_cfi')

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('results_'+fileLabel+today+'.root')
)

# process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

##################
# Kinematic cuts #
##################

process.twoJetsAboveHundred = cms.EDFilter("EtMinCaloJetCountFilter",
    src = cms.InputTag("sisCone7CaloJets"),
    minNumber = cms.uint32(2),
    etMin = cms.double(100.0)
)

process.getTwoJetsAboveHundred = cms.EDProducer("LargestEtCaloJetSelector",
    src = cms.InputTag("sisCone7CaloJets"),
    maxNumber = cms.uint32(2)
)

#########
# Plots #
#########

process.plotJetsGeneral = cms.EDAnalyzer("CaloJetHistoAnalyzer",
    src = cms.InputTag("getTwoJetsAboveHundred"),
    histograms = jethistos
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

process.trackAnalysis = cms.EDAnalyzer("RSTrackAnalyzer",
                                       tracks = cms.InputTag("generalTracks"),
                                       jets = cms.InputTag("getTwoJetsAboveHundred"),
                                       jetRadius = cms.double(0.7)
)

process.jetAnalysis = cms.EDAnalyzer("RSJetAnalyzer",
                                         jets = cms.InputTag("getTwoJetsAboveHundred")
                                         )

#########
# Paths #
#########

# Path after all cuts.
process.theCuts = cms.Sequence(process.twoJetsAboveHundred * process.getTwoJetsAboveHundred)

# Flow path.
process.theFlow = cms.Sequence(process.plotFlowJet1 + process.plotFlowJet2)

process.otherAnalyses = cms.Sequence(process.trackAnalysis + process.jetAnalysis)

process.p = cms.Path(process.theCuts * (process.plotJetsGeneral +
                                        process.theFlow +
                                        process.otherAnalyses) )
