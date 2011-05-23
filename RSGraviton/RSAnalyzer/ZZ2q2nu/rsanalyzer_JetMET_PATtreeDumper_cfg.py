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
process.load('Configuration.EventContent.EventContent_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')

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
    
cms.tracer = cms.Service("Tracer")

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
#readFiles.extend(['file:pattuple_'+setupFileName+'.root',])
readFiles.extend(["file:/home/trtomei/hdacs/CMSSW_3_9_9/src/RSGraviton/RSAnalyzer/analysis_Winter2011/pattuple_"+setupFileName+".root",])
#setupFileName='VVJets'
#process.load("RSGraviton.RSAnalyzer.Fall10."+setupFileName+"_cff")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(setupNumEvents)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output_'+setupFileName+'_'+setupSuffix+'.root')
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

# Counting - important
# Gives 18 histograms - One to nine, alpha to iota
# that can be used to count how many events remain
# at each step of the analysis
process.load("RSGraviton.RSAnalyzer.eventCounters_cfi")

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

#######
# TIV #
#######
process.load("RSGraviton.RSAnalyzer.trackerIndirectVeto_cfi")
process.TIVCut.filter = False
process.TIVStarCut = process.TIVCut.clone(excludeTracks = cms.bool(True),tracksToExclude = cms.InputTag("leadingMuon"))

#########
# Muons #
#########
process.load("RSGraviton.RSAnalyzer.muonSequence_cfi")

######################
# Jet Kinematic cuts #
######################

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
#########
# TREES #
#########

process.treeDumper = cms.EDAnalyzer("ZZ2q2nuTreeMaker",
                                    jets = cms.InputTag("getHardJets"),
                                    met = cms.InputTag("patMETsPFlow"),
                                    electrons = cms.InputTag("cleanPatElectronsPFlow"),
                                    muons = cms.InputTag("cleanPatMuonsPFlow"),
                                    genParticles = cms.InputTag("hardGenParticles"),
                                    VBTFmuon = cms.InputTag("VBTFmuons"),
                                    TIV = cms.InputTag("TIVCut"),
                                    TIVStar = cms.InputTag("TIVStarCut"),
                                    isData = cms.bool(False),
                                    weight = cms.double(1.0)
                                    )
#########
# PATHS #
#########
process.p = cms.Path(process.cleanPatCandidatesPFlow +
                     process.jetIdCut + 
                     process.differentPtCut +
                     process.getHardJets +
                     process.muonSequence + 
                     process.TIVCut +
                     process.TIVStarCut +
                     process.treeDumper
                     )
