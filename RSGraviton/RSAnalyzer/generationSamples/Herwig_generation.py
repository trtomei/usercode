import FWCore.ParameterSet.Config as cms
import sys
import random
import uuid

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.MessageLogger.cerr.threshold = 'WARNING'
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(40000)
)

process.source = cms.Source("EmptySource")

# Additional output definition

# Other statements
myOptions = sys.argv
gravMass = 1000.0
lambdaPi = 5219.62

if 'mass' in myOptions:
    gravMass = float(myOptions[myOptions.index('mass')+1])

if 'lambdaPi' in myOptions:
    lambdaPi = float(myOptions[myOptions.index('lambdaPi')+1])

lambdaPiString = 'set RS/Model:Lambda_pi '+str(lambdaPi)+'*GeV'
gravMassString = 'set /Herwig/Particles/Graviton:NominalMass '+str(gravMass)+'*GeV'

myuuid = uuid.uuid4()
random.seed(myuuid.int)
process.RandomNumberGeneratorService.generator.initialSeed = random.randint(1,99999999)
#print process.RandomNumberGeneratorService.generator.initialSeed

process.load("GeneratorInterface.ThePEGInterface.herwigDefaults_cff")
process.generator = cms.EDFilter("ThePEGGeneratorFilter",
                                 process.herwigDefaultsBlock,
                                 configFiles = cms.vstring('RS.model'),
                                 parameterSets = cms.vstring(
                                   'cm7TeV', 'pdfMRST2001',
                                   'ExampleParameters',
                                   'basicSetup', 'setParticlesStableForDetector',
                                   ),
                                 ExampleParameters = cms.vstring(
                                   'cd /Herwig/NewPhysics',
                                   'insert ResConstructor:Incoming 0 /Herwig/Particles/g ',
                                   'insert ResConstructor:Incoming 1 /Herwig/Particles/u ',
                                   'insert ResConstructor:Incoming 2 /Herwig/Particles/ubar ',
                                   'insert ResConstructor:Incoming 3 /Herwig/Particles/d ',
                                   'insert ResConstructor:Incoming 4 /Herwig/Particles/dbar',
                                   'insert ResConstructor:Intermediates 0 /Herwig/Particles/Graviton',
                                   'insert ResConstructor:Outgoing 0 /Herwig/Particles/Z0 ',
                                   lambdaPiString,
                                   gravMassString
                                   ),
                                 )

process.nunujjFilter = cms.EDFilter("TwoVBGenFilter",
                                    src = cms.untracked.InputTag("generator"),
                                    nunujj = cms.bool(True),
                                    taunujj = cms.bool(False),
                                    tautaujj = cms.bool(False),
                                    eejj = cms.bool(False),
                                    enujj = cms.bool(False),
                                    munujj = cms.bool(False),
                                    mumujj = cms.bool(False)
                                    )

process.output = cms.OutputModule("PoolOutputModule",
                                  fileName = cms.untracked.string('Herwig_m1000GeV_kmpl005_GEN.root'),
                                  SelectEvents = cms.untracked.PSet(
                                      SelectEvents = cms.vstring('generation_step')
                                      )
                                  )

# Path and EndPath definitions
process.generation_step = cms.Path(process.generator*process.nunujjFilter)
process.end = cms.EndPath(process.output)
