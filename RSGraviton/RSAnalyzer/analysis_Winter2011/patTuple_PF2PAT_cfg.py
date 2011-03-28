## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

# the source is already defined in patTemplate_cfg.
# overriding source and various other things
#process.load("PhysicsTools.PFCandProducer.Sources.source_ZtoEles_DBS_312_cfi")
#process.source = cms.Source("PoolSource", 
#     fileNames = cms.untracked.vstring('file:myAOD.root')
#)

# load the PAT config
process.load("PhysicsTools.PatAlgos.patSequences_cff")

from PhysicsTools.PatAlgos.cleaningLayer1.cleanPatCandidates_cff import *

process.GlobalTag.globaltag = 'MC_38Y_V14::All'    ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
 
process.source.fileNames = [
    'file:/home/trtomei/storage/METFwd_Run2010B-Dec22ReReco/preselection_Run2010Bp1_cutAK7PFJet110.root',
    'file:/home/trtomei/storage/METFwd_Run2010B-Dec22ReReco/preselection_Run2010Bp2_cutAK7PFJet110.root',
    ]   

process.maxEvents.input = -1         ##  (e.g. -1 to run on all events)

process.MessageLogger.cerr.FwkReport.reportEvery = 10

# Configure PAT to use PF2PAT instead of AOD sources
# this function will modify the PAT sequences. It is currently 
# not possible to run PF2PAT+PAT and standart PAT at the same time
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.coreTools import *

postfix = "PFlow"
jetAlgo="AK7"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=False, postfix=postfix) 

# to run second PF2PAT+PAT with differnt postfix uncomment the following lines
# and add it to path
#postfix2 = "PFlow2"
#jetAlgo2="AK7"
#usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo2, runOnMC=True, postfix=postfix2) 

# to use tau-cleaned jet collection uncomment the following:
#useTauCleanedPFJets(process, jetAlgo=jetAlgo, postfix=postfix)

# to switch default tau to HPS tau uncomment the following:
#adaptPFTaus(process,"hpsPFTau",postfix=postfix)


# Let it run
process.p = cms.Path(
#    process.patDefaultSequence  +
    getattr(process,"patPF2PATSequence"+postfix) +
    process.cleanPatCandidatesPFlow
)

# Add PF2PAT output to the created file
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning
process.load("PhysicsTools.PFCandProducer.PF2PAT_EventContent_cff")

process.out.outputCommands = cms.untracked.vstring('drop *',
                                                   'keep recoPFCandidates_particleFlow_*_*',
                                                   'keep cleanPatMuonsPFlow_*_*_*',
                                                   'keep cleanPatElectronsPFlow_*_*_*',
                                                   'keep cleanPatJetsPFlow_*_*_*' ,
                                                   'keep recoTracks_generalTracks_*_*',
                                                   *patEventContentNoCleaning ) 

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
process.pfNoMuonPFlow.enable = False 
process.pfNoElectronPFlow.enable = True 
process.pfNoTauPFlow.enable = True 
process.pfNoJetPFlow.enable = True 

process.pfNoMuon.verbose = True

