#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms
import sys
process = cms.Process("COUNT")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.load('RSGraviton.RSAnalyzer.Summer11.METBTag_Run2011A_May10ReReco')
#fileList = cms.untracked.vstring('file:pattuple_Run2010Bp2_HLTMET45.root')
#process.source = cms.Source("PoolSource",fileNames = fileList)

# Good lumis
#import PhysicsTools.PythonAnalysis.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#myLumis = LumiList.LumiList(filename = 'Run2010B_p2.json').getCMSSWString().split(',')
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#process.source.lumisToProcess.extend(myLumis)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )
