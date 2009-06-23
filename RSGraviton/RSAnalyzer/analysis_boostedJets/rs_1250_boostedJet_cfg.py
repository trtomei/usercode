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
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0198/46F8A299-4BE6-DD11-A4A4-001F296A4DC2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/FA695979-49E6-DD11-89D9-001F29C4C3BC.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/F6336420-4AE6-DD11-B7BC-001E0B49D098.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/EE80DD94-49E6-DD11-BA7D-001E0B5FE436.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/E8C6D227-4AE6-DD11-9103-001F296A377E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/E8BBA825-4AE6-DD11-B275-001F29C4A3A2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/E4CF7A85-49E6-DD11-BCC3-001E0B5FC420.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/E064779D-49E6-DD11-9B7B-001F29C424DA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/CAA64E95-49E6-DD11-8DD1-001E0B471C7E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/C8CFE388-49E6-DD11-9650-001E0B482938.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/C46D5875-49E6-DD11-AE2C-001F29C4A30E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/B83BBC21-4AE6-DD11-8B7B-001F296A27EA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/B0F46E69-49E6-DD11-855A-001E0B5FA554.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/B045059B-49E6-DD11-B1FB-001F296BD566.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/AE30F364-49E6-DD11-8361-001F296A4DC2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/A4B94AA7-49E6-DD11-A698-001E0B472C98.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/A2D12A7D-46E6-DD11-AB21-001E0B472C98.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/A07BE417-4AE6-DD11-90C0-001E0B5FA554.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/8CA05082-49E6-DD11-AC8B-001F296B9566.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/84418161-46E6-DD11-BDCA-001F29C4C338.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/8288D466-49E6-DD11-A234-001E0B472C98.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/802C3FC5-38E6-DD11-8DD7-001F296A27EA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/6480D01C-4AE6-DD11-B555-001F29C4D34E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/60534D7A-46E6-DD11-938B-001E0B5FE436.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/5880EE88-49E6-DD11-8AE1-001F296A27EA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/46DEE60C-31E6-DD11-8DE1-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/460A1293-49E6-DD11-B69B-001E0B48D104.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/42F31C5B-46E6-DD11-9B0C-001E0B49D098.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/3E49756C-49E6-DD11-9C02-001E0BE912A8.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/3C29639B-49E6-DD11-B799-001F29C4D34E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/36FC3CA4-49E6-DD11-886F-001E0B5FA554.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/1A038D78-49E6-DD11-A0C7-001F29C4A3A2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/0CB4DCC1-30E6-DD11-B589-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/04C52665-49E6-DD11-AB3E-001F29C424DA.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/00D5B196-49E6-DD11-A4B7-00215AAC88D6.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0197/0088BC65-49E6-DD11-A76B-001E0B5FE418.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/F8A6FDE7-1EE6-DD11-BE24-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/F60ADB76-19E6-DD11-907D-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/F01517A8-1AE6-DD11-ACC7-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/EC937869-1EE6-DD11-9113-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/D2CD905E-1EE6-DD11-AEAA-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/BCC8BA46-1DE6-DD11-9C5E-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/B8F0B173-1BE6-DD11-ACA1-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/B2962B7A-19E6-DD11-AD1A-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/B0B7A654-1DE6-DD11-B6AA-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/ACF59CCC-1AE6-DD11-9740-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/A8408FC2-1DE6-DD11-8442-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/A80402E0-19E6-DD11-9F69-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/9ABAD163-1EE6-DD11-A174-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/948B9BCF-18E6-DD11-8A54-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/86951CCF-19E6-DD11-9C64-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/7C732DAD-1AE6-DD11-946B-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/789CA5D0-1DE6-DD11-8512-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/74C0163D-1BE6-DD11-A38D-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/70DF0605-1BE6-DD11-8403-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/6EF067C9-18E6-DD11-8AEE-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/6A565E7A-19E6-DD11-A77C-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/604752B3-19E6-DD11-B5FA-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/58F1A8D7-1AE6-DD11-9F8B-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/581DB63E-1BE6-DD11-856C-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/562E24D3-18E6-DD11-A1A9-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/4E2F90D6-19E6-DD11-9004-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/422C20A6-19E6-DD11-B254-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/38AB8F10-1BE6-DD11-A04D-0018FE28FFB2.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/2C6A1A11-19E6-DD11-AFB5-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/2AD1D7B5-1AE6-DD11-AF12-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/28311F15-1BE6-DD11-93E4-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/12344B03-19E6-DD11-9351-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/0A6BF885-1EE6-DD11-9D9B-0018FE28CC94.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/0A3A7CC4-1EE6-DD11-9A79-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0196/0835AC83-1DE6-DD11-803B-0018FE290052.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/DED50AC3-0DE6-DD11-9F1D-001F29C4D34E.root',
                  '/store/mc/Summer08/Exotica_RSGravitonWWJetMET_M1250/GEN-SIM-RECO/IDEAL_V11_redigi_v1/0195/6683BE05-0AE6-DD11-B4F2-001CC4A934E0.root' ] );
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
