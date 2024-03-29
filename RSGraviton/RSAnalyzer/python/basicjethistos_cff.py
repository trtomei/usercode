import FWCore.ParameterSet.Config as cms

histograms = cms.VPSet(cms.PSet(
# Basic kinematics
    nbins = cms.untracked.int32(100),
    description = cms.untracked.string('jet_%d_et'),
    plotquantity = cms.untracked.string('et'),
    min = cms.untracked.double(0.0),
    max = cms.untracked.double(1000.0),
    itemsToPlot = cms.untracked.int32(4),
    name = cms.untracked.string('jet_%d_et')
    ), 
    cms.PSet(
        nbins = cms.untracked.int32(100),
        description = cms.untracked.string('jet_%d_eta'),
        plotquantity = cms.untracked.string('eta'),
        min = cms.untracked.double(-4.0),
        max = cms.untracked.double(4.0),
        itemsToPlot = cms.untracked.int32(4),
        name = cms.untracked.string('jet_%d_eta')
    ), 
    cms.PSet(
        nbins = cms.untracked.int32(100),
        description = cms.untracked.string('jet_%d_pt'),
        plotquantity = cms.untracked.string('pt'),
        min = cms.untracked.double(0.0),
        max = cms.untracked.double(1000.0),
        itemsToPlot = cms.untracked.int32(4),
        name = cms.untracked.string('jet_%d_pt')
    ), 
# Jet mass
     cms.PSet(
        nbins = cms.untracked.int32(120),
        description = cms.untracked.string('jet_%d_mass'),
        plotquantity = cms.untracked.string('mass'),
        min = cms.untracked.double(0.0),
        max = cms.untracked.double(300.0),
        itemsToPlot = cms.untracked.int32(4),
        name = cms.untracked.string('jet_%d_mass')
    ))

