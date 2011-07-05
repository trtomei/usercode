## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

import sys
# the source is already defined in patTemplate_cfg.
# overriding source and various other things
#process.load("PhysicsTools.PFCandProducer.Sources.source_ZtoEles_DBS_312_cfi")
#process.source = cms.Source("PoolSource", 
#     fileNames = cms.untracked.vstring('file:myAOD.root')
#)

# Some command line options
myOptions = sys.argv
skipEvents = 0
numEvents = -1
if 'skipEvents' in myOptions:
    skipEvents = int(myOptions[myOptions.index('skipEvents')+1])
if 'numEvents' in myOptions:
    numEvents = int(myOptions[myOptions.index('numEvents')+1])

# load the PAT config
process.load("PhysicsTools.PatAlgos.patSequences_cff")

from PhysicsTools.PatAlgos.cleaningLayer1.cleanPatCandidates_cff import *

process.GlobalTag.globaltag = 'GR_R_42_V12::All' ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
 
process.load("RSGraviton.RSAnalyzer.Summer11.METBTag_Run2011A_May10ReReco")
process.maxEvents.input = numEvents         ##  (e.g. -1 to run on all events)
process.source.skipEvents=cms.untracked.uint32(skipEvents)

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

# Configure PAT to use PF2PAT instead of AOD sources
# this function will modify the PAT sequences. It is currently 
# not possible to run PF2PAT+PAT and standart PAT at the same time
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.coreTools import *

postfix = "PFlow"
jetAlgo="AK7"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=False, postfix=postfix) 

# A small fix to run while there are no L2L3residuals for 4_2_x
if 'L2L3Residual' in getattr(process,'patJetCorrFactors' + postfix).levels:
    getattr(process,'patJetCorrFactors' + postfix).levels.remove('L2L3Residual')
# And for whatever reason... it was using L1Offset.
# Move to L1Fastjet
if 'L1Offset' in getattr(process,'patJetCorrFactors' + postfix).levels:
    getattr(process,'patJetCorrFactors' + postfix).levels[0] = 'L1FastJet'
    
# to run second PF2PAT+PAT with differnt postfix uncomment the following lines
# and add it to path
#postfix2 = "PFlow2"
#jetAlgo2="AK7"
#usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo2, runOnMC=True, postfix=postfix2) 

# to use tau-cleaned jet collection uncomment the following:
#useTauCleanedPFJets(process, jetAlgo=jetAlgo, postfix=postfix)

# to switch default tau to HPS tau uncomment the following:
#adaptPFTaus(process,"hpsPFTau",postfix=postfix)

### Keep some MC info
process.hardGenParticles = cms.EDProducer("GenParticlePruner",
                                          src = cms.InputTag("genParticles"),
                                          select = cms.vstring("drop  *  ", # this is the default
                                                               "keep status = 3"
                                                               )
                                          )

### Cleaning
process.cleanPatMuonsPFlow = cms.EDProducer("PATMuonCleaner",
                                            src = cms.InputTag("selectedPatMuonsPFlow"),
                                            # preselection (any string-based cut for pat::Muon)
                                            preselection = cms.string(''),
                                            # overlap checking configurables
                                            checkOverlaps = cms.PSet(),
                                            # finalCut (any string-based cut for pat::Muon)
                                            finalCut = cms.string(''),
                                            )

process.cleanPatElectronsPFlow = cms.EDProducer("PATElectronCleaner",
                                                src = cms.InputTag("selectedPatElectronsPFlow"),
                                                # preselection (any string-based cut on pat::Electrons)
                                                preselection = cms.string(''),
                                                # overlap checking configurables
                                                checkOverlaps = cms.PSet(muons = cms.PSet(src       = cms.InputTag("cleanPatMuonsPFlow"),
                                                                                          algorithm = cms.string("byDeltaR"),
                                                                                          preselection        = cms.string(""),
                                                                                          deltaR              = cms.double(0.3),
                                                                                          checkRecoComponents = cms.bool(False),
                                                                                          pairCut             = cms.string(""),
                                                                                          requireNoOverlaps   = cms.bool(False),
                                                                                          )
                                                                         ),
                                                # finalCut (any string-based cut for pat::Electron)
                                                finalCut = cms.string(''),
                                                )

process.cleanPatJetsPFlow = cms.EDProducer("PATJetCleaner",
                                           src = cms.InputTag("selectedPatJetsPFlow"),
                                           # preselection (any string-based cut on pat::Jet)
                                           preselection = cms.string(''),
                                           # overlap checking configurables
                                           checkOverlaps = cms.PSet(muons = cms.PSet(src       = cms.InputTag("cleanPatMuonsPFlow"),
                                                                                     algorithm = cms.string("byDeltaR"),
                                                                                     preselection        = cms.string(""),
                                                                                     deltaR              = cms.double(0.3),
                                                                                     checkRecoComponents = cms.bool(False),
                                                                                     pairCut             = cms.string(""),
                                                                                     requireNoOverlaps   = cms.bool(False),
                                                                                     ),
                                                                    electrons = cms.PSet(src       = cms.InputTag("cleanPatElectronsPFlow"),
                                                                                         algorithm = cms.string("byDeltaR"),
                                                                                         preselection        = cms.string(""),
                                                                                         deltaR              = cms.double(0.3),
                                                                                         checkRecoComponents = cms.bool(False),
                                                                                         pairCut             = cms.string(""),
                                                                                         requireNoOverlaps   = cms.bool(False),
                                                                                         ),
                                                                    ),
                                           finalCut = cms.string('')
                                           )
