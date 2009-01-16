#####################################
# CMSSW configuration file - Python #
#####################################

import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/0E896ABC-CEBB-DD11-89F3-001E0BC198A2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/34BC46EF-74BC-DD11-9120-00163E11240B.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/36190C89-C6BB-DD11-B043-001E0B48D104.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/50835B88-C6BB-DD11-821F-0018FE28BF3E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/62B50289-C6BB-DD11-8975-001CC443B7B8.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/769F8A1A-DCBB-DD11-8ADF-001A645933C4.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/78E38887-C6BB-DD11-A90F-0018FE28AFE6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/98382D87-C6BB-DD11-9786-001F2969CD08.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/A4EEC8BC-CEBB-DD11-AB08-001E0BC1E34C.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/B4EAB943-86BC-DD11-8335-00163E1124E0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/C24E1FDC-7ABC-DD11-9797-00163E1124CD.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/C632F988-C6BB-DD11-9FEA-001E0B48A1BE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0000/FE346F88-C6BB-DD11-984F-001CC416B322.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0002/2CF8849B-52C0-DD11-90F6-001A645CED70.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0002/782C905F-EFBF-DD11-8A36-001E0B49D098.root',
                  '/store/mc/Summer08/Exotica_RSGravitonZZJetMET_M1000/GEN-SIM-RECO/IDEAL_V9_v1/0002/A223A387-1AC0-DD11-BEA3-00163E1124D7.root' ] );


secFiles.extend( [
                   ] )

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('results_ZZ1000_withFlow.root')
)

# process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

##################
# Kinematic cuts #
##################

process.twoJetsAboveThirty = cms.EDFilter("EtMinCaloJetCountFilter",
    src = cms.InputTag("sisCone7CaloJets"),
    minNumber = cms.uint32(2),
    etMin = cms.double(30.0)
)                           

process.twoJetsAboveHundred = cms.EDFilter("EtMinCaloJetCountFilter",
    src = cms.InputTag("sisCone7CaloJets"),
    minNumber = cms.uint32(2),
    etMin = cms.double(100.0)
)

process.getTwoJetsAboveHundred = cms.EDProducer("LargestEtCaloJetSelector",
    src = cms.InputTag("sisCone7CaloJets"),
    maxNumber = cms.uint32(2)
)

process.massRangeJets = cms.EDProducer("MassRangeCaloJetSelector",
    massMin = cms.double(60.0),
    massMax = cms.double(100.0),                                   
    src = cms.InputTag("getTwoJetsAboveHundred")
)

process.twoJetsAfterCuts = cms.EDFilter("CaloJetCountFilter",
    src = cms.InputTag("massRangeJets"),
    minNumber = cms.uint32(2)
)

###########################
# Graviton Reconstruction #
###########################

process.directGravitons = cms.EDFilter("CandViewCombiner",
    cut = cms.string('600.0 < mass < 2000.0'),
    decay = cms.string('massRangeJets massRangeJets')
)

#########
# Plots #
#########

process.plotJetsBeforeCuts = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("sisCone7CaloJets"),
    histograms = jethistos
)

process.plotJetsAfterCuts = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("massRangeJets"),
    histograms = jethistos
)

process.plotDirectGravitons = cms.EDAnalyzer("CandViewHistoAnalyzer",
    src = cms.InputTag("directGravitons"),
    histograms = Ghistos
)

process.plotFlowJet1 = cms.EDAnalyzer("RSFlowAnalyzer",
                                      tracks = cms.InputTag("generalTracks"),
                                      jets = cms.InputTag("getTwoJetsAboveHundred"),
                                      maxDeltaR = cms.double(0.7),
                                      jetNumber = cms.int32(0)
)

process.plotFlowJet2 = cms.EDAnalyzer("RSFlowAnalyzer",
                                      tracks = cms.InputTag("generalTracks"),
                                      jets = cms.InputTag("getTwoJetsAboveHundred"),
                                      maxDeltaR = cms.double(0.7),
                                      jetNumber = cms.int32(1)
)

#########
# Paths #
#########

# Path before all cuts.
process.p1 = cms.Path(process.twoJetsAboveThirty * process.plotJetsBeforeCuts)

# Path after all cuts.
process.theCuts = cms.Sequence(process.twoJetsAboveHundred * process.getTwoJetsAboveHundred *
                               process.massRangeJets *
                               process.twoJetsAfterCuts * process.directGravitons)

# Flow path.
process.theFlow = cms.Sequence(process.plotFlowJet1 + process.plotFlowJet2)

process.p2 = cms.Path(process.theCuts * (process.plotJetsAfterCuts +
                                         process.theFlow +
                                         process.plotDirectGravitons) )
