#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("PRESELECTION")

###########################
# Basic process controls. #
###########################

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.EventContent.EventContent_cff')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# Get options
myOptions = sys.argv
print myOptions

if 'startFile' in myOptions:
    startFile = int(myOptions[myOptions.index('startFile')+1])
else:
    startFile = 1

if 'endFile' in myOptions:
    endFile = int(myOptions[myOptions.index('endFile')+1])
else:
    endFile = 99999                                        

# Summary
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
# from RSGraviton.RSAnalyzer.filesReRecoDec22_Run2010Bp1_cff import theFiles as filelist1
# from RSGraviton.RSAnalyzer.filesReRecoDec22_Run2010Bp2_cff import theFiles as filelist2
# myFilesList = filelist2[startFile-1:endFile:]

# print "Running on files:"
# for i in myFilesList:
#     print i

# readFiles.extend( myFilesList )
readFiles.extend(['file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/selectedHBHEAndTrigger.root',])
#process.load("RSGraviton.RSAnalyzer.Fall10_RSToZZToNuNuJJ_m1000_cff")

### The output
#process.TFileService = cms.Service("TFileService",
#                                   fileName = cms.string('report_Run2010Bp2_'+str(startFile)+str(endFile)+'.root')
#
#)

process.TFileService = cms.Service("TFileService",fileName = cms.string('temp9.root'))

#process.Tracer = cms.Service("Tracer")

# Global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = 'GR_R_39X_V5::All' # 3_9_X RECO
process.GlobalTag.globaltag = 'GR_R_38X_V15::All ' # 3_8_X RECO

#process.GlobalTag.globaltag = "MC_38Y_V13::All"
##################
# Mandatory cuts #
##################

##########
# Jet ID #
##########
# This will filter out events where any jet above 30 GeV fails the Jet ID cut.
# Default is loose cut, use tightQuality if you want tight cut.
process.jetIdCut = cms.EDFilter("RSJetIdSelector",
                                jets = cms.InputTag("ak7CaloJets"),
                                jetID = cms.InputTag("ak7JetID"),
                                threshold = cms.double(30.0),
                                filter = cms.bool(True),
                                tightQuality = cms.bool(False)
                                )

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

###############
# Corrections #
###############
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.ak7CaloL2Relative.useCondDB = False
process.ak7CaloL3Absolute.useCondDB = False
process.ak7CaloResidual.useCondDB = False
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('ak7CaloL2L3')
                                             )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

##################
# Kinematic cuts #
##################

jetPtCut = 80.0
jetEtaCut = 2.4
jetMassCut = 0.0
METCut = 80.0

### For Path 1 - FAT jet from Z.
process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDFilter("LargestPtCaloJetSelector",
                                     src = cms.InputTag("oneJetAboveZero"),
                                     maxNumber = cms.uint32(1)
                                     )

process.ptCut = cms.EDFilter("JetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > "+str(jetPtCut)),
                             minNumber = cms.int32(1),
                             )

process.etaCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("abs(eta) < "+str(jetEtaCut)),
                              minNumber = cms.int32(1),
                              )

process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("corMetGlobalMuons"),
                              ptMin = cms.double(METCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

############
# Counting #
############
# In case you want to check efficiencies cut by cut.
process.eventCounter = cms.EDAnalyzer("EventCounter")
process.eventCounterTwo = process.eventCounter.clone()
process.eventCounterThree = process.eventCounter.clone()
process.eventCounterFour = process.eventCounter.clone()
process.eventCounterFive = process.eventCounter.clone()
process.eventCounterSix = process.eventCounter.clone()

#########
# Paths #
#########

# Summary of cuts.
process.goodVertexSequence = cms.Sequence(process.primaryVertexFilter+process.noscraping)
process.jetId  = cms.Sequence(process.jetIdCut + process.myCorrections)
process.cuts0  = cms.Sequence(process.oneJetAboveZero)
process.cuts1  = cms.Sequence(process.ptCut)
process.cuts2  = cms.Sequence(process.etaCut)
process.cuts3  = cms.Sequence(process.METCut)

process.thiagoSelection = cms.Sequence(
    process.eventCounter + process.goodVertexSequence + # Good vertex
    process.eventCounterTwo + process.jetId +
    process.eventCounterThree + process.cuts0 + process.getLargestJet +
    process.eventCounterFour + process.cuts1 + process.cuts2 + # Jet must be above pt cut
    process.eventCounterFive + process.cuts3 + # MET must be above MET cut
    process.eventCounterSix + process.HBHENoiseFilter
    )

process.pathSelection = cms.Path(process.thiagoSelection)

process.preselectionOut = cms.OutputModule("PoolOutputModule",
                                           fileName = cms.untracked.string('Run2010Bp2_oldReco.root'),
                                           outputCommands = process.RECOEventContent.outputCommands,
                                           dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO'),
                                                                        filterName = cms.untracked.string('PRESELECTION')),
                                           SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('pathSelection')
                                                                             )
                                           )

process.e = cms.EndPath(process.preselectionOut)
