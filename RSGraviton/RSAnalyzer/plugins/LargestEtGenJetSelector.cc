#include "FWCore/Framework/interface/MakerMacros.h"
#include "PhysicsTools/UtilAlgos/interface/ObjectSelector.h"
#include "PhysicsTools/UtilAlgos/interface/SortCollectionSelector.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "CommonTools/Utils/interface/EtComparator.h"

 typedef ObjectSelector<
   SortCollectionSelector<
     reco::GenJetCollection, 
     GreaterByEt<reco::GenJet> 
   > 
 > LargestEtGenJetSelector;

DEFINE_FWK_MODULE( LargestEtGenJetSelector );
