# Starting with a skeleton process which gets imported with the following line
from PhysicsTools.PatAlgos.patTemplate_cfg import *
from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.pfTools import *

import sys

# Some command line options
myOptions = sys.argv
skipEvents = 0
numEvents = -1
useData = True

if 'skipEvents' in myOptions:
    skipEvents = int(myOptions[myOptions.index('skipEvents')+1])
if 'numEvents' in myOptions:
    numEvents = int(myOptions[myOptions.index('numEvents')+1])
if 'useData' in myOptions:
    x = myOptions[myOptions.index('useData')+1]
    if x == 'False':
        useData = False
    if x == 'True':
        useData = True
    
###############################
####### Global Setup ##########
###############################

if useData:
    process.GlobalTag.globaltag = 'GR_R_42_V19::All' ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
    inputJetCorrLabelAK5 = ('AK5PF', ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']) # Will have L2L3ResidualEventually
    inputJetCorrLabelAK7 = ('AK7PF', ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'])

else :
    process.GlobalTag.globaltag = 'START42_v12::All'
    inputJetCorrLabelAK5 = ('AK5PF', ['L1FastJet', 'L2Relative', 'L3Absolute'])
    inputJetCorrLabelAK7 = ('AK7PF', ['L1FastJet', 'L2Relative', 'L3Absolute'])

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options.wantSummary = True

##########
# Source #
##########

#process.load("RSGraviton.RSAnalyzer.Summer11.METBTag_Run2011A_May10ReReco")
#process.load("RSGraviton.RSAnalyzer.Summer11.METBTag_Run2011A_May10ReReco_triggerStudies")
#process.load("RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_PromptReco_2011Jun06")
#process.load("RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_PromptReco_2011Jun13")
#process.load("RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_PromptReco_2011Jun20")
#process.load("RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_PromptReco_2011Jun27")
#process.load("RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_PromptReco_2011Jul06")
#process.load("RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_PromptReco_2011Jul06")
#process.load("RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_PromptReco_v5")
#process.load("RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_PromptReco_v6_2011Ago26")
#process.load('RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_PromptReco_v6_2011Set30')
process.load('RSGraviton.RSAnalyzer.Summer11.MET_Run2011B_PromptReco')
#process.load('RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_ReReco_Aug5')
#process.load("RSGraviton.RSAnalyzer.Summer11.signal_RSG2000_ZZ2q2nu_cff")
#process.load("RSGraviton.RSAnalyzer.Summer11.WJets_pt100_cff")
#maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.maxEvents.input = numEvents         ##  (e.g. -1 to run on all events)
process.source.skipEvents=cms.untracked.uint32(skipEvents)

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
                                                  filterParams = pvSelector.clone( minNdof = cms.double(4.0), maxZ = cms.double(24.0) ),
                                                  src=cms.InputTag('offlinePrimaryVertices'),
                                                  filter = cms.bool(True)
                                                  )

process.noScraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )

process.load('CommonTools.RecoAlgos.HBHENoiseFilter_cfi')
# New recommendations for 50 ns bunch spacing
process.HBHENoiseFilter.minIsolatedNoiseSumE = cms.double(999999.)
process.HBHENoiseFilter.minNumIsolatedNoiseChannels = cms.int32(999999)
process.HBHENoiseFilter.minIsolatedNoiseSumEt = cms.double(999999.)

# Also Beam Halo
process.load('RecoMET.METAnalyzers.CSCHaloFilter_cfi')

process.preselection = cms.Sequence(process.goodOfflinePrimaryVertices +
                                    #process.vertexCounter +
                                    process.noScraping +
                                    process.HBHENoiseFilter +
                                    process.CSCTightHaloFilter)

###############################
########## Gen Setup ##########
###############################

### Keep some MC info
process.hardGenParticles = cms.EDProducer("GenParticlePruner",
                                          src = cms.InputTag("genParticles"),
                                          select = cms.vstring("drop  *  ", # this is the default
                                                               "keep status = 3"
                                                               )
                                          )

###############################
#### Jet RECO includes ########
###############################

from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.CaloJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
from RecoJets.JetProducers.CATopJetParameters_cfi import *

###############################
########## PF Setup ###########
###############################

# Default PF2PAT with AK5 jets. Make sure to turn ON the L1fastjet stuff. 
postfix = "PFlow"
jetAlgo="AK7"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=not useData, postfix=postfix)

# Top projections in PF2PAT
process.pfPileUpPFlow.Enable = True
process.pfPileUpPFlow.Vertices = 'goodOfflinePrimaryVertices'
process.pfPileUpPFlow.checkClosestZVertex = cms.bool(False)
process.pfNoMuonPFlow.enable = True 
process.pfNoElectronPFlow.enable = True 
process.pfNoJetPFlow.enable = True 
process.pfNoTauPFlow.enable = True

# Charged Hadron Subtraction
process.pfJetsPFlow.doAreaFastjet = True
process.pfJetsPFlow.doRhoFastjet = False
process.patJetCorrFactorsPFlow.payload = inputJetCorrLabelAK7[0]
process.patJetCorrFactorsPFlow.levels = inputJetCorrLabelAK7[1]
process.patJetCorrFactorsPFlow.rho = cms.InputTag("kt6PFJetsPFlow", "rho")

