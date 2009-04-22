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
fileLabel = 'RS1000ZZ_'

# Source
process.load('RSGraviton.RSAnalyzer.Summer08_'+fileLabel+'JetMET_cfi')
process.maxEvents.input = 1;

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('results_'+fileLabel+today+'.root')
)

process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as jethistos

############################
# Reconstruct the C-A jets #
############################

# Load geometry
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('IDEAL_V9::All')
process.load("Configuration.StandardSequences.MagneticField_cff")

# CATopJets
process.load("TopQuarkAnalysis.TopPairBSM.caTopJets_cff")
process.load("TopQuarkAnalysis.TopPairBSM.CATopJetTagger_cfi")

# turn off sum-et dependent stuff.
process.caTopJetsProducer.ptBins = cms.vdouble(0,10e9)
process.caTopJetsProducer.rBins  = cms.vdouble(0.8,0.8)
process.caTopJetsProducer.ptFracBins = cms.vdouble(0.05,0.05)
process.caTopJetsProducer.nCellBins = cms.vint32(1,1)

process.makeCAJets = cms.Sequence(process.caTopJetsProducer)

##################
# Kinematic cuts #
##################

process.jetsAboveHundred = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("caTopJetsProducer"),
    cut = cms.string("pt > 15.0")
)

process.twoJetsAboveHundred = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("jetsAboveHundred"),
    minNumber = cms.uint32(2)
)

process.makeCACuts = cms.Sequence(process.jetsAboveHundred + process.twoJetsAboveHundred)

#########
# Plots #
#########

# Basic jet plots
process.plotJetsGeneral = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("twoJetsAboveHundred"),
    histograms = jethistos
)

# Run my analyzer.
process.compoundJetAnalyzer = cms.EDAnalyzer("CompoundJetAnalyzer",
                                             src = cms.InputTag("twoJetsAboveHundred")
                                             )

process.makeCAPlots = cms.Sequence(process.plotJetsGeneral + process.compoundJetAnalyzer)

#########
# Paths #
#########

# Make the jets.
process.p = cms.Path(process.makeCAJets + process.makeCACuts + process.makeCAPlots)
