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
readFiles = cms.untracked.vstring('/store/relval/CMSSW_2_2_8/RelValZMM/GEN-SIM-RECO/STARTUP_V9_v1/0000/6820DE4B-BE2C-DE11-975D-000423D99658.root')
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

##################
# Kinematic cuts #
##################

# Make SISCone 1.0 jets.
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

process.plotTwoJets = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                     src = cms.InputTag("getTwoJets"),
                                     histograms = jethistos
                                     )

process.directGravitons = cms.EDProducer("QuickCombiner",
                                         src = cms.InputTag("getTwoJets")
                                         )

process.cutDirectGravitons = cms.EDFilter("CandViewSelector",
                                          src = cms.InputTag("directGravitons"),
                                          cut = cms.string("mass > 600")
                                          )

process.plotDirectGravitons = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                             src = cms.InputTag("directGravitons"),
                                             histograms = Ghistos
                                             )

process.doSisConeJets = cms.Sequence(process.sisCone10PFJets + process.twoJets + process.getTwoJets + process.plotTwoJets)
process.doGravitons = cms.Sequence(process.directGravitons + process.cutDirectGravitons+ process.plotDirectGravitons)

# Write collection of particles inside each jet, boosted to the jet rest frame.

process.particlesFirstJet = cms.EDProducer("RSJetParticlesBooster",
                                           jets = cms.InputTag("getTwoJets"),
                                           nJet = cms.uint32(0)
                                           )

process.particlesSecondJet = cms.EDProducer("RSJetParticlesBooster",
                                            jets = cms.InputTag("getTwoJets"),
                                            nJet = cms.uint32(1)
                                            )

process.getParticlesInJets = cms.Sequence(process.particlesFirstJet + process.particlesSecondJet)

# Redo jets with those particles. I expect to find two jets back to back.
process.jetsFromFirstJet03 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.3)
                                            )
process.jetsFromSecondJet03 = cms.EDProducer("SISConeJetProducer",
                                             PFJetParameters,
                                             SISConeJetParameters,
                                             FastjetNoPU,
                                             coneRadius = cms.double(0.3)
                                             )
process.jetsFromFirstJet04 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.4)
                                            )
process.jetsFromSecondJet04 = cms.EDProducer("SISConeJetProducer",
                                             PFJetParameters,
                                             SISConeJetParameters,
                                             FastjetNoPU,
                                             coneRadius = cms.double(0.4)
                                             )
process.jetsFromFirstJet05 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.5)
                                            )
process.jetsFromSecondJet05 = cms.EDProducer("SISConeJetProducer",
                                             PFJetParameters,
                                             SISConeJetParameters,
                                             FastjetNoPU,
                                             coneRadius = cms.double(0.5)
                                             )
process.jetsFromFirstJet06 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.6)
                                            )
process.jetsFromSecondJet06 = cms.EDProducer("SISConeJetProducer",
                                             PFJetParameters,
                                             SISConeJetParameters,
                                             FastjetNoPU,
                                             coneRadius = cms.double(0.6)
                                             )
process.jetsFromFirstJet07 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.7)
                                            )
process.jetsFromSecondJet07 = cms.EDProducer("SISConeJetProducer",
                                             PFJetParameters,
                                             SISConeJetParameters,
                                             FastjetNoPU,
                                             coneRadius = cms.double(0.7)
                                             )

process.jetsFromFirstJet03.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet03.src = cms.InputTag("particlesSecondJet")
process.jetsFromFirstJet04.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet04.src = cms.InputTag("particlesSecondJet")
process.jetsFromFirstJet05.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet05.src = cms.InputTag("particlesSecondJet")
process.jetsFromFirstJet06.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet06.src = cms.InputTag("particlesSecondJet")
process.jetsFromFirstJet07.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet07.src = cms.InputTag("particlesSecondJet")

process.getjetsFromFirstJet03 = cms.EDFilter("PtMinPFJetSelector",
                                             src = cms.InputTag("jetsFromFirstJet03"),
                                             ptMin = cms.double(10.0)
                                             )
process.getjetsFromSecondJet03 = cms.EDFilter("PtMinPFJetSelector",
                                              src = cms.InputTag("jetsFromSecondJet03"),
                                              ptMin = cms.double(10.0)
                                              )
process.getjetsFromFirstJet04 = cms.EDFilter("PtMinPFJetSelector",
                                             src = cms.InputTag("jetsFromFirstJet04"),
                                             ptMin = cms.double(10.0)
                                             )
process.getjetsFromSecondJet04 = cms.EDFilter("PtMinPFJetSelector",
                                              src = cms.InputTag("jetsFromSecondJet04"),
                                              ptMin = cms.double(10.0)
                                              )
process.getjetsFromFirstJet05 = cms.EDFilter("PtMinPFJetSelector",
                                             src = cms.InputTag("jetsFromFirstJet05"),
                                             ptMin = cms.double(10.0)
                                             )
