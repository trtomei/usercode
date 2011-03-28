#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms
import sys
process = cms.Process("COUNT")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

if 'input' in sys.argv:
    myInput = sys.argv[sys.argv.index('input')+1]

process.load("RSGraviton.RSAnalyzer.Fall10."+myInput+"_cff")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )
