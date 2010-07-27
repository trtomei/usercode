# Auto generated configuration file
# using: 
# Revision: 1.168.2.1 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: somename.py -s RAW2DIGI,L1Reco,RECO --datatier GEN-SIM-RECO --eventcontent RECOSIM --conditions START3X_V25::All --no_exec --filein file:GenHLT.root --customise Configuration/GlobalRuns/customise_CollisionMC_35X.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.MixingNoPileUp_cff')
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.168.2.1 $'),
    annotation = cms.untracked.string('somename.py nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.options = cms.untracked.PSet(
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_f45700a77d5b4818b0df5e130db6ad46.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_65aa15c2fddc47f5a3e0b708fff56000.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_da8181d959ab441d9f6e29decdc3a2ff.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_24834e64d79b4f8f9c06364269ffea7a.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_ef83d9674de84125ad3743264cd0b5ef.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_95a4e41055e9486c954c99106c4be21f.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_f573a4026dd849dc8576a859b2db01c9.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_d3544981817b45aa8494ddea48b9ef88.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_18b69ffff45640bc841bc348982ab6b2.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_8c6eef1f5e9c477991715a39e819d373.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_c9530e8b6faf4062a172b5508287bcd1.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_ea401b6747d04a7eabc5f79eaf7a5154.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_d362517e9402440393565859e7f525cb.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_ea7502052da84e4687a2d34c6dec3b11.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_de9603e30f9e4a72b4c882704b72428f.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_6d5575ddceb64f31a05b37280fc0489d.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_74f2854d686d4e5f9f5d415e52d193b4.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_7a674e2e71f8493582bf71c07c64ac06.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_2fed2e2c545b4d88a13aa1ed7fe8d01e.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_184f9ac3c168407bb400fa13995a1aa5.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_432e552604d346978d30aac737b6b3e5.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_a8c32829bca34d6898a332f433eca5a1.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_f4c3abd0c59a4f95adc8592c89f70181.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_21d00d102b6f4497af3272312e6c3c76.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_cfd371b7d1a64553ab3117f519b75d8d.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_ff22a49b560b4d3aa660b5195e043393.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_c0fa4d64a9364617859eb5896fe81687.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_f52ae301a495463aafeadca41a838ec2.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_7cc95bb4085d451badf727a1e25348e8.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_ce95bbf0b3fd451ba239f01875705fe6.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_22c2331b50c948abbae08466cf60934d.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_589e7b45190d4a9591d8b3a4c63746de.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_548f34a729d549c181774b4bcfe6f38d.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_f06a7ecdf0f64abeb351856e2833d497.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_271b612686134dfba86de8be459f7dff.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_cac554ea00ea45f5804fd0005ff4a7a4.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_fc7480554d154f1eb1b1372d70be401b.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_f71211f02c81454b82e83314dffbd2e3.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_53d3d05f7ec7492d8a0daf1bd9aa433e.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_64bee5b74a764435add97d4d4abfee4f.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_59a08c34bbf04887a9493af3fb6928cf.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_a35006fb6fa04501a55a9a6f344a7915.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_fdd7088544204448967a399db2959d33.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_46f8973cd6874f4888d8bad0bcc61660.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_8507a05fe6434fcface6288af70dfd54.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_08b4c46c21eb47d18666d602d2c2c51f.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_e2d3a2bb56f7494b8a43356999b7f7c1.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_d382ed1bb5cc4ca3aaa5c51c3cdf9a0b.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_b7e62fae593d42138039e73dedff3ea5.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_9fd200144440466787020d8f94a705ae.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_ff02afd3cdb948bc99f1595ede5edbe1.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_7a05c38e4ce14226aceeac78ae37c59f.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_4b2e0eac140a49e4abc3ef429504a3fd.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_99bcc45b455d4a6d8201c964b35c2a5d.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_ec9e8a66094641fa98fa91abd50933fc.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_080aa3122bfb4635a34d2c3e30274e6e.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_aafe696e0e7d427290280d2ce64b8e7a.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_1f5712d5b006412398c9be08df34862a.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_56bc0ed5696d4353968d14f008e0c8fe.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_b5dc28953a8240faa2826a5c9d0b68b3.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_02f5028f79ac45c29815157b07cacd4b.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_4951f0acda7c4640b87d6a85c91cfac3.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_bdec21cb80b546118666035681c27dd5.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_569bc79a652c44508f2acd641933fee2.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_584512adb1aa49ac851694ebf230324f.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_32c404666f3b4fb480fd7c963017938b.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_8de197f00862486baaddf3cc2c4f4192.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_9dc2ca3a78ca476792d7c8b0084ac6f4.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_d307f93c2cef40cd964d99c7ae234389.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_f493d9ffba154a5183dbdc9a311fb065.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_6660c5ca75bc4755bcb1e6222001de2a.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_11bce24266e34bac84d8ac5b0c793469.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_adc616eb85ad42869ad1777fd04933e8.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_0eefff9b7c434882b341c03ff6ac91d5.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_e26c9188d2924fedb1de171e5e12eea5.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_0acc1fba138b4775a6ec730f4a0e4093.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_457cb289f44e4f0a8c64ca53b5852860.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_c869744b666d466b9e75dc16334fd782.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_22ed0f66f3c74ceca5034177d0d15bb1.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_bbbe0fa79fb1486da87fa2c9025113c4.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_696cffa0f7374526a00cc9c8b775a0f1.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_b01a4cece87a45a7a9a75b3beed2ba6d.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_e06148487f6b4b67a6b8f945f481db20.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_c9a0a902904841b5b6abf68eb4d932e8.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_fa91ac8a7a204bf889ce21740f4dac02.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_a4333a951bf14897b0b2a8661b48347c.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_0873c208a4f642be82315db6880b0ec8.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_78392336f0234b4d9891f1134a3303bb.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_8567b9bfc56b490688ab91e8ff0d42a1.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_3975fe5bc41d449d8771256edc93283b.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_4ef9ad0b6a264692b569e5b45dc19610.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_33f3a88719674492a6c20ed5497a4bb5.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_48e887cc8c2342a98ca0387e4e4a97e0.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_3c324a07c0e349f8bd9f4be274af7671.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_b0964545ec9f4454a85d9689ea99b5b1.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_01fa0a6eabc444c5a5c3c8ddff27740b.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_6ec26d20590c4df0b311f218a177315f.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_6cfdd21f156d4a08989fde4cc820112b.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_191e70a72af7479396d5852687d47c8d.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_ae4845e1bd454e1c8bda4fee907064b9.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_f3ab677c011b48aaad907aac268e2c19.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_56bfd7bd0b3d41fdbebf98528cfc15a8.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_6749ff97ff4b4d98bf0c5804529b997b.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_2aa66abcb6ab42a6b386960d0683c023.root',
'file:/storage/trtomei/data/FULLSIM/RSG_WWqqlnu/Pythia_Wjjlnu_0b39c17b6b034618bf40079f26cec9ae.root'
)
                            )

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('/hdacs/trtomei/PythiaWjjlnu_GEN_SIM_RECO.root'),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START3X_V25::All'

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.Path(process.endOfProcess)
process.out_step = cms.EndPath(process.output)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.out_step)


