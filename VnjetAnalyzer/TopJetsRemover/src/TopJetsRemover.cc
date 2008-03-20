// -*- C++ -*-
//
// Package:    TopJetsRemover
// Class:      TopJetsRemover
// 
/**\class TopJetsRemover TopJetsRemover.cc VnjetAnalyzer/TopJetsRemover/src/TopJetsRemover.cc

Description: <one line class summary>

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Thu Mar  6 10:35:14 CET 2008
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

// My includes
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/ShallowCloneCandidate.h"
#include "DataFormats/Common/interface/Ref.h"
#include "FWCore/Utilities/interface/Exception.h"
using namespace std;
using namespace reco;
using namespace edm;

//
// class decleration
//

class TopJetsRemover : public edm::EDProducer {
public:
  explicit TopJetsRemover(const edm::ParameterSet&);
  ~TopJetsRemover();

private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  vector<int> getAncestors(const Candidate*);
  // ----------member data ---------------------------

  InputTag particles_;

};

//
// constants, enums and typedefs
//
const int top_id = 6;
const int proton_id = 2212;
const int string_id = 92;

//
// static data member definitions
//

//
// constructors and destructor
//
TopJetsRemover::TopJetsRemover(const edm::ParameterSet& iConfig):
particles_(iConfig.getParameter<InputTag>("src") )
{
  //register your products
     produces<CandidateCollection>();

  //now do what ever other initialization is needed
}


TopJetsRemover::~TopJetsRemover()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TopJetsRemover::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;

  Handle<CandidateCollection> particles;
  iEvent.getByLabel(particles_, particles);
   
  auto_ptr<CandidateCollection> outputcands(new CandidateCollection);
  outputcands->reserve(particles->size());

  size_t idx = 0;

  // Check the ancestors of all particles, searching for top.
  
  bool foundtop;
  idx = 0;
  for( CandidateCollection::const_iterator piter = particles->begin();
       piter != particles->end();
       ++piter, ++idx) {
    
    foundtop = false;
    
    const Candidate* theParticle = &*piter;
    vector<int> particleAncestors = getAncestors(theParticle);

    for(size_t i = 0; i != particleAncestors.size(); ++i)
      if(abs(particleAncestors[i]) == top_id)
	foundtop = true;
    
    if(!foundtop) {
      CandidateBaseRef ref( CandidateRef( particles, idx ) );
      outputcands->push_back( new ShallowCloneCandidate( ref ) );
    }

  } // Ends particle loop
  
  iEvent.put(outputcands);

}

// ------------ method called once each job just before starting event loop  ------------
void 
TopJetsRemover::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TopJetsRemover::endJob() {
}

// Function to recursively get all ancestors of a Candidate.
vector<int>
TopJetsRemover::getAncestors(const Candidate* cand) {
  
  vector<int> theAncestors;
  int numOfMothers = cand->numberOfMothers();
  
  for(int i = 0; i != numOfMothers; ++i) { 
    const Candidate* thisMother = cand->mother(i);
    theAncestors.push_back(thisMother->pdgId());
    vector<int> momAncestors = getAncestors(thisMother);
    if(!momAncestors.empty())
      theAncestors.insert(theAncestors.end(), momAncestors.begin(), momAncestors.end());
  }

  return theAncestors;
}


//define this as a plug-in
DEFINE_FWK_MODULE(TopJetsRemover);
