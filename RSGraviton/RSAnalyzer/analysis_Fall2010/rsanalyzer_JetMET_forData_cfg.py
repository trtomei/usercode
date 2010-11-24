#####################################
# CMSSW configuration file - Python #
#####################################
import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################

##################
# Basic services #
##################
# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:skimmedFiles/skim_11_1_aFn.root',
    'file:skimmedFiles/skim_12_2_mq8.root',
    'file:skimmedFiles/skim_13_2_b4b.root',
    'file:skimmedFiles/skim_14_2_fqv.root',
    'file:skimmedFiles/skim_15_2_beN.root',
    'file:skimmedFiles/skim_16_2_gSy.root',
    'file:skimmedFiles/skim_17_2_xsM.root',
    'file:skimmedFiles/skim_18_2_FbO.root',
    'file:skimmedFiles/skim_19_1_Xkc.root',
    'file:skimmedFiles/skim_1_1_nKs.root',
    'file:skimmedFiles/skim_20_2_YfY.root',
    'file:skimmedFiles/skim_21_1_3zL.root',
    'file:skimmedFiles/skim_22_1_tKH.root',
    'file:skimmedFiles/skim_23_2_Tvs.root',
    'file:skimmedFiles/skim_24_2_16Q.root',
    'file:skimmedFiles/skim_26_1_Ici.root',
    'file:skimmedFiles/skim_27_2_m9b.root',
    'file:skimmedFiles/skim_28_2_Pgl.root',
    'file:skimmedFiles/skim_29_2_Jqf.root',
    'file:skimmedFiles/skim_2_1_2Jz.root',
    'file:skimmedFiles/skim_30_2_GpX.root',
    'file:skimmedFiles/skim_31_2_dyf.root',
    'file:skimmedFiles/skim_32_1_msv.root',
    'file:skimmedFiles/skim_33_2_3nm.root',
    'file:skimmedFiles/skim_34_2_rrj.root',
    'file:skimmedFiles/skim_36_2_tVQ.root',
    'file:skimmedFiles/skim_37_2_MAF.root',
    'file:skimmedFiles/skim_38_2_oHj.root',
    'file:skimmedFiles/skim_39_1_Pds.root',
    'file:skimmedFiles/skim_3_1_uFy.root',
    'file:skimmedFiles/skim_40_1_NK0.root',
    'file:skimmedFiles/skim_41_1_vYn.root',
    'file:skimmedFiles/skim_42_1_Pm5.root',
    'file:skimmedFiles/skim_43_2_AfL.root',
    'file:skimmedFiles/skim_44_1_qiF.root',
    'file:skimmedFiles/skim_45_1_5U2.root',
    'file:skimmedFiles/skim_46_1_ROj.root',
    'file:skimmedFiles/skim_46_2_HVc.root',
    'file:skimmedFiles/skim_47_1_vZx.root',
    'file:skimmedFiles/skim_48_1_Dgs.root',
    'file:skimmedFiles/skim_49_1_2rF.root',
    'file:skimmedFiles/skim_4_1_Pu3.root',
    'file:skimmedFiles/skim_50_2_qZO.root',
    'file:skimmedFiles/skim_51_2_buD.root',
    'file:skimmedFiles/skim_52_1_fOk.root',
    'file:skimmedFiles/skim_53_1_lgu.root',
    'file:skimmedFiles/skim_54_2_s3z.root',
    'file:skimmedFiles/skim_55_2_sxg.root',
    'file:skimmedFiles/skim_56_1_ud8.root',
    'file:skimmedFiles/skim_57_2_DOx.root',
    'file:skimmedFiles/skim_58_1_yiN.root',
    'file:skimmedFiles/skim_5_3_46G.root',
    'file:skimmedFiles/skim_60_1_u1z.root',
    'file:skimmedFiles/skim_61_1_33Z.root',
    'file:skimmedFiles/skim_62_2_FET.root',
    'file:skimmedFiles/skim_63_2_CBQ.root',
    'file:skimmedFiles/skim_64_1_n61.root',
    'file:skimmedFiles/skim_65_2_Y1R.root',
    'file:skimmedFiles/skim_66_1_I4w.root',
    'file:skimmedFiles/skim_67_1_mM2.root',
    'file:skimmedFiles/skim_68_1_5Pm.root',
    'file:skimmedFiles/skim_69_2_beL.root',
    'file:skimmedFiles/skim_70_1_vc2.root',
    'file:skimmedFiles/skim_71_2_0wb.root',
    'file:skimmedFiles/skim_72_1_ZZ3.root',
    'file:skimmedFiles/skim_73_2_PeR.root',
    'file:skimmedFiles/skim_74_2_6yg.root',
    'file:skimmedFiles/skim_76_2_q7J.root',
    'file:skimmedFiles/skim_77_2_jSa.root',
    'file:skimmedFiles/skim_79_1_31s.root',
    'file:skimmedFiles/skim_7_1_J9t.root',
    'file:skimmedFiles/skim_80_1_aKS.root',
    'file:skimmedFiles/skim_81_1_6UE.root',
    'file:skimmedFiles/skim_82_2_kut.root',
    'file:skimmedFiles/skim_83_1_knC.root',
    'file:skimmedFiles/skim_84_1_rdb.root',
    'file:skimmedFiles/skim_85_1_JM1.root',
    'file:skimmedFiles/skim_86_1_Va2.root',
    'file:skimmedFiles/skim_87_2_LeU.root',
    'file:skimmedFiles/skim_88_1_0Pw.root',
    'file:skimmedFiles/skim_89_2_Gxf.root',
    'file:skimmedFiles/skim_8_1_QGZ.root',
    'file:skimmedFiles/skim_90_1_H4n.root',
    'file:skimmedFiles/skim_91_1_L5Y.root',
    'file:skimmedFiles/skim_9_1_krj.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

