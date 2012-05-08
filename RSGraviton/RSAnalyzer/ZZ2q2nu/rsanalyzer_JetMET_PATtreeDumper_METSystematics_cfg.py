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

if 'skipEvents' in myOptions:
    skipEvents = int(myOptions[myOptions.index('skipEvents')+1])
else:
    skipEvents = 0
    
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()

### Different inputs
QCDHT1000 = [
"file:condor_MCPattuples_QCD_HT1000_0/output.root",
"file:condor_MCPattuples_QCD_HT1000_1/output.root",
"file:condor_MCPattuples_QCD_HT1000_2/output.root",
"file:condor_MCPattuples_QCD_HT1000_3/output.root",
"file:condor_MCPattuples_QCD_HT1000_4/output.root",
"file:condor_MCPattuples_QCD_HT1000_5/output.root"
]

QCDHT500to1000 = [
"file:condor_MCPattuples_QCD_HT500to1000_0/output.root",
"file:condor_MCPattuples_QCD_HT500to1000_1/output.root",
"file:condor_MCPattuples_QCD_HT500to1000_2/output.root",
"file:condor_MCPattuples_QCD_HT500to1000_3/output.root"
]

Run2011B_2011Nov11 = [
 "file:condor_dataPattuples_Run2011B_2011Nov11_0/output.root",
 "file:condor_dataPattuples_Run2011B_2011Nov11_1/output.root",
 "file:condor_dataPattuples_Run2011B_2011Nov11_2/output.root",
 "file:condor_dataPattuples_Run2011B_2011Nov11_3/output.root",
 "file:condor_dataPattuples_Run2011B_2011Nov11_4/output.root",
 "file:condor_dataPattuples_Run2011B_2011Nov11_5/output.root",
 "file:condor_dataPattuples_Run2011B_2011Nov11_6/output.root",
 "file:condor_dataPattuples_Run2011B_2011Nov11_7/output.root",
 "file:condor_dataPattuples_Run2011B_2011Nov11_8/output.root",
 "file:condor_dataPattuples_Run2011B_2011Nov11_9/output.root"
]

Run2011A_May10ReReco = [
 "file:condor_dataPattuples_Run2011A_May10ReReco_0/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_1/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_10/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_11/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_12/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_13/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_14/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_15/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_16/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_17/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_18/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_19/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_2/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_20/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_21/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_22/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_3/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_4/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_5/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_6/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_7/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_8/output_filtered.root",
 "file:condor_dataPattuples_Run2011A_May10ReReco_9/output_filtered.root",
]

