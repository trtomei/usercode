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

class RSEventDeltaPhiAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSEventDeltaPhiAnalyzer(const edm::ParameterSet&);
  ~RSEventDeltaPhiAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
      // ----------Member data ---------------------------
  edm::InputTag jets_;
  TH1F* h_deltaPhi;
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
RSEventDeltaPhiAnalyzer::RSEventDeltaPhiAnalyzer(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets"))
{
  edm::Service<TFileService> fs;
  h_deltaPhi = fs->make<TH1F>("h_deltaPhi","h_deltaPhi",72,0.0,M_PI);

}


RSEventDeltaPhiAnalyzer::~RSEventDeltaPhiAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
RSEventDeltaPhiAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  
  Handle<View<Candidate> > jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);

  bool accepted = false;

  // We plot the deltaPhi between the two leading jets. We assume those jets are already sorted...
  if(jetsHandle->size() > 1) {
    double phiJet1 = ((*jetsHandle)[0]).phi();
    double phiJet2 = ((*jetsHandle)[1]).phi();
    double diffPhi = deltaPhi(phiJet1,phiJet2);
    h_deltaPhi->Fill(diffPhi);
  }
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSEventDeltaPhiAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSEventDeltaPhiAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSEventDeltaPhiAnalyzer);
