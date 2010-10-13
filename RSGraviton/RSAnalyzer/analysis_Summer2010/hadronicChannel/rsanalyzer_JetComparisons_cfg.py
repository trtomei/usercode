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
# Dictionaries
#####
### Weights for 300/pb
myWeightDict =      dict({'signal':1.95E-03,
                          '2j_120to280':5.73E+01,
                          '2j_280to500':6.87E-01,
                          '2j_40to120':1.08E+04,
                          '2j_500to5000':3.24E-02,
                          '3j_120to280':8.58E+01,
                          '3j_280to500':2.67E+00,
                          '3j_40to120':1.76E+03,
                          '3j_500to5000':9.90E-02,
                          '4j_120to280':4.89E+01,
                          '4j_280to500':1.60E+00,
                          '4j_40to120':2.34E+02,
                          '4j_500to5000':5.76E-02,
                          '5j_120to280':3.48E+01,
                          '5j_280to500':8.10E-01,
                          '5j_40to120':9.66E+01,
                          '5j_500to5000':6.12E-02,
                          '6j_120to280':4.44E+00,
                          '6j_280to500':2.76E-01,
                          '6j_40to120':5.37E+00,
                          '6j_500to5000':6.84E-02,
                          'W0j_0to100':1.73E+00,
                          'W1j_0to100':1.53E+00,
                          'W2j_0to100':4.23E-01,
                          'W3j_0to100':1.64E-01,
                          'W4j_0to100':1.46E-01,
                          'W5j_0to100':3.06E-01,
                          'W1j_100to300':1.47E-01,
                          'W2j_100to300':1.52E-01,
                          'W3j_100to300':1.58E-01,
                          'W4j_100to300':2.94E-01,
                          'W5j_100to300':1.03E-01,
                          'W1j_300to800':2.06E-03,
                          'W2j_300to800':4.44E-03,
                          'W3j_300to800':5.49E-03,
                          'W4j_300to800':8.10E-03,
                          'W5j_300to800':3.96E-03,
                          'W1j_800to1600':3.99E-06,
                          'W2j_800to1600':3.03E-05,
                          'W3j_800to1600':4.98E-05,
                          'W4j_800to1600':2.44E-05,
                          'W5j_800to1600':1.86E-05,
                          'TTbar0j_40GeV':1.40E-02,
                          'TTbar1j_40GeV':3.15E-02,
                          'TTbar2j_40GeV':1.09E-01,
                          'TTbar3j_40GeV':5.22E-02,
                          'TTbar4j_40GeV':2.50E-02,
                          'RSZZ_mass600_coupling005':5.10E-03,
                          'RSZZ_mass800_coupling005':1.98E-03,
                          'RSZZ_mass1000_coupling005':3.15E-04
                          })

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# Command-line options
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing()
# setup my own options
options.register ('maxEvents',
                  -1,
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.int,
                  "Number of events to process (-1 for all)")
options.register ('skipEvents',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.int,
                  "Number of events to skip initially")
options.register ('jetPtCut',
                  -1.0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "Transverse momentum cut on leading jet")
options.register ('jetEtaCut',
                  9999.9, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "Pseudorapidity cut on leading jet")
options.register ('jetMassCut',
                  -1.0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "Invariant mass cut on leading jet")
options.register ('metCut',
                  -1.0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "Transverse missing energy cut")
options.register ('jetDimension',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Jet dimension for clustering X 10"
                  )
options.register ('fileLabel',
                  '',
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,
                  "Label for the output file")

options.setupTags (tag = 'jetPtCut%d',
                  ifCond = 'jetPtCut > 0',
                  tagArg = 'jetPtCut')
options.setupTags (tag = 'jetEtaCut%d',
                  ifCond = 'jetEtaCut > 0',
                  tagArg = 'jetEtaCut')
options.setupTags (tag = 'jetMassCut%d',
                  ifCond = 'massCut > 0',
                  tagArg = 'massCut')
options.setupTags (tag = 'metCut%d',
                  ifCond = 'metCut > 0',
                  tagArg = 'metCut')
options.setupTags (tag = 'jetDimension%d',
                   ifCond = 'jetDimension > 0',
                   tagArg = 'jetDimension'
                   )

# setup any defaults you want, and fix some of the options
options.parseArguments()
outputFileName = 'results_'+'jetDimension_'+str(options.jetDimension)+'_'+options.fileLabel+'_'+today+'.root'
myWeight = myWeightDict[options.fileLabel]

### The input
if options.fileLabel == "signal":
    myInput = "RSGraviton.RSAnalyzer.Spring10."+options.fileLabel+"_cfi"
elif options.fileLabel == "RSWWjjlnu":
    myInput = "RSGraviton.RSAnalyzer.Spring10."+options.fileLabel+"_cfi"
else:
    myInput = "RSGraviton.RSAnalyzer.Spring10.Alpgen"+options.fileLabel+"_cfi"
process.load(myInput)
process.source.skipEvents = cms.untracked.uint32(options.skipEvents)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(outputFileName)
                                   )
#process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos
from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as basicjethistos

# Global tag
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START3X_V25::All'

##################
# Mandatory cuts #
##################

# The "select collisions" trigger ...
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskAlgoTrigConfig_cff')
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
process.load('HLTrigger/HLTfilters/hltLevel1GTSeed_cfi')