Run2011B = [
 "file:condor_dataPattuples_Run2011B_0/output.root",
 "file:condor_dataPattuples_Run2011B_1/output.root",
 "file:condor_dataPattuples_Run2011B_10/output.root",
 "file:condor_dataPattuples_Run2011B_11/output.root",
 "file:condor_dataPattuples_Run2011B_12/output.root",
 "file:condor_dataPattuples_Run2011B_13/output.root",
 "file:condor_dataPattuples_Run2011B_14/output.root",
 "file:condor_dataPattuples_Run2011B_15/output.root",
 "file:condor_dataPattuples_Run2011B_16/output.root",
 "file:condor_dataPattuples_Run2011B_17/output.root",
 "file:condor_dataPattuples_Run2011B_18/output.root",
 "file:condor_dataPattuples_Run2011B_19/output.root",
 "file:condor_dataPattuples_Run2011B_2/output.root",
 "file:condor_dataPattuples_Run2011B_20/output.root",
 "file:condor_dataPattuples_Run2011B_21/output.root",
 "file:condor_dataPattuples_Run2011B_22/output.root",
 "file:condor_dataPattuples_Run2011B_23/output.root",
 "file:condor_dataPattuples_Run2011B_24/output.root",
 "file:condor_dataPattuples_Run2011B_25/output.root",
 "file:condor_dataPattuples_Run2011B_26/output.root",
 "file:condor_dataPattuples_Run2011B_27/output.root",
 "file:condor_dataPattuples_Run2011B_28/output.root",
 "file:condor_dataPattuples_Run2011B_29/output.root",
 "file:condor_dataPattuples_Run2011B_3/output.root",
 "file:condor_dataPattuples_Run2011B_30/output.root",
 "file:condor_dataPattuples_Run2011B_31/output.root",
 "file:condor_dataPattuples_Run2011B_32/output.root",
 "file:condor_dataPattuples_Run2011B_33/output.root",
 "file:condor_dataPattuples_Run2011B_34/output.root",
 "file:condor_dataPattuples_Run2011B_35/output.root",
 "file:condor_dataPattuples_Run2011B_36/output.root",
 "file:condor_dataPattuples_Run2011B_37/output.root",
 "file:condor_dataPattuples_Run2011B_38/output.root",
 "file:condor_dataPattuples_Run2011B_39/output.root",
 "file:condor_dataPattuples_Run2011B_4/output.root",
 "file:condor_dataPattuples_Run2011B_40/output.root",
 "file:condor_dataPattuples_Run2011B_41/output.root",
 "file:condor_dataPattuples_Run2011B_42/output.root",
 "file:condor_dataPattuples_Run2011B_43/output.root",
 "file:condor_dataPattuples_Run2011B_44/output.root",
 "file:condor_dataPattuples_Run2011B_45/output.root",
 "file:condor_dataPattuples_Run2011B_46/output.root",
 "file:condor_dataPattuples_Run2011B_47/output.root",
 "file:condor_dataPattuples_Run2011B_48/output.root",
 "file:condor_dataPattuples_Run2011B_5/output.root",
 "file:condor_dataPattuples_Run2011B_6/output.root",
 "file:condor_dataPattuples_Run2011B_7/output.root",
 "file:condor_dataPattuples_Run2011B_8/output.root",
 "file:condor_dataPattuples_Run2011B_9/output.root",
]

Run2011A_2011Set30 = [
 "file:condor_dataPattuples_Run2011A_PromptRecoSet30_0/output.root",
 "file:condor_dataPattuples_Run2011A_PromptRecoSet30_1/output.root",
 "file:condor_dataPattuples_Run2011A_PromptRecoSet30_2/output.root",
 "file:condor_dataPattuples_Run2011A_PromptRecoSet30_3/output.root",
]

Run2011A_Aug05ReReco = [
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_0/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_1/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_2/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_3/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_4/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_5/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_6/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_7/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_8/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_9/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_10/output.root",
 "file:condor_dataPattuples_Run2011A_ReRecoAug5_11/output.root",
]

WJetspt100 = [
 "file:condor_MCPattuples_WJetspt100_0/output.root",
 "file:condor_MCPattuples_WJetspt100_1/output.root",
 "file:condor_MCPattuples_WJetspt100_10/output.root",
 "file:condor_MCPattuples_WJetspt100_11/output.root",
 "file:condor_MCPattuples_WJetspt100_12/output.root",
 "file:condor_MCPattuples_WJetspt100_13/output.root",
 "file:condor_MCPattuples_WJetspt100_14/output.root",
 "file:condor_MCPattuples_WJetspt100_15/output.root",
 "file:condor_MCPattuples_WJetspt100_16/output.root",
 "file:condor_MCPattuples_WJetspt100_17/output.root",
 "file:condor_MCPattuples_WJetspt100_18/output.root",
 "file:condor_MCPattuples_WJetspt100_19/output.root",
 "file:condor_MCPattuples_WJetspt100_2/output.root",
 "file:condor_MCPattuples_WJetspt100_20/output.root",
 "file:condor_MCPattuples_WJetspt100_21/output.root",
 "file:condor_MCPattuples_WJetspt100_22/output.root",
 "file:condor_MCPattuples_WJetspt100_23/output.root",
 "file:condor_MCPattuples_WJetspt100_24/output.root",
 "file:condor_MCPattuples_WJetspt100_25/output.root",
 "file:condor_MCPattuples_WJetspt100_26/output.root",
 "file:condor_MCPattuples_WJetspt100_27/output.root",
 "file:condor_MCPattuples_WJetspt100_28/output.root",
 "file:condor_MCPattuples_WJetspt100_29/output.root",
 "file:condor_MCPattuples_WJetspt100_3/output.root",
 "file:condor_MCPattuples_WJetspt100_30/output.root",
 "file:condor_MCPattuples_WJetspt100_31/output.root",
 "file:condor_MCPattuples_WJetspt100_32/output.root",
 "file:condor_MCPattuples_WJetspt100_33/output.root",
 "file:condor_MCPattuples_WJetspt100_34/output.root",
 "file:condor_MCPattuples_WJetspt100_35/output.root",
 "file:condor_MCPattuples_WJetspt100_36/output.root",
 "file:condor_MCPattuples_WJetspt100_37/output.root",
 "file:condor_MCPattuples_WJetspt100_38/output.root",
 "file:condor_MCPattuples_WJetspt100_4/output.root",
 "file:condor_MCPattuples_WJetspt100_5/output.root",
 "file:condor_MCPattuples_WJetspt100_6/output.root",
 "file:condor_MCPattuples_WJetspt100_7/output.root",
 "file:condor_MCPattuples_WJetspt100_8/output.root",
]

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

