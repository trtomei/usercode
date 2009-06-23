#####################################
# CMSSW configuration file - Python #
#####################################

import FWCore.ParameterSet.Config as cms
import datetime

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################
today = str(datetime.date.today())
fileLabel = ''

# Source
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
readFiles.extend( [
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/FE2B44A1-43E6-DD11-81E7-001F29C4C3BC.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/F8B30EC4-38E6-DD11-83AE-001E0B5FE418.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/F86E04D0-44E6-DD11-AAD2-001F29C4C338.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/F4CEE5C6-38E6-DD11-A25B-001E0B5FE436.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/F22A35B0-3CE6-DD11-A1A6-001E0B5FC420.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/EC606C45-45E6-DD11-8B5C-001F296BE5A6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/EAE24F78-45E6-DD11-B401-001F296B9566.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/E44FAA7C-43E6-DD11-910D-001E0B487196.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/E4277465-45E6-DD11-A344-001F296BC5B6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/E2A7EB42-45E6-DD11-AB17-001F296A377E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/DEA5F6CF-44E6-DD11-85CF-001F29C424DA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/DCC55B2E-45E6-DD11-A137-001F29C4C338.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/D44E05A5-44E6-DD11-B6DD-001F29C4A3A2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/D27176F9-44E6-DD11-804C-001E0B49A0B6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/D21987B4-44E6-DD11-8F0A-001F29C4A30E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/CA9709A4-43E6-DD11-94D4-001E0B482938.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/C846FC0C-40E6-DD11-B65D-001CC416B322.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/BCFE7C12-45E6-DD11-AD77-001F29C424DA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/BCE49E4B-45E6-DD11-9E25-001F296B7586.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/BA1344C5-44E6-DD11-9BC4-001F29C4D344.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/B819743B-45E6-DD11-8FB1-001F296A27EA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/A87B4B3A-45E6-DD11-84FA-001F29C4A30E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/A6C5C21B-45E6-DD11-81D5-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/9C794A03-45E6-DD11-9D08-001F296B7586.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/96788CFA-44E6-DD11-BE32-001F296B24D0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/9091CCFC-44E6-DD11-B0F7-001F29C4D34E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/7CFF5627-45E6-DD11-B292-001F296A27EA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/7688697D-45E6-DD11-98B9-001F29C4A3A2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/762DF81C-45E6-DD11-9016-001F296BD566.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/7250480D-40E6-DD11-981B-001E0B5FE53C.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/6AFDA183-43E6-DD11-95A4-001E0B48E91C.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/567C7C1E-45E6-DD11-8C4B-001F296A52A4.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/54BFC4C4-38E6-DD11-BBBD-001F29C450E2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/48B9820C-40E6-DD11-9774-001E0B5FA5BE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/44633B49-45E6-DD11-B8CE-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/3C0E904C-45E6-DD11-B820-001F296A52A4.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/3867180B-45E6-DD11-8521-001F296A377E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/2C7D6C5E-43E6-DD11-8999-001CC47A52AE.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/2AD4E5AC-44E6-DD11-A01C-001F296B24D0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/22E3583C-45E6-DD11-8101-001F29C464E0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/1C86CE33-45E6-DD11-98D0-001E0B5FA4DC.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/1C6F474F-45E6-DD11-915F-001F296B24D0.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/10F60458-45E6-DD11-BE41-001F29C424DA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/D8D2D864-1FE6-DD11-92AD-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/D6926837-18E6-DD11-9981-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/D2D9BF42-18E6-DD11-B7A9-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/BE58EC73-18E6-DD11-85DB-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/A83F6D24-20E6-DD11-A48F-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/884B6B83-18E6-DD11-A9B4-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/7A9985F0-1EE6-DD11-A21E-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/729938F4-1FE6-DD11-98D8-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/6E978B72-18E6-DD11-BA7E-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/60D1ED69-1FE6-DD11-9475-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/48FA7A11-20E6-DD11-BA69-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/3EDC0068-20E6-DD11-98D3-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/34F37F3B-20E6-DD11-A240-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/32EC71CA-1BE6-DD11-8C9E-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/24F66B07-20E6-DD11-ADAE-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/24510D1B-1FE6-DD11-A11E-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/1A71D343-1FE6-DD11-B0F1-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/0C803E73-1FE6-DD11-92D7-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/063D023F-1FE6-DD11-9ACA-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M750/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/00F3D1E0-1BE6-DD11-9F72-0018FE290052.root' ] );
process.source = cms.Source ("PoolSource",fileNames = readFiles)
    
##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('results_'+fileLabel+today+'.root')
)

#process.Tracer = cms.Service("Tracer")

from RSGraviton.RSAnalyzer.Zhistos_cff import histograms as Zhistos
from RSGraviton.RSAnalyzer.Ghistos_cff import histograms as Ghistos
from RSGraviton.RSAnalyzer.basicjethistos_cff import histograms as jethistos

##################
# Kinematic cuts #
##################

# Make SISCone 1.0 jets.
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.FastjetParameters_cfi import *
from RecoJets.JetProducers.SISConeJetParameters_cfi import *

process.sisCone10PFJets = cms.EDProducer("SISConeJetProducer",
                                         PFJetParameters,
                                         SISConeJetParameters,
                                         FastjetNoPU,
                                         coneRadius = cms.double(1.0)
                                         )

process.twoJets = cms.EDFilter("EtMinPFJetCountFilter",
                               src = cms.InputTag("sisCone10PFJets"),
                               minNumber = cms.uint32(2),
                               etMin = cms.double(70.0)
                               )

process.getTwoJets = cms.EDProducer("LargestEtPFJetSelector",
                                    src = cms.InputTag("sisCone10PFJets"),
                                    maxNumber = cms.uint32(2)
                                    )

process.plotTwoJets = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                     src = cms.InputTag("getTwoJets"),
                                     histograms = jethistos
                                     )

