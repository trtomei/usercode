#include "FWCore/Framework/interface/MakerMacros.h"
#include "PhysicsTools/UtilAlgos/interface/HistoAnalyzer.h"
#include "DataFormats/JetReco/interface/BasicJet.h"

typedef HistoAnalyzer<reco::BasicJetCollection> BasicJetHistoAnalyzer;

DEFINE_FWK_MODULE( BasicJetHistoAnalyzer );
