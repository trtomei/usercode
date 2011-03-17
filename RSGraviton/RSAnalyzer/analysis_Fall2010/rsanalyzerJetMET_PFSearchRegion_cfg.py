#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("MUONS")

###########################
# Basic process controls. #
###########################

thiagoOutputFileName = 'signalAndControlTogether_realData_Run2010B.root'
thiagoInputFilesList = ''
thiagoJetPtCut = 150.0
thiagoSmallJetPtCut = 30.0
thiagoJetEtaCut = 2.4
thiagoJetMassCut = 0.0
thiagoMETCut = 150.0
thiagoMaxJets = 3
thiagoMaxAngle = 2.8

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
readFiles.extend(['file:Run2010Bp1/preselection_Run2010Bp1.root',])
readFiles.extend(['file:Run2010Bp2/preselection_Run2010Bp2.root',])
#readFiles.extend(['file:Run2010Bp2_oldReco.root',])
#readFiles.extend(['file:signal_M1250.root',])

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

from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as basicjethistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos
from RSGraviton.RSAnalyzer.METhistos_cff import histograms as METhistos

##################
# The global tag #
##################
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_R_39X_V5::All' # 3_9_X RECO
#process.GlobalTag.globaltag = 'GR_R_38X_V15::All ' # 3_8_X RECO

##########
# Jet ID #
##########
# This will filter out events where any jet above 30 GeV fails the Jet ID cut.
# Default is loose cut, use tightQuality if you want tight cut.
process.jetIdCut = cms.EDFilter("RSPFJetIdSelector",
                                jets = cms.InputTag("ak7PFJets"),
                                muons = cms.InputTag("leadingMuon"),
                                correctorName = cms.string("ak7PFL2L3Residual"),
                                threshold = cms.double(thiagoSmallJetPtCut),
                                filter = cms.bool(False),
                                neutralHadronFraction = cms.double(0.99),
                                neutralEMFraction = cms.double(0.99),
                                numberOfConstituents = cms.int32(1),
                                chargedHadronFraction = cms.double(0),
                                chargedEMFraction = cms.double(0.99),
                                multiplicity = cms.int32(0),
                                muonDR = cms.double(0.3),
                                clearFromMuons = cms.bool(False)
                                )

process.jetIdCutControl = process.JetIdCut.clone(clearFromMuons = cms.bool(True))

###############
# Corrections #
###############
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.ak7PFL2Relative.useCondDB = False
process.ak7PFL3Absolute.useCondDB = False
process.ak7PFResidual.useCondDB = False
process.myCorrectedJets = cms.EDProducer('PFJetCorrectionProducer',
                                         src        = cms.InputTag('jetIdCut'),
                                         correctors = cms.vstring('ak7PFL2L3Residual')
                                         )
process.myCorrections = cms.Sequence(process.myCorrectedJets)

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

