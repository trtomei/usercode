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
                          'RSWWjjlnu':3.913E-03,
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

# setup any defaults you want, and fix some of the options
options.parseArguments()
outputFileName = 'results_'+options.fileLabel+'_'+today+'.root'
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
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('L2L3JetCorrectorAK7Calo')
                                             )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

##################
# Kinematic cuts #
##################

### Electrons
process.atLeastOneElectron = cms.EDFilter("CandViewCountFilter",
                                          src = cms.InputTag("gsfElectrons"),
                                          minNumber = cms.uint32(1),
                                          )

process.getLargestElectron = cms.EDProducer("LargestPtGsfElectronSelector",
                                            src=cms.InputTag("gsfElectrons"),
                                            maxNumber = cms.uint32(1)
                                            )

from SHarper.HEEPAnalyzer.HEEPSelectionCuts_cfi import *
process.checkHEEPCuts = cms.EDFilter("RSElectronSelector",
                                     eleLabel = cms.InputTag("getLargestElectron"),
                                     barrelCuts = cms.PSet(heepBarrelCuts),
                                     endcapCuts = cms.PSet(heepEndcapCuts)
                                     )

### Jets
process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDProducer("LargestPtCaloJetSelector",
                                       src = cms.InputTag("oneJetAboveZero"),
                                       maxNumber = cms.uint32(1)
                                       )

process.ptCut = cms.EDFilter("JetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > "+str(options.jetPtCut)),
                             minNumber = cms.int32(1),
                             )

process.differentPtCut = cms.EDFilter("JetConfigurableSelector",
                                      src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                      theCut = cms.string("(pt > 25.0) && (abs(eta) < 5.0)"),
                                      minNumber = cms.int32(1)                                       
                                      )

process.getHardJets = cms.EDProducer("LargestPtCaloJetSelector",
                                     src = cms.InputTag("differentPtCut"),
                                     maxNumber = cms.uint32(9999)
                                     )

process.etaCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("abs(eta) < "+str(options.jetEtaCut)),
                              minNumber = cms.int32(1),
                              )

process.massCut = cms.EDFilter("JetConfigurableSelector",
                               src = cms.InputTag("getLargestJet"),
                               theCut = cms.string("mass > "+str(options.jetMassCut)),
                               minNumber = cms.int32(1)
                               )

### Missing Et
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("corMetGlobalMuons"),
                              ptMin = cms.double(options.metCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

############
# Counting #
############

# For selection of right channel at MC level.
# Pruning for Pythia
process.prunedGenParticles = cms.EDProducer("GenParticlePruner",
                                            src = cms.InputTag("genParticles"),
                                            select = cms.vstring("drop  *  ", # this is the default
                                                                 "keep status = 3",
                                                                 "keep pdgId = 5000039 & status = 3",
                                                                 "keep+ pdgId = 24 & status = 3",
                                                                 "drop pdgId = 24 & status = 2"
                                                                 )
                                            )

process.MCelectrons = cms.EDProducer("PdgIdCandViewSelector",
                                     src = cms.InputTag("prunedGenParticles"),
                                     pdgId = cms.vint32( 11 ),
                                     filter = cms.bool(True)
                                     )

# In case you want to check efficiencies cut by cut.
process.eventCounter = cms.EDAnalyzer("EventCounter")
process.eventCounterTwo = process.eventCounter.clone()
process.eventCounterThree = process.eventCounter.clone()
process.eventCounterFour = process.eventCounter.clone()
process.eventCounterFive = process.eventCounter.clone()
process.eventCounterSix = process.eventCounter.clone()
process.eventCounterSeven = process.eventCounter.clone()
process.eventCounterEight = process.eventCounter.clone()

###################
# Plots and Trees #
###################
process.eventAnalyzer = cms.EDAnalyzer("RSLeptonicEventAnalyzer",
                                       jets = cms.InputTag("getHardJets"),
                                       met = cms.InputTag("corMetGlobalMuons"),
                                       electrons = cms.InputTag("getLargestElectron"),
                                       weight = cms.double(myWeight)
                                       )

# In case you want to check the pthat of the event (MC only)
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
                                     cms.PSet(nbins = cms.untracked.int32(500),
                                              description = cms.untracked.string('MET'),
                                              plotquantity = cms.untracked.string('et'),
                                              min = cms.untracked.double(0.0),
                                              max = cms.untracked.double(1000.0),
                                              name = cms.untracked.string('MET')
                                              ),
                                     cms.PSet(nbins = cms.untracked.int32(500),
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
                                         src = cms.InputTag("getHardJets"),
                                         histograms = jethistos
                                         )

process.plotElectron = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                      src = cms.InputTag("getLargestElectron"),
                                      histograms = cms.VPSet(
                                          cms.PSet(nbins = cms.untracked.int32(500),
                                                   description = cms.untracked.string('leading electron pt'),
                                                   plotquantity = cms.untracked.string('pt'),
                                                   min = cms.untracked.double(0.0),
                                                   max = cms.untracked.double(1000.0),
                                                   name = cms.untracked.string('ele1pt')
                                                   ),
                                          cms.PSet(nbins = cms.untracked.int32(72),
                                                   description = cms.untracked.string('leading electron eta'),
                                                   plotquantity = cms.untracked.string('eta'),
                                                   min = cms.untracked.double(-3.141592),
                                                   max = cms.untracked.double(3.141592),
                                                   name = cms.untracked.string('ele1eta')
                                                   )
                                          )
                                      )

#########
# Paths #
#########

# Summary of cuts.
process.goodVertexSequence = cms.Sequence(process.primaryVertexFilter+process.noscraping)
process.jetId  = cms.Sequence(process.jetIdCut + process.myCorrections)
process.eleId  = cms.Sequence(process.atLeastOneElectron + process.getLargestElectron + process.checkHEEPCuts)
process.cuts0  = cms.Sequence(process.oneJetAboveZero)
process.cuts1  = cms.Sequence(process.ptCut)
process.cuts2  = cms.Sequence(process.etaCut)
process.cuts3  = cms.Sequence(process.massCut)
process.cuts4  = cms.Sequence(process.METCut)
process.doMultiJets = cms.Sequence(process.differentPtCut + process.getHardJets)# + process.deltaPhiFilter + process.plotJetsGeneral)

process.MonteCarloSignalPruning = cms.Sequence(process.prunedGenParticles + process.MCelectrons)

# I want only want Primary Vertex + LOOSE Jet ID + at least one jet + at least one HEEP electron.
process.pathCutByCut = cms.Path(#process.MonteCarloSignalPruning +
                                process.eventCounter +
                                process.goodVertexSequence + # Primary Vertex
                                process.eventCounterTwo +
                                process.jetId + process.cuts0 + # at least one good Jet
                                process.eventCounterThree +
                                process.getLargestJet +
                                process.eleId + # at least one HEEP electron
                                process.eventCounterFour +
                                process.doMultiJets +
                                process.plotJetsGeneral + process.plotMET + process.plotElectron +
                                process.eventAnalyzer
                                )
