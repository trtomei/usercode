// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"

class RSEventNumJetsFilter : public edm::EDFilter {
public:
  explicit RSEventNumJetsFilter(const edm::ParameterSet&);
  ~RSEventNumJetsFilter();
  
private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
      // ----------Member data ---------------------------
  edm::InputTag jets_;
  int maxJets_;
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
RSEventNumJetsFilter::RSEventNumJetsFilter(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets")),
  maxJets_(iConfig.getParameter<int>("maxJets"))
{
   //now do what ever initialization is needed

}


RSEventNumJetsFilter::~RSEventNumJetsFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
RSEventNumJetsFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  
  Handle<View<Candidate> > jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);

  bool accepted = false;

  // We accept the event if there is exactly one jet.
  int numJets = int(jetsHandle->size());

  if(numJets < maxJets_)
    accepted = true;
    
  return accepted;
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSEventNumJetsFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSEventNumJetsFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSEventNumJetsFilter);
