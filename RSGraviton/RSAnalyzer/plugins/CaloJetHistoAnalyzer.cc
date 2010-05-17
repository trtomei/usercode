#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/HistoAnalyzer.h"
#include "DataFormats/JetReco/interface/CaloJet.h"

typedef HistoAnalyzer<reco::CaloJetCollection> CaloJetHistoAnalyzer;

DEFINE_FWK_MODULE( CaloJetHistoAnalyzer );
