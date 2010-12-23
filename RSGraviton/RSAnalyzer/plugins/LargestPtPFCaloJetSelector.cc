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
#include "DataFormats/JetReco/interface/PFJet.h"
#include "CommonTools/Utils/interface/PtComparator.h"

typedef ObjectSelector<
          SortCollectionSelector<
  reco::PFJetCollection, 
  GreaterByPt<reco::PFJet> 
          > 
> LargestPtPFJetSelector;

DEFINE_FWK_MODULE( LargestPtPFJetSelector );
