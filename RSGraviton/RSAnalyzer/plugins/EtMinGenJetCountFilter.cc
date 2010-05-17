/* \class EtMinGenJetCountFilter
 *
 * Filters events if at least N gen-jets above 
 * an Et cut are present
 *
 * \author: Luca Lista, INFN
 *
 */
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "CommonTools/UtilAlgos/interface/ObjectCountFilter.h"
#include "CommonTools/UtilAlgos/interface/EtMinSelector.h"

typedef ObjectCountFilter<
  reco::GenJetCollection, 
  EtMinSelector
  >::type EtMinGenJetCountFilter;

DEFINE_FWK_MODULE( EtMinGenJetCountFilter );
