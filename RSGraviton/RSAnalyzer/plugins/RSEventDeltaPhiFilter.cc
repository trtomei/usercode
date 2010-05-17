// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/Math/interface/deltaPhi.h"

class RSEventDeltaPhiFilter : public edm::EDFilter {
public:
  explicit RSEventDeltaPhiFilter(const edm::ParameterSet&);
  ~RSEventDeltaPhiFilter();
  
private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
      // ----------Member data ---------------------------
  edm::InputTag jets_;
  double maxDeltaPhi_;
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
RSEventDeltaPhiFilter::RSEventDeltaPhiFilter(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets")),
  maxDeltaPhi_(iConfig.getParameter<double>("maxDeltaPhi"))
{
   //now do what ever initialization is needed

}


RSEventDeltaPhiFilter::~RSEventDeltaPhiFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
RSEventDeltaPhiFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  
  Handle<CaloJetCollection> jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);

  bool accepted = false;

  // We accept the event if there is exactly one jet.
  if(jetsHandle->size() == 1)
    accepted = true;

  // If there are two jets, we check the deltaPhi in between them.
  if(jetsHandle->size() == 2) {
    double phiJet1 = ((*jetsHandle)[0]).phi();
    double phiJet2 = ((*jetsHandle)[1]).phi();
    double diffPhi = std::abs(deltaPhi(phiJet1,phiJet2));
    if(diffPhi < maxDeltaPhi_)
      accepted = true;
  }
  
  return accepted;
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSEventDeltaPhiFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSEventDeltaPhiFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSEventDeltaPhiFilter);
