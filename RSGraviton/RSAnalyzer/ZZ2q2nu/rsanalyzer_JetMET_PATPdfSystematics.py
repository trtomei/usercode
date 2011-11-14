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
setupJetMassCut = 70.0
setupMETCut = 300.0
setupMaxJets = 3
setupMaxAngle = 2.8

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.EventContent.EventContent_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

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
readFiles.extend(["file:pattuple_signalm1000_PU.root"]);

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(setupNumEvents)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output_'+setupFileName+setupSuffix+'.root')
)

process.MessageLogger.cerr.FwkReport.reportEvery = 100

### PDFs
# Produce PDF weights (maximum is 3)
process.pdfWeights = cms.EDProducer("PdfWeightProducer",
                                    # Fix POWHEG if buggy (this PDF set will also appear on output, 
                                    # so only two more PDF sets can be added in PdfSetNames if not "")
                                    # FixPOWHEG = cms.untracked.string("CT10.LHgrid"),
                                    GenTag = cms.untracked.InputTag("hardGenParticles"),
                                    PdfInfoTag = cms.untracked.InputTag("generator"),
                                    PdfSetNames = cms.untracked.vstring("cteq66.LHgrid",
                                                                        "MRST2006nnlo.LHgrid",
                                                                        "cteq5l.LHgrid")
                                                                        #)
                                    )

##########
# Jet ID #
##########
# This selector selects PAT jets with loose jet ID thresholds.
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
process.jetIdCut = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                filterParams = pfJetIDSelector.clone(),
                                src = cms.InputTag("goodPatJetsPFlow")
                                )

######################
# Jet Kinematic cuts #
######################

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
                                    src = cms.InputTag("selectedPatElectronsPFlow"),
                                    cut = cms.string(""),
                                    filter = cms.bool(True)
                                    )
process.anyMuons = cms.EDFilter("PATMuonSelector",
                                src = cms.InputTag("selectedPatMuonsPFlow"),
                                cut = cms.string(""),
                                filter = cms.bool(True)
                                )
#########
# PLOTS #
#########

#########
# PATHS #
#########
process.analysisSearchSequence = cms.Sequence(process.jetIdCut +
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


process.pSearch = cms.Path(process.pdfWeights + process.analysisSearchSequence)

# Collect uncertainties for rate and acceptance
process.pdfSystematics = cms.EDFilter("PdfSystematicsAnalyzer",
      SelectorPath = cms.untracked.string('pSearch'),
      PdfWeightTags = cms.untracked.VInputTag(
              "pdfWeights:cteq66",
              "pdfWeights:MRST2006nnlo",
              "pdfWeights:cteq5l",
      )
)

process.end = cms.EndPath(process.pdfSystematics)
