import FWCore.ParameterSet.Config as cms

process = cms.Process("ANA")

process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.categories.append('TriggerSummaryAnalyzerAOD')
process.MessageLogger.categories.append('TriggerSummaryAnalyzerRAW')
process.MessageLogger.categories.append('HLTEventAnalyzerAOD')
process.MessageLogger.categories.append('HLTEventAnalyzerRAW')
process.MessageLogger.categories.append('L1GtTrigReport')
process.MessageLogger.categories.append('HLTrigReport')
process.MessageLogger.categories.append('HLTSummaryFilter')
process.MessageLogger.categories.append('HLTConfigProvider')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring('file:pattuple_signalm1000_PU.root')
                            )

process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True) ## default is false
        )

process.load( "HLTrigger.HLTanalyzers.hlTrigReport_cfi" )
process.hlTrigReport.HLTriggerResults   = cms.InputTag("TriggerResults", "", "PAT")
process.hlTrigReport.ReferencePath      = cms.untracked.string( "p0" )
process.hlTrigReport.ReferenceRate      = cms.untracked.double( 1.0 )
process.hlTrigReport.ReportEvery        = cms.string("run")

process.aom = cms.OutputModule("AsciiOutputModule")

process.final = cms.EndPath(process.hlTrigReport+process.aom)#+process.eca)
