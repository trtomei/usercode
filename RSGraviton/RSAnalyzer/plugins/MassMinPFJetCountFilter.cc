/* \class MassMinPFJetCountFilter
 *
 * Filters events if at least N PF-jets above 
 * a mass cut are present
 *
 * \author: Luca Lista, INFN
 *
 */
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "CommonTools/UtilAlgos/interface/ObjectCountFilter.h"
#include "CommonTools/UtilAlgos/interface/PtMinSelector.h"

typedef ObjectCountFilter<
  reco::CaloJetCollection, 
  PtMinSelector
  >::type PtMinCaloJetCountFilter;

DEFINE_FWK_MODULE( PtMinCaloJetCountFilter );