process.directGravitons = cms.EDProducer("QuickCombiner",
                                         src = cms.InputTag("getTwoJets")
                                         )

process.cutDirectGravitons = cms.EDFilter("CandViewSelector",
                                          src = cms.InputTag("directGravitons"),
                                          cut = cms.string("mass > 600")
                                          )

process.plotDirectGravitons = cms.EDAnalyzer("CandViewHistoAnalyzer",
                                             src = cms.InputTag("directGravitons"),
                                             histograms = Ghistos
                                             )

process.doSisConeJets = cms.Sequence(process.sisCone10PFJets + process.twoJets + process.getTwoJets + process.plotTwoJets)
process.doGravitons = cms.Sequence(process.directGravitons + process.cutDirectGravitons+ process.plotDirectGravitons)

# Write collection of particles inside each jet, boosted to the jet rest frame.

process.particlesFirstJet = cms.EDProducer("RSJetParticlesBooster",
                                           jets = cms.InputTag("getTwoJets"),
                                           nJet = cms.uint32(0)
                                           )

process.particlesSecondJet = cms.EDProducer("RSJetParticlesBooster",
                                            jets = cms.InputTag("getTwoJets"),
                                            nJet = cms.uint32(1)
                                            )

process.getParticlesInJets = cms.Sequence(process.particlesFirstJet + process.particlesSecondJet)

# Redo jets with those particles. I expect to find two jets back to back.
process.jetsFromFirstJet03 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.3)
                                            )
process.jetsFromSecondJet03 = cms.EDProducer("SISConeJetProducer",
                                             PFJetParameters,
                                             SISConeJetParameters,
                                             FastjetNoPU,
                                             coneRadius = cms.double(0.3)
                                             )
process.jetsFromFirstJet04 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.4)
                                            )
process.jetsFromSecondJet04 = cms.EDProducer("SISConeJetProducer",
                                             PFJetParameters,
                                             SISConeJetParameters,
                                             FastjetNoPU,
                                             coneRadius = cms.double(0.4)
                                             )
