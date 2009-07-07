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

##################
# Kinematic cuts #
##################

# Make SISCone 1.0 jets, and do the cut at 70 GeV already (cut T1)
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.FastjetParameters_cfi import *
from RecoJets.JetProducers.SISConeJetParameters_cfi import *

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
            
process.outgoingPartonsBefore = cms.EDFilter("PdgIdAndStatusCandViewSelector",
                                             src = cms.InputTag("genParticles"),
                                             pdgId = cms.vint32(1,2,3,4,5,6,-1,-2,-3,-4,-5,-6,21),
                                             status = cms.vint32(3)
                                             )
process.hardestPartonsBefore = cms.EDFilter("LargestPtCandViewSelector",
                                            src = cms.InputTag("outgoingPartonsBefore"),
                                            maxNumber = cms.uint32(1)
                                            )
process.plotPartonsBefore = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                           src = cms.InputTag("hardestPartonsBefore"),
                                           histograms = cms.VPSet(cms.PSet(
                                               nbins = cms.untracked.int32(100),
                                               description = cms.untracked.string('parton_pt'),
                                               plotquantity = cms.untracked.string('pt'),
                                               min = cms.untracked.double(0.0),
                                               max = cms.untracked.double(500.0),
                                               name = cms.untracked.string('parton_pt')
                                               )
                                                                  )
                                           )

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

process.plotTwoJets = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                     src = cms.InputTag("getTwoJets"),
                                     histograms = jethistos
                                     )

process.jetAnalysisT1 = cms.EDAnalyzer("PFJetAnalyzer",
                                       src = cms.InputTag("getTwoJets")
                                       )

###### Two jets with mass > 50 GeV (cut T2)
process.twoMassiveJets = cms.EDFilter("MassMinPFJetCountFilter",
                                      src = cms.InputTag("getTwoJets"),
                                      minNumber = cms.uint32(2),
                                      massMin = cms.double(50.0)
                                      )

process.plotTwoMassiveJets = process.plotTwoJets.clone()
process.jetAnalysisT2 = process.jetAnalysisT1.clone()

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

process.plotDirectGravitons = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                             src = cms.InputTag("directGravitons"),
                                             histograms = Ghistos
                                             )
process.plotTwoJetsGraviton = process.plotTwoJets.clone()

process.jetAnalysisT3 = process.jetAnalysisT1.clone()

process.outgoingPartonsAfter = process.outgoingPartonsBefore.clone()
process.hardestPartonsAfter = process.hardestPartonsBefore.clone()
process.hardestPartonsAfter.src = "outgoingPartonsAfter"
process.plotPartonsAfter = process.plotPartonsBefore.clone()
process.plotPartonsAfter.src = "hardestPartonsAfter"

process.checkPartonsBefore = cms.Sequence(process.outgoingPartonsBefore+process.hardestPartonsBefore+process.plotPartonsBefore) 
process.checkPartonsAfter = cms.Sequence(process.outgoingPartonsAfter+process.hardestPartonsAfter+process.plotPartonsAfter)

process.doSisConeJets = cms.Sequence(process.sisCone10PFJets)
process.cutsT1 = cms.Sequence(process.twoJets + process.getTwoJets + process.plotTwoJets + process.jetAnalysisT1)
process.cutsT2 = cms.Sequence(process.twoMassiveJets + process.plotTwoMassiveJets + process.jetAnalysisT2)
process.doGravitons = cms.Sequence(process.directGravitons + process.cutDirectGravitons + process.filterDirectGravitons + process.plotDirectGravitons)
process.cutsT3 = cms.Sequence(process.plotTwoJetsGraviton + process.jetAnalysisT3)

#########
# Paths #
#########

# Make the jets.
process.p1 = cms.Path(process.checkPartonsBefore +
                      process.doSisConeJets +
                      process.cutsT1 +
                      process.cutsT2 +
                      process.doGravitons +
                      process.cutsT3 +
                      process.checkPartonsAfter )                  
