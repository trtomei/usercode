import FWCore.ParameterSet.Config as cms
import sys

from Configuration.Generator.PythiaUESettings_cfi import *

myParameters = cms.vstring('PMAS(5,1)=4.8 ! b quark mass',
                           'PMAS(6,1)=175.0 ! t quark mass',
                           'PMAS(347,1)=800.0 ! mass of RS Graviton',
                           'PARP(50)=0.27             ! 0.54 == c=0.1 (k/M_PL=0.1)',
                           'MSEL=0                    ! (D=1) to select between full user control',
                           'MSUB(391)=1               ! q qbar -> G* ',
                           'MSUB(392)=1               ! g g -> G*',
                           '5000039:ALLOFF            ! Turn off all decays of G*',
                           '5000039:ONIFANY 23        ! Turn on the decays ZZ',
                           '23:ALLON                  ! Turn on all Z decays'
                           )

source = cms.Source("EmptySource")
generator = cms.EDFilter("Pythia6GeneratorFilter",
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         maxEventsToPrint = cms.untracked.int32(0),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         comEnergy = cms.double(7000.0),
                         PythiaParameters = cms.PSet( pythiaUESettingsBlock,
                                                      processParameters = myParameters,
                                                      parameterSets = cms.vstring('pythiaUESettings',
                                                                                  'processParameters')
                                                      )
                         )

VBDecayGenFilter = cms.EDFilter("VectorBosonPairDecayFilter",
                                verbose=cms.bool(False),
                                wantNeutrinos=cms.bool(True),
                                wantQuarks=cms.bool(False),
                                wantElectrons=cms.bool(True),
                                wantMuons=cms.bool(False),
                                wantTaus=cms.bool(False),
                                )

ProductionFilterSequence = cms.Sequence(generator*VBDecayGenFilter)
