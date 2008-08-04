#####################################
# CMSSW configuration file - Python #
#####################################

import FWCore.ParameterSet.Config as cms

process = cms.Process("DEMO")

# Basic imports.
process.load("RecoJets.Configuration.GenJetParticles_cff")

process.load("RecoMET.Configuration.GenMETParticles_cff")

process.load("RecoMET.Configuration.RecoGenMET_cff")

process.load("RecoJets.JetProducers.sisCone7GenJetsNoNuBSM_cff")

process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")

process.load("RecoJets.JetProducers.sisCone7CaloJets_cff")

process.load("PhysicsTools.RecoAlgos.allTracks_cfi")

###########################
# Basic process controls. #
###########################

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/data1/tomei/CMSSW_1_8_4/src/RSGraviton/RSAnalyzer/production/ParameterSpaceScanRECO/RS1000_ZZ_4j_AOD_10TeV_fastsim.root')
)

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('results.root')
)

######
# MC #
######

process.trueGravitons = cms.EDFilter("PdgIdAndStatusCandViewSelector",
    status = cms.vint32(3),
    src = cms.InputTag("genParticleCandidates"),
    pdgId = cms.vint32(5000039)
)

process.trueZs = cms.EDFilter("PdgIdAndStatusCandViewSelector",
    status = cms.vint32(3),
    src = cms.InputTag("genParticleCandidates"),
    pdgId = cms.vint32(23)
)

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

process.plotTrueZs = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("trueZs"),
    histograms = Zhistos
)

process.plotTrueGravitons = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("trueGravitons"),
    histograms = Ghistos
)

process.makeMC = cms.Sequence(process.genJetParticles*(process.trueGravitons*process.plotTrueGravitons+process.trueZs*process.plotTrueZs))

###########
# GenJets #
###########

process.twoGenJets = cms.EDFilter("LargestEtGenJetSelector",
    maxNumber = cms.uint32(2),
    src = cms.InputTag("sisCone7GenJetsNoNuBSM")
)

process.plotGenJets = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("twoGenJets"),
    histograms = jethistos
)

process.makeGenJets = cms.Sequence(process.sisCone7GenJetsNoNuBSM*process.twoGenJets*process.plotGenJets)

############
# CaloJets #
############

process.twoCaloJets = cms.EDFilter("LargestEtCaloJetSelector",
    maxNumber = cms.uint32(2),
    src = cms.InputTag("sisCone7CaloJets")
)

process.plotCaloJets = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("twoCaloJets"),
    histograms = jethistos
)

process.makeCaloJets = cms.Sequence(process.sisCone7CaloJets*process.twoCaloJets*process.plotCaloJets)

###########################
# Graviton Reconstruction #
###########################

process.directGravitons = cms.EDFilter("CandViewCombiner",
    cut = cms.string('0.0 < mass < 2000.0'),
    decay = cms.string('twoCaloJets twoCaloJets')
)

process.plotDirectGravitons = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("directGravitons"),
    histograms = Ghistos
)

process.makeDirectGravitons = cms.Sequence(process.directGravitons*process.plotDirectGravitons)

process.leadingCaloJet = cms.EDFilter("LargestEtCaloJetSelector",
    maxNumber = cms.uint32(1),
    src = cms.InputTag("sisCone7CaloJets")
)

process.etLeadingCaloJet = cms.EDFilter("CandViewSelector",
    filter = cms.bool(True),
    src = cms.InputTag("leadingCaloJet"),
    cut = cms.string('et > 100')
)

process.makeCuts = cms.Sequence(process.leadingCaloJet*process.etLeadingCaloJet)

#########
# Paths #
#########

process.p1 = cms.Path(process.makeMC+process.makeCaloJets*process.makeCuts*process.makeDirectGravitons*process.makeCuts)

