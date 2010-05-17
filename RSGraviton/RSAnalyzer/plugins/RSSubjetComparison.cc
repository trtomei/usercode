// -*- C++ -*-
//
// Package:    RSSubJetComparison
// Class:      RSSubJetComparison
// 
/**\class RSSubJetComparison RSSubJetComparison.cc RSGraviton/RSSubJetComparison/src/RSSubJetComparison.cc

Description: Class to analyze jets in RS->jets events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSSubjetComparison.cc,v 1.3 2009/05/27 13:48:55 tomei Exp $
//
//


// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/InputTag.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "CommonTools/CandUtils/interface/AddFourMomenta.h"

#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
#include "TH2F.h"
//
// class decleration
//

class RSSubJetComparison : public edm::EDAnalyzer {
public:
  explicit RSSubJetComparison(const edm::ParameterSet&);
  ~RSSubJetComparison();

private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  int countSubJets(const reco::CandidateView v, const double momentumCut);

  // ----------member data ---------------------------

  edm::InputTag srcFirst_;
  edm::InputTag srcSecond_;
  double momentumCut_;
  TH1F* h_jetE_first;
  TH1F* h_jetEt_first;
  TH1F* h_jetE_second;
  TH1F* h_jetEt_second;
  TH1F* h_numJetsFirst;
  TH1F* h_numJetsSecond;
  TH2F* h_numJetsCorr;
  TH1F* h_massFirst;
  TH1F* h_massSecond;
  TH1F* h_massFirst_inc;
  TH1F* h_massSecond_inc;
  TH1F* h_dR3_First;
  TH1F* h_dR3_Second;
  TH2F* h_massCorr;
  TH2F* h_massCorr_inc;
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
RSSubJetComparison::RSSubJetComparison(const edm::ParameterSet& iConfig) :
  srcFirst_(iConfig.getParameter<edm::InputTag>("srcFirst") ),
  srcSecond_(iConfig.getParameter<edm::InputTag>("srcSecond") ),
  momentumCut_(iConfig.getParameter<double>("momentumCut") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_jetE_first          = fs->make<TH1F>( "subJetE_first", "subJetE_first", 80, 0., 200.);
  h_jetEt_first         = fs->make<TH1F>( "subJetEt_first", "subJetEt_first", 80, 0., 200.);
  h_jetE_second         = fs->make<TH1F>( "subJetE_second", "subJetE_second", 80, 0., 200.);
  h_jetEt_second        = fs->make<TH1F>( "subJetEt_second", "subJetEt_second", 80, 0., 200.);
  h_numJetsFirst        = fs->make<TH1F>( "numJetsFirst", "numJetsFirst", 10, -0.5, 9.5);
  h_numJetsSecond       = fs->make<TH1F>( "numJetsSecond", "numJetsSecond", 10, -0.5, 9.5);
  h_numJetsCorr         = fs->make<TH2F>( "numJetsCorr", "numJetsCorr", 10, -0.5, 9.5, 10, -0.5, 9.5);
  h_massFirst           = fs->make<TH1F>( "massFirst", "massFirst", 40,  0., 200.);
  h_massSecond          = fs->make<TH1F>( "massSecond", "massSecond", 40,  0., 200.);
  h_massFirst_inc       = fs->make<TH1F>( "massFirst_inc", "massFirst_inc", 40,  0., 200.);
  h_massSecond_inc      = fs->make<TH1F>( "massSecond_inc", "massSecond_inc", 40,  0., 200.);
  h_dR3_First           = fs->make<TH1F>( "dR3_first", "dR3_first", 50, 0.0, 5.0);
  h_dR3_Second          = fs->make<TH1F>( "dR3_second", "dR3_second", 50, 0.0, 5.0);
  h_massCorr            = fs->make<TH2F>( "massCorr", "massCorr", 40,  0., 200., 40, 0., 200.);
  h_massCorr_inc        = fs->make<TH2F>( "massCorr_inc", "massCorr_inc", 40,  0., 200., 40, 0., 200.);
 
}


RSSubJetComparison::~RSSubJetComparison()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSSubJetComparison::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;

  // Get subjets from first and second jets.
  Handle<CandidateView> firstHandle;
  Handle<CandidateView> secondHandle;
  iEvent.getByLabel(srcFirst_,firstHandle);
  iEvent.getByLabel(srcSecond_,secondHandle);

  // Zeroeth part: get the spectrum of those subjets. 
  for(size_t i = 0; i != firstHandle->size(); ++i) {
    h_jetE_first->Fill((*firstHandle)[i].energy());
    h_jetEt_first->Fill((*firstHandle)[i].et());
  }
  for(size_t i = 0; i != secondHandle->size(); ++i) {
    h_jetE_second->Fill((*secondHandle)[i].energy());
    h_jetEt_second->Fill((*secondHandle)[i].et());
  }

  // Count number of subjets in each.
  int numSubJetsFirst  = this->countSubJets(*firstHandle,momentumCut_);
  int numSubJetsSecond = this->countSubJets(*secondHandle,momentumCut_);
  h_numJetsFirst->Fill(numSubJetsFirst);
  h_numJetsSecond->Fill(numSubJetsSecond);
  h_numJetsCorr->Fill(numSubJetsFirst,numSubJetsSecond);

  // Some variables to use later;
  double mass1;
  double mass2;
  double mass1inc;
  double mass2inc;
  //---------------------------- First subjet ----------------------------
  
  // First part: check if number of subjets is two. If it is, then combine the two jets.
  if(numSubJetsFirst == 2) {
    CompositeCandidate comp;
    const Candidate& dau1 = (*firstHandle)[0];
    const Candidate& dau2 = (*firstHandle)[1];
    comp.addDaughter( dau1 );
    comp.addDaughter( dau2 );
    AddFourMomenta addP4;
    addP4.set( comp );
    mass1 = comp.mass();
    h_massFirst->Fill(mass1); 
  }

  // Second part: if number of subjets is larger than two, do it with the most energetic two,
  // and check if the third is close. 
  if(numSubJetsFirst > 2) {
    int firstJet = -1;
    int secondJet = -1;
    int thirdJet = -1;
    double largerEnergy = 0.;
    double secLargerEnergy = 0.;
    double terLargerEnergy = 0.;
 
    for(size_t i = 0; i != firstHandle->size(); ++i) {
      
      double thisEnergy = ((*firstHandle)[i]).energy();
      if(thisEnergy > largerEnergy) {
	terLargerEnergy = secLargerEnergy;
	secLargerEnergy = largerEnergy;
	thirdJet = secondJet;
	secondJet = firstJet;
	largerEnergy = thisEnergy;
	firstJet = i;
      }
      else if(thisEnergy > secLargerEnergy) {
	terLargerEnergy = secLargerEnergy;
	thirdJet = secondJet;
	secLargerEnergy = thisEnergy;
	secondJet = i;
      }
      else if(thisEnergy > terLargerEnergy) {
	terLargerEnergy = thisEnergy;
	thirdJet = i;
      }
    }

    CompositeCandidate comp;
    const Candidate& dau1 = (*firstHandle)[firstJet];
    const Candidate& dau2 = (*firstHandle)[secondJet];
    const Candidate& extraJet = (*firstHandle)[thirdJet];
    comp.addDaughter( dau1 );
    comp.addDaughter( dau2 );
    AddFourMomenta addP4;
    addP4.set( comp );
    mass1inc = comp.mass();
    h_massFirst_inc->Fill(mass1inc);

    // Find to whom the third jet is closest, and plot it.
    double deltaR1e = deltaR(dau1.eta(), dau1.phi(), extraJet.eta(), extraJet.phi());
    double deltaR2e = deltaR(dau2.eta(), dau2.phi(), extraJet.eta(), extraJet.phi());
    if(deltaR1e < deltaR2e)
      h_dR3_First->Fill(deltaR1e);
    else
      h_dR3_First->Fill(deltaR2e);
  }

  //---------------------------- Second subjet ----------------------------

  // First part: check if number of subjets is two. If it is, then combine the two jets.
  if(numSubJetsSecond == 2) {
    CompositeCandidate comp;
    const Candidate& dau1 = (*secondHandle)[0];
    const Candidate& dau2 = (*secondHandle)[1];
    comp.addDaughter( dau1 );
    comp.addDaughter( dau2 );
    AddFourMomenta addP4;
    addP4.set( comp );
    mass2 = comp.mass();
    h_massSecond->Fill(mass2); 
  }

  // Second part: if number of subjets is larger than two, do it with the most energetic two,
  // and check if the third is close. 
  if(numSubJetsSecond > 2) {
    int firstJet = -1;
    int secondJet = -1;
    int thirdJet = -1;
    double largerEnergy = 0.;
    double secLargerEnergy = 0.;
    double terLargerEnergy = 0.;
 
    for(size_t i = 0; i != secondHandle->size(); ++i) {
      
      double thisEnergy = ((*secondHandle)[i]).energy();
      if(thisEnergy > largerEnergy) {
	terLargerEnergy = secLargerEnergy;
	secLargerEnergy = largerEnergy;
	thirdJet = secondJet;
	secondJet = firstJet;
	largerEnergy = thisEnergy;
	firstJet = i;
      }
      else if(thisEnergy > secLargerEnergy) {
	terLargerEnergy = secLargerEnergy;
	thirdJet = secondJet;
	secLargerEnergy = thisEnergy;
	secondJet = i;
      }
      else if(thisEnergy > terLargerEnergy) {
	terLargerEnergy = thisEnergy;
	thirdJet = i;
      }
    }

    CompositeCandidate comp;
    const Candidate& dau1 = (*secondHandle)[firstJet];
    const Candidate& dau2 = (*secondHandle)[secondJet];
    const Candidate& extraJet = (*secondHandle)[thirdJet];
    comp.addDaughter( dau1 );
    comp.addDaughter( dau2 );
    AddFourMomenta addP4;
    addP4.set( comp );
    mass2inc = comp.mass();
    h_massSecond_inc->Fill(mass2inc);

    // Find to whom the third jet is closest, and plot it.
    double deltaR1e = deltaR(dau1.eta(), dau1.phi(), extraJet.eta(), extraJet.phi());
    double deltaR2e = deltaR(dau2.eta(), dau2.phi(), extraJet.eta(), extraJet.phi());
    if(deltaR1e < deltaR2e)
      h_dR3_Second->Fill(deltaR1e);
    else
      h_dR3_Second->Fill(deltaR2e);
  }

  // Fill the correlation histograms.
  h_massCorr->Fill(mass1,mass2);
  h_massCorr_inc->Fill(mass1inc, mass2inc);
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSSubJetComparison::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSSubJetComparison::endJob() {
}

int
RSSubJetComparison::countSubJets(const reco::CandidateView v, const double momentumCut) {
  int count(0);
  for(size_t i = 0; i != v.size(); ++i) {
    if(v[i].p() > momentumCut) 
      count++; 
  }
  return count;
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSSubJetComparison);
