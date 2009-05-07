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
fileLabel = ''

# Source
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring('file:reco.root');
process.source = cms.Source ("PoolSource",fileNames = readFiles)

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('results_'+fileLabel+today+'.root')
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

# 1 Primary cut with two jets above 100 GeV 
process.twoJetsAboveHundred = cms.EDFilter("EtMinBasicJetCountFilter",
                                           src = cms.InputTag("caTopJetsProducer"),
                                           minNumber = cms.uint32(2),
                                           etMin = cms.double(100.0)
                                           )

process.getTwoJetsAboveHundred = cms.EDProducer("LargestEtBasicJetSelector",
                                                src = cms.InputTag("caTopJetsProducer"),
                                                maxNumber = cms.uint32(2)
                                                )

process.makePrelimCuts = cms.Sequence(process.twoJetsAboveHundred + process.getTwoJetsAboveHundred)

# 2 Secondary cut with 1st jet above 250 GeV, 2nd jet above 180 GeV
process.cutSecondJet = cms.EDFilter("EtMinBasicJetCountFilter",
                                    src = cms.InputTag("caTopJetsProducer"),
                                    minNumber = cms.uint32(2),
                                    etMin = cms.double(180.0)
                                    )

process.cutFirstJet = cms.EDFilter("EtMinBasicJetCountFilter",
                                   src = cms.InputTag("caTopJetsProducer"),
                                   minNumber = cms.uint32(1),
                                   etMin = cms.double(250.0)
                                   )

process.getTwoJetsAfterMainCuts = cms.EDProducer("LargestEtBasicJetSelector",
                                                 src = cms.InputTag("caTopJetsProducer"),
                                                 maxNumber = cms.uint32(2)
                                                 )

process.makeMainCuts = cms.Sequence(process.cutSecondJet + process.cutFirstJet + process.getTwoJetsAfterMainCuts)

#########
# Plots #
#########

# Basic jet plots
process.plotJetsAfterPrelim = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                             src = cms.InputTag("getTwoJetsAboveHundred"),
                                             histograms = jethistos
                                             )

process.plotJetsAfterMainCuts = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                               src = cms.InputTag("getTwoJetsAfterMainCuts"),
                                               histograms = jethistos
                                               )

# Flow producer
process.flowAfterPrelim = cms.EDProducer("RSFlowAnalyzer",
                                         tracks = cms.InputTag("generalTracks"),
                                         jets = cms.InputTag("getTwoJetsAboveHundred"),
                                         maxDeltaR = cms.double(0.7)
                                         )

process.flowAfterMainCuts = cms.EDProducer("RSFlowAnalyzer",
                                           tracks = cms.InputTag("generalTracks"),
                                           jets = cms.InputTag("getTwoJetsAfterMainCuts"),
                                           maxDeltaR = cms.double(0.7)
                                           )
# My analyzer

process.analyzerAfterPrelim = cms.EDAnalyzer("CompoundJetAnalyzer",
                                             src = cms.InputTag("getTwoJetsAboveHundred"),
                                             flowSrc = cms.InputTag("flowAfterPrelim")
                                             )

process.analyzerAfterMainCuts = cms.EDAnalyzer("CompoundJetAnalyzer",
                                               src = cms.InputTag("getTwoJetsAfterMainCuts"),
                                               flowSrc = cms.InputTag("flowAfterMainCuts")
                                               )
                                                                
#########
# Paths #
#########

# Make the jets.
process.p1 = cms.Path(process.makeCAJets + process.makePrelimCuts + process.plotJetsAfterPrelim   + process.flowAfterPrelim   + process.analyzerAfterPrelim)
process.p2 = cms.Path(process.makeCAJets + process.makeMainCuts   + process.plotJetsAfterMainCuts + process.flowAfterMainCuts + process.analyzerAfterMainCuts)
