#####################################
# CMSSW configuration file - Python #
#####################################

import FWCore.ParameterSet.Config as cms
import datetime

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################
today = str(datetime.date.today())
fileLabel = ''

# Source
process.load("RSGraviton.RSAnalyzer.Summer08_RS1000WW_redigi_cfi")
process.maxEvents.input = 100

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('results_'+fileLabel+today+'.root')
                                   )

#process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as jethistos

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
            
process.outgoingPartons = cms.EDFilter("PdgIdAndStatusCandViewSelector",
                                       src = cms.InputTag("genParticles"),
                                       pdgId = cms.vint32(1,2,3,4,5,6,-1,-2,-3,-4,-5,-6,21),
                                       status = cms.vint32(3)
                                       )
process.hardestPartons = cms.EDFilter("LargestPtCandViewSelector",
                                      src = cms.InputTag("outgoingPartons"),
                                      maxNumber = cms.uint32(1)
                                      )

process.plotPartons = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                     src = cms.InputTag("hardestPartons"),
                                     histograms = cms.VPSet(cms.PSet(
                                         nbins = cms.untracked.int32(100),
                                         description = cms.untracked.string('parton_pt'),
                                         plotquantity = cms.untracked.string('pt'),
                                         min = cms.untracked.double(0.0),
                                         max = cms.untracked.double(500.0),
                                         name = cms.untracked.string('parton_pt')
                                         )
                                                            )
                                     )
# Paths
process.p1 = cms.Path(process.outgoingPartons+process.hardestPartons+process.plotPartons)
