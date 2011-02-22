import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.threshold = 'WARNING'
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.source = cms.Source("EmptySource")

# Additional output definition

# Other statements
myOptions = sys.argv
if 'mass' in myOptions:
    gravMass = float(myOptions[myOptions.index('mass')+1])
else:
    gravMass = 800.0

if 'coupling' in myOptions:
    kmpl = float(myOptions[myOptions.index('coupling')+1])
    cConstant = 5.412 * kmpl
else:
    kmpl = 0.05
    cConstant = 5.412 * kmpl

lambdaPi = gravMass/(3.8317*kmpl)
lambdaPiString = 'set RS/Model:Lambda_pi '+str(lambdaPi)+'*GeV'
gravMassString = 'set /Herwig/Particles/Graviton:NominalMass '+str(gravMass)+'*GeV'
print lambdaPiString
print gravMassString

process.load("GeneratorInterface.ThePEGInterface.herwigDefaults_cff")
process.generator = cms.EDFilter("ThePEGGeneratorFilter",
                                 process.herwigDefaultsBlock,
                                 configFiles = cms.vstring('RS.model'),
                                 parameterSets = cms.vstring(
                                   'cm14TeV', 'pdfCTEQ6L1',
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
                                   'insert ResConstructor:Outgoing 0 /Herwig/Particles/e+ ',
                                   'insert ResConstructor:Outgoing 0 /Herwig/Particles/e- ',
                                   lambdaPiString,
                                   gravMassString
                                   ),
                                 )

#process.mygenfilter = cms.EDFilter("ZZDecayFilter",
#                                   verbose = cms.bool(False)
#                                   )

process.getXSec = cms.EDAnalyzer("PythiaXSecAnalyzer",
                                 outFileName = cms.string("xSec_Herwig.txt"),
                                 massParameter = cms.double(gravMass))

process.output = cms.OutputModule("PoolOutputModule",
                                  fileName = cms.untracked.string('Herwig_800GeV_kmpl005_GEN_small.root'),
                                  SelectEvents = cms.untracked.PSet(
                                      SelectEvents = cms.vstring('generation_step')
                                      )
                                  )

# Path and EndPath definitions
process.generation_step = cms.Path(process.generator*process.getXSec)
#process.end = cms.EndPath(process.output)
