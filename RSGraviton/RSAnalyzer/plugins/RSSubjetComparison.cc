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
// $Id: RSSubjetComparison.cc,v 1.1 2009/05/13 15:38:08 tomei Exp $
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
#include "PhysicsTools/CandUtils/interface/AddFourMomenta.h"

#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
#include "TLorentzVector.h"
#include "TVector3.h"
#include "TLorentzRotation.h" 
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
  // ----------member data ---------------------------

  edm::InputTag src_;
  edm::InputTag boost_;
  TH1F* h_dR;
  TH1F* h_dPhi;
  TH1F* h_mass;
  TH1F* h_helicity;
  TH1F* h_numJets;
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
  src_(iConfig.getParameter<edm::InputTag>("src") ),
  boost_(iConfig.getParameter<edm::InputTag>("boost") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_numJets             = fs->make<TH1F>( "numJets", "numJets", 10, -0.5, 9.5);
  h_dR                  = fs->make<TH1F>( "dR"  , "dR", 100,  0., 5.);
  h_dPhi                = fs->make<TH1F>( "dPhi", "dPhi", 72,  -M_PI, M_PI);
  h_mass                = fs->make<TH1F>( "mass", "mass", 40,  0., 200.);
  h_helicity            = fs->make<TH1F>( "helicity", "helicity", 50, -1.0, 1.0);
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

  Handle<CandidateView> srcHandle;
  iEvent.getByLabel(src_,srcHandle);
  // Get also the graviton and the boost vector.
  Handle<CandidateView > gravitonHandle;
  iEvent.getByLabel("directGravitons", gravitonHandle);
  Handle<math::XYZVector> boostVectorHandle;
  iEvent.getByLabel(boost_,boostVectorHandle);

  int firstJet = -1;
  int secondJet = -1;
  double largerEt = 0.;
  double secLargerEt = 0.;

  h_numJets->Fill(srcHandle->size());

  // We check for deltaR, deltaPhi, mass and helicity only IF there are at least two subjets.
  if(srcHandle->size() < 2) {
    return;
  }

  for(size_t i = 0; i != srcHandle->size(); ++i) {

    double thisEt = ((*srcHandle)[i]).et();
    if(thisEt > largerEt) {
      secLargerEt = largerEt;
      secondJet = firstJet;
      largerEt = thisEt;
      firstJet = i;
    }
    else if(thisEt > secLargerEt) {
      secLargerEt = thisEt;
      secondJet = i;
    }
  }

  const Candidate& theFirstJet = (*srcHandle)[firstJet];
  const Candidate& theSecondJet = (*srcHandle)[secondJet];
  
  double thisDeltaR = deltaR(theFirstJet.eta(), theFirstJet.phi(), theSecondJet.eta(), theSecondJet.phi());
  double thisDeltaPhi = deltaPhi(theFirstJet.phi(), theSecondJet.phi());
  
  // The helicity is complicated...
  const Candidate& theGraviton = (*gravitonHandle)[0];
  TLorentzVector pB(theGraviton.px(), theGraviton.py(), theGraviton.pz(), theGraviton.energy());
  TVector3 boostRes(-boostVectorHandle->X(), -boostVectorHandle->Y(), -boostVectorHandle->Z());
  TLorentzRotation ResRif(boostRes);
  TVector3 alreadyBoostedp1Vector(theFirstJet.px(), theFirstJet.py(), theFirstJet.pz());
  double CosThetaHel = (alreadyBoostedp1Vector*(ResRif*pB).Vect())/(alreadyBoostedp1Vector.Mag()*(ResRif*pB).Vect().Mag());

  h_dR->Fill(thisDeltaR);
  h_dPhi->Fill(thisDeltaPhi);
  h_helicity->Fill(CosThetaHel);

  CompositeCandidate comp;
  comp.addDaughter( theFirstJet );
  comp.addDaughter( theSecondJet );
  AddFourMomenta addP4;
  addP4.set( comp );

  h_mass->Fill(comp.mass());

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

//define this as a plug-in
DEFINE_FWK_MODULE(RSSubJetComparison);
