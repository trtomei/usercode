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
    setupOutputFileName = myOptions[myOptions.index('input')+1]
else:
    setupOutputFileName = ''

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
readFiles.extend([
# "file:condor_dataPattuples_Run2011A_Jul06_0/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_1/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_10/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_11/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_2/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_3/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_4/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_5/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_6/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_7/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_8/output.root",
# "file:condor_dataPattuples_Run2011A_Jul06_9/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_0/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_1/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_2/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_3/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_4/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_5/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_6/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_7/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_8/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_0/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_1/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_2/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_3/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_4/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_5/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_6/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_7/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_8/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_0/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_1/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_10/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_2/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_3/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_4/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_5/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_6/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_7/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_8/output.root",
# "file:condor_dataPattuples_Run2011A_Jun20_9/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_0/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_1/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_2/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_3/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_4/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_5/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_6/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_7/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_8/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_0/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_1/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_10/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_11/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_12/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_13/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_14/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_15/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_16/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_17/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_18/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_19/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_2/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_20/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_21/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_22/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_3/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_4/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_5/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_6/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_7/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_8/output.root",
# "file:condor_dataPattuples_Run2011A_May10ReReco_9/output.root",
#"file:condor_MCPattuples_QCD_0/output.root",
#"file:condor_MCPattuples_QCD_1/output.root",
#"file:condor_MCPattuples_QCD_10/output.root",
#"file:condor_MCPattuples_QCD_11/output.root",
#"file:condor_MCPattuples_QCD_12/output.root",
#"file:condor_MCPattuples_QCD_13/output.root",
#"file:condor_MCPattuples_QCD_14/output.root",
#"file:condor_MCPattuples_QCD_2/output.root",
#"file:condor_MCPattuples_QCD_3/output.root",
#"file:condor_MCPattuples_QCD_4/output.root",
#"file:condor_MCPattuples_QCD_5/output.root",
#"file:condor_MCPattuples_QCD_6/output.root",
#"file:condor_MCPattuples_QCD_7/output.root",
#"file:condor_MCPattuples_QCD_8/output.root",
#"file:condor_MCPattuples_QCD_9/output.root",
   "file:condor_MCPattuples_Zinvisible_0/output.root",
   "file:condor_MCPattuples_Zinvisible_1/output.root",
   "file:condor_MCPattuples_Zinvisible_10/output.root",
   "file:condor_MCPattuples_Zinvisible_11/output.root",
   "file:condor_MCPattuples_Zinvisible_12/output.root",
   "file:condor_MCPattuples_Zinvisible_13/output.root",
   "file:condor_MCPattuples_Zinvisible_14/output.root",
   "file:condor_MCPattuples_Zinvisible_15/output.root",
   "file:condor_MCPattuples_Zinvisible_16/output.root",
   "file:condor_MCPattuples_Zinvisible_17/output.root",
   "file:condor_MCPattuples_Zinvisible_18/output.root",
   "file:condor_MCPattuples_Zinvisible_19/output.root",
   "file:condor_MCPattuples_Zinvisible_2/output.root",
   "file:condor_MCPattuples_Zinvisible_20/output.root",
   "file:condor_MCPattuples_Zinvisible_3/output.root",
   "file:condor_MCPattuples_Zinvisible_4/output.root",
   "file:condor_MCPattuples_Zinvisible_5/output.root",
   "file:condor_MCPattuples_Zinvisible_6/output.root",
   "file:condor_MCPattuples_Zinvisible_7/output.root",
   "file:condor_MCPattuples_Zinvisible_8/output.root",
   "file:condor_MCPattuples_Zinvisible_9/output.root",
#"file:condor_MCPattuples_WJets_0/output.root",
#"file:condor_MCPattuples_WJets_1/output.root",
#"file:condor_MCPattuples_WJets_10/output.root",
#"file:condor_MCPattuples_WJets_11/output.root",
#"file:condor_MCPattuples_WJets_12/output.root",
#"file:condor_MCPattuples_WJets_13/output.root",
#"file:condor_MCPattuples_WJets_14/output.root",
#"file:condor_MCPattuples_WJets_2/output.root",
#"file:condor_MCPattuples_WJets_3/output.root",
#"file:condor_MCPattuples_WJets_4/output.root",
#"file:condor_MCPattuples_WJets_5/output.root",
#"file:condor_MCPattuples_WJets_6/output.root",
#"file:condor_MCPattuples_WJets_7/output.root",
#"file:condor_MCPattuples_WJets_8/output.root",
#"file:condor_MCPattuples_WJets_9/output.root",
#"file:condor_MCPattuples_ttbar_0/output.root",
#"file:condor_MCPattuples_ttbar_1/output.root",
#"file:condor_MCPattuples_ttbar_2/output.root",
#"file:condor_MCPattuples_ttbar_3/output.root",
#"file:condor_MCPattuples_ttbar_4/output.root",
#"file:condor_MCPattuples_ttbar_5/output.root",
#"file:condor_MCPattuples_ttbar_6/output.root",
#"file:condor_MCPattuples_ttbar_7/output.root",
#"file:condor_MCPattuples_ttbar_8/output.root",
#"file:condor_MCPattuples_ttbar_9/output.root",
])    

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(setupNumEvents)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output_'+setupOutputFileName+setupSuffix+'.root')
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

##########
# Jet ID #
##########
# This selector selects PAT jets with loose jet ID thresholds.
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
process.jetIdCut = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                filterParams = pfJetIDSelector.clone(),
                                src = cms.InputTag("cleanPatJetsPFlow")
                                )
print process.jetIdCut.filterParams
process.jetIdCut.src = "patJetsCA8PrunedPF"
print process.jetIdCut.src

######################
# Jet Kinematic cuts #
######################

process.differentPtCut = cms.EDFilter("CandViewSelector",
                                      src = cms.InputTag("goodPatJetsPFlow"),
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

process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("patMETsPFlow"),
                                 histograms = METhistos
                                 )

process.plotJetsGeneral = cms.EDAnalyzer("RSJetAnalyzerV2",
                                         jets = cms.InputTag("goodPatJetsPFlow"),
                                         numberInCollection = cms.uint32(0)
                                         )

process.plotDeltaPhi = cms.EDAnalyzer("RSEventDeltaPhiAnalyzer",
                                      jets = cms.InputTag("goodPatJetsPFlow")
                                      )

process.plotNumJets = cms.EDAnalyzer("RSEventNumJetsAnalyzer",
                                     jets = cms.InputTag("goodPatJetsPFlow")
                                     )
#########
# PATHS #
#########
process.p = cms.Path(process.eventCounterOne + 
#                     process.jetIdCut + 
#                     process.differentPtCut +
#                     process.getHardJets +
                     process.plotMET +
                     process.plotJetsGeneral +
                     process.plotDeltaPhi +
                     process.plotNumJets 
                     )