Run2011A_2011Jul06 = [
 "file:condor_dataPattuples_Run2011A_Jul06_0/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_1/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_10/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_11/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_2/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_3/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_4/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_5/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_6/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_7/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_8/output.root",
 "file:condor_dataPattuples_Run2011A_Jul06_9/output.root",
]

Run2011A_2011Jun27 = [
 "file:condor_dataPattuples_Run2011A_Jun27_0/output.root",
 "file:condor_dataPattuples_Run2011A_Jun27_1/output.root",
 "file:condor_dataPattuples_Run2011A_Jun27_2/output.root",
 "file:condor_dataPattuples_Run2011A_Jun27_3/output.root",
 "file:condor_dataPattuples_Run2011A_Jun27_4/output.root",
 "file:condor_dataPattuples_Run2011A_Jun27_5/output.root",
 "file:condor_dataPattuples_Run2011A_Jun27_6/output.root",
 "file:condor_dataPattuples_Run2011A_Jun27_7/output.root",
 "file:condor_dataPattuples_Run2011A_Jun27_8/output.root",
]

Run2011A_2011Jun20 = [
 "file:condor_dataPattuples_Run2011A_Jun20_0/output.root",
 "file:condor_dataPattuples_Run2011A_Jun20_1/output.root",
 "file:condor_dataPattuples_Run2011A_Jun20_10/output.root",
 "file:condor_dataPattuples_Run2011A_Jun20_2/output.root",
 "file:condor_dataPattuples_Run2011A_Jun20_3/output.root",
 "file:condor_dataPattuples_Run2011A_Jun20_4/output.root",
 "file:condor_dataPattuples_Run2011A_Jun20_5/output.root",
 "file:condor_dataPattuples_Run2011A_Jun20_6/output.root",
 "file:condor_dataPattuples_Run2011A_Jun20_7/output.root",
 "file:condor_dataPattuples_Run2011A_Jun20_8/output.root",
 "file:condor_dataPattuples_Run2011A_Jun20_9/output.root",
]

Run2011A_2011Jun13 = [
 "file:condor_dataPattuples_Run2011A_Jun13_0/output.root",
 "file:condor_dataPattuples_Run2011A_Jun13_1/output.root",
 "file:condor_dataPattuples_Run2011A_Jun13_2/output.root",
 "file:condor_dataPattuples_Run2011A_Jun13_3/output.root",
 "file:condor_dataPattuples_Run2011A_Jun13_4/output.root",
 "file:condor_dataPattuples_Run2011A_Jun13_5/output.root",
 "file:condor_dataPattuples_Run2011A_Jun13_6/output.root",
 "file:condor_dataPattuples_Run2011A_Jun13_7/output.root",
 "file:condor_dataPattuples_Run2011A_Jun13_8/output.root",
]

