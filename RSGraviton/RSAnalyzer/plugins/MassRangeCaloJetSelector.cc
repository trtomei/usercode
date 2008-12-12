#include "FWCore/Framework/interface/MakerMacros.h"
#include "PhysicsTools/UtilAlgos/interface/MassRangeSelector.h"
#include "PhysicsTools/UtilAlgos/interface/SingleObjectSelector.h"
#include "DataFormats/JetReco/interface/CaloJet.h"

 typedef SingleObjectSelector<
   reco::CaloJetCollection, 
           MassRangeSelector
   > MassRangeCaloJetSelector;

DEFINE_FWK_MODULE( MassRangeCaloJetSelector );