process.jetsFromFirstJet05 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.5)
                                            )
process.jetsFromSecondJet05 = cms.EDProducer("SISConeJetProducer",
                                             PFJetParameters,
                                             SISConeJetParameters,
                                             FastjetNoPU,
                                             coneRadius = cms.double(0.5)
                                             )
process.jetsFromFirstJet06 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.6)
                                            )
process.jetsFromSecondJet06 = cms.EDProducer("SISConeJetProducer",
                                             PFJetParameters,
                                             SISConeJetParameters,
                                             FastjetNoPU,
                                             coneRadius = cms.double(0.6)
                                             )
process.jetsFromFirstJet07 = cms.EDProducer("SISConeJetProducer",
                                            PFJetParameters,
                                            SISConeJetParameters,
                                            FastjetNoPU,
                                            coneRadius = cms.double(0.7)
                                            )
process.jetsFromSecondJet07 = cms.EDProducer("SISConeJetProducer",
                                             PFJetParameters,
                                             SISConeJetParameters,
                                             FastjetNoPU,
                                             coneRadius = cms.double(0.7)
                                             )

process.jetsFromFirstJet03.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet03.src = cms.InputTag("particlesSecondJet")
process.jetsFromFirstJet04.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet04.src = cms.InputTag("particlesSecondJet")
process.jetsFromFirstJet05.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet05.src = cms.InputTag("particlesSecondJet")
process.jetsFromFirstJet06.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet06.src = cms.InputTag("particlesSecondJet")
process.jetsFromFirstJet07.src = cms.InputTag("particlesFirstJet")
process.jetsFromSecondJet07.src = cms.InputTag("particlesSecondJet")

process.getjetsFromFirstJet03 = cms.EDFilter("PtMinPFJetSelector",
                                             src = cms.InputTag("jetsFromFirstJet03"),
                                             ptMin = cms.double(10.0)
                                             )
process.getjetsFromSecondJet03 = cms.EDFilter("PtMinPFJetSelector",
                                              src = cms.InputTag("jetsFromSecondJet03"),
                                              ptMin = cms.double(10.0)
                                              )
process.getjetsFromFirstJet04 = cms.EDFilter("PtMinPFJetSelector",
                                             src = cms.InputTag("jetsFromFirstJet04"),
                                             ptMin = cms.double(10.0)
                                             )
process.getjetsFromSecondJet04 = cms.EDFilter("PtMinPFJetSelector",
                                              src = cms.InputTag("jetsFromSecondJet04"),
                                              ptMin = cms.double(10.0)
                                              )
process.getjetsFromFirstJet05 = cms.EDFilter("PtMinPFJetSelector",
                                             src = cms.InputTag("jetsFromFirstJet05"),
                                             ptMin = cms.double(10.0)
                                             )
process.getjetsFromSecondJet05 = cms.EDFilter("PtMinPFJetSelector",
                                              src = cms.InputTag("jetsFromSecondJet05"),
                                              ptMin = cms.double(10.0)
                                              )
process.getjetsFromFirstJet06 = cms.EDFilter("PtMinPFJetSelector",
                                             src = cms.InputTag("jetsFromFirstJet06"),
                                             ptMin = cms.double(10.0)
                                             )
process.getjetsFromSecondJet06 = cms.EDFilter("PtMinPFJetSelector",
                                              src = cms.InputTag("jetsFromSecondJet06"),
                                              ptMin = cms.double(10.0)
                                              )
process.getjetsFromFirstJet07 = cms.EDFilter("PtMinPFJetSelector",
                                             src = cms.InputTag("jetsFromFirstJet07"),
                                             ptMin = cms.double(10.0)
                                             )
process.getjetsFromSecondJet07 = cms.EDFilter("PtMinPFJetSelector",
                                              src = cms.InputTag("jetsFromSecondJet07"),
                                              ptMin = cms.double(10.0)
                                              )

