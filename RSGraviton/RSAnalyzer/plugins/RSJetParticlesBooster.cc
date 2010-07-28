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
// $Id: RSJetParticlesBooster.cc,v 1.2 2009/05/22 11:48:11 tomei Exp $
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
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"

#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
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
  produces<reco::PFCandidateCollection>();
  produces<math::XYZVector>();
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
   
   Handle<PFJetCollection> jetsHandle;
   iEvent.getByLabel(jets_,jetsHandle);
   const PFJetCollection theJets = *jetsHandle;
   
   // The products.
   std::auto_ptr<PFCandidateCollection> boostedParticlesJet(new PFCandidateCollection);
   std::auto_ptr<math::XYZVector> boostVector(new math::XYZVector);

   // Get the correct jet.
   const PFJet& theJet(theJets[nJet_]);
   // Get the jet 4vector, and make it into a suitable TLorentzVector.
   TLorentzVector theFourVec(theJet.px(), theJet.py(), theJet.pz(), theJet.energy());
   // Get the BoostVector.
   TVector3 boostVec (theFourVec.BoostVector());
   boostVector->SetXYZ(boostVec.X(), boostVec.Y(), boostVec.Z());

   // Get the constituents of the jet and boost them to jet rest frame.
   std::vector<const Candidate*> theConstituents = theJet.getJetConstituentsQuick();
   for(std::vector<const Candidate*>::const_iterator c = theConstituents.begin();
       c != theConstituents.end(); ++c) {
     TLorentzVector theParticle((*c)->px(), (*c)->py(), (*c)->pz(), (*c)->energy());
     theParticle.Boost(-boostVec);
     math::XYZTLorentzVector theBoostedParticle; 
     theBoostedParticle.SetPxPyPzE(theParticle.Px(), theParticle.Py(), theParticle.Pz(), theParticle.E()); 
     PFCandidate theBP2(0, theBoostedParticle, PFCandidate::h0);
     
     // After all those format shifts, put the particle back in the collection.
     boostedParticlesJet->push_back(theBP2);
   }
   
   iEvent.put(boostVector);
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
