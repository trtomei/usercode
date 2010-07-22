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
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "CommonTools/Utils/interface/PtComparator.h"

typedef ObjectSelector<
          SortCollectionSelector<
  reco::GsfElectronCollection, 
  GreaterByPt<reco::GsfElectron> 
          > 
> LargestPtGsfElectronSelector;

DEFINE_FWK_MODULE( LargestPtGsfElectronSelector );
