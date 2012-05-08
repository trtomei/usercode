import FWCore.ParameterSet.Config as cms
import sys
process = cms.Process("COUNT")

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring("file:electronMuon.root",
                                                              )
)
process.load('RSGraviton.RSAnalyzer.Summer11.WJets_pt100_cff')

process.printDecay = cms.EDAnalyzer("ParticleDecayDrawer",
                                    src = cms.InputTag("genParticles")
                                   )

process.p = cms.Path(process.printDecay)
