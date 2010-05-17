// -*- C++ -*-
//
// Package:    EventCounter
// Class:      EventCounter
// 
/**\class EventCounter EventCounter.cc VnjetAnalyzer/EventCounter/src/EventCounter.cc

Description: Counts events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Mar 19 16:47:30 CET 2008
// $Id: EventCounter.cc,v 1.1 2010/03/22 16:39:33 tomei Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
//
// class decleration
//

class EventCounter : public edm::EDAnalyzer {
public:
  explicit EventCounter(const edm::ParameterSet&);
  ~EventCounter();


private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  TH1F* H_eventcounter;
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
EventCounter::EventCounter(const edm::ParameterSet& iConfig)

{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  H_eventcounter = fs->make<TH1F>("eventcounter", "eventcounter", 1, -0.5, 0.5); 
}


EventCounter::~EventCounter()
{
} 


//
// member functions
//

// ------------ method called to for each event  ------------
void
EventCounter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  H_eventcounter->Fill(0.);
}


// ------------ method called once each job just before starting event loop  ------------
void 
EventCounter::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
EventCounter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(EventCounter);
