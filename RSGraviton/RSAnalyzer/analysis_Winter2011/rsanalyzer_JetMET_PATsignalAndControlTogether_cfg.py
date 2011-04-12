#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("ANALYSIS")

###########################
# Basic process controls. #
###########################

thiagoOutputFileName = ''
thiagoSuffix = ''
thiagoNumEvents =-1
thiagoInputFilesList = ''
thiagoJetPtCut = 300.0
thiagoSmallJetPtCut = 30.0
thiagoJetEtaCut = 2.4
thiagoJetMassCut = 50.0
thiagoMETCut = 200.0
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

# Other statements
myOptions = sys.argv
if 'input' in myOptions:
    thiagoOutputFileName = myOptions[myOptions.index('input')+1]
else:
    thiagoOutputFileName = ''

if 'suffix' in myOptions:
    thiagoSuffix = myOptions[myOptions.index('suffix')+1]
else:
    thiagoSuffix = ''

if 'numEvents' in myOptions:
    thiagoNumEvents = int(myOptions[myOptions.index('numEvents')+1])
else:
    thiagoNumEvents = -1
    

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend(['file:pattuple_'+thiagoOutputFileName+'.root',])
#readFiles.extend(['file:testPattuple.root',])
#process.load("RSGraviton.RSAnalyzer.Fall10."+thiagoOutputFileName+"_cff")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(thiagoNumEvents)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output_'+thiagoOutputFileName+'_Fall2010'+thiagoSuffix+'.root')
)

process.MessageLogger.cerr.FwkReport.reportEvery = 100

from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as basicjethistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos
from RSGraviton.RSAnalyzer.METhistos_cff import histograms as METhistos

##################
# The global tag #
##################
# Notneeded I think, already used in PAT
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = 'GR_R_39X_V5::All' # 3_9_X RECO
#process.GlobalTag.globaltag = 'GR_R_38X_V15::All ' # 3_8_X RECO

### COunting - important
process.eventCounterOne = cms.EDAnalyzer("EventCounter")
process.eventCounterTwo = process.eventCounterOne.clone()
process.eventCounterThree = process.eventCounterOne.clone()
process.eventCounterFour = process.eventCounterOne.clone()
process.eventCounterFive = process.eventCounterOne.clone()
process.eventCounterSix = process.eventCounterOne.clone()
process.eventCounterSeven = process.eventCounterOne.clone()
process.eventCounterEight = process.eventCounterOne.clone()
process.eventCounterNine = process.eventCounterOne.clone()
process.eventCounterAlpha = process.eventCounterOne.clone()
process.eventCounterBeta = process.eventCounterOne.clone()
process.eventCounterGamma = process.eventCounterOne.clone()
process.eventCounterDelta = process.eventCounterOne.clone()
process.eventCounterEpsilon = process.eventCounterOne.clone()
process.eventCounterZeta = process.eventCounterOne.clone()
process.eventCounterEta = process.eventCounterOne.clone()
process.eventCounterTheta = process.eventCounterOne.clone()
process.eventCounterIota = process.eventCounterOne.clone()


### Cleaning
process.cleanPatMuonsPFlow = cms.EDProducer("PATMuonCleaner",
                                            src = cms.InputTag("selectedPatMuonsPFlow"),
                                            # preselection (any string-based cut for pat::Muon)
                                            preselection = cms.string(''),
                                            # overlap checking configurables
                                            checkOverlaps = cms.PSet(),
                                            # finalCut (any string-based cut for pat::Muon)
                                            finalCut = cms.string(''),
                                            )

