# Auto generated configuration file
# using: 
# Revision: 1.168.2.1 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: RSGraviton/RSAnalyzer/python/Pythia_Zjjnunu_cfi.py -s GEN:ProductionFilterSequence,SIM,DIGI,L1,DIGI2RAW,HLT --conditions START3X_V25::All --datatier GEN-SIM-RAW --eventcontent RAWSIM -n 10 --no_exec
import FWCore.ParameterSet.Config as cms
import uuid
import random
import sys

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.MixingNoPileUp_cff')
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('Configuration.StandardSequences.VtxSmearedEarly10TeVCollision_cff')
process.load('Configuration.StandardSequences.Sim_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_8E29_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')

# Correct the random seeds.
myUUID = uuid.uuid4()
random.seed(myUUID.int)

process.RandomNumberGeneratorService.hiSignalG4SimHits.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.simCastorDigis.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.generator.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.simMuonRPCDigis.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.hiSignal.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.simEcalUnsuppressedDigis.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.simSiStripDigis.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.mix.initialSeed =random.randint(10000,9999999)
process.RandomNumberGeneratorService.simHcalUnsuppressedDigis.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.LHCTransport.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.simMuonCSCDigis.initialSeed =random.randint(10000,9999999)
process.RandomNumberGeneratorService.mixData.initialSeed =random.randint(10000,9999999)
process.RandomNumberGeneratorService.VtxSmeared.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.g4SimHits.initialSeed =random.randint(10000,9999999)
process.RandomNumberGeneratorService.simMuonDTDigis.initialSeed = random.randint(10000,9999999)
process.RandomNumberGeneratorService.simSiPixelDigis.initialSeed =random.randint(10000,9999999)
process.RandomNumberGeneratorService.hiSignalLHCTransport.initialSeed = random.randint(10000,9999999)

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.168.2.1 $'),
    annotation = cms.untracked.string('RSGraviton/RSAnalyzer/python/Pythia_Zjjnunu_cfi.py nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(150)
)
process.options = cms.untracked.PSet(

)
# Input source
myOptions = sys.argv
if 'runNumber' in myOptions:
    myRunNumber = int(myOptions[myOptions.index('runNumber')+1])
else:
    myRunNumber = 1
                
process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(myRunNumber)
                            )

# Output definition
myOutputFileLabel = str(myUUID.hex)
myOutputFileString = '/tmp/Pythia_Zjjnunu_'+myOutputFileLabel+'.root'
myFile = open("weAreCreatingTheFile.txt",'w')
myFile.write(myOutputFileString)
myFile.close()

process.output = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string(myOutputFileString),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START3X_V25::All'
process.WWGenFilter = cms.EDFilter("WWDecayFilter",verbose=cms.bool(False))
process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(7000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTJ(11)=3     ! Choice of the fragmentation function', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'MSTP(81)=1     ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model', 
            'MSTU(21)=1     ! Check on possible errors during program execution', 
            'PARP(82)=1.8387   ! pt cutoff for multiparton interactions', 
            'PARP(89)=1960. ! sqrts for which PARP82 is set', 
            'PARP(83)=0.5   ! Multiple interactions: matter distrbn parameter', 
            'PARP(84)=0.4   ! Multiple interactions: matter distribution parameter', 
            'PARP(90)=0.16  ! Multiple interactions: rescaling power', 
            'PARP(67)=2.5    ! amount of initial-state radiation', 
            'PARP(85)=1.0  ! gluon prod. mechanism in MI', 
            'PARP(86)=1.0  ! gluon prod. mechanism in MI', 
            'PARP(62)=1.25   ! ', 
            'PARP(64)=0.2    ! ', 
            'MSTP(91)=1      !', 
            'PARP(91)=2.1   ! kt distribution', 
            'PARP(93)=15.0  ! '),
        processParameters = cms.vstring('PMAS(5,1)=4.8 ! b quark mass', 
            'PMAS(6,1)=175.0 ! t quark mass', 
            'PMAS(347,1)=800.0 ! mass of RS Graviton', 
            'PARP(50)=0.2708           ! 0.54 == c=0.1 (k/M_PL=0.1)', 
            'MSEL=0                    ! (D=1) to select between full user control', 
            'MSUB(391)=1               ! q qbar -> G* ', 
            'MSUB(392)=1               ! g g -> G*', 
            '5000039:ALLOFF            ! Turn off all decays of G*', 
            '5000039:ONIFANY 24        ! Turn on the decays WW', 
            '24:ALLOFF                 ! Turn off all W decays', 
            '24:ONIFANY 1 2 3 4 5 6 12 14 ! W hadronic / MET decays. We do not want taus.'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)
process.ProductionFilterSequence = cms.Sequence(process.generator*process.WWGenFilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.Path(process.endOfProcess)
process.out_step = cms.EndPath(process.output)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.out_step])
# special treatment in case of production filter sequence  
for path in process.paths: 
    getattr(process,path)._seq = process.ProductionFilterSequence*getattr(process,path)._seq
