// -*- C++ -*-
//
// Package:    RSJetAnalyzerV2
// Class:      RSJetAnalyzerV2
// 
/**\class RSJetIdAnalyzer RSJetIdAnalyzer.cc RSGraviton/RSJetIdAnalyzer/src/RSJetIdAnalyzer.cc

Description: Class to select jets based on JetID in RS->jets events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSJetIdAnalyzer.cc,v 1.1 2011/02/09 12:31:19 tomei Exp $
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
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

//
// class decleration
//

class WeightSum : public edm::EDAnalyzer {
public:
  explicit WeightSum(const edm::ParameterSet&);
  ~WeightSum();

private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  double sumOfWeights_;
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
WeightSum::WeightSum(const edm::ParameterSet& iConfig)
{
  sumOfWeights_ = 0.0;
}


WeightSum::~WeightSum()
{
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
WeightSum::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  // weight handle
  Handle<GenEventInfoProduct> infoHandle;
  iEvent.getByLabel("generator",infoHandle);
  const GenEventInfoProduct geneventinfo = *infoHandle;
  double gen_weight=geneventinfo.weight();

  sumOfWeights_ = (sumOfWeights_ + gen_weight);
}

// ------------ method called once each job just before starting event loop  ------------
void 
WeightSum::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
WeightSum::endJob() {
  std::cout << "Sum of weights in this sample = " << sumOfWeights_ << std::endl;

}

//define this as a plug-in
DEFINE_FWK_MODULE(WeightSum);
