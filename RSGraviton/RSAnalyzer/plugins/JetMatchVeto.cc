// -*- C++ -*-
//
// Package:    JetMatchVeto
// Class:      JetMatchVeto
// 
/**\class JetMatchVeto JetMatchVeto.cc RSGraviton/JetMatchVeto/src/JetMatchVeto.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  
//         Created:  Thu Feb  5 11:24:52 BRST 2009
// $Id$
//
//


// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
//
// class declaration
//

class JetMatchVeto : public edm::EDFilter {
public:
  explicit JetMatchVeto(const edm::ParameterSet&);
  ~JetMatchVeto();
  
private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  edm::InputTag src_;
  edm::InputTag matched_;
  TH1F* h_dPtOverPt;
  double maxDeltaR;
  bool jetsOK;

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
JetMatchVeto::JetMatchVeto(const edm::ParameterSet& iConfig):
  src_(iConfig.getParameter<edm::InputTag>("src")),
  matched_(iConfig.getParameter<edm::InputTag>("matched")),
  maxDeltaR(iConfig.getParameter<double>("maxDeltaR")),
  jetsOK(true)
{
  edm::Service<TFileService> fs;
  h_dPtOverPt = fs->make<TH1F> ("dPtOverPt", "dPtOverPt", 100, 0.0, 1.0);
   //now do what ever initialization is needed

}


JetMatchVeto::~JetMatchVeto()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
JetMatchVeto::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   // Get the two collections of jets
   Handle<reco::CaloJetCollection> src;
   iEvent.getByLabel(src_,src);
   Handle<reco::CaloJetCollection> matched;
   iEvent.getByLabel(matched_,matched);
   
   // See if any of the matched jets is inside the src jets.
   double deltaRvalue = 0.0;
   for(reco::CaloJetCollection::const_iterator srcjet = src->begin();
       srcjet != src->end(); ++srcjet) {
     for(reco::CaloJetCollection::const_iterator mtcjet = matched->begin();
       mtcjet != matched->end(); ++mtcjet) {
       deltaRvalue = deltaR(srcjet->eta(),srcjet->phi(),mtcjet->eta(),mtcjet->phi());
       if(deltaRvalue < maxDeltaR) {
	 double dPtOverPt (std::abs(srcjet->pt()-mtcjet->pt())/srcjet->pt());
	 h_dPtOverPt->Fill(dPtOverPt);
	 jetsOK = false;
       }
     }
   }

   // We want the filter to stop if jets match.
   return jetsOK;
}

// ------------ method called once each job just before starting event loop  ------------
void 
JetMatchVeto::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetMatchVeto::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetMatchVeto);
