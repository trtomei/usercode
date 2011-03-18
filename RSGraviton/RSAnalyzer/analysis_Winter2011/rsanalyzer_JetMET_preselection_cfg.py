#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("PRESELECTION")

###########################
# Basic process controls. #
###########################

thiagoInputFilesList = ''
thiagoOutputName = ''
thiagoJetPtCut = 110.0
thiagoSmallJetPtCut = 30.0
thiagoJetEtaCut = 2.4
thiagoJetMassCut = 0.0
thiagoMETCut = 150.0
thiagoMaxJets = 3
thiagoMaxAngle = 2.0

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

#from RSGraviton.RSAnalyzer.filesReRecoDec22_Run2010Bp1_cff import theFiles as filelist1
from RSGraviton.RSAnalyzer.filesReRecoDec22_Run2010Bp2_cff import theFiles as filelist2
myFilesList = filelist2[startFile-1:endFile:]

print "Running on files:"
for i in myFilesList:
    print i

readFiles.extend( myFilesList )

thiagoOutputName = 'Run2010Bp2_'+str(startFile)+'_'+str(endFile)+'.root'

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('report_'+thiagoOutputName)
                                   )

#process.Tracer = cms.Service("Tracer")

# Global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_R_39X_V5::All' # 3_9_X RECO
#process.GlobalTag.globaltag = 'GR_R_38X_V15::All ' # 3_8_X RECO

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
                                correctorName = cms.string("ak7CaloL2L3Residual"),
                                jetID = cms.InputTag("ak7JetID"),
                                n90 = cms.int32(1),
                                EMFraction = cms.double(0.01),
                                HPDnoise = cms.double(0.98),
                                threshold = cms.double(30.0),
                                filter = cms.bool(False),
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
process.myCorrectedJets = cms.EDProducer('CaloJetCorrectionProducer',
                                         src        = cms.InputTag('jetIdCut'),
                                         correctors = cms.vstring('ak7CaloL2L3Residual')
                                         )
process.myCorrections = cms.Sequence(process.myCorrectedJets)

##################
# Kinematic cuts #
##################

process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("myCorrectedJets"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDFilter("LargestPtCaloJetSelector",
                                     src = cms.InputTag("oneJetAboveZero"),
                                     maxNumber = cms.uint32(1)
                                     )


# Jet pt, eta cut
process.ptCut = cms.EDFilter("JetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > "+str(thiagoJetPtCut)),
                             minNumber = cms.int32(1),
                             )

process.etaCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("abs(eta) < "+str(thiagoJetEtaCut)),
                              minNumber = cms.int32(1),
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
process.noiseFilters = cms.Sequence(process.HBHENoiseFilter)
process.jetId  = cms.Sequence(process.jetIdCut + process.myCorrections)
process.cuts0  = cms.Sequence(process.oneJetAboveZero)
process.cuts1  = cms.Sequence(process.ptCut)
process.cuts2  = cms.Sequence(process.etaCut)

process.thiagoSelection = cms.Sequence(
    process.eventCounter + process.goodVertexSequence + process.noiseFilters + # Good vertex
    process.eventCounterTwo + process.jetId +
    process.eventCounterThree + process.cuts0 + process.getLargestJet +
    process.eventCounterFour + process.cuts1 + process.cuts2 # Jet must be above pt, eta cut
    )

process.pathSelection = cms.Path(process.thiagoSelection)

process.preselectionOut = cms.OutputModule("PoolOutputModule",
                                           fileName = cms.untracked.string('preselection_'+thiagoOutputName),
                                           outputCommands = process.RECOEventContent.outputCommands,
                                           dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO'),
                                                                        filterName = cms.untracked.string('PRESELECTION')),
                                           SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('pathSelection')
                                                                             )
                                           )

process.e = cms.EndPath(process.preselectionOut)
