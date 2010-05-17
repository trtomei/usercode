import FWCore.ParameterSet.Config as cms

histograms = cms.VPSet(cms.PSet(
    nbins = cms.untracked.int32(200),
    description = cms.untracked.string('Z_pt'),
    plotquantity = cms.untracked.string('pt'),
    min = cms.untracked.double(0.0),
    max = cms.untracked.double(1000.0),
    name = cms.untracked.string('Z_pt')
), 
    cms.PSet(
        nbins = cms.untracked.int32(100),
        description = cms.untracked.string('Z_eta'),
        plotquantity = cms.untracked.string('eta'),
        min = cms.untracked.double(-4.0),
        max = cms.untracked.double(4.0),
        name = cms.untracked.string('Z_eta')
    ), 
    cms.PSet(
        nbins = cms.untracked.int32(80),
        description = cms.untracked.string('Z_mass'),
        plotquantity = cms.untracked.string('mass'),
        min = cms.untracked.double(0.0),
        max = cms.untracked.double(400.0),
        name = cms.untracked.string('Z_mass')
    ))

