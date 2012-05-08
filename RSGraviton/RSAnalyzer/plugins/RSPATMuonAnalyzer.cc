// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Math/interface/deltaR.h"


//
// class declaration
//

class RSPATMuonAnalyzer : public edm::EDFilter {
public:
  explicit RSPATMuonAnalyzer(const edm::ParameterSet&);
  ~RSPATMuonAnalyzer();

private:
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  edm::InputTag muons_;
  std::string pfcandsModule_;
  std::string pfcandsInstance_;
  // ----------member data ---------------------------
};

RSPATMuonAnalyzer::RSPATMuonAnalyzer(const edm::ParameterSet& iConfig)
{
  edm::Service<TFileService> fs;
  muons_ = iConfig.getParameter<edm::InputTag>("muons");
  pfcandsModule_   = iConfig.getParameter<std::string>("pfcandsModule");
  pfcandsInstance_ = iConfig.getParameter<std::string>("pfcandsInstance");
}


RSPATMuonAnalyzer::~RSPATMuonAnalyzer()
{
}

bool
RSPATMuonAnalyzer::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  
  Handle<View<pat::Muon> > muonsHandle;
  iEvent.getByLabel(muons_,muonsHandle);
  Handle<std::vector<PFCandidate> >pfcandsHandle;
  iEvent.getByLabel(pfcandsModule_,pfcandsInstance_,pfcandsHandle);
  if(muonsHandle->size()==0)
    return false;

  const pat::Muon& theMuon = muonsHandle->at(0);
  
  // Get the reference to PFCandidate from pat::Muon
  PFCandidateRef pfMuonRef = theMuon.pfCandidateRef();
  
  if(pfMuonRef.isNonnull()) {
    printf("Hooray, is non-null\n");
    printf("pt,eta,phi = %g,%g,%g\n",pfMuonRef->pt(),pfMuonRef->eta(),pfMuonRef->phi());
  }
  else {
    printf("Oh noes, is null\n");
    return false;
  }

  // Get the corresponding reference in the big PFCandidates collection
  for(size_t i=0; i!=pfcandsHandle->size(); ++i) {
    PFCandidateRef thisRef(pfcandsHandle,i);
    if(thisRef==pfMuonRef) {
      printf("HOORAY, found corresponding PFMuon\n");
      printf("pt,eta,phi = %g,%g,%g\n",thisRef->pt(),thisRef->eta(),thisRef->phi());
    }
    if(std::abs(thisRef->pdgId())==13) {
      printf("YIIPEE, found corresponding PFMuon\n");
      printf("pt,eta,phi = %g,%g,%g\n",thisRef->pt(),thisRef->eta(),thisRef->phi());
    }
  }
  return  true;
}


//define this as a plug-in
DEFINE_FWK_MODULE(RSPATMuonAnalyzer);
