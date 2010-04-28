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
#process.load('RSGraviton.RSAnalyzer.Summer10_MinBias_LocalData_cfi')
#process.load('RSGraviton.RSAnalyzer.Spring10_QCD_MC_cfi')
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
#    'file:/storage/trtomei/data/QCD_pt30_MERGED.root'
#    'file:/storage/trtomei/data/QCD_pt80_MERGED.root'
#    'file:/storage/trtomei/data/Pythia_800GeV_kmpl005_RECO.root',
#    'file:/storage/trtomei/data/Pythia_800GeV_kmpl005_RECO_02.root',
#    'file:/storage/trtomei/data/Pythia_800GeV_kmpl005_RECO_03.root'
#    'file:/storage/trtomei/data/QCD_ALPGEN_2j_120to280_MERGED.root'
#    'file:/storage/trtomei/data/QCD_ALPGEN_2j_280to500_MERGED.root',
#    'file:/storage/trtomei/data/QCD_ALPGEN_2j_500to5000_1.root',
#    'file:/storage/trtomei/data/QCD_ALPGEN_2j_500to5000_2.root',
#    'file:/storage/trtomei/data/QCD_ALPGEN_2j_500to5000_3.root',
#    'file:/storage/trtomei/data/QCD_ALPGEN_2j_500to5000_4.root',
#    'file:/storage/trtomei/data/QCD_ALPGEN_2j_500to5000_5.root',
#    'file:/storage/trtomei/data/QCD_ALPGEN_2j_500to5000_6.root',

#    'file:/storage/trtomei/data/QCD_ALPGEN_3j_40to120_MERGED.root'
#    '/store/user/tomei/QCD_ALPGEN3j_120to280/qcdSkimming_1.root',
#    '/store/user/tomei/QCD_ALPGEN3j_120to280/qcdSkimming_2.root',
#    '/store/user/tomei/QCD_ALPGEN3j_120to280/qcdSkimming_3.root',
#    '/store/user/tomei/QCD_ALPGEN3j_120to280/qcdSkimming_4.root',
#    '/store/user/tomei/QCD_ALPGEN3j_120to280/qcdSkimming_5.root',
#    '/store/user/tomei/QCD_ALPGEN3j_120to280/qcdSkimming_6.root'
#    '/store/user/tomei/QCD_ALPGEN3j_280to500/qcdSkimming_1.root',
#    '/store/user/tomei/QCD_ALPGEN3j_280to500/qcdSkimming_2.root',
#    '/store/user/tomei/QCD_ALPGEN3j_280to500/qcdSkimming_3.root',
#    '/store/user/tomei/QCD_ALPGEN3j_280to500/qcdSkimming_4.root',
#    '/store/user/tomei/QCD_ALPGEN3j_280to500/qcdSkimming_5.root',
#    '/store/user/tomei/QCD_ALPGEN3j_280to500/qcdSkimming_6.root'
#    '/store/user/tomei/QCD_ALPGEN3j_500to5000/qcdSkimming_1.root',
#    '/store/user/tomei/QCD_ALPGEN3j_500to5000/qcdSkimming_2.root',
#    '/store/user/tomei/QCD_ALPGEN3j_500to5000/qcdSkimming_3.root',
#    '/store/user/tomei/QCD_ALPGEN3j_500to5000/qcdSkimming_4.root',
#    '/store/user/tomei/QCD_ALPGEN3j_500to5000/qcdSkimming_5.root',
#    '/store/user/tomei/QCD_ALPGEN3j_500to5000/qcdSkimming_6.root'

#      '/store/user/tomei/QCD_ALPGEN4j_40to120/qcdSkimming_6.root'
#      '/store/user/tomei/QCD_ALPGEN4j_120to280/qcdSkimming_1.root',
#      '/store/user/tomei/QCD_ALPGEN4j_120to280/qcdSkimming_2.root',
#      '/store/user/tomei/QCD_ALPGEN4j_120to280/qcdSkimming_3.root'
#      '/store/user/tomei/QCD_ALPGEN4j_280to500/qcdSkimming_1.root',
#      '/store/user/tomei/QCD_ALPGEN4j_280to500/qcdSkimming_2.root'
#      '/store/user/tomei/QCD_ALPGEN4j_500to5000/qcdSkimming_1.root',
#      '/store/user/tomei/QCD_ALPGEN4j_500to5000/qcdSkimming_2.root',
#      '/store/user/tomei/QCD_ALPGEN4j_500to5000/qcdSkimming_3.root'

    '/store/user/tomei/QCD_ALPGEN5j_40to120/qcdSkimming_1.root',
    '/store/user/tomei/QCD_ALPGEN5j_40to120/qcdSkimming_2.root',
    '/store/user/tomei/QCD_ALPGEN5j_40to120/qcdSkimming_3.root',
    '/store/user/tomei/QCD_ALPGEN5j_40to120/qcdSkimming_4.root',
    '/store/user/tomei/QCD_ALPGEN5j_40to120/qcdSkimming_5.root'
#    '/store/user/tomei/QCD_ALPGEN5j_120to280/qcdSkimming_1.root',
#    '/store/user/tomei/QCD_ALPGEN5j_120to280/qcdSkimming_2.root',
#    '/store/user/tomei/QCD_ALPGEN5j_120to280/qcdSkimming_3.root',
#    '/store/user/tomei/QCD_ALPGEN5j_120to280/qcdSkimming_4.root',
#    '/store/user/tomei/QCD_ALPGEN5j_120to280/qcdSkimming_5.root',
#    '/store/user/tomei/QCD_ALPGEN5j_120to280/qcdSkimming_6.root',
#    '/store/user/tomei/QCD_ALPGEN5j_120to280/qcdSkimming_7.root',
    

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

