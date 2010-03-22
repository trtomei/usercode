// -*- C++ -*-
//
// Package:    HcalNoiseFilter
// Class:      HcalNoiseFilter
// 
/**\class HcalNoiseFilter HcalNoiseFilter.cc SomeDir/HcalNoiseFilter/src/HcalNoiseFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Thiago Tomei
//         Created:  Wed Feb 24 18:19:14 BRT 2010
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/METReco/interface/HcalNoiseSummary.h"
#include "FWCore/Utilities/interface/Exception.h"

//
// class declaration
//

class HcalNoiseFilter : public edm::EDFilter {
   public:
      explicit HcalNoiseFilter(const edm::ParameterSet&);
      ~HcalNoiseFilter();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
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
HcalNoiseFilter::HcalNoiseFilter(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed

}


HcalNoiseFilter::~HcalNoiseFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
HcalNoiseFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  // get the Noise summary object
  edm::Handle<HcalNoiseSummary> summary_h;
  iEvent.getByType(summary_h);
  if(!summary_h.isValid()) {
    throw edm::Exception(edm::errors::ProductNotFound) << " could not find HcalNoiseSummary.\n";
    return false;
  }
  
  const HcalNoiseSummary summary = *summary_h;
  
  //  bool passLoose = summary.passLooseNoiseFilter();
  bool passTight = summary.passTightNoiseFilter();
  return passTight;
}

// ------------ method called once each job just before starting event loop  ------------
void 
HcalNoiseFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
HcalNoiseFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(HcalNoiseFilter);
