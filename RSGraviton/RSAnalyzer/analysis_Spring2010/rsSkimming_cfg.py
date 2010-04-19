#####################################
# CMSSW configuration file - Python #
#####################################

import FWCore.ParameterSet.Config as cms
import datetime

process = cms.Process("SKIM")

###########################
# Basic process controls. #
###########################
today = str(datetime.date.today())
fileLabel = ''

# Source
# process.load('RSGraviton.RSAnalyzer.Summer10_MinBias_LocalData_cfi')
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:/hdacs/trtomei/CMSSW_3_4_2/src/RSGraviton/RSAnalyzer/generationSamples/allData/Pythia_800GeV_kmpl005_RECO.root',
    'file:/hdacs/trtomei/CMSSW_3_4_2/src/RSGraviton/RSAnalyzer/generationSamples/allData/Pythia_800GeV_kmpl005_RECO_02.root',
    'file:/hdacs/trtomei/CMSSW_3_4_2/src/RSGraviton/RSAnalyzer/generationSamples/allData/Pythia_800GeV_kmpl005_RECO_03.root',
    )
                            )

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.MessageLogger.cerr.threshold = 'WARNING'
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

#process.Tracer = cms.Service("Tracer")

###############
# Corrections #
###############
process.load("JetMETCorrections.Configuration.L2L3Corrections_Summer09_7TeV_cff")
# This will pull in the L2L3CorJetSC7Calo module
process.pcorrection = cms.Path(process.L2L3CorJetSC7Calo)

##################
# Kinematic cuts #
##################

### For Ntuples
process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("L2L3CorJetSC7Calo"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDProducer("LargestPtCaloJetSelector",
                                       src = cms.InputTag("oneJetAboveZero"),
                                       maxNumber = cms.uint32(1)
                                       )

process.minimalCut = cms.EDFilter("JetConfigurableSelector",
                                  src = cms.InputTag("getLargestJet"),
                                  theCut = cms.string("emEnergyFraction > 0.01"),
                                  minNumber = cms.int32(1)
                                  )

process.ptCut = cms.EDFilter("JetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > 60.0"),
                             minNumber = cms.int32(1),
                             )
process.massCut = cms.EDFilter("JetConfigurableSelector",
                               src = cms.InputTag("getLargestJet"),
                               theCut = cms.string("mass > 40.0"),
                               minNumber = cms.int32(1),
                               )
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("corMetGlobalMuons"),
                              ptMin = cms.double(60.0),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

#########
# Paths #
#########

# Paths after cuts.
process.cuts1 = cms.Sequence(process.oneJetAboveZero * process.getLargestJet)
process.cuts2 = cms.Sequence(process.minimalCut)
process.cuts3 = cms.Sequence(process.ptCut)
process.cuts4 = cms.Sequence(process.massCut)
process.cuts5 = cms.Sequence(process.METCut)
process.selectionCuts = cms.Sequence(process.cuts1 + process.cuts2 + process.cuts3
                                     + process.cuts4 + process.cuts5)

process.p = cms.Path(process.selectionCuts)

# The endpath

process.ntuplesOut = cms.OutputModule("PoolOutputModule",
                                      fileName = cms.untracked.string('qcdSkimming.root'),
                                      SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
                                      outputCommands = cms.untracked.vstring("keep *",
                                                                             "drop *_*_*_SKIM"
                                                                             )
                                      )

process.e = cms.EndPath(process.ntuplesOut)
