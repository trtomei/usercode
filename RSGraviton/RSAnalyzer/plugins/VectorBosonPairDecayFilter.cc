// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "FWCore/Utilities/interface/Exception.h"

//
// class declaration
//

class VectorBosonPairDecayFilter : public edm::EDFilter {
public:
  explicit VectorBosonPairDecayFilter(const edm::ParameterSet&);
  ~VectorBosonPairDecayFilter();
  
private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  bool isNeutrino(const HepMC::GenParticle*);
  bool isQuark(const HepMC::GenParticle*);
  bool isElectron(const HepMC::GenParticle*);
  bool isMuon(const HepMC::GenParticle*);
  bool isTau(const HepMC::GenParticle*);

      // ----------Member data ---------------------------
  bool verbose_;
  bool wantNeutrinos_;
  bool wantQuarks_;
  bool wantElectrons_;
  bool wantMuons_;
  bool wantTaus_;
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
VectorBosonPairDecayFilter::VectorBosonPairDecayFilter(const edm::ParameterSet& iConfig) :
  verbose_(iConfig.getParameter<bool>("verbose")),
  wantNeutrinos_(iConfig.getParameter<bool>("wantNeutrinos")),
  wantQuarks_(iConfig.getParameter<bool>("wantQuarks")),
  wantElectrons_(iConfig.getParameter<bool>("wantElectrons")),
  wantMuons_(iConfig.getParameter<bool>("wantMuons")),
  wantTaus_(iConfig.getParameter<bool>("wantTaus"))
{
   //now do what ever initialization is needed

}


VectorBosonPairDecayFilter::~VectorBosonPairDecayFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
VectorBosonPairDecayFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  // Get the HepMC event.
  edm::Handle<edm::HepMCProduct> evt;
  iEvent.getByLabel("generator", evt);
  
  bool accepted = false;
  bool DecayToNeutrinos = false;
  bool DecayToQuarks = false;
  bool DecayToElectrons = false;
  bool DecayToMuons = false;
  bool DecayToTaus = false;

  HepMC::GenEvent* myGenEvent = new HepMC::GenEvent(*(evt->GetEvent()));
    
  for ( HepMC::GenEvent::particle_iterator piter = myGenEvent->particles_begin();
	piter != myGenEvent->particles_end(); ++piter ) {

    // Check for vector bosons.
    const HepMC::GenParticle* p =  *piter;
    if(verbose_) p->print();
    int ppdgid = std::abs(p->pdg_id());
    if(ppdgid!=23 && ppdgid!=24) continue; // If it is not Z or W, go to the next particle.
    
    // Ok, it is either Z or W.
    // Get the decay vertex.
    HepMC::GenVertex* DecayVertex = p->end_vertex();
    if(DecayVertex == 0) continue; // Ooops, it was one of the documentation particles that have no decay vertex. Go to the next one!

    for (HepMC::GenVertex::particle_iterator d = DecayVertex->particles_begin(HepMC::children);
	 d != DecayVertex->particles_end(HepMC::children); d++) {
      const HepMC::GenParticle* theDaughter = *d;

      // Check the nature of this daughter.

      if(isQuark(theDaughter)) {DecayToQuarks=true;}
      if(isNeutrino(theDaughter)) {DecayToNeutrinos=true;}
      if(isElectron(theDaughter)) {DecayToElectrons=true;}
      if(isMuon(theDaughter)) {DecayToMuons=true;}
      if(isTau(theDaughter)) {DecayToTaus=true;}
    }
  }
  
  // Check if the event is accepted. Essentially, everything that was asked must be found.
  bool accepted1 = (wantNeutrinos_ && DecayToNeutrinos) || !wantNeutrinos_;
  bool accepted2 = (wantQuarks_ && DecayToQuarks)    || !wantQuarks_;
  bool accepted3 = (wantElectrons_ && DecayToElectrons) || !wantElectrons_;
  bool accepted4 = (wantMuons_ && DecayToMuons) || !wantMuons_;
  bool accepted5 = (wantTaus_ && DecayToTaus) || !wantTaus_;
  accepted = accepted1 &&
    accepted2 &&
    accepted3 && 
    accepted4 && 
    accepted5;

  if(accepted) 
    if(verbose_)
      std::cout << "ACCEPTED" << std::endl;

  // Because I got a clone of the event.
  delete myGenEvent;
  
  return accepted;
}

// ------------ method called once each job just before starting event loop  ------------
void 
VectorBosonPairDecayFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
VectorBosonPairDecayFilter::endJob() {
}

bool
VectorBosonPairDecayFilter::isQuark(const HepMC::GenParticle* p) {
  bool result;
  int pdgid = std::abs(p->pdg_id());
  if(pdgid == 1 || pdgid == 2 || pdgid == 3 ||
     pdgid == 4 || pdgid == 5 || pdgid == 6) 
    result = true;
  else 
    result = false;
  return result;
}

bool
VectorBosonPairDecayFilter::isNeutrino(const HepMC::GenParticle* p) {
  bool result;
  int pdgid = std::abs(p->pdg_id());
  if(pdgid == 12 || pdgid == 14 || pdgid == 16)
    result = true;
  else 
    result = false;
  return result;
}

bool
VectorBosonPairDecayFilter::isElectron(const HepMC::GenParticle* p) {
  bool result;
  int pdgid = std::abs(p->pdg_id());
  if(pdgid == 11)
    result = true;
  else 
    result = false;
  return result;
}

bool
VectorBosonPairDecayFilter::isMuon(const HepMC::GenParticle* p) {
  bool result;
  int pdgid = std::abs(p->pdg_id());
  if(pdgid == 13)
    result = true;
  else 
    result = false;
  return result;
}

bool
VectorBosonPairDecayFilter::isTau(const HepMC::GenParticle* p) {
  bool result;
  int pdgid = std::abs(p->pdg_id());
  if(pdgid == 15)
    result = true;
  else 
    result = false;
  return result;
}

//define this as a plug-in
DEFINE_FWK_MODULE(VectorBosonPairDecayFilter);
