/* \class MassMinPFJetCountFilter
 *
 * Filters events if at least N PF-jets above 
 * a mass cut are present
 *
 * \author: Luca Lista, INFN
 *
 */
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "PhysicsTools/UtilAlgos/interface/ObjectCountFilter.h"
#include "PhysicsTools/UtilAlgos/interface/MassMinSelector.h"

typedef ObjectCountFilter<
  reco::PFJetCollection, 
  MassMinSelector
  > MassMinPFJetCountFilter;

DEFINE_FWK_MODULE( MassMinPFJetCountFilter );
