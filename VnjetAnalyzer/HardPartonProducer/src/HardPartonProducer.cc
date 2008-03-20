// -*- C++ -*-
//
// Package:    HardPartonProducer
// Class:      HardPartonProducer
// 
/**\class HardPartonProducer HardPartonProducer.cc VnjetAnalyzer/HardPartonProducer/src/HardPartonProducer.cc

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
//#include <cstddef>
//#include <algorithm>
//#include <iostream>
//#include <sstream>
//#include <string>

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

class HardPartonProducer : public edm::EDProducer {
   public:
      explicit HardPartonProducer(const edm::ParameterSet&);
      ~HardPartonProducer();

   private:
      virtual void beginJob(const edm::EventSetup&) ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------

  InputTag particles_;
  bool debugmode_;
};

//
// constants, enums and typedefs
//
const int maxhardpartons = 5;
const int maxparticles = 15;

//
// static data member definitions
//

//
// constructors and destructor
//
HardPartonProducer::HardPartonProducer(const edm::ParameterSet& iConfig):
  particles_(iConfig.getParameter<InputTag>("src") ),
  debugmode_(iConfig.getParameter<bool>("debugmode") )
{
   //register your products
  produces<CandidateCollection>();

  //now do what ever other initialization is needed
}


HardPartonProducer::~HardPartonProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
HardPartonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;

   Handle<CandidateCollection> particles;
   iEvent.getByLabel(particles_, particles);
   
   auto_ptr<CandidateCollection> outputcands( new CandidateCollection );
   outputcands->reserve(particles->size());

   int numhardpartons = 0;

   double temp_pt = 0.;
   int temp_id = 0;
   int temp_status =0;

   int mom_id = 0;
   int grandmom_id = 0;
   const int hard = 3;
   const int protonid = 2212;
   
   size_t idx = 0;

   if(debugmode_)
     cout << "--- BEGIN Hard Parton Listing ---" << endl;

   for( CandidateCollection::const_iterator piter = particles->begin();
	piter != particles->end();
	++piter, ++idx) {
     
     if(debugmode_)
       cout << "In the for loop..." << endl;
     
     if((numhardpartons < maxhardpartons) && (idx < maxparticles)) {  
       // This if is a hack - should look into this later.
       temp_pt = piter->pt();
       temp_id = piter->pdgId(); // Statistics of the particle.
       temp_status = piter->status();
       if(debugmode_) {
	 cout << "Got particle statistics:" << endl;
	 cout << "pt = " << temp_pt << " id = " << temp_id <<  " status = "
	      << temp_status << endl;
       }

       if(temp_id == 0)
	 throw cms::Exception("CorruptedData")
	   << "Particle id = 0 FOUND!" << endl;
       // This is one of the ALIEN events!
       
       if(piter->mother() == 0) {
	 throw cms::Exception("CorruptedData")
	   << "Invalid reference to particle found." << endl;
       }
       mom_id = piter->mother()->pdgId();
       if(mom_id == 0)
	 throw cms::Exception("CorruptedData")
	   << "Particle id = 0 FOUND!" << endl;
       if(debugmode_)
	 cout << "Got mother: id = " << mom_id << endl;
       
       if(piter->mother()->mother() == 0) {
	 throw cms::Exception("CorruptedData")
	   << "Invalid reference to particle found." << endl;
       }
       grandmom_id = piter->mother()->mother()->pdgId();
       if(grandmom_id == 0)
	 throw cms::Exception("CorruptedData")
	   << "Particle id = 0 FOUND!" << endl;
       if(debugmode_)
	 cout << "Got grandmother: id = " << grandmom_id << endl;
       
       if(temp_status == hard)
	 if( (mom_id != protonid) && (grandmom_id != protonid) ) {
	   // Ok, it is one of the hard partons.
	   // Actually, I should check for ALL moms/grandmoms.
	   if(debugmode_)
	     cout << "Hard parton found with pdgId == " << temp_id << " , pt = " 		  << temp_pt << " and status " << temp_status << endl;
	   
	   CandidateBaseRef ref( CandidateRef( particles, idx ) );
	   outputcands->push_back( new ShallowCloneCandidate( ref ) );
	   numhardpartons++;
	 }
     }
   }
   
   if(debugmode_)
     cout << "--- END Hard Parton Listing ---" << endl;
   
   iEvent.put(outputcands);
}

// ------------ method called once each job just before starting event loop  ------------
void 
HardPartonProducer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
HardPartonProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(HardPartonProducer);
