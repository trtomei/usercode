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
setupJetMassCut = 50.0
setupMETCut = 200.0
setupMaxJets = 3
setupMaxAngle = 2.8

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.EventContent.EventContent_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'MC_38Y_V14::All'    ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)

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
process.load("RSGraviton.RSAnalyzer.Fall10.RSToZZToNuNuJJ_"+setupFileName+"_cff")
#process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
#readFiles.extend(["file:tempEDMfile.root",])

process.MessageLogger.cerr.FwkReport.reportEvery = 100

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

# Configure PAT to use PF2PAT instead of AOD sources
# this function will modify the PAT sequences. It is currently 
# not possible to run PF2PAT+PAT and standard PAT at the same time
process.load("PhysicsTools.PatAlgos.patSequences_cff")
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('temp_pattuple.root'),
                               # save only events passing the full path
                               # save PAT Layer 1 output; you need a '*' to
                               # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *', *patEventContent )
                               )

from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.coreTools import *

postfix = "PFlow"
jetAlgo="AK7"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=True, postfix=postfix) 

# top projections in PF2PAT:
process.pfNoPileUpPFlow.enable = True 
process.pfNoMuonPFlow.enable = False 
process.pfNoElectronPFlow.enable = True 
process.pfNoTauPFlow.enable = True 
process.pfNoJetPFlow.enable = True 
process.pfNoMuon.verbose = True

### Preselection cuts
process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(24),
                                           maxd0 = cms.double(2)
                                           )

process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )

process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')

process.preselection = cms.Sequence(process.primaryVertexFilter + process.noscraping + process.HBHENoiseFilter)

process.cutOnJet = cms.EDFilter("CandViewSelector",
                                src = cms.InputTag("cleanPatJetsPFlow"),
                                cut = cms.string("(pt > 110.0) && (abs(eta) < 2.4)"),
                                minNumber = cms.int32(1),
                                filter = cms.bool(True)
                                )

############
# Cleaning #
############
# Standard PAT cleaning - clean muons, then electrons, then jet with deltaR = 0.3
process.load("RSGraviton.RSAnalyzer.patCleaning_cfi")

##########
# Jet ID #
##########
# This selector selects PAT jets with loose jet ID thresholds.
process.load("RSGraviton.RSAnalyzer.pfJetId_cfi")

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
                                      src = cms.InputTag("jetIdCut"),
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
                                    src = cms.InputTag("cleanPatElectronsPFlow"),
                                    cut = cms.string(""),
                                    filter = cms.bool(True)
                                    )
process.anyMuons = cms.EDFilter("PATMuonSelector",
                                src = cms.InputTag("cleanPatMuonsPFlow"),
                                cut = cms.string(""),
                                filter = cms.bool(True)
                                )
##################
# Control region #
##################
# Muon sequence - makes VBTF muons, then the leading muon.
process.load("RSGraviton.RSAnalyzer.muonSequence_cfi")

# TIV cut - veto on isolated tracks.
# Exempt the muon track!
process.TIVStarCut = process.TIVCut.clone(excludeTracks = cms.bool(True),tracksToExclude = cms.InputTag("leadingMuon"))

# build W->MuNu candidates using MET
process.wmnCands = cms.EDProducer("CandViewShallowCloneCombiner",
                                    checkCharge = cms.bool(False),
                                    cut = cms.string(""),
                                    decay = cms.string("leadingMuon patMETsPFlow")
                                    )
# mu+MET Cut
process.wmnCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("wmnCands"),
                              ptMin = cms.double(setupMETCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

process.muonMETCut = cms.Sequence(process.wmnCands + process.wmnCut)

#########
# PLOTS #
#########

#########
# PATHS #
#########
process.analysisSearchSequence = cms.Sequence(process.jetIdCut +
#                                              process.jetScaler +
                                              process.jetCuts +
                                              process.METCut +
                                              ~process.anyElectrons +
                                              ~process.anyMuons +
                                              process.TIVCut +
                                              process.differentPtCut +
                                              process.getHardJets +
                                              process.multiJetCut +
                                              process.angularCut + 
                                              process.jetMassCut
                                              )


process.pSearch = cms.Path(process.preselection + 
                           getattr(process,"patPF2PATSequence"+postfix) +
                           process.cleanPatCandidatesPFlow +
                           process.cutOnJet +
                           process.analysisSearchSequence)