# Automatic addition of the customisation function

def customise(process):
    #####################################################################################################
    ####
    ####  Top level replaces for handling strange scenarios of early collisions
    ####

    ## TRACKING:
    ## Skip events with HV off
    process.newSeedFromTriplets.ClusterCheckPSet.MaxNumberOfPixelClusters=2000
    process.newSeedFromPairs.ClusterCheckPSet.MaxNumberOfCosmicClusters=10000
    process.secTriplets.ClusterCheckPSet.MaxNumberOfPixelClusters=1000
    process.fifthSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters = 5000
    process.fourthPLSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters=10000
    
    ###### FIXES TRIPLETS FOR LARGE BS DISPLACEMENT ######

    ### pixelTracks
    #---- replaces ----
    process.pixelTracks.RegionFactoryPSet.ComponentName = 'GlobalRegionProducerFromBeamSpot' # was GlobalRegionProducer
    process.pixelTracks.OrderedHitsFactoryPSet.GeneratorPSet.useFixedPreFiltering = True     # was False
    #---- new parameters ----
    process.pixelTracks.RegionFactoryPSet.RegionPSet.nSigmaZ  = cms.double(4.06) # was originHalfLength = 15.9; translated assuming sigmaZ ~ 3.8
    process.pixelTracks.RegionFactoryPSet.RegionPSet.beamSpot = cms.InputTag("offlineBeamSpot")

    ### 0th step of iterative tracking
    #---- replaces ----
    process.newSeedFromTriplets.RegionFactoryPSet.ComponentName = 'GlobalRegionProducerFromBeamSpot' # was GlobalRegionProducer
    process.newSeedFromTriplets.OrderedHitsFactoryPSet.GeneratorPSet.useFixedPreFiltering = True     # was False
    #---- new parameters ----
    process.newSeedFromTriplets.RegionFactoryPSet.RegionPSet.nSigmaZ   = cms.double(4.06)  # was originHalfLength = 15.9; translated assuming sigmaZ ~ 3.8
    process.newSeedFromTriplets.RegionFactoryPSet.RegionPSet.beamSpot = cms.InputTag("offlineBeamSpot")
    
    ### 2nd step of iterative tracking
    #---- replaces ----
    process.secTriplets.RegionFactoryPSet.ComponentName = 'GlobalRegionProducerFromBeamSpot' # was GlobalRegionProducer
    process.secTriplets.OrderedHitsFactoryPSet.GeneratorPSet.useFixedPreFiltering = True     # was False
    #---- new parameters ----
    process.secTriplets.RegionFactoryPSet.RegionPSet.nSigmaZ  = cms.double(4.47)  # was originHalfLength = 17.5; translated assuming sigmaZ ~ 3.8
    process.secTriplets.RegionFactoryPSet.RegionPSet.beamSpot = cms.InputTag("offlineBeamSpot")
    
    ## Primary Vertex
    process.offlinePrimaryVerticesWithBS.PVSelParameters.maxDistanceToBeam = 2
    process.offlinePrimaryVerticesWithBS.TkFilterParameters.maxNormalizedChi2 = 20
    process.offlinePrimaryVerticesWithBS.TkFilterParameters.minSiliconHits = 6
    process.offlinePrimaryVerticesWithBS.TkFilterParameters.maxD0Significance = 100
    process.offlinePrimaryVerticesWithBS.TkFilterParameters.minPixelHits = 1
    process.offlinePrimaryVerticesWithBS.TkClusParameters.zSeparation = 10
    process.offlinePrimaryVertices.PVSelParameters.maxDistanceToBeam = 2
    process.offlinePrimaryVertices.TkFilterParameters.maxNormalizedChi2 = 20
    process.offlinePrimaryVertices.TkFilterParameters.minSiliconHits = 6
    process.offlinePrimaryVertices.TkFilterParameters.maxD0Significance = 100
    process.offlinePrimaryVertices.TkFilterParameters.minPixelHits = 1
    process.offlinePrimaryVertices.TkClusParameters.zSeparation = 10
    
    ## ECAL 
    process.ecalRecHit.ChannelStatusToBeExcluded = [ 1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 78, 142 ]
    
    
    ## HCAL temporary fixes
    process.hfreco.firstSample  = 1
    process.hfreco.samplesToAdd = 4
    
    process.zdcreco.firstSample = 4
    process.zdcreco.samplesToAdd = 3
    
    ## EGAMMA
    process.ecalDrivenElectronSeeds.SCEtCut = cms.double(1.0)
    process.ecalDrivenElectronSeeds.applyHOverECut = cms.bool(False)
    process.ecalDrivenElectronSeeds.SeedConfiguration.z2MinB = cms.double(-0.9)
    process.ecalDrivenElectronSeeds.SeedConfiguration.z2MaxB = cms.double(0.9)
    process.ecalDrivenElectronSeeds.SeedConfiguration.r2MinF = cms.double(-1.5)
    process.ecalDrivenElectronSeeds.SeedConfiguration.r2MaxF = cms.double(1.5)
    process.ecalDrivenElectronSeeds.SeedConfiguration.rMinI = cms.double(-2.)
    process.ecalDrivenElectronSeeds.SeedConfiguration.rMaxI = cms.double(2.)
    process.ecalDrivenElectronSeeds.SeedConfiguration.DeltaPhi1Low = cms.double(0.3)
    process.ecalDrivenElectronSeeds.SeedConfiguration.DeltaPhi1High = cms.double(0.3)
    process.ecalDrivenElectronSeeds.SeedConfiguration.DeltaPhi2 = cms.double(0.3)
    process.gsfElectrons.applyPreselection = cms.bool(False)
    process.photons.minSCEtBarrel = 1.
    process.photons.minSCEtEndcap =1.
    process.photonCore.minSCEt = 1.
    process.conversionTrackCandidates.minSCEt =1.
    process.conversions.minSCEt =1.
    process.trackerOnlyConversions.AllowTrackBC = cms.bool(False)
    process.trackerOnlyConversions.AllowRightBC = cms.bool(False)
    process.trackerOnlyConversions.MinApproach = cms.double(-.25)
    process.trackerOnlyConversions.DeltaCotTheta = cms.double(.07)
    process.trackerOnlyConversions.DeltaPhi = cms.double(.2)
    
    ###
    ###  end of top level replacements
    ###
    ###############################################################################################

    return (process)


# End of customisation function definition

process = customise(process)