### The output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('output.root')
                                   )
#process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.jethistos_cff import histograms as jethistos

# Global tag
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR10_P_V10::All'

##################
# Mandatory cuts #
##################
# Good vertices, no scraping
process.primaryVertexFilter = cms.EDFilter("VertexSelector",
                                           src = cms.InputTag("offlinePrimaryVertices"),
                                           cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
                                           filter = cms.bool(True),
                                           )

process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )

##########
# Jet ID #
##########
process.jetIdCut = cms.EDAnalyzer("RSJetIdSelector",
                                  jets = cms.InputTag("ak7CaloJets"),
                                  jetID = cms.InputTag("ak7JetID")
                                  )

###############
# Corrections #
###############
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.ak7CaloL2Relative.useCondDB = False
process.ak7CaloL3Absolute.useCondDB = False
process.ak7CaloResidual.useCondDB = False

# For Calo jets
process.myL2L3CorJetAK7Calo = cms.EDProducer('CaloJetCorrectionProducer',
                                             src        = cms.InputTag('jetIdCut'),
                                             correctors = cms.vstring('ak7CaloL2L3')
                                             )
process.myCorrections = cms.Sequence(process.myL2L3CorJetAK7Calo)

##################
# Kinematic cuts #
##################

thiagoJetPtCut = 150.0
thiagoJetEtaCut = 3.0
thiagoJetMassCut = 0.0
thiagoMETCut = 150.0

### For Path 1 - FAT jet from Z.
process.oneJetAboveZero = cms.EDFilter("JetConfigurableSelector",
                                       src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                       theCut = cms.string("pt > -1.0"),
                                       minNumber = cms.int32(1)                                       
                                       )

process.getLargestJet = cms.EDProducer("LargestPtCaloJetSelector",
                                       src = cms.InputTag("oneJetAboveZero"),
                                       maxNumber = cms.uint32(1)
                                       )

process.ptCut = cms.EDFilter("JetConfigurableSelector",
                             src = cms.InputTag("getLargestJet"),
                             theCut = cms.string("pt > "+str(thiagoJetPtCut)),
                             minNumber = cms.int32(1),
                             )

process.differentPtCut = cms.EDFilter("JetConfigurableSelector",
                                      src = cms.InputTag("myL2L3CorJetAK7Calo"),
                                      theCut = cms.string("(pt > 25.0) && (abs(eta) < 5.0)"),
                                      minNumber = cms.int32(1)                                       
                                      )

process.getHardJets = cms.EDProducer("LargestPtCaloJetSelector",
                                     src = cms.InputTag("differentPtCut"),
                                     maxNumber = cms.uint32(9999)
                                     )

process.etaCut = cms.EDFilter("JetConfigurableSelector",
                              src = cms.InputTag("getLargestJet"),
                              theCut = cms.string("abs(eta) < "+str(thiagoJetEtaCut)),
                              minNumber = cms.int32(1),
                              )

process.massCut = cms.EDFilter("JetConfigurableSelector",
                               src = cms.InputTag("getLargestJet"),
                               theCut = cms.string("mass > -1.0"),
                               minNumber = cms.int32(1)
                               )

########################
# Jets for jet pruning #
########################

