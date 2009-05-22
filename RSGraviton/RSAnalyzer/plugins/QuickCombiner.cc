// -*- C++ -*-
//
// Package:    QuickCombiner
// Class:      QuickCombiner
// 
/**\class QuickCombiner QuickCombiner.cc RSGraviton/QuickCombiner/src/QuickCombiner.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez Tomei
//         Created:  Fri May 22 08:13:21 CEST 2009
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
//
// class decleration
//

class QuickCombiner : public edm::EDProducer {
   public:
      explicit QuickCombiner(const edm::ParameterSet&);
      ~QuickCombiner();

   private:
      virtual void beginJob(const edm::EventSetup&) ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
  edm::InputTag src_;
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
QuickCombiner::QuickCombiner(const edm::ParameterSet& iConfig) :
  src_(iConfig.getParameter<edm::InputTag>("src"))
{
  produces<std::vector<reco::LeafCandidate> >();
}


QuickCombiner::~QuickCombiner()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
QuickCombiner::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;
   Handle<CandidateView> jetsHandle;
   iEvent.getByLabel(src_, jetsHandle);

   double pxTotal = 0;
   double pyTotal = 0;
   double pzTotal = 0;
   double energyTotal = 0;
   for(CandidateView::const_iterator j = jetsHandle->begin(); j != jetsHandle->end(); ++j) {
     pxTotal += j->px();
     pyTotal += j->py();
     pzTotal += j->pz();
     energyTotal += j->energy();
   }

   math::XYZTLorentzVector lv;
   lv.SetPx(pxTotal);
   lv.SetPy(pyTotal);
   lv.SetPz(pzTotal);
   lv.SetE(energyTotal);

   LeafCandidate theGraviton(0, lv);
   
   std::auto_ptr<std::vector<LeafCandidate> > gravitons(new std::vector<LeafCandidate>);
   gravitons->push_back(theGraviton);

   iEvent.put(gravitons);
}

// ------------ method called once each job just before starting event loop  ------------
void 
QuickCombiner::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
QuickCombiner::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(QuickCombiner);