Run2011A_2011Jun06 = [
 "file:condor_dataPattuples_Run2011A_Jun06_0/output.root",
 "file:condor_dataPattuples_Run2011A_Jun06_1/output.root",
 "file:condor_dataPattuples_Run2011A_Jun06_2/output.root",
 "file:condor_dataPattuples_Run2011A_Jun06_3/output.root",
 "file:condor_dataPattuples_Run2011A_Jun06_4/output.root",
 "file:condor_dataPattuples_Run2011A_Jun06_5/output.root",
 "file:condor_dataPattuples_Run2011A_Jun06_6/output.root",
 "file:condor_dataPattuples_Run2011A_Jun06_7/output.root",
 "file:condor_dataPattuples_Run2011A_Jun06_8/output.root",
]

Run2011A_2011Aug26 = [
 "file:condor_dataPattuples_Run2011A_2011Ago26_0/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_1/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_10/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_11/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_12/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_13/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_14/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_2/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_3/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_4/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_5/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_6/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_7/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_8/output.root",
 "file:condor_dataPattuples_Run2011A_2011Ago26_9/output.root",
]

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

Zinvisible = [
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
]

ttbar = [
 "file:condor_MCPattuples_ttbar_0/output.root",
 "file:condor_MCPattuples_ttbar_1/output.root",
 "file:condor_MCPattuples_ttbar_2/output.root",
 "file:condor_MCPattuples_ttbar_3/output.root",
 "file:condor_MCPattuples_ttbar_4/output.root",
 "file:condor_MCPattuples_ttbar_5/output.root",
 "file:condor_MCPattuples_ttbar_6/output.root",
 "file:condor_MCPattuples_ttbar_7/output.root",
 "file:condor_MCPattuples_ttbar_8/output.root",
 "file:condor_MCPattuples_ttbar_9/output.root",
]

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
#"file:condor_MCPattuples_ZZ_0/output.root",
#"file:condor_MCPattuples_ZZ_1/output.root",
#"file:condor_MCPattuples_ZZ_2/output.root",
#"file:condor_MCPattuples_ZZ_3/output.root",

signalm1000 = [
'file:pattuple_signalm1000_PU.root'
]

signalm1250 = [
'file:pattuple_signalm1250_PU.root'
]

signalm1500 = [
'file:pattuple_signalm1500_PU.root'
]

signalm1750 = [
'file:pattuple_signalm1750_PU.root'
]

signalm2000 = [
'file:pattuple_signalm2000_PU.root'
]

### Choose the right input
inputToExtend = []

if ("help" in setupFileName):
    x = [
    "Run2011B_2011Nov11",
    "Run2011A_May10ReReco",
    "Run2011B",
    "Run2011A_2011Set30",
    "Run2011A_Aug05ReReco",
    "Run2011A_2011Jul06",
    "Run2011A_2011Jun27",
    "Run2011A_2011Jun20",
    "Run2011A_2011Jun13",
    "Run2011A_2011Jun06",
    "Run2011A_2011Aug26",
    "WJetspt100",
    "Zinvisible",
    "ttbar",
    "QCDHT500to1000",
    "QCDHT1000",
    "signalm1000",
    "signalm1250",
    "signalm1500",
    "signalm1750",
    "signalm2000",
    ]
    print "Options are"
    for i in x:
        print i
    sys.exit()

if ("Run2011B_2011Nov11" in setupFileName):
    inputToExtend = Run2011B_2011Nov11

if ("Run2011A_May10ReReco" in setupFileName):
    inputToExtend = Run2011A_May10ReReco

if ("Run2011B" in setupFileName):
    inputToExtend = Run2011B

if ("Run2011A_2011Set30" in setupFileName):
    inputToExtend = Run2011A_2011Set30

if ("Run2011A_Aug05ReReco" in setupFileName):
    inputToExtend = Run2011A_Aug05ReReco

if ("Run2011A_2011Jul06" in setupFileName):
    inputToExtend = Run2011A_2011Jul06

if ("Run2011A_2011Jun27" in setupFileName):
    inputToExtend = Run2011A_2011Jun27

if ("Run2011A_2011Jun20" in setupFileName):
    inputToExtend = Run2011A_2011Jun20

