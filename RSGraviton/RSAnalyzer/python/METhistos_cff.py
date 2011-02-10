import FWCore.ParameterSet.Config as cms

histograms = cms.VPSet(
    cms.PSet(nbins = cms.untracked.int32(500),
             description = cms.untracked.string('MET'),
             plotquantity = cms.untracked.string('et'),
             min = cms.untracked.double(0.0),
             max = cms.untracked.double(5000.0),
             name = cms.untracked.string('MET')
             ),
    cms.PSet(nbins = cms.untracked.int32(500),
             description = cms.untracked.string('METpt'),
             plotquantity = cms.untracked.string('pt'),
             min = cms.untracked.double(0.0),
             max = cms.untracked.double(5000.0),
             name = cms.untracked.string('METpt')
             ),
    cms.PSet(nbins = cms.untracked.int32(72),
             description = cms.untracked.string('MET phi'),
             plotquantity = cms.untracked.string('phi'),
             min = cms.untracked.double(-3.141592),
             max = cms.untracked.double(3.141592),
             name = cms.untracked.string('MET_phi')
             )
    )
