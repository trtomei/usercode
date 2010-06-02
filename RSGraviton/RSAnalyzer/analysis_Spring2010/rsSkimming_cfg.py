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
#process.source.fileNames = ('/store/mc/Spring10/QCD4Jets_Pt40to120-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0012/56743007-B648-DF11-8358-0024E8768099.root',)
process.source.fileNames = ('file:reco.root',)

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.MessageLogger.cerr.threshold = 'WARNING'
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
    )

#process.Tracer = cms.Service("Tracer")

###############
# Corrections #
###############
#process.load("JetMETCorrections.Configuration.L2L3Corrections_Summer09_7TeV_cff")
process.load("JetMETCorrections.Configuration.L2L3Corrections_Summer09_7TeV_ReReco332_cff")
#L2JetCorrectorAK7Calo = cms.ESSource("L2RelativeCorrectionService",
#                                     tagName = cms.string('Summer09_7TeV_ReReco332_L2Relative_AK7Calo'),
#                                     label = cms.string('L2RelativeJetCorrectorAK7Calo')
#                                     )
#L3JetCorrectorAK7Calo = cms.ESSource("L3AbsoluteCorrectionService",
#                                     tagName = cms.string('Summer09_7TeV_ReReco332_L3Absolute_AK7Calo'),
#                                     label = cms.string('L3AbsoluteJetCorrectorAK7Calo')
#                                     )
#L2L3JetCorrectorAK7Calo = cms.ESSource("JetCorrectionServiceChain",
#                                       correctors = cms.vstring('L2RelativeJetCorrectorAK7Calo','L3AbsoluteJetCorrectorAK7Calo'),
#                                       label = cms.string('L2L3JetCorrectorAK7Calo')
#                                       )
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('L2L3JetCorrectorAK7Calo')
                                             )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

##################
# Kinematic cuts #
##################

### Jet ID
process.jetIdCut = cms.EDAnalyzer("RSJetIdSelector",
                                  jets = cms.InputTag("ak7CaloJets"),
                                  jetID = cms.InputTag("ak7JetID")
                                  )


### For Ntuples
process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("myL2L3CorJetAK7Calo"),
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
                             theCut = cms.string("pt > 40.0"),
                             minNumber = cms.int32(1),
                             )
process.massCut = cms.EDFilter("JetConfigurableSelector",
                               src = cms.InputTag("getLargestJet"),
                               theCut = cms.string("mass > 30.0"),
                               minNumber = cms.int32(1),
                               )
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("corMetGlobalMuons"),
                              ptMin = cms.double(40.0),
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

#process.p = cms.Path(process.selectionCuts)

# The endpath

process.ntuplesOut = cms.OutputModule("PoolOutputModule",
                                      fileName = cms.untracked.string('qcdSkimming.root'),
                                      SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
                                      outputCommands = cms.untracked.vstring("keep *",
                                                                             "drop *_*_*_SKIM"
                                                                             )
                                      )

#process.e = cms.EndPath(process.ntuplesOut)
process.p = cms.Path(process.jetIdCut + process.myCorrections)
