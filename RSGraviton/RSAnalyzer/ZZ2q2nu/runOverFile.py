#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms
import sys
process = cms.Process("COUNT")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

fileList = cms.untracked.vstring('/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0098/DE650923-D11D-E011-9E15-485B39800C36.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0098/B802E214-D11D-E011-8090-90E6BA19A205.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0098/B2CB5925-D11D-E011-8E05-90E6BA19A1F9.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0098/724D453E-D11D-E011-9C36-485B39800B75.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0098/60E04724-D11D-E011-8158-E0CB4E19F969.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/EE7DFBFB-CA1C-E011-A599-E0CB4E29C505.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/E259CDA4-CB1C-E011-B7AC-0030487CDA68.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/E251BF6F-CB1C-E011-9D58-001EC9D87221.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/822253AC-CB1C-E011-A411-90E6BA442F07.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/60107C71-CB1C-E011-B555-485B39800C39.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/4AB488D7-CA1C-E011-8727-90E6BA19A205.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/48A25D89-CB1C-E011-9F12-0019BB3F834E.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/481180DA-CA1C-E011-A75B-E0CB4E55363A.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/2A1BBC57-CB1C-E011-A71F-90E6BA442F0A.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/24E00077-CB1C-E011-B341-485B39800BED.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/1EE7C457-CB1C-E011-A2E7-90E6BA442F0A.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/0C326871-CB1C-E011-8759-E0CB4E55366B.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/08A7FAA4-CB1C-E011-826D-90E6BA442F0B.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0088/06355B7C-CB1C-E011-96E4-90E6BA442F3E.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0082/84A75ADA-5F1C-E011-AB74-485B39800BF3.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0082/3E3385A9-611C-E011-B017-E0CB4EA0A909.root',
                                 '/store/data/Run2010B/JetMETTauMonitor/AOD/Dec22ReReco_v1/0080/E0151B98-531C-E011-86DA-E0CB4EA0A91A.root'
                                 )

#fileList = cms.untracked.vstring('file:pattuple_Run2010Bp2_HLTMET45.root')
process.source = cms.Source("PoolSource",fileNames = fileList)

# Good lumis
import PhysicsTools.PythonAnalysis.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
myLumis = LumiList.LumiList(filename = 'Run2010B_p2.json').getCMSSWString().split(',')
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
process.source.lumisToProcess.extend(myLumis)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )
