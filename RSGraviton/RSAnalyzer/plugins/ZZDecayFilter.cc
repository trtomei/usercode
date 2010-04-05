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

class ZZDecayFilter : public edm::EDFilter {
public:
  explicit ZZDecayFilter(const edm::ParameterSet&);
  ~ZZDecayFilter();
  
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
ZZDecayFilter::ZZDecayFilter(const edm::ParameterSet& iConfig) :
  verbose_(iConfig.getParameter<bool>("verbose"))
{
   //now do what ever initialization is needed

}


ZZDecayFilter::~ZZDecayFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
ZZDecayFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  // Get the HepMC event.
  edm::Handle<edm::HepMCProduct> evt;
  iEvent.getByLabel("generator", evt);
  
  bool accepted = false;
  bool ZDecayToNeutrinos = false;
  bool ZDecayToQuarks = false;
  HepMC::GenEvent* myGenEvent = new HepMC::GenEvent(*(evt->GetEvent()));
    
  for ( HepMC::GenEvent::particle_iterator piter = myGenEvent->particles_begin();
	piter != myGenEvent->particles_end(); ++piter ) {
    // Check for Z bosons.
    const HepMC::GenParticle* p =  *piter;
    if(verbose_) p->print();
    if(p->pdg_id() != 23) continue;
    
    // Get the decay vertex.
    HepMC::GenVertex* ZDecayVertex = p->end_vertex();
    if(ZDecayVertex == 0) continue;

    for (HepMC::GenVertex::particle_iterator d = ZDecayVertex->particles_begin(HepMC::children);
	 d != ZDecayVertex->particles_end(HepMC::children); d++) {
      const HepMC::GenParticle* theDaughter = *d;
      if(isQuark(theDaughter)) {ZDecayToQuarks=true;}
      if(isNeutrino(theDaughter)) {ZDecayToNeutrinos=true;}

      if(verbose_ && isQuark(theDaughter)) {
	std::cout << "A quark from the Z" << std::endl;
	theDaughter->print(); 
      }
      if(verbose_ && isNeutrino(theDaughter)) {
	std::cout << "A neutrino from the Z" << std::endl;
	theDaughter->print();
      }
	  
    }
  }
  
  accepted = (ZDecayToNeutrinos && ZDecayToQuarks);
  
  if(accepted) 
    if(verbose_)
      std::cout << "ACCEPTED" << std::endl;

  delete myGenEvent;
  
  return accepted;
}

// ------------ method called once each job just before starting event loop  ------------
void 
ZZDecayFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ZZDecayFilter::endJob() {
}

bool
ZZDecayFilter::isQuark(const HepMC::GenParticle* p) {
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
ZZDecayFilter::isNeutrino(const HepMC::GenParticle* p) {
  bool result;
  int pdgid = std::abs(p->pdg_id());
  if(pdgid == 12 || pdgid == 14 || pdgid == 16)
    result = true;
  else 
    result = false;
  return result;
}

//define this as a plug-in
DEFINE_FWK_MODULE(ZZDecayFilter);
