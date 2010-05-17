/* \class EtMinGenJetCountFilter
 *
 * Filters events if at least N gen-jets above 
 * an Et cut are present
 *
 * \author: Luca Lista, INFN
 *
 */
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "CommonTools/UtilAlgos/interface/ObjectCountFilter.h"
#include "CommonTools/UtilAlgos/interface/EtMinSelector.h"

typedef ObjectCountFilter<
  reco::CaloMET, 
  EtMinSelector
  >::type EtMinCaloMetCountFilter;

DEFINE_FWK_MODULE( EtMinCaloMetCountFilter );
