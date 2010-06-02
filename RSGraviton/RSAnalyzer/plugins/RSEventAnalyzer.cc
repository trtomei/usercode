// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/CaloMETFwd.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
#include "TTree.h"
#include "TLorentzVector.h"
//
// class decleration
//

class RSEventAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSEventAnalyzer(const edm::ParameterSet&);
  ~RSEventAnalyzer();

private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag jets_;
  edm::InputTag met_;
  TH1F* h_dPhi_jet_MET;
  TH1F* h_dPhi_jets;
  TH1F* h_gravTransMass;
  TH1F* h_numJets;
  TH1F* h_MET;
  TH1F* h_alphaT;
  double G_gravTransMass;
  double G_alphaT;
  double G_weight;
  double G_jet1pt;
  double G_jet1eta;
  double G_jet1phi;
  double G_jet1mass;
  double G_jet2pt;
  double G_jet2eta;
  double G_jet2phi;
  double G_jet2mass;
  double G_METpt;
  double G_METphi;
  TTree* mytree;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
RSEventAnalyzer::RSEventAnalyzer(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets") ),
  met_(iConfig.getParameter<edm::InputTag>("met") ),
  G_gravTransMass(0),
  G_weight(iConfig.getParameter<double>("weight") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_dPhi_jet_MET  = fs->make<TH1F>( "dPhi_jet_MET", "dPhi jet and MET", 72, -M_PI, M_PI);
  h_dPhi_jets = fs->make<TH1F>( "dPhi_jets", "dPhi 2 leading jets", 72, -M_PI, M_PI);
  h_gravTransMass = fs->make<TH1F>( "gravTransMass", "Graviton transverse mass", 300, 0, 1500);
  h_numJets = fs->make<TH1F>("numJets", "Number of jets", 10, -0.5, 9.5);
  h_MET = fs->make<TH1F>("MET","MET",500,0,1000);
  h_alphaT = fs->make<TH1F>("alphaT", "alphaT", 40, 0.0, 2.0);
  mytree = fs->make<TTree>("mytree","Analysis Tree");
  mytree->Branch("gravTransMass",&G_gravTransMass);
  mytree->Branch("alphaT",&G_alphaT);
  mytree->Branch("weight",&G_weight);
  mytree->Branch("jet1pt",&G_jet1pt);
  mytree->Branch("jet1eta",&G_jet1eta);
  mytree->Branch("jet1phi",&G_jet1phi);
  mytree->Branch("jet1mass",&G_jet1mass);
  mytree->Branch("jet2pt",&G_jet2pt);
  mytree->Branch("jet2eta",&G_jet2eta);
  mytree->Branch("jet2phi",&G_jet2phi);
  mytree->Branch("jet2mass",&G_jet2mass);
  mytree->Branch("METpt",&G_METpt);
  mytree->Branch("METphi",&G_METphi);
}

RSEventAnalyzer::~RSEventAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSEventAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;

  Handle<CaloJetCollection> jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);
  Handle<CaloMETCollection> metHandle;
  iEvent.getByLabel(met_, metHandle);
  const CaloMET& theMET = metHandle->front();
  const CaloJet& theJet = (*jetsHandle)[0];
  
  double phiJet = theJet.phi();
  double phiMET = theMET.phi();
  double diffPhi = deltaPhi(phiJet,phiMET);

  // The lovely variables
  double theGravTransMass = sqrt(2*theMET.pt()*theJet.pt()*(1-cos(diffPhi)));
  double largerEt = 0.0;
  double smallerEt = 0.0;
  if(theJet.pt() >= theMET.pt()) {
    largerEt = theJet.pt();
    smallerEt = theMET.pt();
  }
  else {
    largerEt = theMET.pt();
    smallerEt = theJet.pt();
  }
  double theAlphaT = sqrt((largerEt/smallerEt)/(2*(1-cos(diffPhi))));

  // Fill the histograms.
  h_alphaT->Fill(theAlphaT);
  h_MET->Fill(theMET.pt());
  h_dPhi_jet_MET->Fill(diffPhi);
  h_gravTransMass->Fill(theGravTransMass);
  h_numJets->Fill(jetsHandle->size());

  if(jetsHandle->size() > 1) {
    const CaloJet& theSecondJet = (*jetsHandle)[1];
    double phiSecondJet = theSecondJet.phi();
    double jetsDPhi = deltaPhi(phiJet,phiSecondJet);
    h_dPhi_jets->Fill(jetsDPhi);
  }
  
  // Fill the Tree
  G_gravTransMass = theGravTransMass;
  G_alphaT = theAlphaT;
  G_jet1pt = theJet.pt();
  G_jet1eta = theJet.eta();
  G_jet1phi = theJet.phi();
  G_jet1mass = theJet.mass();
  if(jetsHandle->size() > 1) {
    const CaloJet& theSecondJet = (*jetsHandle)[1];
    G_jet2pt = theSecondJet.pt();
    G_jet2eta = theSecondJet.eta();
    G_jet2phi = theSecondJet.phi();
    G_jet2mass = theSecondJet.mass();
  }
  else {
    G_jet2pt = -9999.9;
    G_jet2eta = -9999.9;
    G_jet2phi = -9999.9;
    G_jet2mass = -9999.9;
  }
  G_METpt = theMET.pt();
  G_METphi = theMET.phi();
  
  mytree->Fill();
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSEventAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSEventAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSEventAnalyzer);
