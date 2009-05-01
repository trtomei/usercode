// -*- C++ -*-
//
// Package:    RSAnalyzer
// Class:      RSAnalyzer
// 
/**\class RSAnalyzer RSAnalyzer.cc RSGraviton/RSAnalyzer/src/RSAnalyzer.cc

Description: Thiago's class for analyzing G*->ZZ->2j + nunu and
                                          G*->ZZ->4j events. 

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Feb 13 15:08:56 CET 2008
// $Id: RSAnalyzer.cc,v 1.4 2009/01/16 12:16:31 tomei Exp $
//
//


// system include files
#include <memory>
#include <utility>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

//
// class declaration
//

class RSAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSAnalyzer(const edm::ParameterSet&);
  ~RSAnalyzer();
  
private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
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
RSAnalyzer::RSAnalyzer(const edm::ParameterSet& iConfig)
{
}


RSAnalyzer::~RSAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
}

// ------------ method called once each job just after ending the event loop  ------------                                                                                       
void
RSAnalyzer::beginJob(const edm::EventSetup& iSetup) {

}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSAnalyzer::endJob() {

}

//define this as a plug-in
DEFINE_FWK_MODULE(RSAnalyzer);
