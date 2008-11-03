import FWCore.ParameterSet.Config as cms

numcands = cms.EDAnalyzer('CandidateCounter',
                          src = cms.string('dummy'),
                          weight = cms.double(1.0),
                          min = cms.double(-0.5),
                          max = cms.double(9.5),
                          nbins = cms.int32(10),
                          description = cms.string('description'),
                          name = cms.string('name')
)
