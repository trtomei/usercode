import FWCore.ParameterSet.Config as cms

VBTFelectrons = cms.EDFilter("PATElectronSelector",
                         src = cms.InputTag("selectedPatElectronsPFlow"),
                         cut = cms.string("pt > 20.0 && "+
                                          "abs(eta) < 2.4 && "+
                                          "electronID('eidLooseMC') > 0.5 && "+

                                          # Equivalent isolation from muons
                                          #"(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt < 0.15"

                                          # WP95, as stolen from
                                          # http://cmssdt.cern.ch/SDT/lxr/source/PhysicsTools/TagAndProbe/test/Electron_TagProbeTreeProducer_cfg.py#312
#                                          " && (gsfTrack.trackerExpectedHitsInner.numberOfHits <= 1)" +
#                                          " && ((isEB" +
#                                          " && ( dr03TkSumPt/p4.Pt < 0.15 && dr03EcalRecHitSumEt/p4.Pt < 2.0 && dr03HcalTowerSumEt/p4.Pt < 0.12 )" +
#                                          " && (sigmaIetaIeta<0.01)" +
#                                          " && ( -0.8<deltaPhiSuperClusterTrackAtVtx<0.8 )" +
#                                          " && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )" +
#                                          " && (hadronicOverEm<0.15)" +
#                                          ")" +
#                                          " || (isEE" +
#                                          " && (dr03TkSumPt/p4.Pt < 0.08 && dr03EcalRecHitSumEt/p4.Pt < 0.06  && dr03HcalTowerSumEt/p4.Pt < 0.05 )" +
#                                          " && (sigmaIetaIeta<0.03)" +
#                                          " && ( -0.7<deltaPhiSuperClusterTrackAtVtx<0.7 )" +
#                                          " && ( -0.01<deltaEtaSuperClusterTrackAtVtx<0.01 )" +
#                                          " && (hadronicOverEm<0.07) " +
#                                          "))"
                                          
                                          # My old isolation...
                                          #"(trackIso + caloIso)/p4.pt < 0.15"
                                          
                                          # A crude approximation
#                                          "(dr03EcalRecHitSumEt + dr03HcalTowerSumEt + dr03TkSumPt)/p4.pt < 0.15"
                                          
                                          # A better approximation
#                                          "((isEB" +
#                                          " && (dr03TkSumPt + max(0., dr03EcalRecHitSumEt - 1.) + dr03HcalTowerSumEt)/p4.pt < 0.15 )" +
#                                          " || (isEE"+
#                                          " && (dr03TkSumPt + dr03EcalRecHitSumEt + dr03HcalTowerSumEt )/p4.pt < 0.15" +
#                                          " ))"
                                          
                                          # Particle-based isolation
                                          "(chargedHadronIso + photonIso + neutralHadronIso )/p4.pt < 0.15"
                                          ),
                             filter = cms.bool(True)
                             )

print VBTFelectrons.cut

leadingElectron = cms.EDFilter("LargestPtCandViewSelector",
                           src = cms.InputTag("VBTFelectrons"),
                           maxNumber = cms.uint32(1)
                           )

electronSequence = cms.Sequence(VBTFelectrons + leadingElectron)

#H/E           = electron->hadronicOverEm()
#deltaPhi      = electron->deltaPhiSuperClusterTrackAtVtx()
#deltaEta      = electron->deltaEtaSuperClusterTrackAtVtx()
#sigmaIEtaIEta = electron->sigmaIetaIeta()
#fbrem         = electron->fbrem()
#etaSC         = electron->superCluster()->eta()
#E/p           = electron->eSuperClusterOverP()
