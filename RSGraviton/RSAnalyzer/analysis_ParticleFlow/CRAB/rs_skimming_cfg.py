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
process.load("RSGraviton.RSAnalyzer.Summer08_RS1000WW_redigi_cfi")
process.maxEvents.input=-1
##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

#process.TFileService = cms.Service("TFileService",
#    fileName = cms.string('results_'+fileLabel+today+'.root')
#)

#process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as jethistos

##################
# Kinematic cuts #
##################

# Make SISCone 1.0 jets, and do the cut at 70 GeV already (cut T1)
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.FastjetParameters_cfi import *
from RecoJets.JetProducers.SISConeJetParameters_cfi import *


process.sisCone10PFJets = cms.EDProducer("SISConeJetProducer",
                                         PFJetParameters,
                                         SISConeJetParameters,
                                         FastjetNoPU,
                                         coneRadius = cms.double(1.0)
                                         )

process.twoJets = cms.EDFilter("EtMinPFJetCountFilter",
                               src = cms.InputTag("sisCone10PFJets"),
                               minNumber = cms.uint32(2),
                               etMin = cms.double(70.0)
                               )


process.getTwoJets = cms.EDProducer("LargestEtPFJetSelector",
                                    src = cms.InputTag("sisCone10PFJets"),
                                    maxNumber = cms.uint32(2)
                                    )

###### Two jets with mass > 50 GeV (cut T2)
process.twoMassiveJets = cms.EDFilter("MassMinPFJetCountFilter",
                                      src = cms.InputTag("getTwoJets"),
                                      minNumber = cms.uint32(2),
                                      massMin = cms.double(50.0)
                                      )

###### Invariant mass larger than 500 GeV (cut T3)
process.directGravitons = cms.EDProducer("QuickCombiner",
                                         src = cms.InputTag("getTwoJets")
                                         )

process.cutDirectGravitons = cms.EDProducer("CandViewSelector",
                                            src = cms.InputTag("directGravitons"),
                                            cut = cms.string("mass > 500.0")
                                            )

process.filterDirectGravitons = cms.EDFilter("CandViewCountFilter",
                                             src = cms.InputTag("cutDirectGravitons"),
                                             minNumber = cms.uint32(1)
                                             )

process.doSisConeJets = cms.Sequence(process.sisCone10PFJets)
process.cutsT1 = cms.Sequence(process.twoJets + process.getTwoJets)
process.cutsT2 = cms.Sequence(process.twoMassiveJets)
process.cutsT3 = cms.Sequence(process.directGravitons + process.cutDirectGravitons + process.filterDirectGravitons)

process.load("Configuration.EventContent.EventContent_cff")
myOutputCommands = cms.untracked.vstring('keep *_sisCone10PFJets_*_*','keep *_directGravitons_*_*')
process.RECOSIMEventContent.outputCommands.extend(myOutputCommands)

process.RECOSIM = cms.OutputModule("PoolOutputModule",
                                   process.RECOSIMEventContent,
                                   SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p1")),
                                   fileName = cms.untracked.string('skim.root')
                                   )

#print process.RECOSIMEventContent.outputCommands
#########
# Paths #
#########




# Make the jets.
process.p1 = cms.Path(process.doSisConeJets +
                      process.cutsT1 +
                      process.cutsT2 +
                      process.cutsT3)

process.e1 = cms.EndPath(process.RECOSIM)
