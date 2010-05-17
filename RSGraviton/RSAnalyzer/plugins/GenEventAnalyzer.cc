// system include files
#include <memory>
#include <string>
#include <iostream>
#include <fstream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "CommonTools/UtilAlgos/interface/ExpressionHisto.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

//
// class declaration
//

class GenEventAnalyzer : public edm::EDAnalyzer {
public:
  explicit GenEventAnalyzer(const edm::ParameterSet&);
  ~GenEventAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
      // ----------member data ---------------------------
  typedef ExpressionHisto<GenEventInfoProduct> GenEventHisto;
  GenEventHisto histo;
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
GenEventAnalyzer::GenEventAnalyzer(const edm::ParameterSet& iConfig):
  histo(iConfig)
{
  edm::Service<TFileService> fs;
  histo.initialize( fs );
}


GenEventAnalyzer::~GenEventAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
GenEventAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // Get the GenEventInfoProduct
  edm::Handle<GenEventInfoProduct> genEventInfoProduct_h;
  iEvent.getByLabel("generator", genEventInfoProduct_h );
  const GenEventInfoProduct gEIP (*genEventInfoProduct_h);
  histo.fill(gEIP);

}

// ------------ method called once each job just before starting event loop  ------------
void 
GenEventAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
GenEventAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenEventAnalyzer);
