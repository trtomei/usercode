#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring("file:Pythia_Zjjnunu_cfi_py_GEN_FASTSIM.root")
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output.root')
                                   )
#process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

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

##################
# Kinematic cuts #
##################

### For Path 1 - FAT jet from Z.
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
                             theCut = cms.string("pt > "+str(150.0)),
                             minNumber = cms.int32(1),
                             )

### This is the point where the trees should be dropped.

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
                              theCut = cms.string("abs(eta) < "+str(9999.9)),
                              minNumber = cms.int32(1),
                              )

process.massCut = cms.EDFilter("JetConfigurableSelector",
                               src = cms.InputTag("getLargestJet"),
                               theCut = cms.string("mass > "+str(-1.0)),
                               minNumber = cms.int32(1)
                               )

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
                              ptMin = cms.double(-1.0),
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

process.trackerIndirectVeto = cms.EDFilter("RSTrackerIndirectVetoFilter",
                                           src = cms.InputTag("generalTracks"),
                                           trackMinPt = cms.double(1.0),
                                           seedTrackMinPt = cms.double(10.0),
                                           trackMaxEta = cms.double(2.4),
                                           minCone = cms.double(0.02),
                                           maxCone = cms.double(0.3),
                                           minAcceptableTIV = cms.double(0.1), # 10%, has no effect if filter is False
                                           pixelHits = cms.int32(1),
                                           trackerHits = cms.int32(5),
                                           highPurityRequired = cms.bool(True),
                                           filter = cms.bool(False) #DON'T make the cut, just store the largest TIV
                                           )

process.eventAnalyzer = cms.EDAnalyzer("RSEventAnalyzer",
                                       jets = cms.InputTag("getHardJets"),
                                       compoundJets = cms.InputTag("CACaloSubjets"),
                                       met = cms.InputTag("corMetGlobalMuons"),
                                       TIV = cms.InputTag("trackerIndirectVeto"),
                                       weight = cms.double(1.0)
                                       )

process.compoundJetAnalyzer = cms.EDAnalyzer("CompoundJetAnalyzer",
                                             compoundJets = cms.InputTag("CACaloSubjets"),
                                             standardJets = cms.InputTag("getHardJets")
                                             )
                                             
#process.jetAnalyzer = cms.EDAnalyzer("RSJetAnalyzerV2",
#                                     jets = cms.InputTag("getLargestJet"),
#                                     numberInCollection = cms.uint32(0)
#                                     )

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


# This is for the PF analysis.
process.onePFJetAboveZero = cms.EDFilter("EtMinPFJetCountFilter",
                                         src = cms.InputTag("myL2L3CorJetAK7PF"),
                                         etMin = cms.double(-1.0),
                                         minNumber = cms.uint32(1)
                                         )

process.getLargestPFJet = cms.EDProducer("LargestPtPFJetSelector",
                                         src = cms.InputTag("myL2L3CorJetAK7PF"),
                                         maxNumber = cms.uint32(1)
                                         )

process.plotThisPFJet = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                       src = cms.InputTag("getLargestPFJet"),
                                       histograms = cms.VPSet(cms.PSet(nbins = cms.untracked.int32(500),
                                                                       description = cms.untracked.string('jet_et'),
                                                                       plotquantity = cms.untracked.string('et'),
                                                                       min = cms.untracked.double(0.0),
                                                                       max = cms.untracked.double(1000.0),
                                                                       name = cms.untracked.string('jet_et')
                                                                       ),
                                                              cms.PSet(nbins = cms.untracked.int32(100),
                                                                       description = cms.untracked.string('jet_eta'),
                                                                       plotquantity = cms.untracked.string('eta'),
                                                                       min = cms.untracked.double(-5.0),
                                                                       max = cms.untracked.double(5.0),
                                                                       name = cms.untracked.string('jet_eta')
                                                                       ),
                                                              cms.PSet(nbins = cms.untracked.int32(72),
                                                                       description = cms.untracked.string('jet_phi'),
                                                                       plotquantity = cms.untracked.string('phi'),
                                                                       min = cms.untracked.double(-3.141592),
                                                                       max = cms.untracked.double(3.141592),
                                                                       name = cms.untracked.string('jet_phi')
                                                                       ),
                                                              cms.PSet(nbins = cms.untracked.int32(80),
                                                                       description = cms.untracked.string('jet_mass'),
                                                                       plotquantity = cms.untracked.string('mass'),
                                                                       min = cms.untracked.double(0.0),
                                                                       max = cms.untracked.double(200.0),
                                                                       name = cms.untracked.string('jet_mass')
                                                                       )
                                                              )
                                       )

#process.trackAnalysis = cms.EDAnalyzer("RSTrackAnalyzer",
#                                       tracks = cms.InputTag("generalTracks"),
#                                       jets = cms.InputTag("getLargestJet"),
#                                       jetRadius = cms.double(0.7)
#)

#########
# Paths #
#########

# Summary of cuts.
process.goodVertexSequence = cms.Sequence(process.primaryVertexFilter+process.noscraping)
process.jetId  = cms.Sequence(process.jetIdCut + process.myCorrections)
process.cuts0  = cms.Sequence(process.oneJetAboveZero)
process.cuts1  = cms.Sequence(process.ptCut)
process.cuts2  = cms.Sequence(process.etaCut)
process.cuts3  = cms.Sequence(process.massCut)
process.cuts4  = cms.Sequence(process.METCut)
process.doMultiJets = cms.Sequence(process.differentPtCut + process.getHardJets)# + process.deltaPhiFilter + process.plotJetsGeneral)
process.cuts5 = cms.Sequence(process.deltaPhiFilter)
process.cuts6 = cms.Sequence(process.trackerIndirectVeto)
process.jetPruning = cms.Sequence(process.CACaloSubjets + process.compoundJetAnalyzer)

# I want only want Primary Vertex + LOOSE Jet ID + at least one jet + at least one jet above pT cut.
process.pathCutByCut = cms.Path(process.eventCounter + process.goodVertexSequence +
                                process.eventCounterTwo + process.jetId + process.cuts0 +
                                process.eventCounterThree + process.getLargestJet +
                                process.eventCounterFour + process.cuts1 +
                                process.eventCounterFive +
                                process.doMultiJets +
                                process.jetPruning +
                                process.cuts6 + # This one is not cutting!
                                process.eventCounterSix + 
                                process.eventAnalyzer
                                )
