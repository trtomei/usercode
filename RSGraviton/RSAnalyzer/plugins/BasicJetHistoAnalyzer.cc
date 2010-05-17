#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/HistoAnalyzer.h"
#include "DataFormats/JetReco/interface/BasicJet.h"

typedef HistoAnalyzer<reco::BasicJetCollection> BasicJetHistoAnalyzer;

DEFINE_FWK_MODULE( BasicJetHistoAnalyzer );
