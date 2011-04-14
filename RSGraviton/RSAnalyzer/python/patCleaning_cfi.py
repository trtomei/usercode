import FWCore.ParameterSet.Config as cms

cleanPatMuonsPFlow = cms.EDProducer("PATMuonCleaner",
                                    src = cms.InputTag("selectedPatMuonsPFlow"),
                                    # preselection (any string-based cut for pat::Muon)
                                    preselection = cms.string(''),
                                    # overlap checking configurables
                                    checkOverlaps = cms.PSet(),
                                    # finalCut (any string-based cut for pat::Muon)
                                    finalCut = cms.string(''),
                                    )

cleanPatElectronsPFlow = cms.EDProducer("PATElectronCleaner",
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

cleanPatJetsPFlow = cms.EDProducer("PATJetCleaner",
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
cleanPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
                                          logName = cms.untracked.string("cleanPatCandidates|PATSummaryTables"),
                                          candidates = cms.VInputTag(cms.InputTag("cleanPatElectronsPFlow"),
                                                                     cms.InputTag("cleanPatMuonsPFlow"),
                                                                     cms.InputTag("cleanPatJetsPFlow"),
                                                                     )
                                          )


cleanPatCandidatesPFlow = cms.Sequence(
    cleanPatMuonsPFlow     *        # NOW WE MUST USE '*' AS THE ORDER MATTERS
    cleanPatElectronsPFlow *
    cleanPatJetsPFlow     *
    cleanPatCandidateSummary
    )
