#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/MassRangeSelector.h"
#include "CommonTools/UtilAlgos/interface/SingleObjectSelector.h"
#include "DataFormats/JetReco/interface/CaloJet.h"

 typedef SingleObjectSelector<
   reco::CaloJetCollection, 
           MassRangeSelector
   > MassRangeCaloJetSelector;

DEFINE_FWK_MODULE( MassRangeCaloJetSelector );
