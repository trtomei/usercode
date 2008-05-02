// -*- C++ -*-
//
// Package:    RSAnalyzer
// Class:      RSAnalyzer
// 
/**\class RSAnalyzer RSAnalyzer.cc RSGraviton/RSAnalyzer/src/RSAnalyzer.cc

Description: Thiago's class for analyzing G*->ZZ->2j + nunu and
                                          G*->ZZ->4j events. 

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Feb 13 15:08:56 CET 2008
// $Id: RSAnalyzer.cc,v 1.2 2008/04/14 17:59:46 tomei Exp $
//
//


// system include files
#include <memory>
#include <utility>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "PhysicsTools/CandUtils/interface/AddFourMomenta.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile.h" 
//
// class decleration
//
bool compare(const reco::GenParticle& x, const reco::GenParticle& y);

class RSAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSAnalyzer(const edm::ParameterSet&);
  ~RSAnalyzer();
  
private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  // ----------member data ---------------------------
  TH1F* h_Zdau_dR;
};

//
// constants, enums and typedefs
//
const int Z_id = 23;
const int grav_id = 5000039;
//
// static data member definitions
//

//
// constructors and destructor
//
RSAnalyzer::RSAnalyzer(const edm::ParameterSet& iConfig)

{
  edm::Service<TFileService> fs;
  h_Zdau_dR = fs->make<TH1F>( "Zdau_dR"  , "dR", 50,  0., 2.);
}


RSAnalyzer::~RSAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;

  Handle<CandidateCollection> genParticles_handle;
  iEvent.getByLabel("genParticleCandidates", genParticles_handle);
  const CandidateCollection genParticles = *genParticles_handle.product();

  // Getting the dR between the two children, and plotting it.
  for(CandidateCollection::const_iterator it = genParticles.begin(); it != genParticles.end();	++it) {
    const Candidate* Z = &*it;
    if(Z->pdgId() == Z_id && Z->status() == 3) {
      std::vector<std::pair<double, double> > Zdaughters;
      for(Candidate::const_iterator dauit = Z->begin(); dauit != Z->end(); ++dauit) {
	if(dauit->pdgId() == Z_id)
	  continue;
	std::pair<double, double> dau(dauit->eta(),dauit->phi());
	Zdaughters.push_back(dau);
      }
      double eta1 = Zdaughters.at(0).first;
      double eta2 = Zdaughters.at(1).first;
      double phi1 = Zdaughters.at(0).second;
      double phi2 = Zdaughters.at(1).second;
      double dR = deltaR(eta1, phi1, eta2, phi2);
      h_Zdau_dR->Fill(dR);
    }
  }
 
}

bool compare(const reco::GenParticle& x, const reco::GenParticle& y)
{
  return x.pt() < y.pt();
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSAnalyzer::beginJob(const edm::EventSetup&)
{
  
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSAnalyzer::endJob() {

}

//define this as a plug-in
DEFINE_FWK_MODULE(RSAnalyzer);
