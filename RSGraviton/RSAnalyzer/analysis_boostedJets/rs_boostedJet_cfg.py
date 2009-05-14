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
fileLabel = 'test'

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

##################
# Kinematic cuts #
##################

# Make SISCone 1.0 jets.
from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.FastjetParameters_cfi import *
from RecoJets.JetProducers.SISConeJetParameters_cfi import *

process.genParticlesForJets = cms.EDFilter("InputGenJetsParticleSelector",
                                           src = cms.InputTag("genParticles"),
                                           ignoreParticleIDs = cms.vuint32(1000022, 2000012, 2000014, 2000016, 1000039,
                                                                           5000039, 4000012, 9900012, 9900014, 9900016,
                                                                           39),
                                           partonicFinalState = cms.bool(False),
                                           excludeResonances = cms.bool(True),
                                           excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
                                           tausAsJets = cms.bool(False)
                                           )

process.sisCone10GenJets = cms.EDProducer("SISConeJetProducer",
                                          GenJetParameters,
                                          SISConeJetParameters,
                                          FastjetNoPU,
                                          coneRadius = cms.double(1.0)
                                          )

process.twoJets = cms.EDFilter("EtMinGenJetCountFilter",
                               src = cms.InputTag("sisCone10GenJets"),
                               minNumber = cms.uint32(2),
                               etMin = cms.double(1.314)
                               )

process.getTwoJets = cms.EDProducer("LargestEtGenJetSelector",
                                    src = cms.InputTag("sisCone10GenJets"),
                                    maxNumber = cms.uint32(2)
                                    )

process.plotTwoJets = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                     src = cms.InputTag("getTwoJets"),
                                     histograms = jethistos
                                     )

process.doSisConeJets = cms.Sequence(process.genParticlesForJets + process.sisCone10GenJets + process.twoJets + process.getTwoJets + process.plotTwoJets)

# Make CATop 0.7 and compare with SISCone 0.7 from Event. 
# Load geometry
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('IDEAL_V9::All')
process.load("Configuration.StandardSequences.MagneticField_cff")

from RecoJets.JetProducers.CaloJetParameters_cfi import *
from RecoJets.JetProducers.CATopJetParameters_cfi import *
process.compound7CaloJets = cms.EDProducer("CATopJetProducer",
                                           CATopJetParameters,
                                           CaloJetParameters
                                           )

# turn off sum-et dependent stuff.
process.compound7CaloJets.ptBins = cms.vdouble(0,10e9)
process.compound7CaloJets.rBins  = cms.vdouble(0.7,0.7)
process.compound7CaloJets.ptFracBins = cms.vdouble(0.05,0.05)
process.compound7CaloJets.nCellBins = cms.vint32(1,1)

process.twoCAJets = cms.EDFilter("EtMinBasicJetCountFilter",
                                 src = cms.InputTag("compound7CaloJets"),
                                 minNumber = cms.uint32(2),
                                 etMin = cms.double(1.314)
                                 )

process.getTwoCAJets = cms.EDProducer("LargestEtBasicJetSelector",
                                      src = cms.InputTag("compound7CaloJets"),
                                      maxNumber = cms.uint32(2)
                                      )

process.plotTwoCAJets = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                       src = cms.InputTag("getTwoCAJets"),
                                       histograms = jethistos
                                       )

process.twoSISJets = cms.EDFilter("EtMinCaloJetCountFilter",
                                 src = cms.InputTag("sisCone7CaloJets"),
                                 minNumber = cms.uint32(2),
                                 etMin = cms.double(1.314)
                                 )

process.getTwoSISJets = cms.EDProducer("LargestEtCaloJetSelector",
                                       src = cms.InputTag("sisCone7CaloJets"),
                                       maxNumber = cms.uint32(2)
                                       )

process.plotTwoSISJets = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                        src = cms.InputTag("getTwoSISJets"),
                                        histograms = jethistos
                                        )

process.compareJets = cms.EDAnalyzer("RSJetComparison",
                                     src = cms.InputTag("getTwoCAJets"),
                                     matched = cms.InputTag("getTwoSISJets")
                                     )

process.doCompoundJets = cms.Sequence(process.compound7CaloJets + process.twoCAJets + process.getTwoCAJets + process.plotTwoCAJets
                                      + process.twoSISJets + process.getTwoSISJets + process.plotTwoSISJets + process.compareJets)

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
process.jetsFromFirstJet = cms.EDProducer("SISConeJetProducer",
                                          GenJetParameters,
                                          SISConeJetParameters,
                                          FastjetNoPU,
                                          coneRadius = cms.double(0.5)
                                          )
process.jetsFromSecondJet = cms.EDProducer("SISConeJetProducer",
                                           GenJetParameters,
                                           SISConeJetParameters,
                                           FastjetNoPU,
                                           coneRadius = cms.double(0.5)
                                           )

process.jetsFromFirstJet.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet.src = cms.InputTag("particlesSecondJet")

process.jetsFromFirstJet10 = cms.EDFilter("PtMinGenJetSelector",
                                          src = cms.InputTag("jetsFromFirstJet"),
                                          ptMin = cms.double(10.0)
                                          )

process.jetsFromSecondJet10 = cms.EDFilter("PtMinGenJetSelector",
                                           src = cms.InputTag("jetsFromSecondJet"),
                                           ptMin = cms.double(10.0)
                                           )

process.makeBoostedJets = cms.Sequence(process.jetsFromFirstJet + process.jetsFromSecondJet + process.jetsFromFirstJet10 + process.jetsFromSecondJet10)

# Analysis
process.directGravitons = cms.EDFilter("CandViewCombiner",
                                       cut = cms.string('600.0 < mass < 2000.0'),
                                       decay = cms.string('getTwoJets getTwoJets')
                                       )

process.plotDirectGravitons = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                             src = cms.InputTag("directGravitons"),
                                             histograms = Ghistos
                                             )

process.analysisFirstJet = cms.EDAnalyzer("RSSubJetComparison",
                                          src = cms.InputTag("jetsFromFirstJet10")
                                          )

process.analysisSecondJet = cms.EDAnalyzer("RSSubJetComparison",
                                           src = cms.InputTag("jetsFromSecondJet10")
                                           )

process.analysis = cms.Sequence(process.directGravitons + process.plotDirectGravitons + process.analysisFirstJet + process.analysisSecondJet)

#########
# Paths #
#########

# Make the jets.
process.p1 = cms.Path(process.doSisConeJets + process.getParticlesInJets + process.makeBoostedJets + process.analysis)
process.p2 = cms.Path(process.doCompoundJets)
#process.copyAll = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string("out.root") )
#process.out = cms.EndPath(process.copyAll)
