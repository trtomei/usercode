// -*- C++ -*-
//
// Package:    WeightGetter
// Class:      WeightGetter
// 
/**\class WeightGetter WeightGetter.cc RSGraviton/WeightGetter/src/WeightGetter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Thiago Tomei
//         Created:  Thu Mar  4 16:26:36 BRT 2010
// $Id: WeightGetter.cc,v 1.1 2011/05/23 09:40:16 tomei Exp $
//
//


// system include files
#include <memory>
#include <vector>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
//
// class declaration
//

class WeightGetter : public edm::EDProducer {
   public:
      explicit WeightGetter(const edm::ParameterSet&);
      ~WeightGetter();

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
  std::string src_;
  std::string instance_;
  edm::InputTag theInputTag; /// HAS TO BE AFTER src_, instance_ ... stupid C++
  unsigned int numberInVector_;
  bool verbose_;
  bool dummy_;
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
WeightGetter::WeightGetter(const edm::ParameterSet& iConfig) :
  src_(iConfig.getParameter<std::string>("src")),
  instance_(iConfig.getParameter<std::string>("instance")),
  theInputTag(src_,instance_),
  numberInVector_(iConfig.getParameter<unsigned int>("numberInVector")),
  verbose_(iConfig.getParameter<bool>("verbose")),
  dummy_(iConfig.getParameter<bool>("dummy"))
{
  produces<double>();
}


WeightGetter::~WeightGetter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
WeightGetter::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  edm::Handle<std::vector<double> > weightsHandle;

  if(!dummy_)
    iEvent.getByLabel(theInputTag,weightsHandle);

  std::auto_ptr<double>pWeight(new double);

  if(dummy_) {
    *pWeight = 1;
    iEvent.put(pWeight);
    return;
  }    
    
  if(verbose_)
    printf("Ready to get the weight\n");
  
  size_t vectorSize = weightsHandle->size();
  if(vectorSize==0) {
    printf("Ooops... no weights\n");
    *pWeight = 0;
    iEvent.put(pWeight);
    return;
  }

  if(verbose_)
    printf("Got the weight vector\n");

  double weight = weightsHandle->at(numberInVector_);
  *pWeight = weight; 

  if(verbose_)
    printf("Got the weight\n");
  
  iEvent.put(pWeight);

  if(verbose_)
    printf("Weight is %g\n",weight);
}

// ------------ method called once each job just before starting event loop  ------------
void 
WeightGetter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
WeightGetter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(WeightGetter);