from RecoJets.JetProducers.CaloJetParameters_cfi import CaloJetParameters
from RecoJets.JetProducers.AnomalousCellParameters_cfi import AnomalousCellParameters
from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
#these are ignored, but required by VirtualJetProducer:
virtualjet_parameters = cms.PSet(jetAlgorithm=cms.string("SISCone"), rParam=cms.double(0.00001))

process.CACaloSubjets = cms.EDProducer("SubJetProducer",
                                       SubJetParameters,
                                       virtualjet_parameters,
                                       #this is required also for GenJets of PFJets:
                                       AnomalousCellParameters,
                                       CaloJetParameters
                                       )

process.CACaloSubjets.nSubjets = 2

### FIXME PF MET?
process.METCut = cms.EDFilter("PtMinCandViewSelector",
                              src = cms.InputTag("pfMet"),
                              ptMin = cms.double(thiagoMETCut),
                              minNumber = cms.uint32(1),
                              filter = cms.bool(True)
                              )

############
# Counting #
############
# In case you want to check efficiencies cut by cut.
process.eventCounter = cms.EDAnalyzer("EventCounter")
process.eventCounterTwo = process.eventCounter.clone()
process.eventCounterThree = process.eventCounter.clone()
process.eventCounterFour = process.eventCounter.clone()
process.eventCounterFive = process.eventCounter.clone()
process.eventCounterSix = process.eventCounter.clone()
process.eventCounterSeven = process.eventCounter.clone()
process.eventCounterEight = process.eventCounter.clone()

###########
# Filters #
###########
process.deltaPhiFilter = cms.EDFilter("RSEventDeltaPhiFilter",
                                      jets = cms.InputTag("getHardJets"),
                                      maxDeltaPhi = cms.double(2.8)
                                      )

process.goodElectrons = cms.EDFilter("LargestPtGsfElectronSelector",
                                     src = cms.InputTag("gsfElectrons"),
                                     maxNumber = cms.uint32(2)
                                     )

process.goodMuons = cms.EDFilter("LargestPtMuonSelector",
                                 src = cms.InputTag("muons"),
                                 maxNumber = cms.uint32(2)
                                 )

process.trackerIndirectVeto = cms.EDFilter("RSTrackerIndirectVetoFilter",
                                           src = cms.InputTag("generalTracks"),
                                           trackMinPt = cms.double(1.0),
                                           seedTrackMinPt = cms.double(10.0),
                                           trackMaxEta = cms.double(2.4),
                                           minCone = cms.double(0.02),
                                           maxCone = cms.double(0.3),
                                           minAcceptableTIV = cms.double(0.1), # 10%, has no effect if filter is False
                                           pixelHits = cms.int32(1),
                                           trackerHits = cms.int32(5),
                                           highPurityRequired = cms.bool(True),
                                           filter = cms.bool(False) #DON'T make the cut, just store the largest TIV
                                           )

#################
# VBTF electron #
#################
process.load("RSGraviton.RSAnalyzer.simpleEleIdSequence_cff")
process.seqEleId = cms.Sequence(process.simpleEleId80relIso)

process.electronVBTFFilter = cms.EDFilter('RSElectronVBTFFilter',
                                          # cuts
                                          ETCut = cms.untracked.double(20.),
                                          vetoSecondElectronEvents = cms.untracked.bool(False),
                                          ETCut2ndEle = cms.untracked.double(20.),
                                          # electrons
                                          electronCollectionTag = cms.untracked.InputTag("gsfElectrons"),   # Electron collection name
                                          # electron ID
                                          electronIdTag = cms.untracked.InputTag("simpleEleId80relIso"),    # Eletron ID map name
                                          electronIdMin = cms.untracked.double(6.5), # Must pass ALL selections, i.e., 7
                                          # fiducial definition
                                          BarrelMaxEta = cms.untracked.double(1.4442),
                                          EndCapMinEta = cms.untracked.double(1.566),
                                          EndCapMaxEta = cms.untracked.double(2.5),
                                          filter = cms.untracked.bool(False)
                                          )

process.VBTFelectron = cms.Sequence(process.goodElectrons + process.simpleEleId80relIso + process.electronVBTFFilter);

