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

class WWDecayFilter : public edm::EDFilter {
public:
  explicit WWDecayFilter(const edm::ParameterSet&);
  ~WWDecayFilter();
  
private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  bool isNeutrino(const HepMC::GenParticle*);
  bool isQuark(const HepMC::GenParticle*);
  
      // ----------Member data ---------------------------
  bool verbose_;
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
WWDecayFilter::WWDecayFilter(const edm::ParameterSet& iConfig) :
  verbose_(iConfig.getParameter<bool>("verbose"))
{
   //now do what ever initialization is needed

}


WWDecayFilter::~WWDecayFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
WWDecayFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  // Get the HepMC event.
  edm::Handle<edm::HepMCProduct> evt;
  iEvent.getByLabel("generator", evt);
  
  bool accepted = false;
  bool WDecayToNeutrinos = false;
  bool WDecayToQuarks = false;
  HepMC::GenEvent* myGenEvent = new HepMC::GenEvent(*(evt->GetEvent()));
    
  for ( HepMC::GenEvent::particle_iterator piter = myGenEvent->particles_begin();
	piter != myGenEvent->particles_end(); ++piter ) {
    // Check for Z bosons.
    const HepMC::GenParticle* p =  *piter;
    if(verbose_) p->print();
    if(std::abs(p->pdg_id()) != 24) continue;
    
    // Get the decay vertex.
    HepMC::GenVertex* WDecayVertex = p->end_vertex();
    if(WDecayVertex == 0) continue;

    for (HepMC::GenVertex::particle_iterator d = WDecayVertex->particles_begin(HepMC::children);
	 d != WDecayVertex->particles_end(HepMC::children); d++) {
      const HepMC::GenParticle* theDaughter = *d;
      if(isQuark(theDaughter)) {WDecayToQuarks=true;}
      if(isNeutrino(theDaughter)) {WDecayToNeutrinos=true;}

      if(verbose_ && isQuark(theDaughter)) {
	std::cout << "A quark from the W" << std::endl;
	theDaughter->print(); 
      }
      if(verbose_ && isNeutrino(theDaughter)) {
	std::cout << "A neutrino from the W" << std::endl;
	theDaughter->print();
      }
	  
    }
  }
  
  accepted = (WDecayToNeutrinos && WDecayToQuarks);
  
  if(accepted) 
    if(verbose_)
      std::cout << "ACCEPTED" << std::endl;

  delete myGenEvent;
  
  return accepted;
}

// ------------ method called once each job just before starting event loop  ------------
void 
WWDecayFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
WWDecayFilter::endJob() {
}

bool
WWDecayFilter::isQuark(const HepMC::GenParticle* p) {
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
WWDecayFilter::isNeutrino(const HepMC::GenParticle* p) {
  bool result;
  int pdgid = std::abs(p->pdg_id());
  if(pdgid == 12 || pdgid == 14 || pdgid == 16)
    result = true;
  else 
    result = false;
  return result;
}

//define this as a plug-in
DEFINE_FWK_MODULE(WWDecayFilter);