# turn to false when running on data
if useData :
    removeMCMatching( process, ['All'] )

###############################
###### Electron ID ############
###############################

# NOTE: ADDING THE ELECTRON IDs FROM CiC ----- USED WITH 42X 
process.load('RecoEgamma.ElectronIdentification.cutsInCategoriesElectronIdentificationV06_cfi')
process.eidCiCSequence = cms.Sequence(
    process.eidVeryLooseMC *
    process.eidLooseMC *
    process.eidMediumMC*
    process.eidTightMC *
    process.eidSuperTightMC *
    process.eidHyperTight1MC *
    process.eidHyperTight2MC *
    process.eidHyperTight3MC *
    process.eidHyperTight4MC
    )

for iele in [ process.patElectrons,
              process.patElectronsPFlow ] :
        iele.electronIDSources = cms.PSet(
            eidVeryLooseMC = cms.InputTag("eidVeryLooseMC"),
            eidLooseMC = cms.InputTag("eidLooseMC"),
            eidMediumMC = cms.InputTag("eidMediumMC"),
            eidTightMC = cms.InputTag("eidTightMC"),
            eidSuperTightMC = cms.InputTag("eidSuperTightMC"),
            eidHyperTight1MC = cms.InputTag("eidHyperTight1MC"),
            eidHyperTight2MC = cms.InputTag("eidHyperTight2MC"),
            eidHyperTight3MC = cms.InputTag("eidHyperTight3MC"),
            eidHyperTight4MC = cms.InputTag("eidHyperTight4MC")        
            )


###############################
###### Bare KT 0.6 jets #######
###############################

# Have to do this to get the Voronoi Areas
from RecoJets.JetProducers.kt4PFJets_cfi import kt4PFJets
process.kt6PFJetsPFlow = kt4PFJets.clone(
    rParam = cms.double(0.6),
    src = cms.InputTag('pfNoElectron'+postfix),
    doAreaFastjet = cms.bool(True),
    doRhoFastjet = cms.bool(True),
    voronoiRfact = cms.double(0.9)
    )

###############################
###### Jet Pruning Setup ######
###############################

# Pruned PF Jets
process.caPrunedPFlow = cms.EDProducer(
    "SubJetProducer",
    PFJetParameters.clone( src = cms.InputTag('pfNoElectron'+postfix),
                           doAreaFastjet = cms.bool(True),
                           doRhoFastjet = cms.bool(False)
                           ),
    AnomalousCellParameters,
    SubJetParameters,
    jetAlgorithm = cms.string("CambridgeAachen"),
    rParam = cms.double(0.8),
    jetCollInstanceName=cms.string("subjets")
    )
process.caPrunedPFlow.nSubjets = cms.int32(2)

# Put everything in sequence
for ipostfix in [postfix] :
    for module in (
        getattr(process,"kt6PFJets" + ipostfix),
        getattr(process,"caPruned" + ipostfix)
        ) :
        getattr(process,"patPF2PATSequence"+ipostfix).replace( getattr(process,"pfNoElectron"+ipostfix), getattr(process,"pfNoElectron"+ipostfix)*module )

# Use the good primary vertices everywhere. 
for imod in [process.patMuonsPFlow,
             process.patElectronsPFlow,
             process.patMuons,
             process.patElectrons] :
    imod.pvSrc = "goodOfflinePrimaryVertices"
    imod.embedTrack = True

addJetCollection(process, 
                 cms.InputTag('caPrunedPFlow'),         # Jet collection; must be already in the event when patLayer0 sequence is executed
                 'CA8Pruned', 'PF',
                 doJTA=True,            # Run Jet-Track association & JetCharge
                 doBTagging=True,       # Run b-tagging
                 jetCorrLabel=inputJetCorrLabelAK5,
                 doType1MET=False,
                 doL1Cleaning=False,
                 doL1Counters=False,
                 genJetCollection = cms.InputTag("ak7GenJetsNoNu"),
                 doJetID = False
                 )

for icorr in [process.patJetCorrFactors,process.patJetCorrFactorsCA8PrunedPF,] :
    icorr.rho = cms.InputTag("kt6PFJetsPFlow", "rho")

###############################
### TagInfo and Matching Setup#
###############################

# Do some configuration of the jet substructure things
for jetcoll in (process.patJetsPFlow,
                process.patJetsCA8PrunedPF,
                ) :
    if useData == False :
        jetcoll.addGenJetMatch = True
        jetcoll.embedGenJetMatch = True
        jetcoll.getJetMCFlavour = False
    # Add CATopTag info... piggy-backing on b-tag functionality
    jetcoll.addBTagInfo = True
    # Add the calo towers and PFCandidates.
    # I'm being a little tricksy here, because I only
    # actually keep the products if the "writeFat" switch
    # is on. However, this allows for overlap checking
    # with the Refs so satisfies most use cases without
    # having to add to the object size
    jetcoll.embedCaloTowers = True
    jetcoll.embedPFCandidates = True
    # never try to match gen partons
    jetcoll.addGenPartonMatch = False
    jetcoll.embedGenPartonMatch = False

