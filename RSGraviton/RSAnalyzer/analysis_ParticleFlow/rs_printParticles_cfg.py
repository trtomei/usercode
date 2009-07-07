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
process.maxEvents.input = 10

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

#process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as jethistos

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
            
process.printTree = cms.EDAnalyzer("ParticleListDrawer",
                                   maxEventsToPrint = cms.untracked.int32(1),
                                   src = cms.InputTag("genParticles")
                                   )
# Paths
process.p1 = cms.Path(process.printTree)
