#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

###########################
# Basic process controls. #
###########################

thiagoOutputFileName = 'controlRegion_realData.root'
thiagoInputFilesList = "RSGraviton.RSAnalyzer.Spring10."+'AlpgenW2j_100to300_cfi'
thiagoJetPtCut = 150.0
thiagoJetEtaCut = 2.4
thiagoJetMassCut = 0.0
thiagoMETCut = 150.0

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.EventContent.EventContent_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
#readFiles.extend( [
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/F4A840A8-6CCC-DF11-A218-A4BADB3D00FF.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/9A07F077-3DCD-DF11-A190-003048C9CA8E.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/62AC2F3D-68CC-DF11-99A1-001E682F8738.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/4C699E75-3CCD-DF11-B294-0030487CAA5D.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/2A6004A3-3DCD-DF11-B959-00238BBDEAF7.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/1A64EBE3-72CC-DF11-BA19-E0CB4E29C4DB.root' ] );

readFiles.extend( [ 'file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/selectedHBHEAndTrigger.root', ] )

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

##########
# Jet ID #
##########
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
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('ak7CaloL2L3')
                                             )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

###########
# Trigger #
###########
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskAlgoTrigConfig_cff')
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtStableParametersConfig_cff')
process.load('HLTrigger/HLTfilters/hltLevel1GTSeed_cfi')

process.triggerSelection = cms.EDFilter("TriggerResultsFilter",
                                        triggerConditions = cms.vstring(
    'HLT_MET65_CenJet50U_v*',
    'HLT_MET80_CenJet50U_v*',
    ),
                                        hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
                                        l1tResults = cms.InputTag( "" ),
                                        l1tIgnoreMask = cms.bool( True ),
                                        l1techIgnorePrescales = cms.bool( False ),
                                        daqPartitions = cms.uint32( 1 ),
                                        throw = cms.bool( False )
                                        )

##################
# For MC Studies #
##################
process.MCmuons = cms.EDFilter("PdgIdAndStatusCandViewSelector",
                               src = cms.InputTag("genParticles"),
                               pdgId = cms.vint32( 13 ),
                               status = cms.vint32( 3 ),
                               filter = cms.bool(True)
                               )
      
process.MCelectrons = process.MCmuons.clone(pdgId = cms.vint32(11))
process.MCtaus = process.MCmuons.clone(pdgId = cms.vint32(15))

##################
# Kinematic cuts #
##################

### For Path 1 - FAT jet from Z.
process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDFilter("LargestPtCaloJetSelector",
                                     src = cms.InputTag("oneJetAboveZero"),
                                     maxNumber = cms.uint32(1)
                                     )

# Jet pt, eta cut
process.ptCut = cms.EDFilter("JetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > "+str(thiagoJetPtCut)),
                             minNumber = cms.int32(1),
                             )
process.etaCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("abs(eta) < "+str(thiagoJetEtaCut)),
                              minNumber = cms.int32(1),
                              )
process.jetCuts = cms.Sequence(process.oneJetAboveZero + process.getLargestJet + process.ptCut + process.etaCut)

# MET cut
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("corMetGlobalMuons"),
                              ptMin = cms.double(thiagoMETCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

process.differentPtCut = cms.EDFilter("JetConfigurableSelector",
                                      src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                      theCut = cms.string("(pt > 25.0) && (abs(eta) < 5.0)"),
                                      minNumber = cms.int32(1)                                       
                                      )

process.getHardJets = cms.EDFilter("LargestPtCaloJetSelector",
                                   src = cms.InputTag("differentPtCut"),
                                   maxNumber = cms.uint32(9999)
                                   )

process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')

# Other cuts
#
# EMF cut
process.EMFCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("(emEnergyFraction > 0.1) && (emEnergyFraction < 0.9)"),
                              minNumber = cms.int32(1)
                              )

