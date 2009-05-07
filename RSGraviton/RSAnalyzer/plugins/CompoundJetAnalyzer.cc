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
#include <TH2F.h>
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
  edm::InputTag flowSrc_;

  TH1F* h_numSubJets;

  TH1F* h_jet1_subJet1Pt;
  TH1F* h_jet1_subJet2Pt;
  TH1F* h_jet1_invMassSubJets;
  TH1F* h_jet1_flow;
  TH2F* h_jet1_EtMass;
  TH2F* h_jet1_EtFlow;
  TH2F* h_jet1_FlowMass;

  TH1F* h_jet2_subJet1Pt;
  TH1F* h_jet2_subJet2Pt;
  TH1F* h_jet2_invMassSubJets;
  TH1F* h_jet2_flow;
  TH2F* h_jet2_EtMass;
  TH2F* h_jet2_EtFlow;
  TH2F* h_jet2_FlowMass;

  TH2F* h_bothJets_Et;
  TH2F* h_bothJets_Mass;
  TH2F* h_bothJets_MassSJ;
  TH2F* h_bothJets_Flow;
      // ----------member data ---------------------------
  typedef std::vector<double> FlowValueCollection;
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
  src_(iConfig.getParameter<edm::InputTag>("src")),
  flowSrc_(iConfig.getParameter<edm::InputTag>("flowSrc"))
{
  edm::Service<TFileService> fs;

  h_numSubJets = fs->make<TH1F> ("numSubJets","numSubJets",10,-0.5,9.5);

  h_jet1_subJet1Pt = fs->make<TH1F> ("jet1_subJet1Pt","jet1_subJet1Pt",100,0.0,1000.0);
  h_jet1_subJet2Pt = fs->make<TH1F> ("jet1_subJet2Pt","jet1_subJet2Pt",100,0.0,1000.0);
  h_jet1_invMassSubJets = fs->make<TH1F> ("jet1_invMassSubJets","jet1_invMassSubJets",100,0.0,200.0);
  h_jet1_flow = fs->make<TH1F> ("jet1_flow","jet1_flow",100,0.0,1.0);
  h_jet1_EtMass = fs->make<TH2F> ("jet1_EtMass","jet1_EtMass",100,0.0,1000.0, 100,0.0,200.0);
  h_jet1_EtFlow = fs->make<TH2F> ("jet1_EtFlow","jet1_EtFlow",100,0.0,1000.0, 100,0.0,1.0);
  h_jet1_FlowMass = fs->make<TH2F> ("jet1_FlowMass","jet1_FlowMass",100,0.0,1.0, 100,0.0,200.0);

  h_jet2_subJet1Pt = fs->make<TH1F> ("jet2_subJet1Pt","jet2_subJet1Pt",100,0.0,1000.0);
  h_jet2_subJet2Pt = fs->make<TH1F> ("jet2_subJet2Pt","jet2_subJet2Pt",100,0.0,1000.0);
  h_jet2_invMassSubJets = fs->make<TH1F> ("jet2_invMassSubJets","jet2_invMassSubJets",100,0.0,200.0);
  h_jet2_flow = fs->make<TH1F> ("jet2_flow","jet2_flow",100,0.0,1.0);
  h_jet2_EtMass = fs->make<TH2F> ("jet2_EtMass","jet2_EtMass",100,0.0,1000.0, 100,0.0,200.0);
  h_jet2_EtFlow = fs->make<TH2F> ("jet2_EtFlow","jet2_EtFlow",100,0.0,1000.0, 100,0.0,1.0);
  h_jet2_FlowMass = fs->make<TH2F> ("jet2_FlowMass","jet2_FlowMass",100,0.0,1.0, 100,0.0,200.0);

  h_bothJets_Et = fs->make<TH2F> ("bothjets_Et", "bothJets_Et", 100,0.0,1000.0, 100,0.0,1000.0 );
  h_bothJets_Mass = fs->make<TH2F> ("bothjets_Mass", "bothJets_Mass", 100,0.0,200.0, 100,0.0,200.0 );
  h_bothJets_MassSJ = fs->make<TH2F> ("bothjets_MassSJ", "bothJets_MassSJ", 100,0.0,200.0, 100,0.0,200.0 );
  h_bothJets_Flow = fs->make<TH2F> ("bothjets_Flow", "bothJets_Flow", 100,0.0,1.0, 100,0.0,1.0 );

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

   // Get the associated flows.
   Handle<FlowValueCollection> pFlows;
   iEvent.getByLabel(flowSrc_, pFlows);

   // Get a convenient handle.
   View<Jet> const & hardJets = *pBasicJets;

   // Utility
   AddFourMomenta addFourMomenta;

   // To be used later.
   double invMassSJ1, invMassSJ2;

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
       if(iihardJet==0) {
	 h_jet1_subJet1Pt->Fill(firstSubjet->pt());
	 h_jet1_subJet2Pt->Fill(secondSubjet->pt());
	 CompositeCandidate bosonCand("bosonCand");
	 bosonCand.addDaughter( *firstSubjet, "firstSubjet" );
	 bosonCand.addDaughter( *secondSubjet, "secondSubjet" );
	 addFourMomenta.set(bosonCand);
	 double invMass = bosonCand.mass();
	 h_jet1_invMassSubJets->Fill(invMass);
	 invMassSJ1 = invMass;
       }
       if(iihardJet==1) {
  	 h_jet2_subJet1Pt->Fill(firstSubjet->pt());
	 h_jet2_subJet2Pt->Fill(secondSubjet->pt());
	 CompositeCandidate bosonCand("bosonCand");
	 bosonCand.addDaughter( *firstSubjet, "firstSubjet" );
	 bosonCand.addDaughter( *secondSubjet, "secondSubjet" );
	 addFourMomenta.set(bosonCand);
	 double invMass = bosonCand.mass();
	 h_jet2_invMassSubJets->Fill(invMass);
	 invMassSJ2 = invMass;
       }
     }

     // Intrajet correlations.
     if(iihardJet==0) {
       h_jet1_flow->Fill((*pFlows)[0]);
       h_jet1_EtMass->Fill(ihardJet->et(),ihardJet->mass());
       h_jet1_EtFlow->Fill(ihardJet->et(),(*pFlows)[0]);
       h_jet1_FlowMass->Fill((*pFlows)[0],ihardJet->et());
     }
     if(iihardJet==1) {
       h_jet2_flow->Fill((*pFlows)[1]);
       h_jet2_EtMass->Fill(ihardJet->et(),ihardJet->mass());
       h_jet2_EtFlow->Fill(ihardJet->et(),(*pFlows)[1]);
       h_jet2_FlowMass->Fill((*pFlows)[1],ihardJet->et());
     }

   } // Closes loop over hard jets

   // Jet-jet correlations.
   h_bothJets_Et->Fill(hardJets[0].et(),hardJets[1].et());
   h_bothJets_Mass->Fill(hardJets[0].mass(),hardJets[1].mass());
   h_bothJets_MassSJ->Fill(invMassSJ1,invMassSJ2);
   h_bothJets_Flow->Fill((*pFlows)[0],(*pFlows)[1]);
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
