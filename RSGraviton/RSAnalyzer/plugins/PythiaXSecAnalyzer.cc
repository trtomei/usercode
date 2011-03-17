// system include files
#include <memory>
#include <string>
#include <iostream>
#include <fstream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

//
// class declaration
//

class PythiaXSecAnalyzer : public edm::EDAnalyzer {
public:
  explicit PythiaXSecAnalyzer(const edm::ParameterSet&);
  ~PythiaXSecAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  virtual void endRun(const edm::Run& , const edm::EventSetup&);
  std::string outFileName_;
  double massParameter_;
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
PythiaXSecAnalyzer::PythiaXSecAnalyzer(const edm::ParameterSet& iConfig)
{
  outFileName_ = iConfig.getParameter<std::string>("outFileName");
  massParameter_ = iConfig.getParameter<double>("massParameter");
}


PythiaXSecAnalyzer::~PythiaXSecAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
PythiaXSecAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
}

// ------------ method called once each job just before starting event loop  ------------
void 
PythiaXSecAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
PythiaXSecAnalyzer::endJob() {
}

void
PythiaXSecAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup& iESetup) {
  edm::Handle<GenRunInfoProduct> handleRunInfo;
  iRun.getByLabel("generator",handleRunInfo);
  //  edm::Handle<LHERunInfoProduct> handleLHE;
  //  iRun.getByLabel("source",handleLHE);

  GenRunInfoProduct::XSec crossSection = handleRunInfo->internalXSec();
  GenRunInfoProduct::XSec extCrossSection = handleRunInfo->externalXSecNLO();
  double xSecValue = 0.0;
  double extXSecValue = 0.0;
  if(crossSection.isSet()) xSecValue = crossSection.value();
  if(extCrossSection.isSet()) extXSecValue = extCrossSection.value();
  double xSecError = 0.0;
  if(crossSection.hasError()) xSecError = crossSection.error();
  
  std::ofstream myfile;
  myfile.open (outFileName_.c_str());
  myfile << massParameter_ << "\t" << xSecValue << std::endl;
  //  std::cout << "Found " << handleLHE->headers_size() << " headers." << std::endl;

  //  std::vector<LHERunInfoProduct::Header>::const_iterator header = handleLHE->headers_begin();
  //  header++; 

  //  for(LHERunInfoProduct::Header::const_iterator i = header->begin(); i != header->end(); ++i) {
  //    myfile << *i;
  //  }
  myfile.close();
}
//define this as a plug-in
DEFINE_FWK_MODULE(PythiaXSecAnalyzer);
