#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/ObjectSelector.h"
#include "CommonTools/UtilAlgos/interface/SortCollectionSelector.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "CommonTools/Utils/interface/EtComparator.h"

 typedef ObjectSelector<
   SortCollectionSelector<
     reco::PFJetCollection, 
     GreaterByEt<reco::PFJet> 
   > 
 > LargestEtPFJetSelector;

DEFINE_FWK_MODULE( LargestEtPFJetSelector );
