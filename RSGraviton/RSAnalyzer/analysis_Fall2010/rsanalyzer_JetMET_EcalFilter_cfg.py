#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("CHECK")

###########################
# Basic process controls. #
###########################

##################
# Basic services #
##################
# import of standard configurations
process.load('Configuration.EventContent.EventContent_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')


readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles, noEventSort = cms.untracked.bool(True))
#readFiles.extend( [
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/F4A840A8-6CCC-DF11-A218-A4BADB3D00FF.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/9A07F077-3DCD-DF11-A190-003048C9CA8E.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/62AC2F3D-68CC-DF11-99A1-001E682F8738.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/4C699E75-3CCD-DF11-B294-0030487CAA5D.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/2A6004A3-3DCD-DF11-B959-00238BBDEAF7.root',
#    '/store/mc/Fall10/RSGravitonToZZToNuNuJJ_M-1000_7TeV-pythia6/AODSIM/START38_V12-v1/0013/1A64EBE3-72CC-DF11-BA19-E0CB4E29C4DB.root' ] );

readFiles.extend(['file:/home/trtomei/storage/data/skimming/METFwd_Run2010B-Nov4ReReco_v1/selectedHBHEAndTrigger.root'])

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output.root')
)

from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

##########
# Jet ID #
##########
process.jetIdCut = cms.EDFilter("RSJetIdSelector",
                                jets = cms.InputTag("ak7CaloJets"),
                                jetID = cms.InputTag("ak7JetID"),
                                threshold = cms.double(30.0),
                                filter = cms.bool(False),
                                tightQuality = cms.bool(False)
                                )

###############
# Corrections #
###############
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.ak7CaloL2Relative.useCondDB = False
process.ak7CaloL3Absolute.useCondDB = False
process.ak7CaloResidual.useCondDB = False
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('ak7CaloL2L3')
                                             )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

##################
# Kinematic cuts #
##################
process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDFilter("LargestPtCaloJetSelector",
                                     src = cms.InputTag("oneJetAboveZero"),
                                     maxNumber = cms.uint32(1)
                                     )

process.etaCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("(eta < 2.4) & (eta > -2.4)"),
                              minNumber = cms.int32(1),
                              )

process.EMFCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("(emEnergyFraction > 0.1) & (emEnergyFraction < 0.9)"),
                              minNumber = cms.int32(1),
                              )


process.plotNormalJets = cms.EDAnalyzer("CaloJetHistoAnalyzer",
                                        src = cms.InputTag("getLargestJet"),
                                        histograms = jethistos
                                        )
process.plotHotJets = cms.EDAnalyzer("CaloJetHistoAnalyzer",
                                     src = cms.InputTag("getLargestJet"),
                                     histograms = jethistos
                                     )
process.deepNormalJets = cms.EDAnalyzer("RSJetIdAnalyzer",
                                        jet = cms.InputTag("getLargestJet"),
                                        originalJets = cms.InputTag("ak7CaloJets"),
                                        jetID = cms.InputTag("ak7JetID")
                                        )
process.deepHotJets = cms.EDAnalyzer("RSJetIdAnalyzer",
                                     jet = cms.InputTag("getLargestJet"),
                                     originalJets = cms.InputTag("ak7CaloJets"),
                                     jetID = cms.InputTag("ak7JetID")
                                     )
                                        
# Path
process.load('UserCode.EcalDeadCellEventFilter.ecalDeadCellEventFilter_cfi')

process.EcalAnomalousEventFilter = cms.EDFilter('EcalAnomalousEventFilter',
                                                EBRecHitsLabel = cms.untracked.InputTag("reducedEcalRecHitsEB"),
                                                EERecHitsLabel = cms.untracked.InputTag("reducedEcalRecHitsEE"),
                                                FilterAlgo= cms.untracked.string("FilterMode"),
                                                #the following parameters skimGap,skimSingle, skimDead are only used in TuningMode
                                                #switch bool to True to turn on filter: only Events with chosen signature pass, otherwise all events pass
                                                skimGap  = cms.untracked.bool(False),
                                                skimSingle  = cms.untracked.bool(False),
                                                skimDead  = cms.untracked.bool(False),
                                                #cuts for finding Single RecHits/Ecal Spikes
                                                #max. boundary energy around RecHit (fraction of RecHits energy!)
                                                cutBoundEnergyPctEB_SingleRecHit=cms.untracked.double(0.02),
                                                cutBoundEnergyPctEE_SingleRecHit=cms.untracked.double(0.02),
                                                #max. boundary energy around RecHit (abs value)
                                                cutBoundEnergyAbsEB_SingleRecHit=cms.untracked.double(5),
                                                cutBoundEnergyAbsEE_SingleRecHit=cms.untracked.double(5),
                                                #min. energy of RecHit (abs value)
                                                cutEnergyEB_SingleRecHit=cms.untracked.double(5),
                                                cutEnergyEE_SingleRecHit=cms.untracked.double(5),
                                                #cuts for finding energy deposit near Gaps
                                                #min. boundary energy (RecHit next to Gap) (abs value)
                                                cutBoundEnergyGapEE=cms.untracked.double(10),
                                                cutBoundEnergyGapEB=cms.untracked.double(10),
                                                #####CUTS FOR DEAD CELL STUDY
                                                #cuts for finding energy deposit near dead region
                                                #min. boundary energy (RecHits next to Dead Region) (abs value)
                                                cutBoundEnergyDeadCellsEB=cms.untracked.double(5),
                                                cutBoundEnergyDeadCellsEE=cms.untracked.double(5),
                                                #############CUT USED FOR 'FilterMode' only, together with 'cutBoundEnergyDeadCellsEB'
                                                minDeadClusterSizeForFilterMode=cms.untracked.double(24)
                                                )

process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("corMetGlobalMuons"),
                                 histograms = cms.VPSet(cms.PSet(nbins = cms.untracked.int32(500),
                                                                 description = cms.untracked.string('MET'),
                                                                 plotquantity = cms.untracked.string('et'),
                                                                 min = cms.untracked.double(0.0),
                                                                 max = cms.untracked.double(1000.0),
                                                                 name = cms.untracked.string('MET')
                                                                 ),
                                                        cms.PSet(nbins = cms.untracked.int32(500),
                                                                 description = cms.untracked.string('METpt'),
                                                                 plotquantity = cms.untracked.string('pt'),
                                                                 min = cms.untracked.double(0.0),
                                                                 max = cms.untracked.double(1000.0),
                                                                 name = cms.untracked.string('METpt')
                                                                 ),
                                                        cms.PSet(nbins = cms.untracked.int32(72),
                                                                 description = cms.untracked.string('MET phi'),
                                                                 plotquantity = cms.untracked.string('phi'),
                                                                 min = cms.untracked.double(-3.141592),
                                                                 max = cms.untracked.double(3.141592),
                                                                 name = cms.untracked.string('MET_phi')
                                                                 )
                                                        )
                                 )

process.plotMETnormal = process.plotMET.clone()
process.plotMETanomalous = process.plotMET.clone()

process.pnormal = cms.Path(
    process.jetIdCut +
    process.EcalDeadCellEventFilter +
    process.plotMETnormal
    )

#process.panomalous = cms.Path(
#    process.jetIdCut +
#    ~process.EcalAnomalousEventFilter +
#    process.plotMETanomalous
#    )
