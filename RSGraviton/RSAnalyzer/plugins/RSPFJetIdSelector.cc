// -*- C++ -*-
//
// Package:    RSJetAnalyzerV2
// Class:      RSJetAnalyzerV2
// 
/**\class RSPFJetIdSelector RSPFJetIdSelector.cc RSGraviton/RSPFJetIdSelector/src/RSPFJetIdSelector.cc

Description: Class to select jets based on JetID in RS->jets events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSPFJetIdSelector.cc,v 1.2 2010/07/28 01:29:20 tomei Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/JetReco/interface/JetID.h"
#include "JetMETCorrections/Objects/interface/JetCorrector.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
//
// class decleration
//

class RSPFJetIdSelector : public edm::EDFilter {
public:
  explicit RSPFJetIdSelector(const edm::ParameterSet&);
  ~RSPFJetIdSelector();

private:
  virtual void beginJob();
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag jets_;
  edm::InputTag jetID_;
  double threshold_;
  bool filter_;
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
RSPFJetIdSelector::RSPFJetIdSelector(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets") ),
  threshold_(iConfig.getParameter<double>("threshold") ),
  filter_(iConfig.getParameter<bool>("filter") )
{
  //now do what ever initialization is needed
  produces<reco::PFJetCollection>();
  edm::Service<TFileService> fs;
}


RSPFJetIdSelector::~RSPFJetIdSelector()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
bool
RSPFJetIdSelector::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  // jets
  edm::Handle<reco::PFJetCollection> hJets;
  iEvent.getByLabel(jets_, hJets );
  
  // Implementing loose cuts.
  //* Neutral Hadron Fraction <0.99
  //* Neutral EM Fraction <0.99
  //* Number of Constituents >1
  //*  And for |eta| < 2.4 
  //*  Charged Hadron Fraction >0
  //*  Charged Multiplicity >0
  //*  Charged EM Fraction <0.99
  
  const std::string correctorName("ak7PFL2L3");
  const JetCorrector* corrector = JetCorrector::getJetCorrector(correctorName,iSetup);   //Define the jet corrector
  bool foundProblematicJets = false;
  
  std::auto_ptr<reco::PFJetCollection> passingJets( new reco::PFJetCollection );
  const int size = hJets->size();
  passingJets->reserve( size );

  for ( reco::PFJetCollection::const_iterator ibegin = hJets->begin(),
	  iend = hJets->end(), ijet = ibegin;
	ijet != iend; ++ijet ) {
  
    reco::PFJet theJet = *ijet;

    bool nhfCut = false;
    bool nemCut = false;
    bool numConstituentsCut = false;
    bool chfCut = false;
    bool chargedMultCut = false;
    bool cemCut = false;
    if(std::abs(theJet.eta()) < 2.4) { // This means we are in the tracker...
      chfCut = (theJet.chargedHadronEnergyFraction() > 0.0);
      chargedMultCut = (theJet.chargedMultiplicity() > 0);
      cemCut = (theJet.chargedEmEnergyFraction() < 0.99);
    } 
    else {
      chfCut = true;
      cemCut = true;
      chargedMultCut = true;
    }

    nhfCut = (theJet.neutralHadronEnergyFraction() < 0.99);
    nemCut = (theJet.neutralEmEnergyFraction() < 0.99);
    numConstituentsCut = (theJet.nConstituents() >  1);

    // Calculate correction
    double scale = corrector->correction(theJet.p4());  //calculate the correction
    double newPt = scale*(theJet.pt());

    if(nhfCut && nemCut && numConstituentsCut && chfCut && cemCut && chargedMultCut) {
      passingJets->push_back(theJet);
    }
    else {
      if(newPt > threshold_)
	foundProblematicJets = true;
    }
    
  }
  
  iEvent.put(passingJets);
  // We want to return FALSE if we foundProblematicJets
  if(filter_)
    return (!foundProblematicJets);
  else
    return true;
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSPFJetIdSelector::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSPFJetIdSelector::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSPFJetIdSelector);
