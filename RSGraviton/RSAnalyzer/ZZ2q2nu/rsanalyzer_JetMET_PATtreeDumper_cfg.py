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
readFiles.extend(["file:condor_dataPattuples_2011Jun20_0/output.root",
                  "file:condor_dataPattuples_2011Jun20_1/output.root",
                  "file:condor_dataPattuples_2011Jun20_10/output.root",
                  "file:condor_dataPattuples_2011Jun20_2/output.root",
                  "file:condor_dataPattuples_2011Jun20_3/output.root",
                  "file:condor_dataPattuples_2011Jun20_4/output.root",
                  "file:condor_dataPattuples_2011Jun20_5/output.root",
                  "file:condor_dataPattuples_2011Jun20_6/output.root",
                  "file:condor_dataPattuples_2011Jun20_7/output.root",
                  "file:condor_dataPattuples_2011Jun20_8/output.root",
                  "file:condor_dataPattuples_2011Jun20_9/output.root",
                  ])                  

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