#############
# VBTF muon #
#############
process.muonVBTFFilter = cms.EDFilter('RSMuonVBTFFilter',
                                      MuonTag = cms.untracked.InputTag("muons"),
                                      JetTag = cms.untracked.InputTag("ak5CaloJets"),
                                      # Preselection!
                                      PtThrForZ1 = cms.untracked.double(20.0),
                                      PtThrForZ2 = cms.untracked.double(10.0),
                                      vetoSecondMuonEvents = cms.untracked.bool(False),
                                      EJetMin = cms.untracked.double(40.),
                                      NJetMax = cms.untracked.int32(999999),
                                      # Main cuts ->
                                      PtCut = cms.untracked.double(20.0),
                                      EtaCut = cms.untracked.double(2.1),
                                      IsRelativeIso = cms.untracked.bool(True),
                                      IsCombinedIso = cms.untracked.bool(True),
                                      IsoCut03 = cms.untracked.double(0.15),
                                      # Muon quality cuts ->
                                      DxyCut = cms.untracked.double(0.2), # dxy < 0.2 cm (cosmics)
                                      NormalizedChi2Cut = cms.untracked.double(10.), # chi2/ndof < 10.
                                      TrackerHitsCut = cms.untracked.int32(11),  # Hits in inner track > 10
                                      PixelHitsCut = cms.untracked.int32(1),  # Pixel Hits  > 0
                                      MuonHitsCut = cms.untracked.int32(1),  # Valid Muon Hits  > 0
                                      IsAlsoTrackerMuon = cms.untracked.bool(True),
                                      NMatchesCut = cms.untracked.int32(2),  # At least 2 Chambers matched with segments
                                      # filter
                                      filter = cms.untracked.bool(False)
                                      )
process.VBTFmuon = cms.Sequence(process.goodMuons + process.muonVBTFFilter)

###############
# Tree Dumper #
###############
process.eventAnalyzer = cms.EDAnalyzer("RSEventAnalyzer",
                                       jets = cms.InputTag("getHardJets"),
                                       compoundJets = cms.InputTag("CACaloSubjets"),
                                       met = cms.InputTag("corMetGlobalMuons"),
                                       PFmet = cms.InputTag("pfMet"),
                                       TIV = cms.InputTag("trackerIndirectVeto"),
                                       electrons = cms.InputTag("goodElectrons"),
                                       muons = cms.InputTag("goodMuons"),
                                       genParticles = cms.InputTag("hardGenParticles"),
                                       VBTFelectron = cms.InputTag("electronVBTFFilter"),
                                       VBTFmuon = cms.InputTag("muonVBTFFilter"),
                                       weight = cms.double(1.0),
                                       isData = cms.bool(True)
                                       )

process.compoundJetAnalyzer = cms.EDAnalyzer("CompoundJetAnalyzer",
                                             compoundJets = cms.InputTag("CACaloSubjets"),
                                             standardJets = cms.InputTag("getHardJets")
                                             )

process.plotMET = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                 src = cms.InputTag("corMetGlobalMuons"),
                                 histograms = cms.VPSet(
                                     cms.PSet(nbins = cms.untracked.int32(500),
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

process.plotJetsGeneral = cms.EDAnalyzer("CaloJetHistoAnalyzer",
                                         src = cms.InputTag("getHardJets"),
                                         histograms = jethistos
                                         )

#########
# Paths #
#########

# Summary of cuts.
process.goodVertexSequence = cms.Sequence(process.primaryVertexFilter+process.noscraping)
process.jetId  = cms.Sequence(process.jetIdCut + process.myCorrections)
process.cuts0  = cms.Sequence(process.oneJetAboveZero)
process.cuts1  = cms.Sequence(process.ptCut)
process.cuts2  = cms.Sequence(process.etaCut)
process.cuts3  = cms.Sequence(process.massCut)
process.cuts4  = cms.Sequence(process.METCut)
process.doMultiJets = cms.Sequence(process.differentPtCut + process.getHardJets)# + process.deltaPhiFilter + process.plotJetsGeneral)
process.cuts5 = cms.Sequence(process.deltaPhiFilter)
process.cuts6 = cms.Sequence(process.trackerIndirectVeto)
process.leptonStuff = cms.Sequence(process.trackerIndirectVeto + process.VBTFelectron + process.VBTFmuon)
process.jetPruning = cms.Sequence(process.CACaloSubjets + process.compoundJetAnalyzer)

# I want only want Primary Vertex + LOOSE Jet ID + at least one jet + at least one jet above pT cut + MET cut
process.pathCutByCut = cms.Path(process.eventCounter + process.goodVertexSequence +
                                process.eventCounterTwo + process.jetId + process.cuts0 +
                                process.eventCounterThree + process.getLargestJet +
                                process.eventCounterFour + process.etaCut +
                                process.eventCounterFive + process.ptCut +
                                process.eventCounterSix + process.METCut + 
                                process.doMultiJets +
                                process.jetPruning +
                                process.leptonStuff + # This one is not cutting!
                                process.eventCounterSeven + 
#                                process.hardGenParticles + 
                                process.eventAnalyzer
                                )
