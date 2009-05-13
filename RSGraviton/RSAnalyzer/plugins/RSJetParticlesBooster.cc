// -*- C++ -*-
//
// Package:    RSJetParticlesBooster
// Class:      RSJetParticlesBooster
// 
/**\class RSJetParticlesBooster RSJetParticlesBooster.cc RSGraviton/RSJetParticlesBooster/src/RSJetParticlesBooster.cc

 Description: Class to analyze the flow of energy inside jets, using tracks.

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  
//         Created:  Thu Jan 15 18:14:18 BRST 2009
// $Id: RSJetParticlesBooster.cc,v 1.3 2009/05/07 13:52:19 tomei Exp $
//
//


// system include files
#include <memory>
#include <vector>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/InputTag.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"

#include "DataFormats/Math/interface/LorentzVector.h"
#include <TLorentzVector.h> 
#include <TVector3.h>

//
// class decleration
//

class RSJetParticlesBooster : public edm::EDProducer {
public:
  explicit RSJetParticlesBooster(const edm::ParameterSet&);
  ~RSJetParticlesBooster();
  
  
private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  // ----------member data ---------------------------
  edm::InputTag jets_;
  size_t nJet_;
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
RSJetParticlesBooster::RSJetParticlesBooster(const edm::ParameterSet& iConfig)

{
  jets_ = iConfig.getParameter<edm::InputTag>("jets");
  nJet_ = iConfig.getParameter<unsigned int>("nJet");
  produces<reco::GenParticleCollection>();
}


RSJetParticlesBooster::~RSJetParticlesBooster()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSJetParticlesBooster::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;
   
   Handle<GenJetCollection> jetsHandle;
   iEvent.getByLabel(jets_,jetsHandle);
   const GenJetCollection theJets = *jetsHandle;
   
   // The products.
   std::auto_ptr<GenParticleCollection> boostedParticlesJet(new GenParticleCollection);

   // Get the correct jet.
   const GenJet& theJet(theJets[nJet_]);
   // Get the jet 4vector, and make it into a suitable TLorentzVector.
   TLorentzVector theFourVec(theJet.px(), theJet.py(), theJet.pz(), theJet.energy());
   // Get the BoostVector.
   TVector3 boostVec (theFourVec.BoostVector());
   
   // Get the constituents of the jet and boost them to jet rest frame.
   std::vector<const Candidate*> theConstituents = theJet.getJetConstituentsQuick();
   for(std::vector<const Candidate*>::const_iterator c = theConstituents.begin();
       c != theConstituents.end(); ++c) {
     TLorentzVector theParticle((*c)->px(), (*c)->py(), (*c)->pz(), (*c)->energy());
     theParticle.Boost(-boostVec);
     math::XYZTLorentzVector theBoostedParticle; 
     theBoostedParticle.SetPxPyPzE(theParticle.Px(), theParticle.Py(), theParticle.Pz(), theParticle.E()); 
     LeafCandidate theBP2((*c)->charge(), theBoostedParticle);
     GenParticle theBP3(theBP2);
     
     // After all those format shifts, put the particle back in the collection.
     boostedParticlesJet->push_back(theBP3);
   }
   
   iEvent.put(boostedParticlesJet);
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSJetParticlesBooster::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSJetParticlesBooster::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSJetParticlesBooster);
