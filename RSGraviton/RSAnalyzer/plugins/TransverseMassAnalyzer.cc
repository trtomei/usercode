// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include <TH1F.h>
//
// class declaration
//

class TransverseMassAnalyzer : public edm::EDAnalyzer {
public:
  explicit TransverseMassAnalyzer(const edm::ParameterSet&);
  ~TransverseMassAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  edm::InputTag objectOne_;
  edm::InputTag objectTwo_;
  double xmax_;
  double xmin_;
  int nbins_;
  TH1F* h_transverseMass;
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
TransverseMassAnalyzer::TransverseMassAnalyzer(const edm::ParameterSet& iConfig):
  objectOne_(iConfig.getParameter<edm::InputTag>("objectOne")),
  objectTwo_(iConfig.getParameter<edm::InputTag>("objectTwo")),
  xmax_(iConfig.getParameter<double>("xmax")),
  xmin_(iConfig.getParameter<double>("xmin")),
  nbins_(iConfig.getParameter<int>("nbins"))
{
  edm::Service<TFileService> fs;

  h_transverseMass = fs->make<TH1F> ("transverseMass","transverseMass",nbins_,xmin_,xmax_);
  //now do what ever initialization is needed
}


TransverseMassAnalyzer::~TransverseMassAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
TransverseMassAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;
   
   // Get the objects
   Handle<View<Candidate> > objectOne;
   iEvent.getByLabel(objectOne_, objectOne);
   Handle<View<Candidate> > objectTwo;
   iEvent.getByLabel(objectTwo_, objectTwo);
   
   // Get the needed quantities
   if(objectOne->size() > 0 && objectTwo->size() > 0) {
     double pta = objectOne.product()->at(0).pt();
     double ptb = objectTwo.product()->at(0).pt();
     double phia = objectOne.product()->at(0).phi();
     double phib  = objectTwo.product()->at(0).phi();
     double dphi = deltaPhi(phia,phib);
     double transverseMass = sqrt(2*pta*ptb*(1.0-cos(dphi)));
     
     h_transverseMass->Fill(transverseMass);
   }
}
// ------------ method called once each job just before starting event loop  ------------
void 
TransverseMassAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TransverseMassAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE( TransverseMassAnalyzer );
