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
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
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
  virtual void beginJob(const edm::EventSetup&) ;
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
  double G_gravTransMass;
  double G_weight;
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
  mytree = fs->make<TTree>("mytree","Analysis Tree");
  mytree->Branch("gravTransMass",&G_gravTransMass);
  mytree->Branch("weight",&G_weight);
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

  double theGravTransMass = sqrt(2*theMET.pt()*theJet.pt()*(1-cos(diffPhi)));
  // Fill the histograms.
  h_MET->Fill(theMET.pt());
  h_dPhi_jet_MET->Fill(diffPhi);
  h_gravTransMass->Fill(theGravTransMass);
  h_numJets->Fill(jetsHandle->size());

  if(jetsHandle->size() == 2) {
    const CaloJet& theSecondJet = (*jetsHandle)[1];
    double phiSecondJet = theSecondJet.phi();
    double jetsDPhi = deltaPhi(phiJet,phiSecondJet);
    h_dPhi_jets->Fill(jetsDPhi);
  }
  // Fill the Tree
  G_gravTransMass = theGravTransMass;
  mytree->Fill();
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSEventAnalyzer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSEventAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSEventAnalyzer);
