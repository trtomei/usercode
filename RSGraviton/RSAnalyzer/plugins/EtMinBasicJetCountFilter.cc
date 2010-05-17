/* \class EtMinBasicJetCountFilter
 *
 * Filters events if at least N basic-jets above 
 * an Et cut are present
 *
 * \author: Luca Lista, INFN
 *
 */
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "CommonTools/UtilAlgos/interface/ObjectCountFilter.h"
#include "PhysicsTools/UtilAlgos/interface/EtMinSelector.h"

typedef ObjectCountFilter<
  reco::BasicJetCollection, 
  EtMinSelector
  >::type EtMinBasicJetCountFilter;

DEFINE_FWK_MODULE( EtMinBasicJetCountFilter );
