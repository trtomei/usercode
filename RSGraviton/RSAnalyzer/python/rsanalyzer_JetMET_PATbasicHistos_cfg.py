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
thiagoJetPtCut = 150.0
thiagoSmallJetPtCut = 30.0
thiagoJetEtaCut = 2.4
thiagoJetMassCut = 50.0
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
#readFiles.extend(['file:pattuple_'+thiagoOutputFileName+'.root',])
readFiles.extend(['file:patTuple_Run2010B.root',])
#readFiles.extend(['file:Run2010Bp1/preselection_Run2010Bp1.root',])
#readFiles.extend(['file:Run2010Bp2/preselection_Run2010Bp2.root',])
#readFiles.extend(['file:Run2010Bp2_oldReco.root',])
#readFiles.extend(['file:signal_M1250.root',])
#readFiles.extend(['file:/home/trtomei/hdacs/CMSSW_3_9_9/src/RSGraviton/RSAnalyzer/analysis_Winter2011/manualGo/patTuple_'+thiagoOutputFileName+'.root'])
#process.load("RSGraviton.RSAnalyzer.Fall10.ZinvisibleJets_cff")
#process.load("RSGraviton.RSAnalyzer.Fall10."+thiagoOutputFileName+"_cff")

#process.load(thiagoInputFilesList)
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
# Kinematic cuts #
##################
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
#########
# PLOTS #
#########

process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("patMETsPFlow"),
                                 histograms = METhistos
                                 )

process.plotMETControl = process.plotMET.clone(src = cms.InputTag("wmnCands"))

process.plotJetsGeneral = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                         src = cms.InputTag("getHardJets"),
                                         histograms = basicjethistos
                                         )
process.plotJetsGeneralControl = process.plotJetsGeneral.clone()

process.plotDeltaPhi = cms.EDAnalyzer("RSEventDeltaPhiAnalyzer",
                                      jets = cms.InputTag("getHardJets")
                                      )

process.plotNumJets = cms.EDAnalyzer("RSEventNumJetsAnalyzer",
                                     jets = cms.InputTag("getHardJets")
                                     )
#########
# PATHS #
#########
process.p = cms.Path(process.eventCounterOne + 
                     process.cleanPatCandidatesPFlow +
                     process.jetIdCut + 
                     process.differentPtCut +
                     process.getHardJets +
                     process.plotMET +
                     process.plotJetsGeneral +
                     process.plotDeltaPhi +
                     process.plotNumJets 
                     )
