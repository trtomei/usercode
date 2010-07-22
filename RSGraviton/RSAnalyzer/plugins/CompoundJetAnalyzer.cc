// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include <TH1F.h>
#include <TH2F.h>
#include <TLorentzVector.h>
//
// class declaration
//

class CompoundJetAnalyzer : public edm::EDAnalyzer {
public:
  explicit CompoundJetAnalyzer(const edm::ParameterSet&);
  ~CompoundJetAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  edm::InputTag compoundJets_;
  edm::InputTag standardJets_;
  
  TH1F* h_numSubJets;

  TH1F* h_jet1_subJet1Pt;
  TH1F* h_jet1_subJet2Pt;
  TH1F* h_jet1_invMassSubJets;
  TH1F* h_jet1_massDropT1;
  TH1F* h_jet1_massDropT2;
      // ----------member data ---------------------------
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
CompoundJetAnalyzer::CompoundJetAnalyzer(const edm::ParameterSet& iConfig):
  compoundJets_(iConfig.getParameter<edm::InputTag>("compoundJets")),
  standardJets_(iConfig.getParameter<edm::InputTag>("standardJets"))
{
  edm::Service<TFileService> fs;

  h_numSubJets = fs->make<TH1F> ("numSubJets","numSubJets",10,-0.5,9.5);

  h_jet1_subJet1Pt = fs->make<TH1F> ("jet1_subJet1Pt","jet1_subJet1Pt",200,0.0,1000.0);
  h_jet1_subJet2Pt = fs->make<TH1F> ("jet1_subJet2Pt","jet1_subJet2Pt",200,0.0,1000.0);
  h_jet1_invMassSubJets = fs->make<TH1F> ("jet1_invMassSubJets","jet1_invMassSubJets",100,0.0,200.0);
  h_jet1_massDropT1 = fs->make<TH1F>("jet1_massDropT1","jet1_massDropT1",100,0.0,1.0);
  h_jet1_massDropT2 = fs->make<TH1F>("jet1_massDropT2","jet1_massDropT2",100,0.0,1.0);
  //now do what ever initialization is needed
}


CompoundJetAnalyzer::~CompoundJetAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
CompoundJetAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   
   // Get the compound jets collection.
   Handle<std::vector<reco::BasicJet> > pBasicJets;
   iEvent.getByLabel(compoundJets_, pBasicJets);
   
   // Get the standard jets collection.
   // Ideally by now we would like to have a single CaloJet here.
   Handle<reco::CaloJetCollection> pCaloJets;
   iEvent.getByLabel(standardJets_, pCaloJets);
   const reco::CaloJet& standardJet = pCaloJets->at(0);

   // Now Loop over the compound jets and find the one which matches. 
   int theMatchingJetNumber = 0;
   double minDR = 9999.9;
 
   for(size_t j=0; j < pBasicJets->size(); j++) {

     // Find the closest jet.
     const reco::BasicJet& thisJet = pBasicJets->at(j);
     double dR = deltaR(standardJet.eta(),standardJet.phi(),thisJet.eta(),thisJet.phi());
     if(dR < minDR) {
       theMatchingJetNumber = j;
       minDR = dR;
     }
   }   
   
   // Check that the jet really matches
   if (minDR>0.25)
     return;
   
   const reco::BasicJet& fatJet = pBasicJets->at(theMatchingJetNumber);
   // If we managed to get here, they match.
   h_numSubJets->Fill(fatJet.numberOfDaughters());

   // Check if there are two subjets. If not, BREAK!
   if(fatJet.numberOfDaughters() != 2)
     return;
   
   const reco::Candidate* subJetA = fatJet.daughter(0);
   const reco::Candidate* subJetB = fatJet.daughter(1);
   if(subJetA->pt() > subJetB->pt()) {
     h_jet1_subJet1Pt->Fill(subJetA->pt());
     h_jet1_subJet2Pt->Fill(subJetB->pt());
   }
   if(subJetB->pt() > subJetA->pt()) {
     h_jet1_subJet1Pt->Fill(subJetB->pt());
     h_jet1_subJet2Pt->Fill(subJetA->pt());
   }
   
   TLorentzVector sum;
   sum.SetPx(subJetA->px()+subJetB->px());
   sum.SetPy(subJetA->py()+subJetB->py());
   sum.SetPz(subJetA->pz()+subJetB->pz());
   sum.SetE(subJetA->energy()+subJetB->energy());
   h_jet1_invMassSubJets->Fill(sum.M());
   
   double averageMass = (subJetA->mass() + subJetB->mass())/2.0;
   double largestMass;
   if(subJetA->mass() > subJetB->mass())
     largestMass = subJetA->mass();
   else
     largestMass = subJetB->mass();
   double massDropT1 = (sum.M()-averageMass)/sum.M();
   double massDropT2 = (sum.M()-largestMass)/sum.M();
   h_jet1_massDropT1->Fill(massDropT1);
   h_jet1_massDropT2->Fill(massDropT2);
}

// ------------ method called once each job just before starting event loop  ------------
void 
CompoundJetAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CompoundJetAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE( CompoundJetAnalyzer );
