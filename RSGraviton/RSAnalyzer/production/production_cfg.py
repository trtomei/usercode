import FWCore.ParameterSet.Config as cms

process = cms.Process("PROD")

# Source

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(1)
        )
process.options = cms.untracked.PSet(
        Rethrow = cms.untracked.vstring('ProductNotFound')
        )


process.load("Configuration.Generator.PythiaUESettings_cfi")
process.source = cms.Source("PythiaSource",
                            pythiaPylistVerbosity = cms.untracked.int32(1),
                            filterEfficiency = cms.untracked.double(1.0),
                            pythiaHepMCVerbosity = cms.untracked.bool(False),
                            comEnergy = cms.untracked.double(10000.0),
                            crossSection = cms.untracked.double(0.3804),
                            maxEventsToPrint = cms.untracked.int32(0),
                            PythiaParameters = cms.PSet(
                                process.pythiaUESettingsBlock,
                                processParameters = cms.vstring('PMAS(347,1)= 1000.0 ! graviton mass',
                                                                'PARP(50)=0.54  ! c(k/Mpl) * 5.4',
                                                                'MSEL=0         ! User defined processes',
                                                                'MSUB(391)=1    ! ffbar->G*',
                                                                'MSUB(392)=1    ! gg->G*',
                                                                '5000039:ALLOFF ! Turn off graviton decays',
                                                                '5000039:ONIFANY 23 ! graviton decays into Z0',
                                                                '23:ALLOFF ! Turn off Z decays',
                                                                '23:ONIFANY 1 2 3 4 5 6 ! Z decays to q and nu',
                                                                'CKIN(3)=25.    ! Pt hat lower cut',
                                                                'CKIN(4)=-1.    ! Pt hat upper cut',
                                                                'CKIN(13)=-10.  ! etamin',
                                                                'CKIN(14)=10.   ! etamax',
                                                                'CKIN(15)=-10.  ! -etamax',
                                                                'CKIN(16)=10.   ! -etamin'),
                                parameterSets = cms.vstring('pythiaUESettings',
                                                            'processParameters')
                                )
)


# Services, Geometry, Magnetic Field, VtxSmearing, Conditions
process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.VtxSmearedEarly10TeVCollision_cff")
process.load("Configuration.StandardSequences.FakeConditions_cff")

# SIM and DIGI 
process.load("Configuration.StandardSequences.Simulation_cff")
process.load("Configuration.StandardSequences.MixingNoPileUp_cff")
process.load("Configuration.StandardSequences.L1Emulator_cff")
process.load("Configuration.StandardSequences.DigiToRaw_cff")
process.load("Configuration.StandardSequences.RawToDigi_cff")

# RECO
process.load("Configuration.StandardSequences.Reconstruction_cff")

# Event output
process.load("Configuration.EventContent.EventContent_cff")
process.FEVT = cms.OutputModule("PoolOutputModule",
                                process.FEVTSIMEventContent,
                                fileName = cms.untracked.string('test_FEVT.root')
                                )
process.GENSIM = cms.OutputModule("PoolOutputModule",
                                  process.FEVTDEBUGHLTEventContent,
                                  dataset = cms.untracked.PSet(dataTier = cms.untracked.string('GEN-SIM')),
                                  fileName = cms.untracked.string('test_GENSIM.root')
                                  )

# Paths
# process.p0 = cms.Path(process.pgen)
process.p1 = cms.Path(process.psim)
process.p2 = cms.Path(process.pdigi)
process.p3 = cms.Path(process.L1Emulator)
process.p4 = cms.Path(process.DigiToRaw)
process.p5 = cms.Path(process.RawToDigi)
process.p6 = cms.Path(process.reconstruction)
process.outpath = cms.EndPath(process.GENSIM)
process.schedule = cms.Schedule(process.p1,process.p2,process.p3,process.p4,process.p5,process.p6,process.outpath)
