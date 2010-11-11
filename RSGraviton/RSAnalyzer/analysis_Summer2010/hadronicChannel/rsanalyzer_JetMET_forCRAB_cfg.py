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
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring("file:/home/trtomei/storage/data/Pythia_GZZjjnunu_1000GeV_kmpl005_CMSSW_358_RECO.root")
#                            fileNames = cms.untracked.vstring(
#    'file:W1j_800pt1600_1_1_nRJ.root',
#    'file:W1j_800pt1600_2_1_omh.root',
#    'file:W1j_800pt1600_3_1_akt.root',
#    'file:EDMfilesForTesting/exception.root')
#    ),
#                            skipEvents = cms.untracked.uint32(1171)
#
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
process.GlobalTag.globaltag = 'START3X_V26::All'

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
process.load('JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff')

# For Calo jets
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('ak7CaloL2L3')
                                             )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

##################
# Kinematic cuts #
##################

thiagoJetPtCut = 80.0
thiagoJetEtaCut = 3.0
thiagoJetMassCut = 0.0
thiagoMETCut = 80.0

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
                             theCut = cms.string("pt > "+str(thiagoJetPtCut)),
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
                              theCut = cms.string("abs(eta) < "+str(thiagoJetEtaCut)),
                              minNumber = cms.int32(1),
                              )