# One module to count objects
process.cleanPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
                                                  logName = cms.untracked.string("cleanPatCandidates|PATSummaryTables"),
                                                  candidates = cms.VInputTag(cms.InputTag("cleanPatElectronsPFlow"),
                                                                             cms.InputTag("cleanPatMuonsPFlow"),
                                                                             cms.InputTag("cleanPatJetsPFlow"),
                                                                             )
                                                  )


process.cleanPatCandidatesPFlow = cms.Sequence(
            process.cleanPatMuonsPFlow     *        # NOW WE MUST USE '*' AS THE ORDER MATTERS
            process.cleanPatElectronsPFlow *
            process.cleanPatJetsPFlow     *
            process.cleanPatCandidateSummary
            )


# top projections in PF2PAT:
process.pfNoPileUpPFlow.enable = True 
process.pfPileUpPFlow.Vertices = 'goodOfflinePrimaryVertices'
process.pfPileUpPFlow.checkClosestZVertex = cms.bool(False)
process.pfNoMuonPFlow.enable = True 
process.pfNoElectronPFlow.enable = True 
process.pfNoJetPFlow.enable = True 
process.pfNoTauPFlow.enable = True

# Preparing Charged Hadron Subtraction
process.pfJetsPFlow.doAreaFastjet = True
process.pfJetsPFlow.doRhoFastjet = False
process.patJetCorrFactorsPFlow.rho = cms.InputTag("kt6PFJetsPFlow", "rho")

# Have to do this to get the Voronoi areas
from RecoJets.JetProducers.kt4PFJets_cfi import kt4PFJets
process.kt6PFJetsPFlow = kt4PFJets.clone(
        rParam = cms.double(0.6),
        src = cms.InputTag('pfNoElectron'+postfix),
        doAreaFastjet = cms.bool(True),
        doRhoFastjet = cms.bool(True),
        voronoiRfact = cms.double(0.9)
        )

### Preselection cuts
#process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
#                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
#                                           minimumNDOF = cms.uint32(4) ,
#                                           maxAbsZ = cms.double(24),
#                                           maxd0 = cms.double(2)
#                                           )
# In 42X, the good vertices are the DAF (deterministic annealing filter) vertices
from PhysicsTools.SelectorUtils.pvSelector_cfi import pvSelector
process.goodOfflinePrimaryVertices = cms.EDFilter("PrimaryVertexObjectFilter",
                                                  filterParams = pvSelector.clone( minNdof = cms.double(7.0), maxZ = cms.double(24.0) ),
                                                  src=cms.InputTag('offlinePrimaryVertices')
                                                  )

process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )

process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')
# New recommendations for 50 ns bunch spacing
process.HBHENoiseFilter.minIsolatedNoiseSumE = cms.double(999999.)
process.HBHENoiseFilter.minNumIsolatedNoiseChannels = cms.int32(999999)
process.HBHENoiseFilter.minIsolatedNoiseSumEt = cms.double(999999.)

process.preselection = cms.Sequence(process.goodOfflinePrimaryVertices + process.noscraping + process.HBHENoiseFilter)

### Cut to make small
process.cutOnJet = cms.EDFilter("CandViewSelector",
                                src = cms.InputTag("cleanPatJetsPFlow"),
                                cut = cms.string("(pt > 110.0) && (abs(eta) < 2.4)"),
                                minNumber = cms.int32(1),
                                filter = cms.bool(True)
                                )

# insert those kt6PFJets there, just after pfNoElectron
getattr(process,"patPF2PATSequence"+postfix).replace(
    getattr(process,"pfNoElectron"+postfix), getattr(process,"pfNoElectron"+postfix)*process.kt6PFJetsPFlow
    )

# Let it run
process.p = cms.Path(
#    process.patDefaultSequence  +
    process.preselection + 
    getattr(process,"patPF2PATSequence"+postfix) +
    process.cleanPatCandidatesPFlow +
#    process.hardGenParticles +
    process.cutOnJet
)

# Add PF2PAT output to the created file
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning
process.load("CommonTools.ParticleFlow.PF2PAT_EventContent_cff")

process.out.outputCommands = cms.untracked.vstring('drop *',
#                                                   'keep *_hardGenParticles_*_*',
                                                   'keep *_TriggerResults_*_*',
                                                   'keep recoPFCandidates_particleFlow_*_*',
                                                   'keep *_cleanPatMuonsPFlow_*_*',
                                                   'keep *_cleanPatElectronsPFlow_*_*',
                                                   'keep *_cleanPatJetsPFlow_*_*' ,
                                                   'keep recoTracks_generalTracks_*_*',
                                                   'keep *_selectedPatPFParticlesPFlow_*_*',
                                                   'keep *_patMETsPFlow_*_*') 

process.out.fileName = cms.untracked.string("pattuple.root")
