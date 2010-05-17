/* \class LargestEtBasicJetSelector
 *
 * selects the N basic-jets with largest Et
 *
 * \author: Luca Lista, INFN
 *
 */
#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/ObjectSelector.h"
#include "CommonTools/UtilAlgos/interface/SortCollectionSelector.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "CommonTools/Utils/interface/EtComparator.h"

typedef ObjectSelector<
          SortCollectionSelector<
  reco::BasicJetCollection, 
  GreaterByEt<reco::BasicJet> 
          > 
> LargestEtBasicJetSelector;

DEFINE_FWK_MODULE( LargestEtBasicJetSelector );
