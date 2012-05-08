import FWCore.ParameterSet.Config as cms

VBTFmuons = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("selectedPatMuonsPFlow"),
                         cut = cms.string("pt > 20.0 && "+
                                          "abs(eta) < 2.1 && "+
                                          "muonID('GlobalMuonPromptTight') &&"+
                                          "numberOfMatches > 1 &&  "+
                                          "track.numberOfValidHits > 10 && track.hitPattern.numberOfValidPixelHits > 0 && "+
                                          "abs(dB) < 0.2 && " +
                                          "(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt < 0.15"
                                          )
                         )

print VBTFmuons.cut

leadingMuon = cms.EDFilter("LargestPtCandViewSelector",
                           src = cms.InputTag("VBTFmuons"),
                           maxNumber = cms.uint32(1)
                           )

muonSequence = cms.Sequence(VBTFmuons + leadingMuon)
