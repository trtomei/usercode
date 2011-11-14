#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("SKIM")

###########################
# Basic process controls. #
###########################

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.EventContent.EventContent_cff')
#process.load("Configuration.StandardSequences.Geometry_cff")
#process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery=1000
# Summary
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output.root')
                                   )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FED96BE1-859A-E011-836E-001A92971B56.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FED7DD5E-9D9A-E011-A3BD-002618943954.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FEA0438B-7E9A-E011-AD8A-001A92971B64.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FE914DE9-9C9B-E011-BC85-0026189438E3.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FE814A47-C09B-E011-B839-00261894388A.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FE35D041-B49B-E011-AFAE-0018F3D09626.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FE15CD1A-969A-E011-9657-002354EF3BDD.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FE0895E0-889A-E011-AA9F-00248C0BE018.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FCFC3343-EF9A-E011-BC18-0018F3D096D8.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FCDE863D-759A-E011-BFD4-003048679168.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FAD210CF-499A-E011-BC91-002354EF3BD0.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FA94F02C-EA9A-E011-B0C7-0018F3D09676.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FA6B1A31-959A-E011-877D-0018F3D0961A.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FA2A96DB-E69A-E011-8DA5-0018F3D095FA.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FA17D9E0-C49B-E011-B0AB-001A92810ACA.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FA15BF3C-7C9A-E011-A262-003048678B86.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/FA152E41-DB9A-E011-8D3E-0018F3D095FA.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/F8DD7940-C49B-E011-8085-00304867D446.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/F8C0B0DB-F19A-E011-B4B9-0018F3D0964A.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/F89940FA-889A-E011-99D5-0018F3D09628.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/F8799B8A-A99A-E011-9362-0018F3D0961A.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/F86EAFC1-B49A-E011-B963-00261894387D.root',
                  '/store/mc/Summer11/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0001/F85F474D-9A9B-E011-95B5-001A92811736.root'
           )
                            )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

### The output
#process.TFileService = cms.Service("TFileService",
#                                   fileName = cms.string('output.root')
#                                   )

#process.Tracer = cms.Service("Tracer")

# Global tag
#process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_R_42_V14::All'

###########
# Weights #
###########
process.pileupAnalyzer = cms.EDFilter("RSPileupSummaryInfoAnalyzer",
                                        pileupInfo = cms.InputTag("addPileupInfo")
                                        )

process.p = cms.Path(process.pileupAnalyzer)
