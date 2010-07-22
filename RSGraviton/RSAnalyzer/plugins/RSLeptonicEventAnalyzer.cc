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
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/LorentzVectorFwd.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

//
// class decleration
//

class RSLeptonicEventAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSLeptonicEventAnalyzer(const edm::ParameterSet&);
  ~RSLeptonicEventAnalyzer();

private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag jets_;
  edm::InputTag met_;
  edm::InputTag electrons_;
  double G_gravTransMass;
  double G_weight;
  double G_jet1pt;
  double G_jet1eta;
  double G_jet1phi;
  double G_jet1mass;
  double G_jet1EMF;
  double G_jet2pt;
  double G_jet2eta;
  double G_jet2phi;
  double G_jet2mass;
  double G_jet2EMF;
  double G_jet3pt;
  double G_jet3eta;
  double G_jet3phi;
  double G_jet3mass;
  double G_jet3EMF;
  double G_METpt;
  double G_METphi;
  double G_MHTpt;
  double G_MHTphi;
  double G_elept;
  double G_eleeta;
  double G_elephi;
  double G_eleenergy;
  int    G_numJets;
  int    G_numElectrons;
  math::XYZTLorentzVectorCollection* G_allJets;
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
RSLeptonicEventAnalyzer::RSLeptonicEventAnalyzer(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets") ),
  met_(iConfig.getParameter<edm::InputTag>("met") ),
  electrons_(iConfig.getParameter<edm::InputTag>("electrons") ),
  G_gravTransMass(0),
  G_weight(iConfig.getParameter<double>("weight") )
{
  //now do what ever initialization is needed
  G_allJets = new math::XYZTLorentzVectorCollection;

  edm::Service<TFileService> fs;
  mytree = fs->make<TTree>("mytree","Analysis Tree");
  mytree->Branch("gravTransMass",&G_gravTransMass);
  mytree->Branch("weight",&G_weight);
  mytree->Branch("jet1pt",&G_jet1pt);
  mytree->Branch("jet1eta",&G_jet1eta);
  mytree->Branch("jet1phi",&G_jet1phi);
  mytree->Branch("jet1mass",&G_jet1mass);
  mytree->Branch("jet1EMF",&G_jet1EMF);
  mytree->Branch("jet2pt",&G_jet2pt);
  mytree->Branch("jet2eta",&G_jet2eta);
  mytree->Branch("jet2phi",&G_jet2phi);
  mytree->Branch("jet2mass",&G_jet2mass);
  mytree->Branch("jet2EMF",&G_jet2EMF);
  mytree->Branch("jet3pt",&G_jet3pt);
  mytree->Branch("jet3eta",&G_jet3eta);
  mytree->Branch("jet3phi",&G_jet3phi);
  mytree->Branch("jet3mass",&G_jet3mass);
  mytree->Branch("jet3EMF",&G_jet3EMF);
  mytree->Branch("METpt",&G_METpt);
  mytree->Branch("METphi",&G_METphi);
  mytree->Branch("MHTpt",&G_MHTpt);
  mytree->Branch("MHTphi",&G_MHTphi);
  mytree->Branch("elept",&G_elept);
  mytree->Branch("eleeta",&G_eleeta);
  mytree->Branch("elephi",&G_elephi);
  mytree->Branch("eleenergy",&G_eleenergy);
  mytree->Branch("numJets",&G_numJets);
  mytree->Branch("numElectrons",&G_numElectrons);
  mytree->Bronch("allJets", "std::vector<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > >", &G_allJets);
}

RSLeptonicEventAnalyzer::~RSLeptonicEventAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSLeptonicEventAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;

  Handle<CaloJetCollection> jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);
  Handle<CaloMETCollection> metHandle;
  iEvent.getByLabel(met_, metHandle);
  Handle<GsfElectronCollection> electronsHandle;
  iEvent.getByLabel(electrons_,electronsHandle);

  const CaloMET& theMET = metHandle->front();
  const CaloJet& theJet = jetsHandle->front();
  const GsfElectron& theElectron = electronsHandle->front();
  
  // Combine the electron and the missing Et to make the W candidate.
  double Wpx = theMET.px()+theElectron.px();
  double Wpy = theMET.py()+theElectron.py();
  double Wpt = sqrt(Wpx*Wpx+Wpy*Wpy);
  double Wphi = (Wpx==0 && Wpy==0) ? 0 : atan2(Wpy,Wpx);
  
  // Get information from the the jet.
  double jetPt = theJet.pt();
  double jetPhi = theJet.phi();
  
  // The lovely variable
  double diffPhi = deltaPhi(jetPhi,Wphi);
  double theGravTransMass = sqrt(2*Wpt*jetPt*(1-cos(diffPhi)));
  
  // Calculate MHT
  double MHTx = 0.0;
  double MHTy = 0.0;
  for(size_t i = 0; i != jetsHandle->size(); ++i) {
    MHTx += jetsHandle->at(i).px();
    MHTy += jetsHandle->at(i).py();
  }
  MHTx = (-MHTx);
  MHTy = (-MHTy);
  double MHTpt = sqrt(MHTx*MHTx + MHTy*MHTy);
  double MHTphi = (MHTx==0 && MHTy==0) ? 0 : atan2(MHTy,MHTx);
 
  // Get the largest EMF in those jets.
  double largestEMF = 0.0;
  for(size_t i = 0; i != jetsHandle->size(); ++i) {
    double theEMF = jetsHandle->at(i).emEnergyFraction();
    if(theEMF > largestEMF) largestEMF = theEMF;
  }
  
  // Fill the Tree
  G_gravTransMass = theGravTransMass;
  G_jet1pt = theJet.pt();
  G_jet1eta = theJet.eta();
  G_jet1phi = theJet.phi();
  G_jet1mass = theJet.mass();
  G_jet1EMF = theJet.emEnergyFraction();
  G_elept = theElectron.pt();
  G_eleeta = theElectron.eta();
  G_elephi = theElectron.phi();
  G_eleenergy = theElectron.energy();
  
  if(jetsHandle->size() > 1) {
    const CaloJet& theSecondJet = (*jetsHandle)[1];
    G_jet2pt = theSecondJet.pt();
    G_jet2eta = theSecondJet.eta();
    G_jet2phi = theSecondJet.phi();
    G_jet2mass = theSecondJet.mass();
    G_jet2EMF = theSecondJet.emEnergyFraction();
  }
  else {
    G_jet2pt = -9999.9;
    G_jet2eta = -9999.9;
    G_jet2phi = -9999.9;
    G_jet2mass = -9999.9;
    G_jet2EMF = -9999.9;
  }
  
  if(jetsHandle->size() > 2) {
    const CaloJet& theThirdJet = (*jetsHandle)[2];
    G_jet3pt = theThirdJet.pt();
    G_jet3eta = theThirdJet.eta();
    G_jet3phi = theThirdJet.phi();
    G_jet3mass = theThirdJet.mass();
    G_jet3EMF = theThirdJet.emEnergyFraction();
  }
  else {
    G_jet3pt = -9999.9;
    G_jet3eta = -9999.9;
    G_jet3phi = -9999.9;
    G_jet3mass = -9999.9;
    G_jet3EMF = -9999.9;
  }

  G_METpt = theMET.pt();
  G_METphi = theMET.phi();
  G_MHTpt = MHTpt;
  G_MHTphi = MHTphi;
  G_numJets = jetsHandle->size();
  G_numElectrons = electronsHandle->size();

  // And the joys of serializing a ROOT Collection.
  G_allJets->clear();
  for(size_t i = 0; i != jetsHandle->size(); ++i) {
    double jetPx = jetsHandle->at(i).px();
    double jetPy = jetsHandle->at(i).py();
    double jetPz = jetsHandle->at(i).pz();
    double jetEnergy = jetsHandle->at(i).energy();
    math::XYZTLorentzVector theJet; theJet.SetPxPyPzE(jetPx,jetPy,jetPz,jetEnergy);
    G_allJets->push_back(theJet);
  }
  
  mytree->Fill();
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSLeptonicEventAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSLeptonicEventAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSLeptonicEventAnalyzer);
