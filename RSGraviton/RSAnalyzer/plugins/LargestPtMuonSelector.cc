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
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "CommonTools/Utils/interface/PtComparator.h"

typedef ObjectSelector<
          SortCollectionSelector<
  reco::MuonCollection, 
  GreaterByPt<reco::Muon> 
          > 
> LargestPtMuonSelector;

DEFINE_FWK_MODULE( LargestPtMuonSelector );
