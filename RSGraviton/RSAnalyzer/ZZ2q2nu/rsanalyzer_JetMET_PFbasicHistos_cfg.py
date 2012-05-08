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
setupJetPtCut = 0.0
setupSmallJetPtCut = 30.0
setupJetEtaCut = 2.4
setupJetMassCut = 0.0
setupMETCut = 0.0
setupMaxJets = 9999
setupMaxAngle = 9999.9

##################
# Basic services #
##################
# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')

readFiles = cms.untracked.vstring('/store/data/Run2011A/DoubleMu/AOD/May10ReReco-v1/0000/0018F4B5-F37B-E011-9EF8-00261894397E.root')
secFiles = cms.untracked.vstring()

process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
process.load("RSGraviton.RSAnalyzer.Summer11.signal_RSG1500_ZZ2q2nu_cff")

import PhysicsTools.PythonAnalysis.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(setupNumEvents)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output.root')
)

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

from RSGraviton.RSAnalyzer.PFjethistos_cff import histograms as PFjethistos
from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as basicjethistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos
from RSGraviton.RSAnalyzer.METhistos_cff import histograms as METhistos

##################
# The global tag #
##################

# Counting - important
# Gives 18 histograms - One to nine, alpha to iota
# that can be used to count how many events remain
# at each step of the analysis
process.load("RSGraviton.RSAnalyzer.eventCounters_cfi")

######################
# Jet Kinematic cuts #
######################
process.goodJetsPFlow = cms.EDFilter("CandViewSelector",
                                     src = cms.InputTag("ak7PFJets"),
                                     cut = cms.string("(abs(eta) < 2.4) &&"+
                                                      "(chargedHadronEnergyFraction > 0) &&"+
                                                      "(chargedEmEnergyFraction < 0.99) &&"+
                                                      "(((neutralHadronEnergy + HFHadronEnergy)/energy) < 0.99) &&"+
                                                      "(neutralEmEnergyFraction < 0.99) &&"+
                                                      "(chargedMultiplicity > 0) &&"+
                                                      "(numberOfDaughters > 1)"
                                                      ),
                                     minNumber = cms.int32(1),
                                     filter = cms.bool(True)
                                     )

process.differentPtCut = cms.EDFilter("CandViewSelector",
                                      src = cms.InputTag("goodJetsPFlow"),
                                      cut = cms.string("(pt > "+str(setupSmallJetPtCut)+") && (abs(eta) < "+str(setupJetEtaCut)+")"),
                                      minNumber = cms.int32(1),
                                      filter = cms.bool(False)
                                      )

process.getHardJets = cms.EDFilter("LargestPtCandViewSelector",
                                   src = cms.InputTag("differentPtCut"),
                                   maxNumber = cms.uint32(9999)
                                   )
#########
# PLOTS #
#########

process.pileupReweighter= cms.EDFilter("RSPileupReweighter",
                                       generatedFile = cms.string("PUMC_dist.root"),
                                       dataFile = cms.string("PUData_dist.root"),
                                       genHistName = cms.string("pileup"),
                                       dataHistName = cms.string("pileup"),
                                       useROOThistos = cms.bool(True)
                                       )

process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("pfMet"),
                                 histograms = METhistos
                                 )

process.plotJetsGeneral = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                         src = cms.InputTag("getHardJets"),
                                         histograms = basicjethistos
                                         )

process.plotDeltaPhi = cms.EDAnalyzer("RSEventDeltaPhiAnalyzer",
                                      jets = cms.InputTag("getHardJets")
                                      )

process.plotNumJets = cms.EDAnalyzer("RSEventNumJetsAnalyzer",
                                     jets = cms.InputTag("getHardJets")
                                     )

process.gravTransMass = cms.EDAnalyzer("TransverseMassAnalyzer",
                                       objectOne = cms.InputTag("pfMet"),
                                       objectTwo = cms.InputTag("getHardJets"),
                                       xmin = cms.double(0.0),
                                       xmax = cms.double(2000.0),
                                       nbins = cms.int32(200)
                                       )

#########
# PATHS #
#########
process.p = cms.Path(process.eventCounterOne + 
                     process.goodJetsPFlow + 
                     process.differentPtCut +
                     process.getHardJets +
                     process.plotMET +
                     process.plotJetsGeneral +
                     process.plotDeltaPhi +
                     process.plotNumJets +
                     process.gravTransMass
                     )
