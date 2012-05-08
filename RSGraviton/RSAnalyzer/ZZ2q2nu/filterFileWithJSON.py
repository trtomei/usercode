#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms
import sys
process = cms.Process("FILTER")

myOptions = sys.argv

if "inputFileName" in myOptions:
    inputFileName = myOptions[myOptions.index('inputFileName')+1]
if "inputJSONFile" in myOptions:
    inputJSONFile = myOptions[myOptions.index('inputJSONFile')+1]
                                        
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( ['file:'+inputFileName] )

# Good lumis
import PhysicsTools.PythonAnalysis.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
myLumis = LumiList.LumiList(filename = inputJSONFile).getCMSSWString().split(',')
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
process.source.lumisToProcess.extend(myLumis)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.Out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string ("output_filtered.root")
                               )
 
process.End = cms.EndPath(process.Out)
