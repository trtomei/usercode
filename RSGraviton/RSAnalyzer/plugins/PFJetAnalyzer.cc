// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include <TH1F.h>
#include <TH2F.h>
//
// class declaration
//

class PFJetAnalyzer : public edm::EDAnalyzer {
public:
  explicit PFJetAnalyzer(const edm::ParameterSet&);
  ~PFJetAnalyzer();
  
private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  edm::InputTag src_;
  TH2F* h_jet1_EtMass;
  TH2F* h_jet2_EtMass;
  TH2F* h_bothJets_Et;
  TH2F* h_bothJets_Mass;
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
PFJetAnalyzer::PFJetAnalyzer(const edm::ParameterSet& iConfig):
  src_(iConfig.getParameter<edm::InputTag>("src"))
{
  edm::Service<TFileService> fs;

  h_jet1_EtMass = fs->make<TH2F> ("jet1_EtMass","jet1_EtMass",100,0.0,1000.0, 100,0.0,200.0);
  h_jet2_EtMass = fs->make<TH2F> ("jet2_EtMass","jet2_EtMass",100,0.0,1000.0, 100,0.0,200.0);
  h_bothJets_Et = fs->make<TH2F> ("bothjets_Et", "bothJets_Et", 100,0.0,1000.0, 100,0.0,1000.0 );
  h_bothJets_Mass = fs->make<TH2F> ("bothjets_Mass", "bothJets_Mass", 100,0.0,200.0, 100,0.0,200.0 );
  //now do what ever initialization is needed
}


PFJetAnalyzer::~PFJetAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
PFJetAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;

   // Get the hard jets collection.
   Handle<CandidateView> pHardJets;
   iEvent.getByLabel(src_,pHardJets);

   // Get a convenient handle.
   CandidateView const & hardJets = *pHardJets;

   // Single jet correlations.
   h_jet1_EtMass->Fill(hardJets[0].et(),hardJets[0].mass());
   h_jet2_EtMass->Fill(hardJets[1].et(),hardJets[1].mass());

   // Jet-jet correlations.
   h_bothJets_Et->Fill(hardJets[0].et(),hardJets[1].et());
   h_bothJets_Mass->Fill(hardJets[0].mass(),hardJets[1].mass());
}

// ------------ method called once each job just before starting event loop  ------------
void 
PFJetAnalyzer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PFJetAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE( PFJetAnalyzer );
