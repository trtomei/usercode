// -*- C++ -*-
//
// Package:    CustomCandidateProducer
// Class:      CustomCandidateProducer
// 
/**\class CustomCandidateProducer CustomCandidateProducer.cc VnjetAnalyzer/CustomCandidateProducer/src/CustomCandidateProducer.cc

Description: <one line class summary>

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Fri Nov 23 09:02:06 CET 2007
// $Id$
//
//


// system include files
#include <memory>
//#include <vector>
//#include <utility>

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

class CustomCandidateProducer : public edm::EDProducer {
public:
  explicit CustomCandidateProducer(const edm::ParameterSet&);
  ~CustomCandidateProducer();

private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  bool statusCheck(int status, int goal);
  bool pdgIdCheck(int status, vector<int> goal);
  // ----------member data ---------------------------

  InputTag particles_;
  bool debugmode_;
  int maxInputParticles;
  int maxOutputParticles;
  vector<int> vpdgId;
  int status;
  vector<int> vpdgIdmothers;
  int statusmothers;
   vector<int> vpdgIdgmothers;
  int statusgmothers;
  bool keep;
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
CustomCandidateProducer::CustomCandidateProducer(const edm::ParameterSet& iConfig):
  particles_(iConfig.getParameter<InputTag>("src") ),
  debugmode_(iConfig.getParameter<bool>("debugmode") ),
  maxInputParticles(iConfig.getParameter<int>("maxInputParticles")),
  maxOutputParticles(iConfig.getParameter<int>("maxOutputParticles")),
  vpdgId(iConfig.getParameter<vector<int> >("pdgId") ),
  status(iConfig.getParameter<int>("status") ),
  vpdgIdmothers(iConfig.getParameter<vector<int> >("mothers") ),
  statusmothers(iConfig.getParameter<int>("statusmothers") ),
  vpdgIdgmothers(iConfig.getParameter<vector<int> >("gmothers") ),
  statusgmothers(iConfig.getParameter<int>("statusgmothers") ),
  keep(iConfig.getParameter<bool>("keep") )
{
  //register your products
  produces<CandidateCollection>();

  //now do what ever other initialization is needed
}


CustomCandidateProducer::~CustomCandidateProducer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
CustomCandidateProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;

  Handle<CandidateCollection> particles;
  iEvent.getByLabel(particles_, particles);
   
  auto_ptr<CandidateCollection> outputcands( new CandidateCollection );
  outputcands->reserve(particles->size());

  int numOutputParticles = 0;

  double temp_pt = 0.;
  int temp_id = 0;
  int temp_status = 0;
  int mom_id = 0;
  int mom_status = 0;
  int gmom_id = 0;
  int gmom_status = 0;
  size_t idx = 0;
  bool found = false;

  for( CandidateCollection::const_iterator piter = particles->begin();
       piter != particles->end();
       ++piter, ++idx) {
     
    found = false;
     
    if((numOutputParticles < maxOutputParticles) && 
       (idx < maxInputParticles)) {  
      // The idea is that I will look only over the first (maxInputParticles)
      // particles in the event, and will only produce a
      // collection of up to (maxOutputParticles) particles.
       
      temp_pt = piter->pt();
      temp_id = piter->pdgId(); // Statistics of the particle.
      temp_status = piter->status();

      // Safeguards.
      if(temp_id == 0)
	throw cms::Exception("CorruptedData")
	  << "Particle id = 0 FOUND!" << endl;
       
      // Get mother particle.
      // CAVEAT: what if there is more than one mother???
      if((piter->mother()) != 0) {
	mom_id = piter->mother()->pdgId();
	mom_status = piter->mother()->status();
	if((piter->mother()->mother()) != 0) {
	  gmom_id = piter->mother()->mother()->pdgId();
	  gmom_status = piter->mother()->mother()->status();
	}
      }
      
      int goal_status = status;
      int goal_mom_status = statusmothers;
      int goal_gmom_status = statusgmothers;
      
      found =  ( statusCheck(temp_status, goal_status) &&
		 statusCheck(mom_status, goal_mom_status) &&
		 statusCheck(gmom_status, goal_gmom_status) &&
		 pdgIdCheck(temp_id, vpdgId) &&
		 pdgIdCheck(mom_id, vpdgIdmothers) &&
		 pdgIdCheck(gmom_id, vpdgIdgmothers) );
	       
      if(found)
	if(debugmode_)
	  cout << "Particle found with pdgId == " << temp_id << " , pt = "
	       << temp_pt << " and status " << temp_status << endl;
      // Ok, this is one of the particles I was searching for.
      // Actually, I should check for ALL moms/grandmoms.
       
       
      // I either keep it or not.
      if( (found && keep) || ((!found) && (!keep)) ) {
	CandidateBaseRef ref( CandidateRef( particles, idx ) );
	outputcands->push_back( new ShallowCloneCandidate( ref ) );
	numOutputParticles++;
      }
    }     
  }
   
  iEvent.put(outputcands);
}

// ------------ method called once each job just before starting event loop  ------------
void 
CustomCandidateProducer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CustomCandidateProducer::endJob() {
}

bool
CustomCandidateProducer::statusCheck(int status, int goal) {
  if (goal == 0)
    return true;
  else
    return (status == goal);
}

bool
CustomCandidateProducer::pdgIdCheck(int id, vector<int> goal) {
  if (goal.front() == 0)
    return true;
  else {
    bool result = false;
    for(size_t i = 0; i < goal.size(); ++i) {
      result = (id == goal.at(i));
      if (result)
	return result;
    }
    return result;
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE(CustomCandidateProducer);
