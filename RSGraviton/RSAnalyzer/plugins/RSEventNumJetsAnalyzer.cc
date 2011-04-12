// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"

class RSEventNumJetsAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSEventNumJetsAnalyzer(const edm::ParameterSet&);
  ~RSEventNumJetsAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
      // ----------Member data ---------------------------
  edm::InputTag jets_;
  TH1F* h_numJets;
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
RSEventNumJetsAnalyzer::RSEventNumJetsAnalyzer(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets"))
{
  edm::Service<TFileService> fs;
  h_numJets = fs->make<TH1F>("h_numJets","h_numJets",10,-0.5,9.5);

}


RSEventNumJetsAnalyzer::~RSEventNumJetsAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
RSEventNumJetsAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  
  Handle<View<Candidate> > jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);

  bool accepted = false;

  // We plot the number of jets
  int nJets = jetsHandle->size();    
  h_numJets->Fill(nJets);
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSEventNumJetsAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSEventNumJetsAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSEventNumJetsAnalyzer);
