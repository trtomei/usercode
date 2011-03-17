// system include files
#include <memory>
#include <string>
#include <iostream>
#include <fstream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TLorentzVector.h"
#include "TVector3.h"
#include "TH1F.h"
#include "TH2F.h"
//
// class declaration
//

class RSGenEventAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSGenEventAnalyzer(const edm::ParameterSet&);
  ~RSGenEventAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
      // ----------member data ---------------------------
  int  gravPdgId_;
  bool allProcesses_;
  bool qqbarProcess_;
  
  TH1F*   h_cTheta;
  TH2F*   h_jetMass_Zpt;
  TH2F*   h_dRJetZ_Zpt;
  TH2F*   h_dPtJetZ_Zpt;
  TH1F*   h_gravTransMass;
  TH1F*   h_genMET;
  TH2F*   h_dRDaughtersZ1;
  TH2F*   h_dRDaughtersZ2;
  TH2F*   h_dRZ1D1;
  TH2F*   h_dRZ1D2;
  TH2F*   h_dRZ2D1;
  TH2F*   h_dRZ2D2;
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
RSGenEventAnalyzer::RSGenEventAnalyzer(const edm::ParameterSet& iConfig) :
  gravPdgId_(iConfig.getParameter<int>("gravPdgId")),
  allProcesses_(iConfig.getParameter<bool>("allProcesses")),
  qqbarProcess_(iConfig.getParameter<bool>("qqbarProcess"))
{
  edm::Service<TFileService> fs;
  h_cTheta = fs->make<TH1F>("cTheta","Cos theta*",25,-1,1);
  h_jetMass_Zpt = fs->make<TH2F>("jetMas_Zpt","Jet mass X Z pT",40,0.0,200.0,400,0.0,2000.0);
  h_dRJetZ_Zpt = fs->make<TH2F>("dRJetZ_Zpt","dR between jet and Z X Z pT",200,0.0,2.0,400,0.0,2000.0);
  h_dPtJetZ_Zpt = fs->make<TH2F>("dPtJetZ_Zpt","dpT between jet and Z X Z pT",50,0.0,50.0,400,0.0,2000.0);
  h_gravTransMass = fs->make<TH1F>("gravTransMass","Graviton transverse mass",400,0.0,2000.0);
  h_genMET = fs->make<TH1F>("genMET","Missing transverse energy",400,0.0,2000.0);
  h_dRDaughtersZ1 = fs->make<TH2F>("dRDaughtersZ1","dR between daughters of Z",200,0.0,2.0,400,0.0,2000.0);
  h_dRDaughtersZ2 = fs->make<TH2F>("dRDaughtersZ2","dR between daughters of Z",200,0.0,2.0,400,0.0,2000.0);
  h_dRZ1D1 = fs->make<TH2F>("dRZ1D1","dR between daughter and Z X Z pT",200,0.0,2.0,400,0.0,2000.0);
  h_dRZ1D2 = fs->make<TH2F>("dRZ1D2","dR between daughter and Z X Z pT",200,0.0,2.0,400,0.0,2000.0);
  h_dRZ2D1 = fs->make<TH2F>("dRZ2D1","dR between daughter and Z X Z pT",200,0.0,2.0,400,0.0,2000.0);
  h_dRZ2D2 = fs->make<TH2F>("dRZ2D2","dR between daughter and Z X Z pT",200,0.0,2.0,400,0.0,2000.0);
}


RSGenEventAnalyzer::~RSGenEventAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
RSGenEventAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  std::cout << "uno" << std::endl;
  // Get everything we need from the Event
  edm::Handle<reco::GenParticleCollection> genParticles_h;
  iEvent.getByLabel("prunedGenParticles",genParticles_h);
  edm::Handle<reco::GenMETCollection> genMet_h;
  iEvent.getByLabel("genMetTrue",genMet_h);
  edm::Handle<reco::GenJetCollection> genJets_h;
  iEvent.getByLabel("sortedJets",genJets_h);

  std::cout << "dos" << std::endl;
  // Get the Graviton
  const reco::GenParticle* theGraviton = 0;
  for(reco::GenParticleCollection::const_iterator i = genParticles_h->begin();
      i != genParticles_h->end();
      ++i) {
    if(i->pdgId() == gravPdgId_ && i->numberOfDaughters() == 2) {
      theGraviton = &(*i);
      break;
    }
  }
  
  // Do the check for the sixth particle - to be sure we are coming from qqbar or gluongluon, as asked.
  std::cout << "tres" << std::endl;
  const reco::GenParticle* theMother = &(genParticles_h->at(5));
  if(allProcesses_ == false) {
    if(qqbarProcess_ == true)
      if(std::abs(theMother->pdgId()) > 7)
	return;
    if(qqbarProcess_ == false)
      if(theMother->pdgId() != 21)
	return;
  }
  
  std::cout << "cuatro" << std::endl;
  const reco::Candidate* Z1 = theGraviton->daughter(0);
  const reco::Candidate* Z2 = theGraviton->daughter(1);
  const reco::Candidate* Z1D1 = Z1->daughter(0);
  const reco::Candidate* Z1D2 = Z1->daughter(1);
  const reco::Candidate* Z2D1 = Z2->daughter(0);
  const reco::Candidate* Z2D2 = Z2->daughter(1);  

  std::cout << "cinco" << std::endl;
  // dR Z daughters X Z pt
  double dRDaughtersZ1 = deltaR(Z1D1->eta(),Z1D1->phi(),Z1D2->eta(),Z1D2->phi()); 
  double dRZ1D1 = deltaR(Z1->eta(),Z1->phi(),Z1D1->eta(),Z1D1->phi());
  double dRZ1D2 = deltaR(Z1->eta(),Z1->phi(),Z1D2->eta(),Z1D2->phi());
  double dRDaughtersZ2 = deltaR(Z2D1->eta(),Z2D1->phi(),Z2D2->eta(),Z2D2->phi()); 
  double dRZ2D1 = deltaR(Z2->eta(),Z2->phi(),Z2D1->eta(),Z2D1->phi());
  double dRZ2D2 = deltaR(Z2->eta(),Z2->phi(),Z2D2->eta(),Z2D2->phi());
  h_dRDaughtersZ1->Fill(dRDaughtersZ1,Z1->pt());
  h_dRDaughtersZ2->Fill(dRDaughtersZ2,Z2->pt());
  h_dRZ1D1->Fill(dRZ1D1,Z1->pt());
  h_dRZ1D2->Fill(dRZ1D2,Z1->pt());
  h_dRZ2D1->Fill(dRZ2D1,Z2->pt());
  h_dRZ2D2->Fill(dRZ2D2,Z2->pt());
    
  std::cout << "seis" << std::endl;
  // GenMET
  const reco::GenMET& theMET = genMet_h->front();
  h_genMET->Fill(theMET.pt());
  
  std::cout << "siete" << std::endl;
  // GenJets
  const reco::GenJet& theJet= (*genJets_h)[0];
  const reco::Candidate* ZHad = 0;
  if(std::abs(Z1D1->pdgId()) < 7)
    ZHad = Z1;
  else if (std::abs(Z2D1->pdgId()) < 7)
    ZHad = Z2;
  double dRJetZ = deltaR(theJet.eta(),theJet.phi(),ZHad->eta(),ZHad->phi());
  double dPtJetZ = std::abs(theJet.pt() - ZHad->pt());
  h_jetMass_Zpt->Fill(theJet.mass(),ZHad->pt());
  h_dRJetZ_Zpt->Fill(dRJetZ,ZHad->pt());
  h_dPtJetZ_Zpt->Fill(dPtJetZ,ZHad->pt());
  
  std::cout << "ocho" << std::endl;
  // GTM
  double phiJet = theJet.phi();
  double phiMET = theMET.phi();
  double diffPhi = deltaPhi(phiJet,phiMET);
  double theGravTransMass = sqrt(2*theMET.pt()*theJet.pt()*(1-cos(diffPhi)));
  h_gravTransMass->Fill(theGravTransMass);
  
  std::cout << "nueve" << std::endl;
  // Cosine theta star
  TLorentzVector zed1; zed1.SetPxPyPzE(Z1->px(),Z1->py(),Z1->pz(),Z1->energy());
  TLorentzVector zed2; zed2.SetPxPyPzE(Z2->px(),Z2->py(),Z2->pz(),Z2->energy());
  TLorentzVector CoM(zed1+zed2);
  TVector3 theBoostVector = -CoM.BoostVector();
  zed1.Boost(theBoostVector);
  zed2.Boost(theBoostVector);
  double cTheta1 = zed1.CosTheta();
  double cTheta2 = zed2.CosTheta();
  h_cTheta->Fill(cTheta1);
  h_cTheta->Fill(cTheta2);
}


// ------------ method called once each job just before starting event loop  ------------
void 
RSGenEventAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
RSGenEventAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSGenEventAnalyzer);