process.makeBoostedJets = cms.Sequence(process.jetsFromFirstJet03 + process.jetsFromSecondJet03 + process.getjetsFromFirstJet03 + process.getjetsFromSecondJet03 +
                                       process.jetsFromFirstJet04 + process.jetsFromSecondJet04 + process.getjetsFromFirstJet04 + process.getjetsFromSecondJet04 +
                                       process.jetsFromFirstJet05 + process.jetsFromSecondJet05 + process.getjetsFromFirstJet05 + process.getjetsFromSecondJet05 +
                                       process.jetsFromFirstJet06 + process.jetsFromSecondJet06 + process.getjetsFromFirstJet06 + process.getjetsFromSecondJet06 +
                                       process.jetsFromFirstJet07 + process.jetsFromSecondJet07 + process.getjetsFromFirstJet07 + process.getjetsFromSecondJet07)

# Analysis
process.analysisFirstJet03 = cms.EDAnalyzer("RSSubJetComparison",
                                            src = cms.InputTag("getjetsFromFirstJet03"),
                                            boost = cms.InputTag("particlesFirstJet")
                                            )
process.analysisSecondJet03 = cms.EDAnalyzer("RSSubJetComparison",
                                             src = cms.InputTag("getjetsFromSecondJet03"),
                                             boost = cms.InputTag("particlesSecondJet")
                                             )
process.analysisFirstJet04 = cms.EDAnalyzer("RSSubJetComparison",
                                            src = cms.InputTag("getjetsFromFirstJet04"),
                                            boost = cms.InputTag("particlesFirstJet")
                                            )
process.analysisSecondJet04 = cms.EDAnalyzer("RSSubJetComparison",
                                             src = cms.InputTag("getjetsFromSecondJet04"),
                                             boost = cms.InputTag("particlesSecondJet")
                                             )
process.analysisFirstJet05 = cms.EDAnalyzer("RSSubJetComparison",
                                            src = cms.InputTag("getjetsFromFirstJet05"),
                                            boost = cms.InputTag("particlesFirstJet")
                                            )
process.analysisSecondJet05 = cms.EDAnalyzer("RSSubJetComparison",
                                             src = cms.InputTag("getjetsFromSecondJet05"),
                                             boost = cms.InputTag("particlesSecondJet")
                                             )
process.analysisFirstJet06 = cms.EDAnalyzer("RSSubJetComparison",
                                            src = cms.InputTag("getjetsFromFirstJet06"),
                                            boost = cms.InputTag("particlesFirstJet")
                                            )
process.analysisSecondJet06 = cms.EDAnalyzer("RSSubJetComparison",
                                             src = cms.InputTag("getjetsFromSecondJet06"),
                                             boost = cms.InputTag("particlesSecondJet")
                                             )
process.analysisFirstJet07 = cms.EDAnalyzer("RSSubJetComparison",
                                            src = cms.InputTag("getjetsFromFirstJet07"),
                                            boost = cms.InputTag("particlesFirstJet")
                                            )
process.analysisSecondJet07 = cms.EDAnalyzer("RSSubJetComparison",
                                             src = cms.InputTag("getjetsFromSecondJet07"),
                                             boost = cms.InputTag("particlesSecondJet")
                                             )

process.analysisSubJets = cms.Sequence(process.analysisFirstJet03 + process.analysisSecondJet03 +
                                       process.analysisFirstJet04 + process.analysisSecondJet04 +
                                       process.analysisFirstJet05 + process.analysisSecondJet05 +
                                       process.analysisFirstJet06 + process.analysisSecondJet06 +
                                       process.analysisFirstJet07 + process.analysisSecondJet07)

#########
# Paths #
#########

# Make the jets.
process.p1 = cms.Path(process.doSisConeJets + process.doGravitons +
                      process.getParticlesInJets + process.makeBoostedJets + process.analysisSubJets)
#process.p2 = cms.Path(process.doCompoundJets)
#process.copyAll = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string("out.root") )
#process.out = cms.EndPath(process.copyAll)
