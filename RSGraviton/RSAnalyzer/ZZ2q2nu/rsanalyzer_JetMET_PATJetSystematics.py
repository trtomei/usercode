#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("ANALYSIS")

###########################
# Basic process controls. #
###########################

setupFileName = ''
setupSuffix = ''
setupNumEvents =-1
setupInputFilesList = ''
setupJetPtCut = 300.0
setupSmallJetPtCut = 30.0
setupJetEtaCut = 2.4
setupJetMassCut = 70.0
setupMETCut = 300.0
setupMaxJets = 3
setupMaxAngle = 2.8

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.EventContent.EventContent_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# Other statements
myOptions = sys.argv
if 'input' in myOptions:
    setupFileName = myOptions[myOptions.index('input')+1]
else:
    setupFileName = ''

if 'suffix' in myOptions:
    setupSuffix = myOptions[myOptions.index('suffix')+1]
else:
    setupSuffix = ''

if 'numEvents' in myOptions:
    setupNumEvents = int(myOptions[myOptions.index('numEvents')+1])
else:
    setupNumEvents = -1
    
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend(["file:pattuple_signalm1750_PU.root"]);
 
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(setupNumEvents)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output_'+setupFileName+setupSuffix+'.root')
)

process.MessageLogger.cerr.FwkReport.reportEvery = 100

from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as basicjethistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos
from RSGraviton.RSAnalyzer.METhistos_cff import histograms as METhistos

##################
# The global tag #
##################
# Not needed I think, already used in PAT
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = 'GR_R_39X_V5::All' # 3_9_X RECO
#process.GlobalTag.globaltag = 'GR_R_38X_V15::All ' # 3_8_X RECO

# Counting - important
# Gives 18 histograms - One to nine, alpha to iota
# that can be used to count how many events remain
# at each step of the analysis
process.load("RSGraviton.RSAnalyzer.eventCounters_cfi")

##########
# Jet ID #
##########
# This selector selects PAT jets with loose jet ID thresholds.
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
process.jetIdCut = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                filterParams = pfJetIDSelector.clone(),
                                src = cms.InputTag("goodPatJetsPFlow")
                                )

######################
# Jet Kinematic cuts #
######################

process.jetScaler = cms.EDProducer("RSDistortedJetsProducer",
                                   src = cms.InputTag("jetIdCut"),
                                   calibrationChanges = cms.double(0.015),
                                   ePU = cms.double(0.75),
                                   JA = cms.double(1.6),
                                   AvgPu = cms.double(2.2),
                                   Constant = cms.double(1.0),
                                   upScale = cms.bool(True)
                                   )

### For Path 1 - FAT jet from Z + MET
process.oneJetAboveZero = cms.EDFilter("CandViewSelector",
                                       src = cms.InputTag("jetScaler"),
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
                             cut = cms.string("pt > "+str(setupJetPtCut)),
                             minNumber = cms.int32(1),
                             filter = cms.bool(True)
                             )

process.etaCut = cms.EDFilter("CandViewSelector",
                              src = cms.InputTag("getLargestJet"),
                              cut = cms.string("abs(eta) < "+str(setupJetEtaCut)),
                              minNumber = cms.int32(1),
                              filter = cms.bool(True)
                              )

# Jet mass cut (separated, but together)
process.massCut = cms.EDFilter("CandViewSelector",
                               src = cms.InputTag("getLargestJet"),
                               cut = cms.string("mass > "+str(setupJetMassCut)),
                               minNumber = cms.int32(1),
                               filter = cms.bool(True)
                               )

process.jetCuts = cms.Sequence(process.oneJetAboveZero + process.getLargestJet + process.ptCut + process.etaCut)
process.jetMassCut = cms.Sequence(process.massCut)

# Multijets 
process.differentPtCut = cms.EDFilter("CandViewSelector",
                                      src = cms.InputTag("jetScaler"),
                                      cut = cms.string("(pt > "+str(setupSmallJetPtCut)+") && (abs(eta) < "+str(setupJetEtaCut)+")"),
                                      minNumber = cms.int32(1),
                                      filter = cms.bool(True)
                                      )

process.getHardJets = cms.EDFilter("LargestPtCandViewSelector",
                                   src = cms.InputTag("differentPtCut"),
                                   maxNumber = cms.uint32(9999)
                                   )

process.multiJetCut = cms.EDFilter("RSEventNumJetsFilter",
                                   jets = cms.InputTag("getHardJets"),
                                   maxJets = cms.int32(setupMaxJets) # Comparison uses "less than"
                                   )

process.angularCut = cms.EDFilter("RSEventDeltaPhiFilter",
                                  jets = cms.InputTag("getHardJets"),
                                  maxValue = cms.double(setupMaxAngle)
                                  )

#################
# Search Region #
#################
# MET cut
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("patMETsPFlow"),
                              ptMin = cms.double(setupMETCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

# TIV cut - veto on isolated tracks.
process.load("RSGraviton.RSAnalyzer.trackerIndirectVeto_cfi")

# Cuts on the presence of leptons - to have inverted results in the Path.
process.anyElectrons = cms.EDFilter("PATElectronSelector",
                                    src = cms.InputTag("selectedPatElectronsPFlow"),
                                    cut = cms.string(""),
                                    filter = cms.bool(True)
                                    )
process.anyMuons = cms.EDFilter("PATMuonSelector",
                                src = cms.InputTag("selectedPatMuonsPFlow"),
                                cut = cms.string(""),
                                filter = cms.bool(True)
                                )

#########
# PLOTS #
#########
process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("patMETsPFlow"),
                                 histograms = METhistos
                                 )

process.plotMETPreselection = process.plotMET.clone()
process.plotMETAfterMassCut = process.plotMET.clone()

process.plotJetsGeneral = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                         src = cms.InputTag("getHardJets"),
                                         histograms = basicjethistos
                                         )
process.plotJetsGeneralPreselection = process.plotJetsGeneral.clone()
process.plotJetsGeneralAfterMassCut = process.plotJetsGeneral.clone()

process.gravtransverseMass = cms.EDAnalyzer("TransverseMassAnalyzer",
                                            objectOne = cms.InputTag("patMETsPFlow"),
                                            objectTwo = cms.InputTag("getLargestJet"),
                                            xmin = cms.double(0.0),
                                            xmax = cms.double(2000.0),
                                            nbins = cms.int32(200)
                                            )
process.gravtransverseMassAfterMassCut = process.gravtransverseMass.clone()

#########
# PATHS #
#########
process.analysisSearchSequence = cms.Sequence(process.eventCounterOne + 
                                              process.jetIdCut +
                                              process.jetScaler + 
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

process.pSearch = cms.Path(process.analysisSearchSequence + process.plotMETAfterMassCut + process.plotJetsGeneralAfterMassCut)
