// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"

#include "DataFormats/Common/interface/View.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "DataFormats/Math/interface/LorentzVectorFwd.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

//
// class decleration
//

class ZZ2q2nuTreeMaker : public edm::EDAnalyzer {
public:
  explicit ZZ2q2nuTreeMaker(const edm::ParameterSet&);
  ~ZZ2q2nuTreeMaker();

private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag jets_;
  edm::InputTag met_;
  edm::InputTag electrons_;
  edm::InputTag muons_;
  edm::InputTag genParticles_;
  edm::InputTag VBTFmuon_;
  edm::InputTag TIV_;
  edm::InputTag TIVStar_;
  edm::InputTag PUweight_;
  edm::InputTag extraWeight_;

  bool isData_;
 
  int G_eventNumber;
  int G_runNumber;
  int G_lumiNumber;

  double G_gravTransMass;
  double G_weight;
  double G_jet1pt;
  double G_jet1eta;
  double G_jet1phi;
  double G_jet1mass;
  double G_jet2pt;
  double G_jet2eta;
  double G_jet2phi;
  double G_jet2mass;
  double G_jet3pt;
  double G_jet3eta;
  double G_jet3phi;
  double G_jet3mass;

  double G_METpt;
  double G_METphi;

  double G_smallestTIV;
  double G_smallestTIVStar;

  double G_PUweight;

  double G_electron1pt;
  double G_electron1eta;
  double G_electron1phi;
  double G_electron2pt;
  double G_electron2eta;
  double G_electron2phi;

  double G_muon1pt;
  double G_muon1eta;
  double G_muon1phi;
  double G_muon2pt;
  double G_muon2eta;
  double G_muon2phi;

  int    G_numJets;
  int    G_numElectrons;
  int    G_numMuons;

  int    G_muonVBTF;  
  int    G_numParticles; 
  int    G_particlesPdg[99];