# TIV cut
process.TIVCut = cms.EDFilter("RSTrackerIndirectVetoFilter",
                              src = cms.InputTag("generalTracks"),
                              excludeTracks = cms.bool(True),
                              tracksToExclude = cms.InputTag("leadingMuon"),
                              trackMinPt = cms.double(1.0),
                              seedTrackMinPt = cms.double(10.0),
                              trackMaxEta = cms.double(2.4),
                              minCone = cms.double(0.02),
                              maxCone = cms.double(0.3),
                              minAcceptableTIV = cms.double(0.1), # 10%, has no effect if filter is False
                              pixelHits = cms.int32(1),
                              trackerHits = cms.int32(5),
                              highPurityRequired = cms.bool(True),
                              filter = cms.bool(True)
                              )

# Multijets cut
process.multiJetCut = cms.EDFilter("RSEventDeltaPhiFilter",
                                   jets = cms.InputTag("getHardJets"),
                                   maxValue = cms.double(0.94)
                                   )

# Anti-hot-region cut
process.hotRegionCut = cms.EDFilter("JetConfigurableSelector",
                                    src = cms.InputTag("getLargestJet"),
                                    theCut = cms.string("phi > -2.7"),
                                    minNumber = cms.int32(1)
                                    )
# Muon control
process.leadingMuon = cms.EDFilter("LargestPtMuonSelector",
                                   src = cms.InputTag("muons"),
                                   maxNumber = cms.uint32(1)
                                   )

process.muonCut = cms.EDFilter("EtaPtMinCandViewSelector",
                               src = cms.InputTag("leadingMuon"),
                               ptMin = cms.double(20.0),
                               etaMin = cms.double(-2.4),
                               etaMax = cms.double(2.4),
                               minNumber = cms.uint32(1),
                               filter = cms.bool(True)
                               )

process.muonVBTFFilter = cms.EDFilter('RSMuonVBTFFilter',
                                      MuonTag = cms.untracked.InputTag("leadingMuon"),
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
                                      filter = cms.untracked.bool(True)
                                      )

process.VBTFmuon = cms.Sequence(process.leadingMuon + process.muonCut + process.muonVBTFFilter)

# build W->MuNu candidates using PF MET
process.wmnCands = cms.EDProducer("CandViewShallowCloneCombiner",
                                    checkCharge = cms.bool(False),
                                    cut = cms.string(""),
                                    decay = cms.string("leadingMuon corMetGlobalMuons")
                                    )
# W filter
# MET cut
process.wmnCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("wmnCands"),
                              ptMin = cms.double(thiagoMETCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

process.muonMETCut = cms.Sequence(process.wmnCands + process.wmnCut)

#########
# PLOTS #
#########

process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("wmnCands"),
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
process.plotMETmuons = process.plotMET.clone()
process.plotMETelectrons = process.plotMET.clone()
process.plotMETtaus = process.plotMET.clone()

process.plotJetsGeneral = cms.EDAnalyzer("CaloJetHistoAnalyzer",
                                         src = cms.InputTag("getHardJets"),
                                         histograms = jethistos
                                         )
process.plotJetsGeneralmuons = process.plotJetsGeneral.clone()
process.plotJetsGeneralelectrons = process.plotJetsGeneral.clone()
process.plotJetsGeneraltaus = process.plotJetsGeneral.clone()

# Path
process.analysisSequence = cms.Sequence(process.HBHENoiseFilter + 
                                        process.VBTFmuon + 
                                        process.jetIdCut +
                                        process.myCorrections +
                                        process.jetCuts +
                                        #                       process.METCut +    
                                        process.muonMETCut +
                                        process.differentPtCut +
                                        process.getHardJets +
                                        process.EMFCut +
                                        process.TIVCut +
                                        process.multiJetCut
                                        #                       process.hotRegionCut +
                                        )

#process.pmuons     = cms.Path(process.MCmuons + process.analysisSequence + process.plotMETmuons + process.plotJetsGeneralmuons)
#process.pelectrons = cms.Path(process.MCelectrons + process.analysisSequence + process.plotMETelectrons + process.plotJetsGeneralelectrons)
#process.ptaus      = cms.Path(process.MCtaus + process.analysisSequence + process.plotMETtaus + process.plotJetsGeneraltaus)

process.pdata = cms.Path(process.analysisSequence + process.plotMET + process.plotJetsGeneral)
