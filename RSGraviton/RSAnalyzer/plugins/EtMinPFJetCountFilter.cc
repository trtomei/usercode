/* \class EtMinPFJetCountFilter
 *
 * Filters events if at least N PF-jets above 
 * an Et cut are present
 *
 * \author: Luca Lista, INFN
 *
 */
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "PhysicsTools/UtilAlgos/interface/ObjectCountFilter.h"
#include "PhysicsTools/UtilAlgos/interface/EtMinSelector.h"

typedef ObjectCountFilter<
  reco::PFJetCollection, 
  EtMinSelector
  > EtMinPFJetCountFilter;

DEFINE_FWK_MODULE( EtMinPFJetCountFilter );
