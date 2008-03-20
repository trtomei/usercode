/* \class LargestEtCandSelector
* 
* Keep the maxNumber biggest (in respect to Et) Candidates from myCollection
* Usage:
*
*
*  module McPartonSele = LargestEtCandSelector {
*      InputTag src     = myCollection
*      uint32 maxNumber = 3            
* } 
*
* \author: Loic Quertenmont, UCL
* \ Modified to Et by Thiago Tomei, SPRACE.
*/
#include "FWCore/Framework/interface/MakerMacros.h"
#include "PhysicsTools/UtilAlgos/interface/ObjectSelector.h"
#include "PhysicsTools/UtilAlgos/interface/SortCollectionSelector.h"
#include "PhysicsTools/Utilities/interface/EtComparator.h"
#include "DataFormats/Candidate/interface/Candidate.h"

typedef ObjectSelector<
  SortCollectionSelector<
  reco::CandidateCollection,
  GreaterByEt<reco::Candidate>
>
> LargestEtCandSelector;

DEFINE_FWK_MODULE( LargestEtCandSelector );