###############################
#### Selections Setup #########
###############################

# AK5 Jets
process.selectedPatJetsPFlow.cut = cms.string("pt > 30 & abs(eta) < 2.4")
process.patJetsPFlow.addTagInfos = True
process.patJetsPFlow.tagInfoSources = cms.VInputTag(
    cms.InputTag("secondaryVertexTagInfosAODPFlow")
    )

# CA8 Pruned jets
process.selectedPatJetsCA8PrunedPF.cut = cms.string("pt > 30 & abs(eta) < 2.4")

# electrons
process.selectedPatElectrons.cut = cms.string('pt > 10.0 & abs(eta) < 2.5')
process.patElectrons.embedTrack = cms.bool(True)
process.selectedPatElectronsPFlow.cut = cms.string('pt > 10.0 & abs(eta) < 2.5')
process.patElectronsPFlow.embedTrack = cms.bool(True)
# muons
process.selectedPatMuons.cut = cms.string('pt > 10.0 & abs(eta) < 2.5')
process.patMuons.embedTrack = cms.bool(True)
process.selectedPatMuonsPFlow.cut = cms.string("pt > 10.0 & abs(eta) < 2.5")
process.patMuonsPFlow.embedTrack = cms.bool(True)
# taus
process.selectedPatTausPFlow.cut = cms.string("pt > 10.0 & abs(eta) < 3")
process.selectedPatTaus.cut = cms.string("pt > 10.0 & abs(eta) < 3")
process.patTausPFlow.isoDeposits = cms.PSet()
process.patTaus.isoDeposits = cms.PSet()
# photons
process.patPhotonsPFlow.isoDeposits = cms.PSet()
process.patPhotons.isoDeposits = cms.PSet()

# Apply jet ID to all of the jets upstream. We aren't going to screw around
# with this, most likely. So, we don't really to waste time with it
# at the analysis level.
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
process.goodPatJetsPFlow = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                        filterParams = pfJetIDSelector.clone(),
                                        src = cms.InputTag("selectedPatJetsPFlow"),
                                        )
process.goodPatJetsCA8PrunedPF = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                              filterParams = pfJetIDSelector.clone(),
                                              src = cms.InputTag("selectedPatJetsCA8PrunedPF")
                                              )

# A cut to make small
process.cutOnJet = cms.EDFilter("CandViewSelector",
                                src = cms.InputTag("goodPatJetsPFlow"),
                                cut = cms.string("(pt > 110.0) && (abs(eta) < 2.4)"),
                                minNumber = cms.int32(1),
                                filter = cms.bool(True)
                                )

# Weights
process.pileupReweighter= cms.EDFilter("RSPileupReweighter",
                                       generatedFile = cms.string("pileup_Wjets.root"),
                                       dataFile = cms.string("Pileup_2011_EPS_8_jul.root"),
                                       genHistName = cms.string("pileup"),
                                       dataHistName = cms.string("pileup"),
                                       useROOThistos = cms.bool(False)
                                       )

process.patseq = cms.Sequence(
    process.preselection*
    getattr(process,"patPF2PATSequence"+postfix)*
    process.patDefaultSequence*
    process.goodPatJetsPFlow*
    process.goodPatJetsCA8PrunedPF*
    process.cutOnJet
    )

if(useData==False) :
    process.patseq.replace( process.goodOfflinePrimaryVertices,
                            process.goodOfflinePrimaryVertices *
                            process.hardGenParticles *
                            process.pileupReweighter)
    
process.patseq.replace( process.goodOfflinePrimaryVertices,
                        process.goodOfflinePrimaryVertices *
                        process.eidCiCSequence )

process.p0 = cms.Path(
    process.patseq
    )

process.out.SelectEvents.SelectEvents = cms.vstring('p0')

# rename output file
name = "temp.root"
process.out.fileName = cms.untracked.string(name)
process.out.dropMetaData = cms.untracked.string("DROPPED")

process.source.inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")

process.out.outputCommands = cms.untracked.vstring('drop *',
                                                   'keep *_TriggerResults_*_*',
                                                   'keep recoTracks_generalTracks_*_*',
                                                   'keep recoPFCandidates_particleFlow__*',
                                                   'keep *_goodOfflinePrimaryVertices*_*_*',    
                                                   'keep *_selectedPat*CA8PrunedPF_*_*',
                                                   'keep *_selectedPat*PFlow_*_*',
                                                   'keep *_goodPat*CA8PrunedPF_*_*',
                                                   'keep *_goodPat*PFlow_*_*',
                                                   'keep *_patMETsPFlow_*_*',
                                                   )

if(useData==False):
    process.out.outputCommands += ['keep *_hardGenParticles_*_*',
                                   'keep *_ak7GenJetsNoNu_*_*',
                                   'keep GenRunInfoProduct_generator_*_*',
                                   'keep GenEventInfoProduct_generator_*_*',
                                   'keep PileupSummaryInfos_*_*_*',
                                   'keep *_pileupReweighter_*_*',
                                   ]
    
#open('junk.py','w').write(process.dumpPython())
