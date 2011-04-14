import FWCore.ParameterSet.Config as cms

MCelectrons = cms.EDFilter("PdgIdAndStatusCandViewSelector",
                                   src = cms.InputTag("genParticles"),
                                   pdgId = cms.vint32( 11 ),
                                   status = cms.vint32( 3 ),
                                   filter = cms.bool(True)
                                   )

MCmuons = MCelectrons.clone(pdgId = cms.vint32(13))
MCtaus = MCelectrons.clone(pdgId = cms.vint32(15))