if ("Run2011A_2011Jun13" in setupFileName):
    inputToExtend = Run2011A_2011Jun13

if ("Run2011A_2011Jun06" in setupFileName):
    inputToExtend = Run2011A_2011Jun06

if ("Run2011A_2011Aug26" in setupFileName):
    inputToExtend = Run2011A_2011Aug26

if ("WJetspt100" in setupFileName):
    inputToExtend = WJetspt100

if ("Zinvisible" in setupFileName):
    inputToExtend = Zinvisible

if ("ttbar" in setupFileName):
    inputToExtend =ttbar

if ("QCDHT500to1000" in setupFileName):
    inputToExtend = QCDHT500to1000

if ("QCDHT1000" in setupFileName):
    inputToExtend = QCDHT1000

if ("signalm1000" in setupFileName):
    inputToExtend = signalm1000

if ("signalm1250" in setupFileName):
    inputToExtend = signalm1250

if ("signalm1500" in setupFileName):
    inputToExtend = signalm1500

if ("signalm1750" in setupFileName):
    inputToExtend = signalm1750

if ("signalm2000" in setupFileName):
    inputToExtend = signalm2000

if not inputToExtend:
    print "No standard input, going manually..."
    # Put the inputToExtend here
    inputToExtend = ["file:pattuple_signalm1250_PU_uncertainties.root"]
    print inputToExtend

readFiles.extend(inputToExtend)
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

import PhysicsTools.PythonAnalysis.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
### IMPORTANT - remember to use myLumis from pattuples with bad lumisections
#lumiFileName = "lumiSummary_METBTag_Run2011A-May10Rereco-2011May10_final.json"
#lumiFileName = "lumiSummary_MET_Run2011A-PromptReco_v4_final.json"
#lumiFileName = "lumiSummary_MET_Run2011A-Aug05Rereco_final.json"
lumiFileName = "officialJSON_Run2011A_allReconstructions.json"
#lumiFileName = "officialJSON_Run2011B_PromptReco_v1.json"
myLumis = LumiList.LumiList(filename = lumiFileName).getCMSSWString().split(',')
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#process.source.lumisToProcess.extend(myLumis)

process.source.skipEvents=cms.untracked.uint32(skipEvents)

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
# Same jet ID as in AN-2011-228
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

#############
# Electrons #
#############
process.load("RSGraviton.RSAnalyzer.electronSequence_cfi")
process.VBTFelectrons.src = "selectedPatElectronsPFlow"
process.VBTFelectrons.filter = cms.bool(False)

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
process.pileupReweighter= cms.EDFilter("RSPileupReweighter",
                                       generatedFile = cms.string("PUMC_dist.root"),
                                       dataFile = cms.string("PUData_dist.root"),
                                       genHistName = cms.string("pileup"),
                                       dataHistName = cms.string("pileup"),
                                       useROOThistos = cms.bool(True)
                                       )
#########
# TREES #
#########

process.treeDumper = cms.EDAnalyzer("ZZ2q2nuTreeMaker",
                                    jets = cms.InputTag("getHardJets"),
                                    met = cms.InputTag("patType1CorrectedPFMet"),
                                    electrons = cms.InputTag("VBTFelectrons"),
                                    muons = cms.InputTag("VBTFmuons"),
                                    genParticles = cms.InputTag("hardGenParticles"),
                                    VBTFmuon = cms.InputTag("VBTFmuons"),
                                    TIV = cms.InputTag("TIVCut"),
                                    TIVStar = cms.InputTag("TIVStarCut"),
                                    isData = cms.bool(False),
                                    weight = cms.double(1.0),
                                    PUweight = cms.InputTag("pileupReweighter")
                                    )
#########
# PATHS #
#########
process.p = cms.Path(process.jetIdCut + 
                     process.differentPtCut +
                     process.getHardJets +
                     process.muonSequence + 
                     process.electronSequence + 
                     process.TIVCut +
                     process.TIVStarCut +
                     process.pileupReweighter +
                     process.treeDumper
                     )