process.massCut = cms.EDFilter("JetConfigurableSelector",
                               src = cms.InputTag("getLargestJet"),
                               theCut = cms.string("mass > -1.0"),
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

### FIXME PF MET?
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("pfMet"),
                              ptMin = cms.double(thiagoMETCut),
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

###########
# Filters #
###########
process.hardaGenParticles = cms.EDProducer("PdgIdAndStatusCandSelector",
                                          src = cms.InputTag("genParticles"),
                                          status = cms.vint32(3),
                                          pdgId = cms.vint32(1,2,3,4,5,6,11,12,13,14,15,16,21,22,23,24,5000039)
                                          )

process.hardGenParticles = cms.EDProducer("GenParticlePruner",
                                            src = cms.InputTag("genParticles"),
                                            select = cms.vstring("drop  *  ", # this is the default
                                                                 "keep status = 3"
                                                                 )
                                            )

process.deltaPhiFilter = cms.EDFilter("RSEventDeltaPhiFilter",
                                      jets = cms.InputTag("getHardJets"),
                                      maxDeltaPhi = cms.double(2.8)
                                      )

process.goodElectrons = cms.EDFilter("LargestPtGsfElectronSelector",
                                     src = cms.InputTag("gsfElectrons"),
                                     maxNumber = cms.uint32(2)
                                     )

process.goodMuons = cms.EDFilter("LargestPtMuonSelector",
                                 src = cms.InputTag("muons"),
                                 maxNumber = cms.uint32(2)
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

#################
# VBTF electron #
#################
process.load("RSGraviton.RSAnalyzer.simpleEleIdSequence_cff")
process.seqEleId = cms.Sequence(process.simpleEleId80relIso)

process.electronVBTFFilter = cms.EDFilter('RSElectronVBTFFilter',
                                          # cuts
                                          ETCut = cms.untracked.double(20.),
                                          vetoSecondElectronEvents = cms.untracked.bool(False),
                                          ETCut2ndEle = cms.untracked.double(20.),
                                          # electrons
                                          electronCollectionTag = cms.untracked.InputTag("gsfElectrons"),   # Electron collection name
                                          # electron ID
                                          electronIdTag = cms.untracked.InputTag("simpleEleId80relIso"),    # Eletron ID map name
                                          electronIdMin = cms.untracked.double(6.5), # Must pass ALL selections, i.e., 7
                                          # fiducial definition
                                          BarrelMaxEta = cms.untracked.double(1.4442),
                                          EndCapMinEta = cms.untracked.double(1.566),
                                          EndCapMaxEta = cms.untracked.double(2.5),
                                          filter = cms.untracked.bool(False)
                                          )

process.VBTFelectron = cms.Sequence(process.goodElectrons + process.simpleEleId80relIso + process.electronVBTFFilter);

#############
# VBTF muon #
#############
process.muonVBTFFilter = cms.EDFilter('RSMuonVBTFFilter',
                                      MuonTag = cms.untracked.InputTag("muons"),
                                      JetTag = cms.untracked.InputTag("ak5CaloJets"),
                                      # Preselection!
                                      PtThrForZ1 = cms.untracked.double(20.0),
                                      PtThrForZ2 = cms.untracked.double(10.0),
                                      vetoSecondMuonEvents = cms.untracked.bool(False),
                                      EJetMin = cms.untracked.double(40.),
                                      NJetMax = cms.untracked.int32(999999),
                                      # Main cuts ->
                                      PtCut = cms.untracked.double(20.0),
                                      EtaCut = cms.untracked.double(2.1),
                                      IsRelativeIso = cms.untracked.bool(True),
                                      IsCombinedIso = cms.untracked.bool(True),
                                      IsoCut03 = cms.untracked.double(0.15),
                                      # Muon quality cuts ->
                                      DxyCut = cms.untracked.double(0.2), # dxy < 0.2 cm (cosmics)
                                      NormalizedChi2Cut = cms.untracked.double(10.), # chi2/ndof < 10.
                                      TrackerHitsCut = cms.untracked.int32(11),  # Hits in inner track > 10
                                      PixelHitsCut = cms.untracked.int32(1),  # Pixel Hits  > 0
                                      MuonHitsCut = cms.untracked.int32(1),  # Valid Muon Hits  > 0
                                      IsAlsoTrackerMuon = cms.untracked.bool(True),
                                      NMatchesCut = cms.untracked.int32(2),  # At least 2 Chambers matched with segments
                                      # filter
                                      filter = cms.untracked.bool(False)
                                      )
process.VBTFmuon = cms.Sequence(process.goodMuons + process.muonVBTFFilter)

###############
# Tree Dumper #
###############
process.eventAnalyzer = cms.EDAnalyzer("RSEventAnalyzer",
                                       jets = cms.InputTag("getHardJets"),
                                       compoundJets = cms.InputTag("CACaloSubjets"),
                                       met = cms.InputTag("corMetGlobalMuons"),
                                       PFmet = cms.InputTag("pfMet"),
                                       TIV = cms.InputTag("trackerIndirectVeto"),
                                       electrons = cms.InputTag("goodElectrons"),
                                       muons = cms.InputTag("goodMuons"),
                                       genParticles = cms.InputTag("hardGenParticles"),
                                       VBTFelectron = cms.InputTag("electronVBTFFilter"),
                                       VBTFmuon = cms.InputTag("muonVBTFFilter"),
                                       weight = cms.double(1.0)
                                       )

process.compoundJetAnalyzer = cms.EDAnalyzer("CompoundJetAnalyzer",
                                             compoundJets = cms.InputTag("CACaloSubjets"),
                                             standardJets = cms.InputTag("getHardJets")
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
process.leptonStuff = cms.Sequence(process.trackerIndirectVeto + process.VBTFelectron + process.VBTFmuon)
process.jetPruning = cms.Sequence(process.CACaloSubjets + process.compoundJetAnalyzer)

# I want only want Primary Vertex + LOOSE Jet ID + at least one jet + at least one jet above pT cut + MET cut
process.pathCutByCut = cms.Path(process.eventCounter + process.goodVertexSequence +
                                process.eventCounterTwo + process.jetId + process.cuts0 +
                                process.eventCounterThree + process.getLargestJet +
                                process.eventCounterFour + process.etaCut +
                                process.eventCounterFive + process.ptCut +
                                process.eventCounterSix + process.METCut + 
                                process.doMultiJets +
                                process.jetPruning +
                                process.leptonStuff + # This one is not cutting!
                                process.eventCounterSeven + 
                                process.hardGenParticles + 
                                process.eventAnalyzer
                                )