  math::XYZTLorentzVectorCollection* G_allJets;
  math::XYZTLorentzVectorCollection* G_allParticles;
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
ZZ2q2nuTreeMaker::ZZ2q2nuTreeMaker(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets") ),
  met_(iConfig.getParameter<edm::InputTag>("met") ),
  electrons_(iConfig.getParameter<edm::InputTag>("electrons") ),
  muons_(iConfig.getParameter<edm::InputTag>("muons") ),
  genParticles_(iConfig.getParameter<edm::InputTag>("genParticles") ),
  VBTFmuon_(iConfig.getParameter<edm::InputTag>("VBTFmuon") ),
  TIV_(iConfig.getParameter<edm::InputTag>("TIV") ),
  TIVStar_(iConfig.getParameter<edm::InputTag>("TIVStar") ),
  PUweight_(iConfig.getParameter<edm::InputTag>("PUweight") ),
  extraWeight_(iConfig.getParameter<edm::InputTag>("extraWeight") ),
  isData_(iConfig.getParameter<bool>("isData") ),
  G_gravTransMass(0),
  G_weight(iConfig.getParameter<double>("weight") )
{
  //now do what ever initialization is needed
  G_allJets = new math::XYZTLorentzVectorCollection;
  G_allParticles = new math::XYZTLorentzVectorCollection;

  edm::Service<TFileService> fs;
  mytree = fs->make<TTree>("mytree","Analysis Tree");
  mytree->Branch("eventNumber",&G_eventNumber);
  mytree->Branch("runNumber",&G_runNumber);
  mytree->Branch("lumiNumber",&G_lumiNumber);

  mytree->Branch("gravTransMass",&G_gravTransMass);
  mytree->Branch("weight",&G_weight);
  mytree->Branch("jet1pt",&G_jet1pt);
  mytree->Branch("jet1eta",&G_jet1eta);
  mytree->Branch("jet1phi",&G_jet1phi);
  mytree->Branch("jet1mass",&G_jet1mass);

  mytree->Branch("jet2pt",&G_jet2pt);
  mytree->Branch("jet2eta",&G_jet2eta);
  mytree->Branch("jet2phi",&G_jet2phi);
  mytree->Branch("jet2mass",&G_jet2mass);

  mytree->Branch("jet3pt",&G_jet3pt);
  mytree->Branch("jet3eta",&G_jet3eta);
  mytree->Branch("jet3phi",&G_jet3phi);
  mytree->Branch("jet3mass",&G_jet3mass);

  mytree->Branch("METpt",&G_METpt);
  mytree->Branch("METphi",&G_METphi);

  mytree->Branch("smallestTIV",&G_smallestTIV);
  mytree->Branch("smallestTIVStar",&G_smallestTIVStar);

  mytree->Branch("PUweight",&G_PUweight);

  mytree->Branch("electron1pt",&G_electron1pt);
  mytree->Branch("electron1eta",&G_electron1eta);
  mytree->Branch("electron1phi",&G_electron1phi);
  mytree->Branch("electron2pt",&G_electron2pt);
  mytree->Branch("electron2eta",&G_electron2eta);
  mytree->Branch("electron2phi",&G_electron2phi);

  mytree->Branch("muon1pt",&G_muon1pt);
  mytree->Branch("muon1eta",&G_muon1eta);
  mytree->Branch("muon1phi",&G_muon1phi);
  mytree->Branch("muon2pt",&G_muon2pt);
  mytree->Branch("muon2eta",&G_muon2eta);
  mytree->Branch("muon2phi",&G_muon2phi);

  mytree->Bronch("allJets", "std::vector<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > >", &G_allJets);
  mytree->Bronch("allParticles", "std::vector<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > >", &G_allParticles);
  mytree->Branch("numJets",&G_numJets);
  mytree->Branch("numElectrons",&G_numElectrons);
  mytree->Branch("numMuons",&G_numMuons);

  mytree->Branch("muonVBTF",&G_muonVBTF);  

  mytree->Branch("numParticles",&G_numParticles);
  mytree->Branch("particlesPdg" ,G_particlesPdg,"particlesPdg[99]/I");
}

ZZ2q2nuTreeMaker::~ZZ2q2nuTreeMaker()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
ZZ2q2nuTreeMaker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;


  // Come on everybody!
  Handle<edm::View<reco::Candidate> > jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);
  Handle<pat::METCollection> metHandle;
  iEvent.getByLabel(met_, metHandle);
  Handle<pat::ElectronCollection> electronsHandle;
  iEvent.getByLabel(electrons_,electronsHandle);
  Handle<pat::MuonCollection> muonsHandle;
  iEvent.getByLabel(muons_,muonsHandle);
  Handle<double> TIVHandle;
  iEvent.getByLabel(TIV_,TIVHandle);
  Handle<double> TIVStarHandle;
  iEvent.getByLabel(TIVStar_,TIVStarHandle);
  Handle<pat::MuonCollection> VBTFmuonHandle;
  iEvent.getByLabel(VBTFmuon_,VBTFmuonHandle);

  const pat::MET& theMET = metHandle->front();
  
  double theGravTransMass = -1.0;

  // Fill the Tree

  G_eventNumber = iEvent.id().event();
  G_runNumber = iEvent.id().run();
  G_lumiNumber = iEvent.id().luminosityBlock();

  if(jetsHandle->size() > 0) {
    const reco::Candidate& theFirstJet = (*jetsHandle)[0];
    G_jet1pt = theFirstJet.pt();
    G_jet1eta = theFirstJet.eta();
    G_jet1phi = theFirstJet.phi();
    G_jet1mass = theFirstJet.mass();
    double dphi = deltaPhi(theMET.phi(),theFirstJet.phi());
    theGravTransMass = sqrt(2.0 * theFirstJet.pt() *
			    theMET.pt() * 
			    (1.0 - cos(dphi))
			    );
  } 
  else {
    G_jet1pt = -9999.9;
    G_jet1eta = -9999.9;
    G_jet1phi = -9999.9;
    G_jet1mass = -9999.9;
  }
  
  G_gravTransMass = theGravTransMass;
  