process.cleanPatElectronsPFlow = cms.EDProducer("PATElectronCleaner",
                                                src = cms.InputTag("selectedPatElectronsPFlow"),
                                                # preselection (any string-based cut on pat::Electrons)
                                                preselection = cms.string(''),
                                                # overlap checking configurables
                                                checkOverlaps = cms.PSet(muons = cms.PSet(src       = cms.InputTag("cleanPatMuonsPFlow"),
                                                                                          algorithm = cms.string("byDeltaR"),
                                                                                          preselection        = cms.string(""),
                                                                                          deltaR              = cms.double(0.3),
                                                                                          checkRecoComponents = cms.bool(False),
                                                                                          pairCut             = cms.string(""),
                                                                                          requireNoOverlaps   = cms.bool(False),
                                                                                          )
                                                                         ),
                                                # finalCut (any string-based cut for pat::Electron)
                                                finalCut = cms.string(''),
                                                )

process.cleanPatJetsPFlow = cms.EDProducer("PATJetCleaner",
                                           src = cms.InputTag("selectedPatJetsPFlow"),
                                           # preselection (any string-based cut on pat::Jet)
                                           preselection = cms.string(''),
                                           # overlap checking configurables
                                           checkOverlaps = cms.PSet(muons = cms.PSet(src       = cms.InputTag("cleanPatMuonsPFlow"),
                                                                                     algorithm = cms.string("byDeltaR"),
                                                                                     preselection        = cms.string(""),
                                                                                     deltaR              = cms.double(0.3),
                                                                                     checkRecoComponents = cms.bool(False),
                                                                                     pairCut             = cms.string(""),
                                                                                     requireNoOverlaps   = cms.bool(False),
                                                                                     ),
                                                                    electrons = cms.PSet(src       = cms.InputTag("cleanPatElectronsPFlow"),
                                                                                         algorithm = cms.string("byDeltaR"),
                                                                                         preselection        = cms.string(""),
                                                                                         deltaR              = cms.double(0.3),
                                                                                         checkRecoComponents = cms.bool(False),
                                                                                         pairCut             = cms.string(""),
                                                                                         requireNoOverlaps   = cms.bool(False),
                                                                                         ),
                                                                    ),
                                           finalCut = cms.string('')
                                           )
# One module to count objects
process.cleanPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
                                                  logName = cms.untracked.string("cleanPatCandidates|PATSummaryTables"),
                                                  candidates = cms.VInputTag(cms.InputTag("cleanPatElectronsPFlow"),
                                                                             cms.InputTag("cleanPatMuonsPFlow"),
                                                                             cms.InputTag("cleanPatJetsPFlow"),
                                                                             )
                                                  )


process.cleanPatCandidatesPFlow = cms.Sequence(
            process.cleanPatMuonsPFlow     *        # NOW WE MUST USE '*' AS THE ORDER MATTERS
            process.cleanPatElectronsPFlow *
            process.cleanPatJetsPFlow     *
            process.cleanPatCandidateSummary
            )

##########
# Jet ID #
##########
# This will filter out events where any jet above 30 GeV fails the Jet ID cut.
# Default is loose cut, use tightQuality if you want tight cut.
process.jetIdCut = cms.EDFilter("PATJetSelector",
                                src = cms.InputTag("cleanPatJetsPFlow"),
                                cut = cms.string("(neutralHadronEnergyFraction < 0.99) &&"+
                                                 "(neutralEmEnergyFraction < 0.99) &&"+
                                                 "(numberOfDaughters > 1) &&"+
                                                 "(chargedHadronEnergyFraction > 0) &&"+
                                                 "(chargedMultiplicity > 0) &&"+
                                                 "(chargedEmEnergyFraction < 0.99)"
                                                 )
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

### For Path 1 - FAT jet from Z + MET
process.oneJetAboveZero = cms.EDFilter("CandViewSelector",
                                       src = cms.InputTag("jetIdCut"),
                                       cut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1),                                       
                                       filter = cms.bool(True)
                                       )

process.getLargestJet = cms.EDFilter("LargestPtCandViewSelector",
                                     src = cms.InputTag("oneJetAboveZero"),
                                     maxNumber = cms.uint32(1)
                                     )

# Jet pt, eta cut
process.ptCut = cms.EDFilter("CandViewSelector",
                             src = cms.InputTag("getLargestJet"),
                             cut = cms.string("pt > "+str(thiagoJetPtCut)),
                             minNumber = cms.int32(1),
                             filter = cms.bool(True)
                             )

process.etaCut = cms.EDFilter("CandViewSelector",
                              src = cms.InputTag("getLargestJet"),
                              cut = cms.string("abs(eta) < "+str(thiagoJetEtaCut)),
                              minNumber = cms.int32(1),
                              filter = cms.bool(True)
                              )

# Jet mass cut
process.massCut = cms.EDFilter("CandViewSelector",
                               src = cms.InputTag("getLargestJet"),
                               cut = cms.string("mass > "+str(thiagoJetMassCut)),
                               minNumber = cms.int32(1),
                               filter = cms.bool(True)
                               )

process.jetCuts = cms.Sequence(process.oneJetAboveZero + process.getLargestJet + process.ptCut + process.etaCut)
process.jetMassCut = cms.Sequence(process.massCut)

# MET cut
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("patMETsPFlow"),
                              ptMin = cms.double(thiagoMETCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

process.differentPtCut = cms.EDFilter("CandViewSelector",
                                      src = cms.InputTag("jetIdCut"),
                                      cut = cms.string("(pt > "+str(thiagoSmallJetPtCut)+") && (abs(eta) < "+str(thiagoJetEtaCut)+")"),
                                      minNumber = cms.int32(1),
                                      filter = cms.bool(True)
                                      )

process.getHardJets = cms.EDFilter("LargestPtCandViewSelector",
                                   src = cms.InputTag("differentPtCut"),
                                   maxNumber = cms.uint32(9999)
                                   )
# EMF cut
#process.EMFCut = cms.EDFilter("JetConfigurableSelector",
#                              src = cms.InputTag("getLargestJet"),
#                              theCut = cms.string("(emEnergyFraction > 0.1) && (emEnergyFraction < 0.9)"),
#                              minNumber = cms.int32(1)
#                              )

# TIV cut
process.TIVCut = cms.EDFilter("RSPATTrackerIndirectVetoFilter",
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

process.anyElectrons = cms.EDFilter("PATElectronSelector",
                                    src = cms.InputTag("cleanPatElectronsPFlow"),
                                    cut = cms.string(""),
                                    filter = cms.bool(True)
                                    )
process.anyMuons = cms.EDFilter("PATMuonSelector",
                                src = cms.InputTag("cleanPatMuonsPFlow"),
                                cut = cms.string(""),
                                filter = cms.bool(True)
                                )
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
process.VBTFmuons = cms.EDFilter("PATMuonSelector",
                                 src = cms.InputTag("selectedPatMuonsPFlow"),
                                 cut = cms.string("numberOfMatches > 1 &&  muonID('GlobalMuonPromptTight') && abs(dB) < 0.2 && "+
                                                  "track.numberOfValidHits > 10 && track.hitPattern.numberOfValidPixelHits > 0 && "+
                                                  "(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt < 0.15"),
                                 )

process.leadingMuon = cms.EDFilter("LargestPtCandViewSelector",
                                   src = cms.InputTag("VBTFmuons"),
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


process.muonSequence = cms.Sequence(process.VBTFmuons + process.leadingMuon)

# build W->MuNu candidates using MET
process.wmnCands = cms.EDProducer("CandViewShallowCloneCombiner",
                                    checkCharge = cms.bool(False),
                                    cut = cms.string(""),
                                    decay = cms.string("leadingMuon patMETsPFlow")
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
                                 src = cms.InputTag("patMETsPFlow"),
                                 histograms = METhistos
                                 )

process.plotMETControl = process.plotMET.clone(src = cms.InputTag("wmnCands"))
process.plotMETPreselection = process.plotMET.clone()
process.plotMETAfterMassCut = process.plotMET.clone()
process.plotMETControlAfterMassCut = process.plotMETControl.clone()

process.plotJetsGeneral = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                         src = cms.InputTag("getHardJets"),
                                         histograms = basicjethistos
                                         )
process.plotJetsGeneralControl = process.plotJetsGeneral.clone()
process.plotJetsGeneralPreselection = process.plotJetsGeneral.clone()
process.plotJetsGeneralAfterMassCut = process.plotJetsGeneral.clone()
process.plotJetsGeneralControlAfterMassCut = process.plotJetsGeneral.clone()

process.WtransverseMass = cms.EDAnalyzer("TransverseMassAnalyzer",
                                         objectOne = cms.InputTag("patMETsPFlow"),
                                         objectTwo = cms.InputTag("leadingMuon"),
                                         xmin = cms.double(0.0),
                                         xmax = cms.double(200.0),
                                         nbins = cms.int32(20)
                                         )

process.gravtransverseMass = cms.EDAnalyzer("TransverseMassAnalyzer",
                                            objectOne = cms.InputTag("patMETsPFlow"),
                                            objectTwo = cms.InputTag("getLargestJet"),
                                            xmin = cms.double(0.0),
                                            xmax = cms.double(2000.0),
                                            nbins = cms.int32(200)
                                            )

process.gravtransverseMassControl = cms.EDAnalyzer("TransverseMassAnalyzer",
                                                   objectOne = cms.InputTag("wmnCands"),
                                                   objectTwo = cms.InputTag("getLargestJet"),
                                                   xmin = cms.double(0.0),
                                                   xmax = cms.double(2000.0),
                                                   nbins = cms.int32(200)
                                                   )

process.WtransverseMassAfterMassCut = process.WtransverseMass.clone()
process.gravtransverseMassAfterMassCut = process.gravtransverseMass.clone()
process.gravtransverseMassControlAfterMassCut = process.gravtransverseMassControl.clone()

#########
# PATHS #
#########
process.analysisSearchSequence = cms.Sequence(process.eventCounterOne + 
                                              process.cleanPatCandidatesPFlow +
                                              process.muonSequence +
                                              process.jetIdCut +
                                              process.jetCuts +
                                              process.eventCounterTwo + 
                                              process.METCut +
                                              process.eventCounterThree + 
                                              ~process.anyElectrons +
                                              ~process.anyMuons +
                                              process.eventCounterFour + 
                                              process.TIVCut +
                                              process.eventCounterFive + 
                                              process.differentPtCut +
                                              process.getHardJets +
                                              process.eventCounterSix + 
                                              process.multiJetCut +
                                              process.eventCounterSeven + 
                                              process.angularCut + 
                                              process.eventCounterEight +
                                              process.gravtransverseMass +
                                              process.plotJetsGeneral +
                                              process.plotMET +
                                              process.jetMassCut +
                                              process.gravtransverseMassAfterMassCut +
                                              process.eventCounterNine)

process.analysisControlSequence = cms.Sequence(process.eventCounterAlpha +
                                               process.cleanPatCandidatesPFlow +
                                               process.muonSequence +
                                               process.muonCut + 
                                               process.eventCounterBeta + 
                                               process.jetIdCut +
                                               process.jetCuts +
                                               process.eventCounterGamma + 
                                               process.muonMETCut +
                                               process.eventCounterDelta + 
                                               process.TIVStarCut +
                                               process.eventCounterEpsilon + 
                                               process.differentPtCut +
                                               process.getHardJets +
                                               process.eventCounterZeta + 
                                               process.multiJetCut +
                                               process.eventCounterEta + 
                                               process.angularCut +
                                               process.eventCounterTheta +
                                               process.WtransverseMass + 
                                               process.gravtransverseMassControl +
                                               process.plotJetsGeneralControl +
                                               process.plotMETControl + 
                                               process.jetMassCut +
                                               process.WtransverseMassAfterMassCut +
                                               process.gravtransverseMassControlAfterMassCut + 
                                               process.eventCounterIota)

process.pSearch = cms.Path(process.analysisSearchSequence + process.plotMETAfterMassCut + process.plotJetsGeneralAfterMassCut)
process.pControl = cms.Path(process.analysisControlSequence + process.plotMETControlAfterMassCut + process.plotJetsGeneralControlAfterMassCut)