process.L1T1coll=process.hltLevel1GTSeed.clone()
process.L1T1coll.L1TechTriggerSeeding = cms.bool(True)
#process.L1T1coll.L1SeedsLogicalExpression = cms.string('0 AND (40 OR 41) AND NOT (36 OR 37 OR 38 OR 39)')
process.L1T1coll.L1SeedsLogicalExpression = cms.string('(40 OR 41) AND NOT (36 OR 37 OR 38 OR 39)')
# Don't ask for bit 0 in the MC.
#process.l1tcollpath = cms.Path(process.L1T1coll)

# The PhysicsDeclared HLT
process.hltHighLevel = cms.EDFilter("HLTHighLevel",
                                    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                    HLTPaths = cms.vstring('HLT_PhysicsDeclared'),# provide list of HLT paths (or patterns) you want
                                    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                                    andOr = cms.bool(True), # how to deal with multiple triggers: True: accept if ANY is true, False:accept if ALL are true
                                    throw = cms.bool(True)  # throw exception on unknown path names
                                    )

# Good vertices, no scraping
process.primaryVertexFilter = cms.EDFilter("VertexSelector",
                                           src = cms.InputTag("offlinePrimaryVertices"),
                                           cut = cms.string("!isFake && ndof > 4 && abs(z) <= 15 && position.Rho <= 2"),
                                           filter = cms.bool(True),
                                           )

process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )

#process.goodvertex=cms.Path(process.primaryVertexFilter+process.noscraping)
process.goodVertexSequence = cms.Sequence(process.primaryVertexFilter+process.noscraping)

# This is for skimming
# process.collout = cms.OutputModule("PoolOutputModule",
#                                   fileName = cms.untracked.string('/tmp/good_coll.root'),
#                                   outputCommands = process.FEVTEventContent.outputCommands,
#                                   dataset = cms.untracked.PSet(
#                                       dataTier = cms.untracked.string('RAW-RECO'),
#                                       filterName = cms.untracked.string('GOODCOLL')),
#                                   SelectEvents = cms.untracked.PSet(
#                                       SelectEvents = cms.vstring('goodvertex','l1tcollpath')
#                                       )
#                                   )


##########
# Jet ID #
##########
process.jetIdCut = cms.EDAnalyzer("RSJetIdSelector",
                                  jets = cms.InputTag("ak7CaloJets"),
                                  jetID = cms.InputTag("ak7JetID")
                                  )

###############
# Corrections #
###############
process.load("JetMETCorrections.Configuration.L2L3Corrections_Summer09_7TeV_ReReco332_cff")
# For Calo jets
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('L2L3JetCorrectorAK7Calo')
                                             )
# For PF jets
process.myL2L3CorJetAK7PF = cms.EDProducer('PFJetCorrectionProducer',
                                             src        = cms.InputTag('ak7PFJets'),
                                             correctors = cms.vstring('L2L3JetCorrectorAK7PF')
                                             )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

########################
# Jets for jet pruning #
########################

from RecoJets.JetProducers.CaloJetParameters_cfi import CaloJetParameters
from RecoJets.JetProducers.AnomalousCellParameters_cfi import AnomalousCellParameters
from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
#these are ignored, but required by VirtualJetProducer:
virtualjet_parameters = cms.PSet(jetAlgorithm=cms.string("SISCone"), rParam=cms.double(0.00001))

process.CACaloSubjets = cms.EDProducer("SubJetProducer",
                                       SubJetParameters,
                                       virtualjet_parameters,
                                       #this is required also for GenJets of PFJets:
                                       AnomalousCellParameters,
                                       CaloJetParameters
                                       )

process.CACaloSubjets.nSubjets = 2

#####################
# ParticleFlow jets #
#####################
# Here we do the jets ourselves
from RecoJets.JetProducers.ak5PFJets_cfi import ak5PFJets
myJetDimension = options.jetDimension/10.0 
process.myJetsForOptimization = ak5PFJets.clone( rParam = myJetDimension )

process.onePFJetAboveZero = cms.EDFilter("EtMinPFJetCountFilter",
                                         src = cms.InputTag("myJetsForOptimization"),
                                         etMin = cms.double(-1.0),
                                         minNumber = cms.uint32(1)
                                         )

process.getLargestPFJet = cms.EDProducer("LargestPtPFJetSelector",
                                         src = cms.InputTag("myJetsForOptimization"),
                                         maxNumber = cms.uint32(1)
                                         )


############
# Counting #
############
# In case you want to check efficiencies cut by cut.
process.eventCounter = cms.EDAnalyzer("EventCounter")
process.eventCounterTwo = process.eventCounter.clone()
process.eventCounterThree = process.eventCounter.clone()
process.eventCounterFour = process.eventCounter.clone()
process.eventCounterFive = process.eventCounter.clone()
process.eventCounterSix = process.eventCounter.clone()
process.eventCounterSeven = process.eventCounter.clone()
process.eventCounterEight = process.eventCounter.clone()

#########
# Plots #
#########

process.plotThisPFJet = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                       src = cms.InputTag("getLargestPFJet"),
                                       histograms = basicjethistos
                                       )

#########
# Paths #
#########

process.pathForSimpleJetAnalysis = cms.Path(process.goodVertexSequence +
                                            process.myJetsForOptimization +
                                            process.onePFJetAboveZero +
                                            process.getLargestPFJet +
                                            process.plotThisPFJet )
                                            