### For Path 1 - FAT jet from Z + MET
process.oneJetAboveZero = cms.EDFilter("PFJetConfigurableSelector",
                                       src = cms.InputTag("myCorrectedJets"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDFilter("LargestPtPFJetSelector",
                                     src = cms.InputTag("oneJetAboveZero"),
                                     maxNumber = cms.uint32(1)
                                     )

# Jet pt, eta cut
process.ptCut = cms.EDFilter("PFJetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > "+str(thiagoJetPtCut)),
                             minNumber = cms.int32(1),
                             )
process.etaCut = cms.EDFilter("PFJetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("abs(eta) < "+str(thiagoJetEtaCut)),
                              minNumber = cms.int32(1),
                              )

# Jet mass cut
process.massCut = cms.EDFilter("PFJetConfigurableSelector",
                               src = cms.InputTag("getLargestJet"),
                               theCut = cms.string("mass > "+str(thiagoJetMassCut)),
                               minNumber = cms.int32(1),
                               )

process.jetCuts = cms.Sequence(process.oneJetAboveZero + process.getLargestJet + process.ptCut + process.etaCut)# + process.massCut)

# MET cut
# MET cut
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("pfMet"),
                              ptMin = cms.double(thiagoMETCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

process.differentPtCut = cms.EDFilter("PFJetConfigurableSelector",
                                      src = cms.InputTag("myCorrectedJets"),
                                      theCut = cms.string("(pt > "+str(thiagoSmallJetPtCut)+") && (abs(eta) < "+str(thiagoJetEtaCut)+")"),
                                      minNumber = cms.int32(1)                                       
                                      )

process.getHardJets = cms.EDFilter("LargestPtPFJetSelector",
                                   src = cms.InputTag("differentPtCut"),
                                   maxNumber = cms.uint32(9999)
                                   )
### Other cuts

# HCAL noise cut
process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')

# ECAL noise cut
process.load('RSGraviton/RSAnalyzer/RSEcalBEFilter_cfi')

# EMF cut
#process.EMFCut = cms.EDFilter("JetConfigurableSelector",
#                              src = cms.InputTag("getLargestJet"),
#                              theCut = cms.string("(emEnergyFraction > 0.1) && (emEnergyFraction < 0.9)"),
#                              minNumber = cms.int32(1)
#                              )

# TIV cut
process.TIVCut = cms.EDFilter("RSTrackerIndirectVetoFilter",
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
                              filter = cms.bool(True)
                              )

process.TIVStarCut = process.TIVCut.clone(excludeTracks = cms.bool(True))

# Multijets cut
process.multiJetCut = cms.EDFilter("RSEventNumJetsFilter",
                                  jets = cms.InputTag("getHardJets"),
                                  maxJets = cms.int32(thiagoMaxJets) # Comparison uses "less than"
                                  )

process.angularCut = cms.EDFilter("RSEventDeltaPhiFilter",
                                  jets = cms.InputTag("getHardJets"),
                                  maxValue = cms.double(thiagoMaxAngle)
                                  )

### Control region

# Muon control
process.leadingMuon = cms.EDFilter("LargestPtMuonSelector",
                                   src = cms.InputTag("muons"),
                                   maxNumber = cms.uint32(1)
                                   )

process.muonCut = cms.EDFilter("EtaPtMinCandViewSelector",
                               src = cms.InputTag("leadingMuon"),
                               ptMin = cms.double(20.0),
                               etaMin = cms.double(-2.1),
                               etaMax = cms.double(2.1),
                               minNumber = cms.uint32(1),
                               filter = cms.bool(True)
                               )

process.VBTFmuons = cms.EDFilter('RSMuonVBTFFilter',
                                 MuonTag = cms.untracked.InputTag("muons"),
                                 JetTag = cms.untracked.InputTag("ak7PFJets"),
                                 # Preselection!
                                 PtThrForZ1 = cms.untracked.double(20.0), # Cut is above
                                 PtThrForZ2 = cms.untracked.double(10.0), # Cut is above
                                 vetoSecondMuonEvents = cms.untracked.bool(False),
                                 EJetMin = cms.untracked.double(30.),
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

process.VBTFmuon = cms.Sequence(process.VBTFmuons + process.leadingMuon + process.muonCut)

# build W->MuNu candidates using MET
process.wmnCands = cms.EDProducer("CandViewShallowCloneCombiner",
                                    checkCharge = cms.bool(False),
                                    cut = cms.string(""),
                                    decay = cms.string("leadingMuon pfMet")
                                    )
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
                                 src = cms.InputTag("pfMet"),
                                 histograms = METhistos
                                 )

process.plotMETControl = process.plotMET.clone(src = cms.InputTag("wmnCands"))

process.plotJetsGeneral = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                         src = cms.InputTag("getHardJets"),
                                         histograms = basicjethistos
                                         )
process.plotJetsGeneralControl = process.plotJetsGeneral.clone()

#########
# PATHS #
#########
process.analysisSignalSequence = cms.Sequence(process.HBHENoiseFilter +
#                                              process.ecalAnomalousEventFilterSequence +
                                              process.jetIdCut +
                                              process.myCorrections +
                                              process.jetCuts +
                                              process.METCut +
#                                              process.EMFCut +
                                              process.TIVCut +
                                              process.differentPtCut +
                                              process.getHardJets +
                                              process.multiJetCut +
                                              process.angularCut
                                              )

process.analysisControlSequence = cms.Sequence(process.HBHENoiseFilter +
#                                               process.ecalAnomalousEventFilterSequence +
                                               process.VBTFmuon + 
                                               process.jetIdCut +
                                               process.myCorrections +
                                               process.jetCuts +
                                               process.muonMETCut +
#                                               process.EMFCut +
                                               process.TIVStarCut + 
                                               process.differentPtCut +
                                               process.getHardJets +
                                               process.multiJetCut +
                                               process.angularCut
                                               )

#process.pSignal = cms.Path(process.analysisSignalSequence + process.plotMET + process.plotJetsGeneral)
process.pControl = cms.Path(process.analysisControlSequence + process.plotMETControl + process.plotJetsGeneralControl)
#process.pTest = cms.Path(process.jetIdCut + process.myCorrectedJets + process.differentPtCut + process.getHardJets + process.plotJetsGeneral)
#process.pTest = cms.Path(process.VBTFmuon)


#process.preselectionOut = cms.OutputModule("PoolOutputModule",
                                           fileName = cms.untracked.string('data_selectedMuons.root'),
                                           outputCommands = process.RECOEventContent.outputCommands,
                                           dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO'),
                                                                        filterName = cms.untracked.string('MUONS')),
                                           SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('pTest')
                                                                             )
                                           )

#process.e = cms.EndPath(process.preselectionOut)


