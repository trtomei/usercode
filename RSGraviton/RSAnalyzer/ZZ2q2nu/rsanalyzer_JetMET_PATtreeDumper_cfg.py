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
    

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
#readFiles.extend(['file:pattuple_'+setupFileName+'.root',])
#readFiles.extend(["file:/home/trtomei/hdacs/CMSSW_3_9_9/src/GeneratorInterface/AlpgenInterface/test/pattuple_"+setupFileName+".root",])
#readFiles.extend(["file:/home/trtomei/hdacs/CMSSW_3_9_9/src/RSGraviton/RSAnalyzer/analysis_Winter2011/pattuple_"+setupFileName+".root",])
readFiles.extend(["file:condor_dataPattuples_2011May10ReReco_0/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_1/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_10/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_11/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_12/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_2/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_3/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_4/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_5/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_6/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_7/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_8/output.root",
                  "file:condor_dataPattuples_2011May10ReReco_9/output.root",
                  ])                  
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

##########
# Jet ID #
##########
# This selector selects PAT jets with loose jet ID thresholds.
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
process.jetIdCut = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                filterParams = pfJetIDSelector.clone(),
                                src = cms.InputTag("cleanPatJetsPFlow")
                                )

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
process.VBTFmuons.src = "cleanPatMuonsPFlow"

######################
# Jet Kinematic cuts #
######################

process.differentPtCut = cms.EDFilter("CandViewSelector",
                                      src = cms.InputTag("jetIdCut"),
                                      cut = cms.string("(pt > "+str(setupSmallJetPtCut)+") && (abs(eta) < "+str(setupJetEtaCut)+")"),
                                      minNumber = cms.int32(1),
                                      filter = cms.bool(False)
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
                                    isData = cms.bool(True),
                                    weight = cms.double(1.0)
                                    )
#########
# PATHS #
#########
process.p = cms.Path(process.jetIdCut + 
                     process.differentPtCut +
                     process.getHardJets +
                     process.muonSequence + 
                     process.TIVCut +
                     process.TIVStarCut +
                     process.treeDumper
                     )
