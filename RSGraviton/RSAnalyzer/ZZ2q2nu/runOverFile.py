#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms
import sys
process = cms.Process("COUNT")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.load('RSGraviton.RSAnalyzer.Summer11.MET_Run2011B_PromptReco')
for i in process.source.fileNames:
    print i
#process.load('RSGraviton.RSAnalyzer.Summer11.signal_RSG1250_ZZ2q2nu_cff')
#process.load('RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_ReReco_Aug5')
#process.load('RSGraviton.RSAnalyzer.Summer11.MET_Run2011A_PromptReco_v6_2011Set30')
#process.load('RSGraviton.RSAnalyzer.Summer11.WJets_pt100_cff')
#process.load("RSGraviton.RSAnalyzer.Summer11.signal_RSG1000_ZZ2q2nu_cff")

# Good lumis
import PhysicsTools.PythonAnalysis.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
myLumis = LumiList.LumiList(filename = 'pickevents.json').getCMSSWString().split(',')
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#process.source.lumisToProcess.extend(myLumis)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.Out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string ("pickevents_pattuple.root")
                               )
 
#process.End = cms.EndPath(process.Out)
