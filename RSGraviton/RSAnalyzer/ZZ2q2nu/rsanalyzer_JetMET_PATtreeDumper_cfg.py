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
#readFiles.extend(["file:"+setupFileName
#                  ])                  
readFiles.extend([
"file:condor_dataPattuples_Run2011A_PromptRecoSet30_0/output.root",
"file:condor_dataPattuples_Run2011A_PromptRecoSet30_1/output.root",
"file:condor_dataPattuples_Run2011A_PromptRecoSet30_2/output.root",
"file:condor_dataPattuples_Run2011A_PromptRecoSet30_3/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_0/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_1/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_2/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_3/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_4/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_5/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_6/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_7/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_8/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_9/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_10/output.root",
#"file:condor_dataPattuples_Run2011A_ReRecoAug5_11/output.root",
# "file:condor_MCPattuples_WJetspt100_0/output.root",
# "file:condor_MCPattuples_WJetspt100_1/output.root",
# "file:condor_MCPattuples_WJetspt100_10/output.root",
# "file:condor_MCPattuples_WJetspt100_11/output.root",
# "file:condor_MCPattuples_WJetspt100_12/output.root",
# "file:condor_MCPattuples_WJetspt100_13/output.root",
# "file:condor_MCPattuples_WJetspt100_14/output.root",
# "file:condor_MCPattuples_WJetspt100_15/output.root",
# "file:condor_MCPattuples_WJetspt100_16/output.root",
# "file:condor_MCPattuples_WJetspt100_17/output.root",
# "file:condor_MCPattuples_WJetspt100_18/output.root",
# "file:condor_MCPattuples_WJetspt100_19/output.root",
# "file:condor_MCPattuples_WJetspt100_2/output.root",
# "file:condor_MCPattuples_WJetspt100_20/output.root",
# "file:condor_MCPattuples_WJetspt100_21/output.root",
# "file:condor_MCPattuples_WJetspt100_22/output.root",
# "file:condor_MCPattuples_WJetspt100_23/output.root",
# "file:condor_MCPattuples_WJetspt100_24/output.root",
# "file:condor_MCPattuples_WJetspt100_25/output.root",
# "file:condor_MCPattuples_WJetspt100_26/output.root",
# "file:condor_MCPattuples_WJetspt100_27/output.root",
# "file:condor_MCPattuples_WJetspt100_28/output.root",
# "file:condor_MCPattuples_WJetspt100_29/output.root",
# "file:condor_MCPattuples_WJetspt100_3/output.root",
# "file:condor_MCPattuples_WJetspt100_30/output.root",
# "file:condor_MCPattuples_WJetspt100_31/output.root",
# "file:condor_MCPattuples_WJetspt100_32/output.root",
# "file:condor_MCPattuples_WJetspt100_33/output.root",
# "file:condor_MCPattuples_WJetspt100_34/output.root",
# "file:condor_MCPattuples_WJetspt100_35/output.root",
# "file:condor_MCPattuples_WJetspt100_36/output.root",
# "file:condor_MCPattuples_WJetspt100_37/output.root",
# "file:condor_MCPattuples_WJetspt100_38/output.root",
# "file:condor_MCPattuples_WJetspt100_4/output.root",
# "file:condor_MCPattuples_WJetspt100_5/output.root",
# "file:condor_MCPattuples_WJetspt100_6/output.root",
# "file:condor_MCPattuples_WJetspt100_7/output.root",
# "file:condor_MCPattuples_WJetspt100_8/output.root",
# "file:condor_MCPattuples_WJetspt100_9/output.root"
#"file:condor_MCPattuples_Zinvisible100to200_0/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_1/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_10/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_11/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_12/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_13/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_14/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_15/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_16/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_17/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_18/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_2/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_3/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_4/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_5/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_6/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_7/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_8/output.root",
#"file:condor_MCPattuples_Zinvisible100to200_9/output.root",
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
# "file:condor_dataPattuples_Run2011A_Jun27_0/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_1/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_2/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_3/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_4/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_5/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_6/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_7/output.root",
# "file:condor_dataPattuples_Run2011A_Jun27_8/output.root",
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
# "file:condor_dataPattuples_Run2011A_Jun13_0/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_1/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_2/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_3/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_4/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_5/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_6/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_7/output.root",
# "file:condor_dataPattuples_Run2011A_Jun13_8/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_0/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_1/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_2/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_3/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_4/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_5/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_6/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_7/output.root",
# "file:condor_dataPattuples_Run2011A_Jun06_8/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_0/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_1/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_10/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_11/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_12/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_13/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_14/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_2/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_3/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_4/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_5/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_6/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_7/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_8/output.root",
#"file:condor_dataPattuples_Run2011A_2011Ago26_9/output.root",
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
# "file:condor_MCPattuples_Zinvisible_0/output.root",
# "file:condor_MCPattuples_Zinvisible_1/output.root",
# "file:condor_MCPattuples_Zinvisible_10/output.root",
# "file:condor_MCPattuples_Zinvisible_11/output.root",
# "file:condor_MCPattuples_Zinvisible_12/output.root",
# "file:condor_MCPattuples_Zinvisible_13/output.root",
# "file:condor_MCPattuples_Zinvisible_14/output.root",
# "file:condor_MCPattuples_Zinvisible_15/output.root",
# "file:condor_MCPattuples_Zinvisible_16/output.root",
# "file:condor_MCPattuples_Zinvisible_17/output.root",
# "file:condor_MCPattuples_Zinvisible_18/output.root",
# "file:condor_MCPattuples_Zinvisible_19/output.root",
# "file:condor_MCPattuples_Zinvisible_2/output.root",
# "file:condor_MCPattuples_Zinvisible_20/output.root",
# "file:condor_MCPattuples_Zinvisible_3/output.root",
# "file:condor_MCPattuples_Zinvisible_4/output.root",
# "file:condor_MCPattuples_Zinvisible_5/output.root",
# "file:condor_MCPattuples_Zinvisible_6/output.root",
# "file:condor_MCPattuples_Zinvisible_7/output.root",
# "file:condor_MCPattuples_Zinvisible_8/output.root",
# "file:condor_MCPattuples_Zinvisible_9/output.root",
# "file:condor_MCPattuples_ttbar_0/output.root",
# "file:condor_MCPattuples_ttbar_1/output.root",
# "file:condor_MCPattuples_ttbar_2/output.root",
# "file:condor_MCPattuples_ttbar_3/output.root",
# "file:condor_MCPattuples_ttbar_4/output.root",
# "file:condor_MCPattuples_ttbar_5/output.root",
# "file:condor_MCPattuples_ttbar_6/output.root",
# "file:condor_MCPattuples_ttbar_7/output.root",
# "file:condor_MCPattuples_ttbar_8/output.root",
# "file:condor_MCPattuples_ttbar_9/output.root",
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
#"file:condor_MCPattuples_WZ_0/output.root",
#"file:condor_MCPattuples_WZ_1/output.root",
#"file:condor_MCPattuples_WZ_2/output.root",
#"file:condor_MCPattuples_WZ_3/output.root",
#'file:pattuple_signalm2000_PU.root'
]);

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

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as basicjethistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos
from RSGraviton.RSAnalyzer.METhistos_cff import histograms as METhistos

process.load("RSGraviton.RSAnalyzer.eventCounters_cfi")

##########
# Jet ID #
##########
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
process.jetIdCut = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                filterParams = pfJetIDSelector.clone(
                                    CHF = cms.double(0.2),
                                    NHF = cms.double(0.7),
                                    CEF = cms.double(0.7),
                                    NEF = cms.double(0.7),
                                    ),
                                src = cms.InputTag("goodPatJetsPFlow"),
                                filter = cms.bool(True)
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
process.VBTFmuons.src = "selectedPatMuonsPFlow"
process.VBTFmuons.filter = cms.bool(False)

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
                                   src = cms.InputTag("jetIdCut"),
                                   maxNumber = cms.uint32(9999)
                                   )
process.pileupReweighter= cms.EDFilter("RSPileupReweighter",
                                       generatedFile = cms.string("pileup_Wjets.root"),
                                       dataFile = cms.string("Pileup_2011_EPS_8_jul.root"),
                                       genHistName = cms.string("pileup"),
                                       dataHistName = cms.string("pileup"),
                                       useROOThistos = cms.bool(False)
                                       )
#########
# TREES #
#########

process.treeDumper = cms.EDAnalyzer("ZZ2q2nuTreeMaker",
                                    jets = cms.InputTag("getHardJets"),
                                    met = cms.InputTag("patMETsPFlow"),
                                    electrons = cms.InputTag("selectedPatElectronsPFlow"),
                                    muons = cms.InputTag("VBTFmuons"),
                                    genParticles = cms.InputTag("hardGenParticles"),
                                    VBTFmuon = cms.InputTag("VBTFmuons"),
                                    TIV = cms.InputTag("TIVCut"),
                                    TIVStar = cms.InputTag("TIVStarCut"),
                                    isData = cms.bool(True),
                                    weight = cms.double(1.0),
                                    PUweight = cms.InputTag("pileupReweighter")
                                    )
#########
# PATHS #
#########
process.p = cms.Path(process.jetIdCut + 
                     #process.differentPtCut +
                     process.getHardJets +
                     process.muonSequence + 
                     process.TIVCut +
                     process.TIVStarCut +
#                     process.pileupReweighter +
                     process.treeDumper
                     )
