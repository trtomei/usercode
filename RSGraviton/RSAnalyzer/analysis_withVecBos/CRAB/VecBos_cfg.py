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

process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/MixingNoPileUp_cff')
process.load('Configuration/StandardSequences/GeometryPilot2_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')

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
# Also make the CaloJets and GenJets, for comparison.
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.FastjetParameters_cfi import *
from RecoJets.JetProducers.SISConeJetParameters_cfi import *
from RecoJets.JetProducers.CaloJetParameters_cfi import *
from RecoJets.JetProducers.GenJetParameters_cfi import *

process.sisCone10CaloJets = cms.EDProducer("SISConeJetProducer",
                                           CaloJetParameters,
                                           SISConeJetParameters,
                                           FastjetNoPU,
                                           coneRadius = cms.double(1.0)
                                           )

process.load("RecoJets.Configuration.GenJetParticles_cff")
process.sisCone10GenJets = cms.EDProducer("SISConeJetProducer",
                                          GenJetParameters,
                                          SISConeJetParameters,
                                          FastjetNoPU,
                                          coneRadius = cms.double(1.0)
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

process.doSisConeJets = cms.Sequence(process.sisCone10CaloJets + process.genJetParticles + process.sisCone10GenJets + process.sisCone10PFJets)
process.cutsT1 = cms.Sequence(process.twoJets + process.getTwoJets + process.plotTwoJets + process.jetAnalysisT1)
process.cutsT2 = cms.Sequence(process.twoMassiveJets + process.plotTwoMassiveJets + process.jetAnalysisT2)
process.doGravitons = cms.Sequence(process.directGravitons + process.cutDirectGravitons + process.filterDirectGravitons + process.plotDirectGravitons)
process.cutsT3 = cms.Sequence(process.plotTwoJetsGraviton + process.jetAnalysisT3)

##################
# Extra Analysis #
##################

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

# Redo jets with those particles.
process.jetsFromFirstJet07 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.7)
                                            )
process.jetsFromSecondJet07 = process.jetsFromFirstJet07.clone()

process.jetsFromFirstJet07.src = "particlesFirstJet"
process.jetsFromSecondJet07.src = "particlesSecondJet"

process.makeBoostedJets = cms.Sequence(process.jetsFromFirstJet07 + process.jetsFromSecondJet07)

# Analysis
process.analysisSubJets = cms.EDAnalyzer("RSSubJetComparison",
                                         srcFirst = cms.InputTag("jetsFromFirstJet07"),
                                         srcSecond = cms.InputTag("jetsFromSecondJet07"),
                                         momentumCut = cms.double(15.0)
                                         )

process.thiagoSequence = cms.Sequence(process.doSisConeJets +
                                      process.cutsT1 +
                                      process.cutsT2 +
                                      process.doGravitons +
                                      process.cutsT3 +
                                      process.getParticlesInJets +
                                      process.makeBoostedJets +
                                      process.analysisSubJets )
                  
# Now for the VecBos part 

# Produce PFMet
process.pfMET = cms.EDProducer("METProducer",
                               src = cms.InputTag("particleFlow"),
                               METType = cms.string('pfMET'),
                               alias = cms.string('pfMET'),
                               noHF = cms.bool(False),
                               globalThreshold = cms.double(0.0),
                               InputType = cms.string('PFCandidateCollection')
                               )

# Produce Candidate tracks.
from SimGeneral.HepPDTESSource.pythiapdt_cfi import *

process.candTracks = cms.EDProducer("ConcreteChargedCandidateProducer",
                                    src = cms.InputTag("generalTracks"),
                                    particleType = cms.string('pi+')
                                    )

# Jet vertexing.
process.jetVertexAlpha1 = cms.EDProducer("JetVertexAssociation",
                                        JV_deltaZ = cms.double(0.3),
                                        JV_sigmaZ = cms.double(9.5),
                                        JV_alpha_threshold = cms.double(0.2),
                                        JV_cone_size = cms.double(1.0),
                                        JV_type_Algo = cms.int32(1),
                                        JET_ALGO = cms.string('sisCone10CaloJets'),
                                        TRACK_ALGO = cms.string('generalTracks'),
                                        VERTEX_ALGO = cms.string('offlinePrimaryVertices'),
                                        JV_cutType = cms.string('delta')
                                        )

process.jetVertexAlpha2 = process.jetVertexAlpha1.clone()

# --- tree dumper ---
process.load("VecBos.ZJetsAnalysis.treeDumper_cfi")
process.treeDumper.trackCollection = 'candTracks'
process.treeDumper.jetCollection1 = 'sisCone10CaloJets'
process.treeDumper.genJetCollection1 = 'sisCone10GenJets'
process.treeDumper.PFjetCollection1 = 'sisCone10PFJets'
process.treeDumper.dumpElectrons = False
process.treeDumper.dumpMuons = False
process.treeDumper.dumpCaloTowers = False
process.treeDumper.dumpZeeCand = False
process.treeDumper.dumpZmumuCand = False
process.treeDumper.dumpParticleFlowObjects = True

process.treeDumper.saveEcal = False
process.treeDumper.saveFatEcal = False
process.treeDumper.saveEleID = False
process.treeDumper.saveZeeColl = False
process.treeDumper.saveZmumuColl = False
process.treeDumper.nameFile = 'default.root'

process.treeDumper.dumpGenInfo = False
process.treeDumper.dumpTree = True
process.treeDumper.dumpRunInfo = True

process.vecbosSequence = cms.Sequence ( process.candTracks +
                                        process.pfMET +
                                        process.jetVertexAlpha1 + process.jetVertexAlpha2)

process.p = cms.Path(process.thiagoSequence + process.vecbosSequence + process.treeDumper)
