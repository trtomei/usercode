/* \class LargestEtBasicJetSelector
 *
 * selects the N basic-jets with largest Et
 *
 * \author: Luca Lista, INFN
 *
 */
#include "FWCore/Framework/interface/MakerMacros.h"
#include "PhysicsTools/UtilAlgos/interface/ObjectSelector.h"
#include "PhysicsTools/UtilAlgos/interface/SortCollectionSelector.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "CommonTools/Utils/interface/PtComparator.h"

typedef ObjectSelector<
          SortCollectionSelector<
  reco::CaloJetCollection, 
  GreaterByPt<reco::CaloJet> 
          > 
> LargestPtCaloJetSelector;

DEFINE_FWK_MODULE( LargestPtCaloJetSelector );
