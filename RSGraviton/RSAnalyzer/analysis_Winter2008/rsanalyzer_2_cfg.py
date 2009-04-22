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
fileLabel = 'RS1250ZZ_'
resultsFileName = 'results_'+fileLabel+today+'.root'
#resultsFileName = 'test.root'

# Source
process.load('RSGraviton.RSAnalyzer.Summer08_'+fileLabel+'JetMET_cfi')
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

# Trigger report
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(resultsFileName)
)

#process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

##################
# Kinematic cuts #
##################

process.twoJetsSIS07 = cms.EDFilter("EtMinCaloJetCountFilter",
    src = cms.InputTag("sisCone7CaloJets"),
    minNumber = cms.uint32(2),
    etMin = cms.double(100.0)
)

process.twoJetsSIS05 = cms.EDFilter("EtMinCaloJetCountFilter",
    src = cms.InputTag("sisCone5CaloJets"),
    minNumber = cms.uint32(2),
    etMin = cms.double(100.0)
)

process.getTwoJetsSIS07 = cms.EDProducer("LargestEtCaloJetSelector",
    src = cms.InputTag("sisCone7CaloJets"),
    maxNumber = cms.uint32(2)
)

process.getTwoJetsSIS05 = cms.EDProducer("LargestEtCaloJetSelector",
    src = cms.InputTag("sisCone5CaloJets"),
    maxNumber = cms.uint32(2)
)

process.massRangeJets = cms.EDProducer("MassRangeCaloJetSelector",
    massMin = cms.double(50.0),
    massMax = cms.double(100.0),                                   
    src = cms.InputTag("getTwoJetsSIS07")
)

process.applyMassCut = cms.EDFilter("CaloJetCountFilter",
    src = cms.InputTag("massRangeJets"),
    minNumber = cms.uint32(2)
)

process.p05 = cms.Sequence(process.twoJetsSIS05 * process.getTwoJetsSIS05)
process.p07 = cms.Sequence(process.twoJetsSIS07 * process.getTwoJetsSIS07)
process.massCuts= cms.Sequence(process.massRangeJets * process.applyMassCut)

########################
# Match SIS07 to SIS05 #
########################

process.matchVeto = cms.EDFilter("JetMatchVeto",
                                 src      = cms.InputTag("getTwoJetsSIS07"),
                                 matched  = cms.InputTag("getTwoJetsSIS05"),
                                 maxDeltaR = cms.double(0.25)

)

#########
# Plots #
#########

process.plotJetsSIS07 = cms.EDAnalyzer("CaloJetHistoAnalyzer",
                                       src = cms.InputTag("getTwoJetsSIS07"),
                                       histograms = jethistos
                                       )

process.plotJetsSIS05 = cms.EDAnalyzer("CaloJetHistoAnalyzer",
                                       src = cms.InputTag("getTwoJetsSIS05"),
                                       histograms = jethistos
                                       )
process.fullPlots = cms.Sequence(process.plotJetsSIS07 + process.plotJetsSIS05)

process.countPass = cms.EDAnalyzer("EventCounter")
process.countFail = cms.EDAnalyzer("EventCounter")

#########
# Paths #
#########

# Found the SIS07 jets (w/ mass cuts), but not the SIS05 jets. Count in countPass.
process.totalSuccess = cms.Path( process.p07 + process.massCuts + ~process.twoJetsSIS05 + process.countPass)
# Found the SIS07 jets (w/ mass cuts), found the SIS05, but matchVeto gives success - they don't match. Count in countPass.
process.noVeto = cms.Path( process.p07 + process.massCuts + process.p05 + process.matchVeto + process.countPass)
# Found the SIS07 jets (w/ mass cuts), found the SIS05, matchVeto gives failure - they match. Count in countFail.
process.veto = cms.Path( process.p07 + process.massCuts + process.p05 + ~process.matchVeto + process.fullPlots + process.countFail)