  if(jetsHandle->size() > 1) {
    const reco::Candidate& theSecondJet = (*jetsHandle)[1];
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
  
  if(jetsHandle->size() > 2) {
    const reco::Candidate& theThirdJet = (*jetsHandle)[2];
    G_jet3pt = theThirdJet.pt();
    G_jet3eta = theThirdJet.eta();
    G_jet3phi = theThirdJet.phi();
  }
  else {
    G_jet3pt = -9999.9;
    G_jet3eta = -9999.9;
    G_jet3phi = -9999.9;
    G_jet3mass = -9999.9;
  }
  G_numJets = jetsHandle->size();

  // The METs
  G_METpt = theMET.pt();
  G_METphi = theMET.phi();

  // The leptons
  int numElectrons = electronsHandle->size();
  int numMuons = muonsHandle->size();

  // Electrons
  G_numElectrons = numElectrons;
  if(numElectrons > 0) {
    const pat::Electron& ele = (*electronsHandle)[0];
    G_electron1pt = ele.pt();
    G_electron1eta = ele.eta();
    G_electron1phi = ele.phi();
  }
  else {
    G_electron1pt = -9999.9;
    G_electron1eta = -9999.9;
    G_electron1phi = -9999.9;
  }
  if(numElectrons > 1) {
    const pat::Electron& ele = (*electronsHandle)[1];
    G_electron2pt = ele.pt();
    G_electron2eta = ele.eta();
    G_electron2phi = ele.phi();
  }
  else {
    G_electron2pt = -9999.9;
    G_electron2eta = -9999.9;
    G_electron2phi = -9999.9;
  }
  // Muons
  G_numMuons = numMuons;
  if(numMuons > 0) {
    const pat::Muon& mu = (*muonsHandle)[0];
    G_muon1pt = mu.pt();
    G_muon1eta = mu.eta();
    G_muon1phi = mu.phi();
  }
  else {
    G_muon1pt = -9999.9;
    G_muon1eta = -9999.9;
    G_muon1phi = -9999.9;
  }
  if(numMuons > 1) {
    const pat::Muon& mu = (*muonsHandle)[1];
    G_muon2pt = mu.pt();
    G_muon2eta = mu.eta();
    G_muon2phi = mu.phi();
  }
  else {
    G_muon2pt = -9999.9;
    G_muon2eta = -9999.9;
    G_muon2phi = -9999.9;
  }

  double theTIV = *TIVHandle;
  double theTIVStar = *TIVStarHandle;
  int theVBTFmu = VBTFmuonHandle->size();
  G_smallestTIV = theTIV;
  G_smallestTIVStar = theTIVStar;
  G_muonVBTF = theVBTFmu;

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
  
  // And the lovely particles.
  Handle<GenParticleCollection> genParticlesHandle;
  Handle<double> PUweightHandle;
  Handle<double> extraWeightHandle;
  if(isData_) {
    G_allParticles->clear();
    math::XYZTLorentzVector theGenParticle; theGenParticle.SetPxPyPzE(-1,-1,-1,-1);
    G_allParticles->push_back(theGenParticle);
    G_particlesPdg[0] = 0;
    G_weight = 1.0;
    G_PUweight = 1.0;
    G_numParticles = -1;
  }
  else {
    Handle<GenEventInfoProduct> infoHandle;
    iEvent.getByLabel("generator",infoHandle);
    const GenEventInfoProduct geneventinfo = *infoHandle;
    double gen_weight=geneventinfo.weight();
    G_weight = gen_weight;
    
    iEvent.getByLabel(genParticles_, genParticlesHandle);
    int actualNumParticles = genParticlesHandle->size();
    iEvent.getByLabel(PUweight_,PUweightHandle);
    double thePUweight = *PUweightHandle;
    
    iEvent.getByLabel(extraWeight_,extraWeightHandle);
    G_weight = *extraWeightHandle;

    G_PUweight = thePUweight;
    G_allParticles->clear();
    for(size_t i = 0; i != genParticlesHandle->size(); ++i) {
      double genParticlePx = genParticlesHandle->at(i).px();
      double genParticlePy = genParticlesHandle->at(i).py();
      double genParticlePz = genParticlesHandle->at(i).pz();
      double genParticleEnergy = genParticlesHandle->at(i).energy();
      math::XYZTLorentzVector theGenParticle; theGenParticle.SetPxPyPzE(genParticlePx,genParticlePy,genParticlePz,genParticleEnergy);
      G_allParticles->push_back(theGenParticle);
      G_particlesPdg[i] = int(genParticlesHandle->at(i).pdgId());
    }
    G_numParticles = actualNumParticles;
  } 
  // Pray
  mytree->Fill();
}

// ------------ method called once each job just before starting event loop  ------------
void 
ZZ2q2nuTreeMaker::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ZZ2q2nuTreeMaker::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(ZZ2q2nuTreeMaker);
