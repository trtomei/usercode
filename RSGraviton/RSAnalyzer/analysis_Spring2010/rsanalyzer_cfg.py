#####################################
# CMSSW configuration file - Python #
#####################################

import FWCore.ParameterSet.Config as cms
import datetime
today = str(datetime.date.today())

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################
# Source
# process.load('RSGraviton.RSAnalyzer.Summer10_MinBias_LocalData_cfi')
#process.load('RSGraviton.RSAnalyzer.Spring10_QCD_MC_cfi')
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

# Command-line options
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing('standard')
# setup my own options
options.register ('ptCut',
                  -1.0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "Transverse momentum cut on leading jet")
options.register ('etaCut',
                  9999.9, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "Pseudorapidity cut on leading jet")
options.register('tenEtaCut',
                 99999,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.float,
                 "Pseudorapidity cut on leading jet times 10")
options.register ('massCut',
                  -1.0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "Invariant mass cut on leading jet")
options.register ('metCut',
                  -1.0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "Transverse missing energy cut")
options.register ('fileLabel',
                  '',
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,
                  "Label for the output file")

options.setupTags (tag = 'ptCut%d',
                  ifCond = 'ptCut > 0',
                  tagArg = 'ptCut')
options.setupTags (tag = 'etaCut%d',
                  ifCond = 'etaCut > 0',
                  tagArg = 'tenEtaCut')
options.setupTags (tag = 'massCut%d',
                  ifCond = 'massCut > 0',
                  tagArg = 'massCut')
options.setupTags (tag = 'metCut%d',
                  ifCond = 'metCut > 0',
                  tagArg = 'metCut')

# setup any defaults you want, and fix some of the options
options.parseArguments()
outputFileName = 'results_'+options.fileLabel+'_'+today+'.root'
options.output=outputFileName
options.tenEtaCut = 10*options.etaCut

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.output)
)

#process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

##################
# Mandatory cuts #
##################

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

###############
# Corrections #
###############
process.load("JetMETCorrections.Configuration.L2L3Corrections_Summer09_7TeV_cff")
# This will pull in the L2L3CorJetSC7Calo module
process.pcorrection = cms.Path(process.L2L3CorJetSC7Calo)
# Use only on non-skimmed data!

##################
# Kinematic cuts #
##################


### For Path 1 - FAT jet

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
                             theCut = cms.string("pt > "+str(options.ptCut)),
                             minNumber = cms.int32(1),
                             )

process.etaCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("abs(eta) < "+str(options.etaCut)),
                              minNumber = cms.int32(1),
                              )

process.massCut = cms.EDFilter("JetConfigurableSelector",
                               src = cms.InputTag("getLargestJet"),
                               theCut = cms.string("mass > "+str(options.massCut)),
                               minNumber = cms.int32(1)
                               )

### Path 2 - TWO jets
                               
process.twoJetsAboveZero = process.oneJetAboveZero.clone(minNumber = 2)
process.getTwoLargestJets = process.getLargestJet.clone(src = "twoJetsAboveZero", maxNumber = 2)
process.minimalCutTwoJets = process.minimalCut.clone(src = "getTwoLargestJets", minNumber = 2)
process.ptCutTwoJets = process.ptCut.clone(src = "getTwoLargestJets", minNumber = 2, theCut = "pt > 60.0")
process.etaCutTwoJets = process.etaCut.clone(src = "getTwoLargestJets", minNumber = 2)

### Common for both paths.
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("corMetGlobalMuons"),
                              ptMin = cms.double(options.metCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

############
# Counting #
############
process.eventCounter = cms.EDAnalyzer("EventCounter")
process.eventCounterTwo = process.eventCounter.clone()
process.eventCounterTwoB = process.eventCounter.clone()
process.eventCounterThree = process.eventCounter.clone()
process.eventCounterThreeB = process.eventCounter.clone()
process.eventCounterFour = process.eventCounter.clone()
process.eventCounterFourB = process.eventCounter.clone()
process.eventCounterFive = process.eventCounter.clone()
process.eventCounterFiveB = process.eventCounter.clone()
process.eventCounterSix = process.eventCounter.clone()
process.eventCounterSixB = process.eventCounter.clone()
process.eventCounterSeven = process.eventCounter.clone()
process.eventCounterSevenB = process.eventCounter.clone()
process.eventCounterEight = process.eventCounter.clone()
process.eventCounterEightB = process.eventCounter.clone()

#########
# Plots #
#########
process.getPtHat = cms.EDAnalyzer("GenEventAnalyzer",
                                  min = cms.untracked.double(0.0),
                                  max = cms.untracked.double(1000.0),
                                  nbins = cms.untracked.int32(200),
                                  description = cms.untracked.string("pthat"),
                                  name = cms.untracked.string("pthat"),
                                  plotquantity = cms.untracked.string("binningValues.front")
                                  )


process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("corMetGlobalMuons"),
                                 histograms = cms.VPSet(
                                     cms.PSet(nbins = cms.untracked.int32(200),
                                              description = cms.untracked.string('MET'),
                                              plotquantity = cms.untracked.string('et'),
                                              min = cms.untracked.double(0.0),
                                              max = cms.untracked.double(1000.0),
                                              name = cms.untracked.string('MET')
                                              ),
                                     cms.PSet(nbins = cms.untracked.int32(200),
                                              description = cms.untracked.string('METpt'),
                                              plotquantity = cms.untracked.string('pt'),
                                              min = cms.untracked.double(0.0),
                                              max = cms.untracked.double(1000.0),
                                              name = cms.untracked.string('METpt')
                                              ),
                                     cms.PSet(nbins = cms.untracked.int32(72),
                                              description = cms.untracked.string('MET phi'),
                                              plotquantity = cms.untracked.string('phi'),
                                              min = cms.untracked.double(-3.141592),
                                              max = cms.untracked.double(3.141592),
                                              name = cms.untracked.string('MET_phi')
                                              )
                                     )
                                 )

process.plotJetsGeneral = cms.EDAnalyzer("CaloJetHistoAnalyzer",
    src = cms.InputTag("getLargestJet"),
    histograms = jethistos
)

process.trackAnalysis = cms.EDAnalyzer("RSTrackAnalyzer",
                                       tracks = cms.InputTag("generalTracks"),
                                       jets = cms.InputTag("getLargestJet"),
                                       jetRadius = cms.double(0.7)
)

process.plotMETNoCuts = process.plotMET.clone()
process.plotJetsGeneralNoCuts = process.plotJetsGeneral.clone()
process.trackAnalysisNoCuts = process.trackAnalysis.clone()
process.getPtHatNoCuts = process.getPtHat.clone()

#########
# Paths #
#########

# Paths after cuts.
process.cuts0  = cms.Sequence(process.oneJetAboveZero)
process.cuts0b = cms.Sequence(process.minimalCut)
process.cuts1  = cms.Sequence(process.ptCut)
process.cuts2  = cms.Sequence(process.etaCut)
process.cuts3  = cms.Sequence(process.massCut)
process.cuts4  = cms.Sequence(process.METCut)

process.pathFatJet = cms.Path(process.eventCounter + process.cuts0 +
                              process.eventCounterTwo + process.getLargestJet + process.cuts0b +
                              process.eventCounterThree + process.cuts1 +
                              process.eventCounterFour + process.cuts2 +
                              process.eventCounterFive + process.cuts3 +
                              process.eventCounterSix + process.cuts4 +
                              process.eventCounterSeven)
