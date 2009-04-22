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
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "PhysicsTools/CandUtils/interface/AddFourMomenta.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include <TH1F.h>
//
// class declaration
//

class CompoundJetAnalyzer : public edm::EDAnalyzer {
public:
  explicit CompoundJetAnalyzer(const edm::ParameterSet&);
  ~CompoundJetAnalyzer();
  
private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  edm::InputTag src_;

  TH1F* h_numSubJets;
  TH1F* h_subJet1Pt;
  TH1F* h_subJet2Pt;
  TH1F* h_invMassSubJets;
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
CompoundJetAnalyzer::CompoundJetAnalyzer(const edm::ParameterSet& iConfig):
  src_(iConfig.getParameter<edm::InputTag>("src"))
{
  edm::Service<TFileService> fs;
  h_numSubJets = fs->make<TH1F> ("numSubJets","numSubJets",10,-0.5,9.5);
  h_subJet1Pt  = fs->make<TH1F> ("subJet1Pt","subJet1Pt",500,0.0,1000.0);
  h_subJet2Pt  = fs->make<TH1F> ("subJet2Pt","subJet2Pt",500,0.0,1000.0);
  h_invMassSubJets = fs->make<TH1F> ("invMassSubJets","invMassSubJets",100,0.0,200.0);

  //now do what ever initialization is needed
}


CompoundJetAnalyzer::~CompoundJetAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
CompoundJetAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;

   // Get the hard jets collection.
   Handle<View<Jet> > pBasicJets;
   iEvent.getByLabel(src_, pBasicJets);

   // Get a convenient handle.
   View<Jet> const & hardJets = *pBasicJets;

   // Utility
   AddFourMomenta addFourMomenta;

   // Now loop over the hard jets and do the plots.
   View<Jet>::const_iterator ihardJet = hardJets.begin(),
     ihardJetEnd = hardJets.end();
   size_t iihardJet = 0;
   for ( ; ihardJet != ihardJetEnd; ++ihardJet, ++iihardJet ) {

     // Get subjets
     Jet::Constituents subjets = ihardJet->getJetConstituents();
     h_numSubJets->Fill(subjets.size());
     
     // Assuming the ideal situation where we have two subjets:
     if(subjets.size() == 2) {
       Jet::Constituent firstSubjet = subjets[0];
       Jet::Constituent secondSubjet = subjets[1];
       h_subJet1Pt->Fill(firstSubjet->pt());
       h_subJet2Pt->Fill(secondSubjet->pt());

       CompositeCandidate bosonCand("bosonCand");
       bosonCand.addDaughter( *firstSubjet, "firstSubjet" );
       bosonCand.addDaughter( *secondSubjet, "secondSubjet" );
       addFourMomenta.set(bosonCand);
       double invMass = bosonCand.mass();
       h_invMassSubJets->Fill(invMass);
     }
   }

}

// ------------ method called once each job just before starting event loop  ------------
void 
CompoundJetAnalyzer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CompoundJetAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE( CompoundJetAnalyzer );
