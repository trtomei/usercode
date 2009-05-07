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
# Second moments 
    cms.PSet(
        nbins = cms.untracked.int32(100),
        description = cms.untracked.string('jet_%d_etaeta'),
        plotquantity = cms.untracked.string('etaetaMoment'),
        min = cms.untracked.double(0.0),
        max = cms.untracked.double(1.0),
        itemsToPlot = cms.untracked.int32(4),
        name = cms.untracked.string('jet_%d_etaeta')
    ), 
    cms.PSet(
        nbins = cms.untracked.int32(100),
        description = cms.untracked.string('jet_%d_etaphi'),
        plotquantity = cms.untracked.string('etaphiMoment'),
        min = cms.untracked.double(0.0),
        max = cms.untracked.double(1.0),
        itemsToPlot = cms.untracked.int32(4),
        name = cms.untracked.string('jet_%d_etaphi')
    ), 
    cms.PSet(
        nbins = cms.untracked.int32(100),
        description = cms.untracked.string('jet_%d_phiphi'),
        plotquantity = cms.untracked.string('phiphiMoment'),
        min = cms.untracked.double(0.0),
        max = cms.untracked.double(1.0),
        itemsToPlot = cms.untracked.int32(4),
        name = cms.untracked.string('jet_%d_phiphi')
     ),
# Hadronic, EM energy fraction, number of constituents
    cms.PSet(
        nbins = cms.untracked.int32(100),
        description = cms.untracked.string('jet_%d_HADFrac'),
        plotquantity = cms.untracked.string('energyFractionHadronic'),
        min = cms.untracked.double(0.0),
        max = cms.untracked.double(1.0),
        itemsToPlot = cms.untracked.int32(4),
        name = cms.untracked.string('jet_%d_HADFrac')
    ),
    cms.PSet(
        nbins = cms.untracked.int32(100),
        description = cms.untracked.string('jet_%d_EMFrac'),
        plotquantity = cms.untracked.string('emEnergyFraction'),
        min = cms.untracked.double(0.0),
        max = cms.untracked.double(1.0),
        itemsToPlot = cms.untracked.int32(4),
        name = cms.untracked.string('jet_%d_EMFrac')
     ),
     cms.PSet(
         nbins = cms.untracked.int32(100),
         description = cms.untracked.string('jet_%d_n90'),
         plotquantity = cms.untracked.string('n90'),
         min = cms.untracked.double(-0.5),
         max = cms.untracked.double(99.5),
         itemsToPlot = cms.untracked.int32(4),
         name = cms.untracked.string('jet_%d_n90')
     ),
     cms.PSet(
         nbins = cms.untracked.int32(100),
         description = cms.untracked.string('jet_%d_n60'),
         plotquantity = cms.untracked.string('n60'),
         min = cms.untracked.double(-0.5),
         max = cms.untracked.double(99.5),
         itemsToPlot = cms.untracked.int32(4),
         name = cms.untracked.string('jet_%d_n60')
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

