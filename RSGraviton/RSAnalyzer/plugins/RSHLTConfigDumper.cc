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
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

//
// class declaration
//

class RSHLTConfigDumper : public edm::EDAnalyzer {
public:
  explicit RSHLTConfigDumper(const edm::ParameterSet&);
  ~RSHLTConfigDumper();
  
private:
  virtual void beginRun(const edm::Run& , const edm::EventSetup&);
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  virtual void endRun(const edm::Run& , const edm::EventSetup&);
  std::string processName_;
  HLTConfigProvider hltConfig_;

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
RSHLTConfigDumper::RSHLTConfigDumper(const edm::ParameterSet& iConfig)
{
  processName_ = iConfig.getUntrackedParameter<std::string>("processName");
}


RSHLTConfigDumper::~RSHLTConfigDumper()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
RSHLTConfigDumper::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  hltConfig_.dump(processName_);
}

void
RSHLTConfigDumper::beginRun(edm::Run const & iRun, edm::EventSetup const& iSetup)
{
  bool changed(true);
  if (hltConfig_.init(iRun,iSetup,processName_,changed)) {
    // if init returns TRUE initialisation has succeeded!
    if (changed) {
      // The HLT config has actually changed wrt the previous Run, hence rebook your
      // histograms or do anything else dependent on the revised HLT config
      edm::LogInfo ("HLTDumper") << "Change run..."; 
    }
  } 
  else {
    // if init returns FALSE, initialisation has NOT succeeded, which indicates a problem
    // with the file and/or code and needs to be investigated!
    edm::LogError("HLTDumper") << " HLT config extraction failure with process name " << processName_;
    // In this case, all access methods will return empty values!
  }
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSHLTConfigDumper::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
RSHLTConfigDumper::endJob() {
}

void
RSHLTConfigDumper::endRun(const edm::Run& iRun, const edm::EventSetup& iESetup) {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSHLTConfigDumper);
