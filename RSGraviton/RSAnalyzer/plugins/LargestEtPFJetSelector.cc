#include "FWCore/Framework/interface/MakerMacros.h"
#include "PhysicsTools/UtilAlgos/interface/ObjectSelector.h"
#include "PhysicsTools/UtilAlgos/interface/SortCollectionSelector.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "PhysicsTools/Utilities/interface/EtComparator.h"

 typedef ObjectSelector<
   SortCollectionSelector<
     reco::PFJetCollection, 
     GreaterByEt<reco::PFJet> 
   > 
 > LargestEtPFJetSelector;

DEFINE_FWK_MODULE( LargestEtPFJetSelector );
