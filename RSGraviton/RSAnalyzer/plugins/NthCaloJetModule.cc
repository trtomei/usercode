#include "FWCore/Framework/interface/MakerMacros.h"
#include "PhysicsTools/UtilAlgos/interface/SingleObjectRefSelector.h"
#include "DataFormats/JetReco/interface/CaloJet.h"

template<typename T>
class NthElementSelector {
public:
  NthElementSelector() {}
  NthElementSelector(const edm::ParameterSet &iConfig)  :
    n_(iConfig.getParameter<uint32_t>("n")) {}
  bool operator()(const typename edm::RefToBase<T> &ref) 
  { return ref.key() == n_; }
private:
  unsigned int n_;
};

typedef NthElementSelector<reco::CaloJet> NthCaloJetSelector;

typedef SingleObjectRefSelector<reco::CaloJet, NthCaloJetSelector,
				std::vector<reco::CaloJet> > NthCaloJetModule;

DEFINE_FWK_MODULE(NthCaloJetModule);
