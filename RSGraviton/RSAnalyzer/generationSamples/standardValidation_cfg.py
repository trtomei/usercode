import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("VALIDATION")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.genParticles.abortOnUnknownPDGCode = False
process.genParticles.excludeUnfragmentedClones = cms.bool(True)

tag = ''
numEvents = -1

if 'input' in sys.argv:
    tag = sys.argv[sys.argv.index('input')+1]
if 'numEvents' in sys.argv:
    numEvents = int(sys.argv[sys.argv.index('numEvents')+1])

process.load("RSGraviton.RSAnalyzer.Fall10."+tag+"_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(numEvents)
    )

gravPdgId = 5000039

# Pruning for Pythia
process.prunedGenParticles = cms.EDProducer("GenParticlePruner",
                                            src = cms.InputTag("genParticles"),
                                            select = cms.vstring("drop  *  ", # this is the default
                                                                 "keep status = 3",
                                                                 "keep pdgId = "+str(gravPdgId)+" & status = 3",
                                                                 "keep+ pdgId = 23 & status = 3",
                                                                "drop pdgId = 23 & status = 2"
                                                               )
                                            )

# Pruning for Herwig
#process.prunedGenParticles = cms.EDProducer("GenParticlePruner",
#                                            src = cms.InputTag("genParticles"),
#                                            select = cms.vstring("drop  *  ", # this is the default
#                                                                 "keep status = 3",
#                                                                 "keep pdgId = "+str(gravPdgId)+" & numberOfDaughters = 2",
#                                                                 "keep+ pdgId = 23 & numberOfDaughters = 2",
#                                                                 )
#                                            )

process.gravitons = cms.EDFilter("PdgIdAndStatusCandViewSelector",
                                   src = cms.InputTag("prunedGenParticles"),
                                   pdgId = cms.vint32( gravPdgId ),
                                   status = cms.vint32(3)
                                   )
process.Zbosons = cms.EDFilter("PdgIdCandViewSelector",
                                 src = cms.InputTag("prunedGenParticles"),
                                 pdgId = cms.vint32( 23 )
                                 )

process.eventCounter = cms.EDAnalyzer("EventCounter")

process.sortedJets = cms.EDFilter("LargestEtGenJetSelector",
                                  src = cms.InputTag("ak7GenJets"),
                                  maxNumber = cms.uint32(1)
                                  )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("validation_pythia"+tag+".root")
                                   )

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

process.plotGraviton = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                      src = cms.InputTag("gravitons"),
                                      histograms = Ghistos
                                      )

process.plotZBosons = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                     src = cms.InputTag("Zbosons"),
                                     histograms = Zhistos
                                     )
process.plotJets = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                  src = cms.InputTag("sortedJets"),
                                  histograms = Zhistos
                                  )

process.analyzer = cms.EDAnalyzer("RSGenEventAnalyzer",
                                  gravPdgId = cms.int32(gravPdgId),
                                  qqbarProcess = cms.bool(True),
                                  allProcesses = cms.bool(True) # This makes the above void.
                                  )

########
# In case we want it.
process.printList = cms.EDAnalyzer("ParticleListDrawer",
                                   maxEventsToPrint = cms.untracked.int32(10),
                                   printVertex = cms.untracked.bool(False),
                                   src = cms.InputTag("prunedGenParticles")
                                   )
process.printDecay = cms.EDAnalyzer("ParticleDecayDrawer",
                                    src = cms.InputTag("genParticles"),
                                    printP4 = cms.untracked.bool(False),
                                    printPtEtaPhi = cms.untracked.bool(False),
                                    printVertex = cms.untracked.bool(False)
                                    )
process.printTree = cms.EDAnalyzer("ParticleTreeDrawer",
                                   src = cms.InputTag("genParticles"),
                                   printP4 = cms.untracked.bool(False),
                                   printPtEtaPhi = cms.untracked.bool(False),
                                   printVertex = cms.untracked.bool(False),
                                   printStatus = cms.untracked.bool(False),
                                   printIndex = cms.untracked.bool(False),
                                   status = cms.untracked.vint32( 2,3 )
                                   )
process.printDecay = cms.EDAnalyzer("ParticleDecayDrawer",
                                    src = cms.InputTag("genParticles"),
                                    printP4 = cms.untracked.bool(False),
                                    printPtEtaPhi = cms.untracked.bool(False),
                                    printVertex = cms.untracked.bool(False)
                                    )

########

#process.goodDecays = cms.EDFilter("ZZDecayFilter",verbose=cms.bool(False))
process.load("RecoJets.Configuration.GenJetParticles_cff")
process.load("RecoJets.Configuration.RecoGenJets_cff")
process.load("RecoMET.Configuration.GenMETParticles_cff")
process.load("RecoMET.Configuration.RecoGenMET_cff")
process.doThings = cms.Sequence(process.genParticlesForJets + process.sisCone7GenJets +
                                process.genParticlesForMETAllVisible + process.genMetTrue)
#process.printer = cms.Path(process.genParticles + process.prunedGenParticles*process.printList)
process.p = cms.Path(#process.goodDecays +
#                     process.genParticles +
#                     process.doThings +                  
#                     process.eventCounter +                 
                     process.prunedGenParticles +
#                     process.printList )#+ 
#                      process.printDecay )
    (process.gravitons + process.Zbosons + process.sortedJets) +
    (process.plotGraviton + process.plotZBosons + process.plotJets) +
#    process.printList)
    process.analyzer)
