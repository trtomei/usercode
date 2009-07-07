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

# --- tree dumper ---
process.load("VecBos.ZJetsAnalysis.treeDumper_cfi")
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

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.p = cms.Path ( process.rogancalotower *
                       process.jetSequence *
                       process.eleIsolationSequence *
                       process.electronSequence *
                       process.muonTracks *
                       process.zToEESequence * process.zToMuMuSequence *
                       process.treeDumper )
