import FWCore.ParameterSet.Config as cms

process = cms.Process("VecBos")

# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/MixingNoPileUp_cff')
process.load('Configuration/StandardSequences/GeometryPilot2_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
#process.load('Configuration/StandardSequences/RawToDigi_cff')
#process.load('Configuration/StandardSequences/Reconstruction_cff')

# ---- source ---
process.load("RSGraviton.RSAnalyzer.Summer08_RS1000WW_redigi_cfi")

# ---- calotowers sequence ---
process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
                                                         MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz') )
process.load("VecBos.ZJetsAnalysis.calotowermaker_cfi")

# --- tracks sequence ---
process.load("VecBos.ZJetsAnalysis.muonTracks_cfi")

# --- jet met sequences ---
process.load("HiggsAnalysis.HiggsToWW2e.jetProducerSequence_cff")

# --- electrons sequence ---
process.load("RecoEgamma.EgammaIsolationAlgos.eleIsolationSequence_cff")
process.load("VecBos.ZJetsAnalysis.electronSequence_cff")

# --- jet-vertex association sequence ---
process.load("VecBos.ZJetsAnalysis.jetProducerSequence_cff")

# --- Z->ee and Z->mumu combiners ---
process.load("VecBos.ZJetsAnalysis.ZToEESequence_cff")
process.load("VecBos.ZJetsAnalysis.ZToMuMuSequence_cff")

# --- Cuts ---
from RecoJets.JetProducers.CaloJetParameters_cfi import *
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.FastjetParameters_cfi import *
from RecoJets.JetProducers.SISConeJetParameters_cfi import *
CaloJetParameters.src = "rogancalotower"

process.sisCone10CaloJets = cms.EDProducer("SISConeJetProducer",
                                           CaloJetParameters,
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

# --- tree dumper ---
process.load("VecBos.ZJetsAnalysis.treeDumper_cfi")
process.treeDumper.jetCollection2 = "sisCone10CaloJets"
process.treeDumper.PFjetCollection2 = "sisCone10PFJets"
process.treeDumper.nameFile = 'default.root'
process.treeDumper.dumpElectrons = False
process.treeDumper.dumpMuons = False
process.treeDumper.saveFatTrk = True
process.treeDumper.saveZeeColl = False
process.treeDumper.saveZmumuColl = False
process.treeDumper.dumpTriggerResults = True
process.treeDumper.dumpCaloTowers = False
process.treeDumper.dumpParticleFlowObjects = True
process.treeDumper.dumpGenInfo = False
process.treeDumper.dumpTree = True
process.treeDumper.dumpRunInfo = True

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.doSisConeJets = cms.Sequence(process.sisCone10PFJets + process.sisCone10CaloJets)
process.cutsT1 = cms.Sequence(process.twoJets + process.getTwoJets)
process.cutsT2 = cms.Sequence(process.twoMassiveJets)
process.cutsT3 = cms.Sequence(process.directGravitons + process.cutDirectGravitons + process.filterDirectGravitons)
process.thiagoSequence = cms.Sequence(process.doSisConeJets + process.cutsT1 + process.cutsT2 + process.cutsT3)

process.p = cms.Path ( process.rogancalotower +
                       process.thiagoSequence +
                       process.jetSequence *
                       process.eleIsolationSequence *
                       process.electronSequence *
                       process.muonTracks *
                       process.zToEESequence * process.zToMuMuSequence *
                       process.treeDumper )