# These will probably be around in the skim, but I add them here just in case.

#
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskAlgoTrigConfig_cff')
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
process.load('HLTrigger/HLTfilters/hltLevel1GTSeed_cfi')

process.L1T1coll=process.hltLevel1GTSeed.clone()
process.L1T1coll.L1TechTriggerSeeding = cms.bool(True)
process.L1T1coll.L1SeedsLogicalExpression = cms.string('0 AND (40 OR 41) AND NOT (36 OR 37 OR 38 OR 39) AND NOT ((42 AND NOT 43) OR (43 AND NOT 42))')
# Should we put the 0 in here in the MC?

# process.l1tcollpath = cms.Path(process.L1T1coll)

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

# process.goodvertex=cms.Path(process.primaryVertexFilter+process.noscraping)


process.collout = cms.OutputModule("PoolOutputModule",
                                   fileName = cms.untracked.string('/tmp/good_coll.root'),
                                   outputCommands = process.FEVTEventContent.outputCommands,
                                       dataset = cms.untracked.PSet(
                                           dataTier = cms.untracked.string('RAW-RECO'),
                                           filterName = cms.untracked.string('GOODCOLL')),
                                   SelectEvents = cms.untracked.PSet(
                                       SelectEvents = cms.vstring('goodvertex','l1tcollpath')
                                       )
                                   )

# Require PhysicsDeclared HLT
process.hltHighLevel = cms.EDFilter("HLTHighLevel",
                                    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                    HLTPaths = cms.vstring('HLT_PhysicsDeclared'),# provide list of HLT paths (or patterns) you want
                                    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                                    andOr = cms.bool(True),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
                                    throw = cms.bool(True)    # throw exception on unknown path names
                                    )

# The noise cut.
process.noiseCut = cms.EDFilter("HcalNoiseFilter")

###############
# Corrections #
###############
# This will pull in the L2L3CorJetSC7Calo module
process.load("JetMETCorrections.Configuration.L2L3Corrections_Summer09_7TeV_cff")
process.pcorrection = cms.Path(process.L2L3CorJetSC7Calo)

##################
# Kinematic cuts #
##################

### For Path 1 - FAT jet from Z.

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

process.differentPtCut = cms.EDFilter("JetConfigurableSelector",
                                      src = cms.InputTag("L2L3CorJetSC7Calo"),
                                      theCut = cms.string("pt > 40.0 & emEnergyFraction > 0.01"),
                                      minNumber = cms.int32(1)                                       
                                      )

process.getHardJets = cms.EDProducer("LargestPtCaloJetSelector",
                                     src = cms.InputTag("differentPtCut"),
                                     maxNumber = cms.uint32(9999)
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

### Path 2 - TWO jets from Z
# Not being used now.                                
#process.twoJetsAboveZero = process.oneJetAboveZero.clone(minNumber = 2)
#process.getTwoLargestJets = process.getLargestJet.clone(src = "twoJetsAboveZero", maxNumber = 2)
#process.minimalCutTwoJets = process.minimalCut.clone(src = "getTwoLargestJets", minNumber = 2)
#process.ptCutTwoJets = process.ptCut.clone(src = "getTwoLargestJets", minNumber = 2, theCut = "pt > 40.0") # Like the "different pt cut" 
#process.etaCutTwoJets = process.etaCut.clone(src = "getTwoLargestJets", minNumber = 2)

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
process.deltaPhiFilter = cms.EDFilter("RSEventDeltaPhiFilter",
                                      jets = cms.InputTag("getHardJets"),
                                      maxDeltaPhi = cms.double(2.8)
                                      )

process.eventAnalyzer = cms.EDAnalyzer("RSEventAnalyzer",
                                     jets = cms.InputTag("getHardJets"),
                                     met = cms.InputTag("corMetGlobalMuons")
                                     )

#process.jetAnalyzer = cms.EDAnalyzer("RSJetAnalyzerV2",
#                                     jets = cms.InputTag("getLargestJet"),
#                                     numberInCollection = cms.uint32(0)
#                                     )

# In case you want to check the pthat of the event (MC only)
#process.getPtHat = cms.EDAnalyzer("GenEventAnalyzer",
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
                                         src = cms.InputTag("getHardJets"),
                                         histograms = jethistos
                                         )

#process.trackAnalysis = cms.EDAnalyzer("RSTrackAnalyzer",
#                                       tracks = cms.InputTag("generalTracks"),
#                                       jets = cms.InputTag("getLargestJet"),
#                                       jetRadius = cms.double(0.7)
#)

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
process.doMultiJets = cms.Sequence(process.differentPtCut + process.getHardJets) + process.deltaPhiFilter + process.plotJetsGeneral)

#process.pathCutByCut = cms.Path(process.eventCounter + process.cuts0 +
#                                process.eventCounterTwo + process.getLargestJet + process.cuts0b +
#                                process.eventCounterThree + process.cuts1 +
#                                process.eventCounterFour + process.cuts2 +
#                                process.eventCounterFive + process.cuts3 +
#                                process.eventCounterSix + process.cuts4 +
#                                process.eventCounterSeven)


process.p = cms.Path(process.cuts0 + process.getLargestJet + process.cuts0b + process.cuts1 + process.cuts3 + process.cuts4 +
                     process.eventCounter +
                     process.doMultiJets +
                     # process.deltaPhiFilter +
                     process.plotJetsGeneral + process.eventAnalyzer)
