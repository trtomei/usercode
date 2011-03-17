#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("TREEDUMPER")

###########################
# Basic process controls. #
###########################

thiagoOutputFileName = 'tree_realData_Run2010Bp1.root'
thiagoInputFilesList = ''
thiagoJetPtCut = 150.0
thiagoJetEtaCut = 2.4
thiagoJetMassCut = 0.0
thiagoMETCut = 150.0

##################
# Basic services #
##################
# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
#readFiles.extend( filelist2 )
readFiles.extend(['file:Run2010Bp1/preselection_Run2010Bp1.root',])
#readFiles.extend(['file:Run2010Bp2/preselection_Run2010Bp2.root',])

#process.load(thiagoInputFilesList)
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(thiagoOutputFileName)
)

from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos
from RSGraviton.RSAnalyzer.METhistos_cff import histograms as METhistos

##################
# The global tag #
##################
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_R_39X_V5::All'


##########
# Jet ID #
##########
# This will filter out events where any jet above 30 GeV fails the Jet ID cut.
# Default is loose cut, use tightQuality if you want tight cut.
process.jetIdCut = cms.EDFilter("RSJetIdSelector",
                                jets = cms.InputTag("ak7CaloJets"),
                                jetID = cms.InputTag("ak7JetID"),
                                threshold = cms.double(30.0),
                                filter = cms.bool(True),
                                tightQuality = cms.bool(False)
                                )

###############
# Corrections #
###############
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.ak7CaloL2Relative.useCondDB = False
process.ak7CaloL3Absolute.useCondDB = False
process.ak7CaloResidual.useCondDB = False

# For Calo jets
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('ak7CaloL2L3Residual')
                                             )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

##################
# Kinematic cuts #
##################
process.differentPtCut = cms.EDFilter("JetConfigurableSelector",
                                      src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                      theCut = cms.string("(pt > 25.0) && (abs(eta) < 5.0)"),
                                      minNumber = cms.int32(1)                                       
                                      )

process.getHardJets = cms.EDFilter("LargestPtCaloJetSelector",
                                   src = cms.InputTag("differentPtCut"),
                                   maxNumber = cms.uint32(9999)
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

###########
# Filters #
###########
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
                                           excludeTracks = cms.bool(False),
                                           tracksToExclude = cms.InputTag("leadingMuon"), # Has no effect if excludeTracks is false
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
# process.load("RSGraviton.RSAnalyzer.simpleEleIdSequence_cff")
# process.seqEleId = cms.Sequence(process.simpleEleId80relIso)

# process.electronVBTFFilter = cms.EDFilter('RSElectronVBTFFilter',
#                                           # cuts
#                                           ETCut = cms.untracked.double(20.),
#                                           vetoSecondElectronEvents = cms.untracked.bool(False),
#                                           ETCut2ndEle = cms.untracked.double(20.),
#                                           # electrons
#                                           electronCollectionTag = cms.untracked.InputTag("gsfElectrons"),   # Electron collection name
#                                           # electron ID
#                                           electronIdTag = cms.untracked.InputTag("simpleEleId80relIso"),    # Eletron ID map name
#                                           electronIdMin = cms.untracked.double(6.5), # Must pass ALL selections, i.e., 7
#                                           # fiducial definition
#                                           BarrelMaxEta = cms.untracked.double(1.4442),
#                                           EndCapMinEta = cms.untracked.double(1.566),
#                                           EndCapMaxEta = cms.untracked.double(2.5),
#                                           filter = cms.untracked.bool(False)
#                                           )

# process.VBTFelectron = cms.Sequence(process.goodElectrons + process.simpleEleId80relIso + process.electronVBTFFilter);

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
                                       weight = cms.double(1.0),
                                       isData = cms.bool(True)
                                       )
#########
# Paths #
#########

# Summary of cuts.
process.jetId  = cms.Sequence(process.jetIdCut + process.myCorrections)
process.doMultiJets = cms.Sequence(process.differentPtCut + process.getHardJets)
process.leptonStuff = cms.Sequence(process.trackerIndirectVeto + process.goodElectrons + process.VBTFmuon)
process.jetPruning = cms.Sequence(process.CACaloSubjets)

process.path = cms.Path(process.jetId +
                        process.doMultiJets +
                        process.jetPruning +
                        process.leptonStuff +
                        process.eventAnalyzer
                        )
