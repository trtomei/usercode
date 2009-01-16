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
// $Id: RSAnalyzer.cc,v 1.3 2008/05/02 10:57:48 tomei Exp $
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
#include "Flow.hh"
#include "PhysicsTools/Utilities/interface/Parameter.h"
#include "PhysicsTools/Utilities/interface/RootMinuit.h"

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
  using namespace math;
  XYZVector v(1,2,3);

  XYZVector v1(8,12,9);
  XYZVector v2(2,-4,7);
  std::vector<XYZVector> vc;
  vc.push_back(v1);
  vc.push_back(v2);

  funct::Parameter phi("Phi",0.7);

  Flow f(v,vc,phi);
  //  for (int i=0; i!=31; ++i) {
  //    phi = double(0.1*i);
  //    std::cout << "Flow of " << double(0.1*i) << " = " << f() << std::endl;
  //  }
  
  phi = 0.7;
  fit::RootMinuit<Flow> minuit(f, false);
  minuit.addParameter(phi, 0.1, 0.0, 1.57);
  minuit.minimize();
  minuit.migrad();
  std::cout << "Min value is " << minuit.minValue() << std::endl;
  minuit.printParameters();
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSAnalyzer::beginJob(const edm::EventSetup&)
{
  
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSAnalyzer::endJob() {

}

//define this as a plug-in
DEFINE_FWK_MODULE(RSAnalyzer);
