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
#fileLabel = 'RS750ZZ_'
fileLabel = ''

# Source
#process.load('RSGraviton.RSAnalyzer.Summer08_'+fileLabel+'JetMET_cfi')
process.load('RSGraviton.RSAnalyzer.Summer10_MinBias_LocalData_cfi')

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('results_'+fileLabel+today+'.root')
)

# process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

##################
# Mandatory cuts #
##################

# Good runs
# Should NOT be used on CRAB!!!
# from RSGraviton.RSAnalyzer.data_2009Nov19_mandatorySetup_cff import lumisToProcess as goodLumis
# process.source.lumisToProcess = goodLumis

# Proper trigger bits
# Already done in the skin!
# process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
# process.load('HLTrigger/HLTfilters/hltLevel1GTSeed_cfi')
# process.L1T1=process.hltLevel1GTSeed.clone()
# process.L1T1.L1TechTriggerSeeding = cms.bool(True)
# process.L1T1.L1SeedsLogicalExpression = cms.string('0 AND (40 OR 41) AND NOT (36 OR 37 OR 38 OR 39)')
# process.bscnobeamhalo = cms.Path(process.L1T1)

# But THIS one is not done in the skim...
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
from HLTrigger.HLTfilters.hltLevel1GTSeed_cfi import hltLevel1GTSeed
process.bptxAnd = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('0'))

# Require PhysicsDeclared HLT
# this is for filtering on HLT path
process.hltHighLevel = cms.EDFilter("HLTHighLevel",
                                    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                    HLTPaths = cms.vstring('HLT_PhysicsDeclared'),# provide list of HLT paths (or patterns) you want
                                    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                                    andOr = cms.bool(True),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
                                    throw = cms.bool(True)    # throw exception on unknown path names
                                    )

# Cut the Beam Scraping out.
process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(True),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )

process.physicsCuts = cms.Sequence(process.bptxAnd * process.hltHighLevel * process.noscraping)

# The noise cut.
process.noiseCut = cms.EDFilter("HcalNoiseFilter")
##################
# Kinematic cuts #
##################

process.twoJetsAboveZero = cms.EDFilter("PtMinCaloJetCountFilter",
    src = cms.InputTag("sisCone7CaloJets"),
    minNumber = cms.uint32(2),
    ptMin = cms.double(0.0)
)

process.getTwoJetsWithCuts = cms.EDFilter("JetConfigurableSelector",
                                          src = cms.InputTag("sisCone7CaloJets"),
                                          ptMin = cms.double(0.0),
                                          etaMax = cms.double(2.6),
                                          emfMin = cms.double(0.01),
                                          massMin = cms.double(0.0),
                                          minNumber = cms.int32(2)
                                          )

process.getTwoLargestJets = cms.EDProducer("LargestPtCaloJetSelector",
                                           src = cms.InputTag("getTwoJetsWithCuts"),
                                           maxNumber = cms.uint32(2)
                                           )

############
# Counting #
############
process.eventCounter = cms.EDAnalyzer("EventCounter")
process.eventCounterTwo = process.eventCounter.clone()
process.eventCounterThree = process.eventCounter.clone()
process.eventCounterFour = process.eventCounter.clone()

#########
# Plots #
#########

process.plotJetsGeneral = cms.EDAnalyzer("CaloJetHistoAnalyzer",
    src = cms.InputTag("getTwoLargestJets"),
    histograms = jethistos
)
process.plotJetsGeneralTwo = process.plotJetsGeneral.clone()

#process.plotFlowJet1 = cms.EDAnalyzer("RSFlowAnalyzer",
#                                      tracks = cms.InputTag("generalTracks"),
#                                      jets = cms.InputTag("getTwoJetsAboveHundred"),
#                                      maxDeltaR = cms.double(0.7),
#                                      jetNumber = cms.int32(0)
#)

#process.plotFlowJet2 = cms.EDAnalyzer("RSFlowAnalyzer",
#                                      tracks = cms.InputTag("generalTracks"),
#                                      jets = cms.InputTag("getTwoJetsAboveHundred"),
#                                      maxDeltaR = cms.double(0.7),
#                                      jetNumber = cms.int32(1)
#)

process.trackAnalysis = cms.EDAnalyzer("RSTrackAnalyzer",
                                       tracks = cms.InputTag("generalTracks"),
                                       jets = cms.InputTag("getTwoLargestJets"),
                                       jetRadius = cms.double(0.7)
)

#process.jetAnalysis = cms.EDAnalyzer("RSJetAnalyzer",
#                                         jets = cms.InputTag("getTwoJetsAboveHundred")
#                                         )

#########
# Paths #
#########

# Paths after cuts.
process.firstSetCuts = cms.Sequence(process.twoJetsAboveZero * process.getTwoJetsWithCuts * process.getTwoLargestJets)
process.secondSetCuts = cms.Sequence(process.noiseCut)

# Flow path.
#process.theFlow = cms.Sequence(process.plotFlowJet1 + process.plotFlowJet2)

process.otherAnalyses = cms.Sequence(process.trackAnalysis)# + process.jetAnalysis)

process.p = cms.Path(process.eventCounter + process.physicsCuts * (process.eventCounterTwo +
                                                                   process.firstSetCuts + process.eventCounterThree + process.plotJetsGeneral +
                                                                   process.secondSetCuts + process.eventCounterFour + process.plotJetsGeneralTwo +
                                                                   process.otherAnalyses))