process.getjetsFromSecondJet05 = cms.EDFilter("PtMinPFJetSelector",
                                              src = cms.InputTag("jetsFromSecondJet05"),
                                              ptMin = cms.double(10.0)
                                              )
process.getjetsFromFirstJet06 = cms.EDFilter("PtMinPFJetSelector",
                                             src = cms.InputTag("jetsFromFirstJet06"),
                                             ptMin = cms.double(10.0)
                                             )
process.getjetsFromSecondJet06 = cms.EDFilter("PtMinPFJetSelector",
                                              src = cms.InputTag("jetsFromSecondJet06"),
                                              ptMin = cms.double(10.0)
                                              )
process.getjetsFromFirstJet07 = cms.EDFilter("PtMinPFJetSelector",
                                             src = cms.InputTag("jetsFromFirstJet07"),
                                             ptMin = cms.double(10.0)
                                             )
process.getjetsFromSecondJet07 = cms.EDFilter("PtMinPFJetSelector",
                                              src = cms.InputTag("jetsFromSecondJet07"),
                                              ptMin = cms.double(10.0)
                                              )

process.makeBoostedJets = cms.Sequence(process.jetsFromFirstJet03 + process.jetsFromSecondJet03 + process.getjetsFromFirstJet03 + process.getjetsFromSecondJet03 +
                                       process.jetsFromFirstJet04 + process.jetsFromSecondJet04 + process.getjetsFromFirstJet04 + process.getjetsFromSecondJet04 +
                                       process.jetsFromFirstJet05 + process.jetsFromSecondJet05 + process.getjetsFromFirstJet05 + process.getjetsFromSecondJet05 +
                                       process.jetsFromFirstJet06 + process.jetsFromSecondJet06 + process.getjetsFromFirstJet06 + process.getjetsFromSecondJet06 +
                                       process.jetsFromFirstJet07 + process.jetsFromSecondJet07 + process.getjetsFromFirstJet07 + process.getjetsFromSecondJet07)

# Analysis
process.analysisFirstJet03 = cms.EDAnalyzer("RSSubJetComparison",
                                            src = cms.InputTag("getjetsFromFirstJet03"),
                                            boost = cms.InputTag("particlesFirstJet")
                                            )
process.analysisSecondJet03 = cms.EDAnalyzer("RSSubJetComparison",
                                             src = cms.InputTag("getjetsFromSecondJet03"),
                                             boost = cms.InputTag("particlesSecondJet")
                                             )
process.analysisFirstJet04 = cms.EDAnalyzer("RSSubJetComparison",
                                            src = cms.InputTag("getjetsFromFirstJet04"),
                                            boost = cms.InputTag("particlesFirstJet")
                                            )
process.analysisSecondJet04 = cms.EDAnalyzer("RSSubJetComparison",
                                             src = cms.InputTag("getjetsFromSecondJet04"),
                                             boost = cms.InputTag("particlesSecondJet")
                                             )
process.analysisFirstJet05 = cms.EDAnalyzer("RSSubJetComparison",
                                            src = cms.InputTag("getjetsFromFirstJet05"),
                                            boost = cms.InputTag("particlesFirstJet")
                                            )
process.analysisSecondJet05 = cms.EDAnalyzer("RSSubJetComparison",
                                             src = cms.InputTag("getjetsFromSecondJet05"),
                                             boost = cms.InputTag("particlesSecondJet")
                                             )
process.analysisFirstJet06 = cms.EDAnalyzer("RSSubJetComparison",
                                            src = cms.InputTag("getjetsFromFirstJet06"),
                                            boost = cms.InputTag("particlesFirstJet")
                                            )
process.analysisSecondJet06 = cms.EDAnalyzer("RSSubJetComparison",
                                             src = cms.InputTag("getjetsFromSecondJet06"),
                                             boost = cms.InputTag("particlesSecondJet")
                                             )
process.analysisFirstJet07 = cms.EDAnalyzer("RSSubJetComparison",
                                            src = cms.InputTag("getjetsFromFirstJet07"),
                                            boost = cms.InputTag("particlesFirstJet")
                                            )
process.analysisSecondJet07 = cms.EDAnalyzer("RSSubJetComparison",
                                             src = cms.InputTag("getjetsFromSecondJet07"),
                                             boost = cms.InputTag("particlesSecondJet")
                                             )

process.analysisSubJets = cms.Sequence(process.analysisFirstJet03 + process.analysisSecondJet03 +
                                       process.analysisFirstJet04 + process.analysisSecondJet04 +
                                       process.analysisFirstJet05 + process.analysisSecondJet05 +
                                       process.analysisFirstJet06 + process.analysisSecondJet06 +
                                       process.analysisFirstJet07 + process.analysisSecondJet07)

#########
# Paths #
#########

# Make the jets.
process.p1 = cms.Path(process.doSisConeJets + process.doGravitons +
                      process.getParticlesInJets + process.makeBoostedJets + process.analysisSubJets)
#process.p2 = cms.Path(process.doCompoundJets)
#process.copyAll = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string("out.root") )
#process.out = cms.EndPath(process.copyAll)
