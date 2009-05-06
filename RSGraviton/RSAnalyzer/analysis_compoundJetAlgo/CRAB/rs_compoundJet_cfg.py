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

# Source
process.load('RSGraviton.RSAnalyzer.Summer08_'+fileLabel+'JetMET_cfi')
process.maxEvents.input = -1;

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('results.root')
)

#process.Tracer = cms.Service("Tracer")

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
from RecoJets.JetProducers.CATopJetParameters_cfi import *
from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.CaloJetParameters_cfi import *
process.caTopJetsProducer = cms.EDProducer("CATopJetProducer",
                                           CATopJetParameters,
                                           CaloJetParameters
                                           )

# turn off sum-et dependent stuff.
process.caTopJetsProducer.ptBins = cms.vdouble(0,10e9)
process.caTopJetsProducer.rBins  = cms.vdouble(0.8,0.8)
process.caTopJetsProducer.ptFracBins = cms.vdouble(0.05,0.05)
process.caTopJetsProducer.nCellBins = cms.vint32(1,1)

process.makeCAJets = cms.Sequence(process.caTopJetsProducer)

##################
# Kinematic cuts #
##################

process.twoJetsAboveHundred = cms.EDFilter("EtMinBasicJetCountFilter",
                                           src = cms.InputTag("caTopJetsProducer"),
                                           minNumber = cms.uint32(2),
                                           etMin = cms.double(100.0)
                                           )

process.getTwoJetsAboveHundred = cms.EDProducer("LargestEtBasicJetSelector",
                                                src = cms.InputTag("caTopJetsProducer"),
                                                maxNumber = cms.uint32(2)
                                                )

process.makeCACuts = cms.Sequence(process.twoJetsAboveHundred + process.getTwoJetsAboveHundred)

#########
# Plots #
#########

# Basic jet plots
process.plotJetsGeneral = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("getTwoJetsAboveHundred"),
    histograms = jethistos
)

# Run my analyzer.
process.compoundJetAnalyzer = cms.EDAnalyzer("CompoundJetAnalyzer",
                                             src = cms.InputTag("getTwoJetsAboveHundred")
                                             )

process.makeCAPlots = cms.Sequence(process.plotJetsGeneral + process.compoundJetAnalyzer)

#########
# Paths #
#########

# Make the jets.
process.p = cms.Path(process.makeCAJets + process.makeCACuts + process.makeCAPlots)
