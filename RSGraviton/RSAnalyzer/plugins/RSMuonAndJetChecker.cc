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
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Math/interface/deltaR.h"


//
// class declaration
//

class RSMuonAndJetChecker : public edm::EDFilter {
public:
  explicit RSMuonAndJetChecker(const edm::ParameterSet&);
  ~RSMuonAndJetChecker();

private:
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  edm::InputTag jets_;        
  edm::InputTag muon_;
  TH1F* h_numJets;
  TH1F* h_numMuons;
  TH1F* h_ptMuons;
  TH1F* h_ptJets;
  TH1F* h_drJetMuon;
  // ----------member data ---------------------------
};

RSMuonAndJetChecker::RSMuonAndJetChecker(const edm::ParameterSet& iConfig)
{
  edm::Service<TFileService> fs;
  h_numJets = fs->make<TH1F>("num_Jets","num_Jets",10,-0.5,9.5);
  h_numMuons = fs->make<TH1F>("num_Muons","num_Muons",10,-0.5,9.5);
  h_ptJets = fs->make<TH1F>("ptJets","ptJets",50,0.0,500.0);
  h_ptMuons = fs->make<TH1F>("ptMuons","ptMuons",50,0.0,500.0);
  h_drJetMuon = fs->make<TH1F>("drJetMuon","drJetMuon",120,0.0,6.0);
  jets_ = iConfig.getParameter<edm::InputTag>("jets");
  muon_ = iConfig.getParameter<edm::InputTag>("muon");
}


RSMuonAndJetChecker::~RSMuonAndJetChecker()
{
}

bool
RSMuonAndJetChecker::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  
  Handle<View<Candidate> > jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);
  Handle<View<Candidate> > muonHandle;
  iEvent.getByLabel(muon_,muonHandle);
  
  const Candidate& theMuon = muonHandle->at(0);
  h_numMuons->Fill(1);
  h_ptMuons->Fill(theMuon.pt());
  printf("Our muon has pt %g, eta %g, phi %g\n",theMuon.pt(),theMuon.eta(),theMuon.phi());
  
  size_t njets = jetsHandle->size();
  h_numJets->Fill(njets);

  for(size_t i =0; i!= njets; ++i) {
    const Candidate& theJet = jetsHandle->at(i);
    printf("Our jet has pt %g, eta %g, phi %g\n",theJet.pt(),theJet.eta(),theJet.phi());    
    h_ptJets->Fill(theJet.pt());
    double dr = deltaR(theJet.eta(),theJet.phi(),theMuon.eta(),theMuon.phi());
    h_drJetMuon->Fill(dr);
  }

  return  true;
}


//define this as a plug-in
DEFINE_FWK_MODULE(RSMuonAndJetChecker);
