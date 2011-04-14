import FWCore.ParameterSet.Config as cms

jetIdCut = cms.EDFilter("PATJetSelector",
                        src = cms.InputTag("cleanPatJetsPFlow"),
                        cut = cms.string("(neutralHadronEnergyFraction < 0.99) &&"+
                                         "(neutralEmEnergyFraction < 0.99) &&"+
                                         "(numberOfDaughters > 1) &&"+
                                         "(chargedHadronEnergyFraction > 0) &&"+
                                         "(chargedMultiplicity > 0) &&"+
                                         "(chargedEmEnergyFraction < 0.99)"
                                         )
                        )
