// -*- C++ -*-
//
// Package:    RSPATJetCorrectionsAnalyzer.cc
// Class:      RSPATJetCorrectionsAnalyzer.cc
// 
/**\class RSPATJetCorrectionsAnalyzer.cc RSPATJetCorrectionsAnalyzer.cc.cc RSGraviton/RSPATJetCorrectionsAnalyzer.cc/src/RSPATJetCorrectionsAnalyzer.cc.cc

Description: Class to analyze jets in RS->jets events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSPATJetCorrectionsAnalyzer.cc.cc,v 1.7 2011/11/14 15:01:56 tomei Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"
#include "TH2F.h"
//
// class decleration
//

class RSPATJetCorrectionsAnalyzer : public edm::EDAnalyzer {
public:
  explicit RSPATJetCorrectionsAnalyzer(const edm::ParameterSet&);
  ~RSPATJetCorrectionsAnalyzer();

private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag jets_;
  unsigned int numberInCollection_;
  bool isData_;
  TH2F*     h_ratioUncGen_genPt;
  TH2F*     h_ratioCorGen_genPt;
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
RSPATJetCorrectionsAnalyzer::RSPATJetCorrectionsAnalyzer(const edm::ParameterSet& iConfig) :
  jets_(iConfig.getParameter<edm::InputTag>("jets") ),
  numberInCollection_(iConfig.getParameter<unsigned int>("numberInCollection") ),
  isData_(iConfig.getParameter<bool>("isData") )
{
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  h_ratioUncGen_genPt   = fs->make<TH2F>( "ratio_UncGen_genPt", "ratio X gen pT", 200, 0., 2., 500, 0., 1000.);
  h_ratioCorGen_genPt   = fs->make<TH2F>( "ratio_CorGen_genPt", "ratio X gen pT", 200, 0., 2., 500, 0., 1000.);
}


RSPATJetCorrectionsAnalyzer::~RSPATJetCorrectionsAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
RSPATJetCorrectionsAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  Handle<edm::View<reco::Candidate> > jetsHandle;
  iEvent.getByLabel(jets_,jetsHandle);

  // Let us double check that we have the wanted jet available.
  if((numberInCollection_+1)>jetsHandle->size())
    throw cms::Exception("ProductNotFound")
      << "The jet collection does not contain enough jets!\n"
      << "We have only " << jetsHandle->size() << " jets!\n";

  // Choose which jet to analyze.
  const pat::Jet & theJet = dynamic_cast<const pat::Jet&>((* jetsHandle)[numberInCollection_]);

  // Get the available  of corrections
  const std::vector<std::string>& JECSets   = theJet.availableJECSets();
  const std::string&  JECSet                = JECSets.at(0);
  const std::vector<std::string>& JECLevels = theJet.availableJECLevels(JECSet);
  const std::string& uncorrectedLevel       = JECLevels.at(0);
  
  // The GEN Jet
  const reco::GenJet* theGenJet = theJet.genJet();
  if(theGenJet == 0) {
    printf("Cade meu genJet???\n");
    return;
  }

  // The uncorrected jet;
  reco::Jet uncorrectedJet = theJet.correctedJet(uncorrectedLevel);

  double genPt = theGenJet->pt();
  double correctedPt = theJet.pt();
  double uncorrectedPt = uncorrectedJet.pt();
  double corRatio = correctedPt/genPt;
  double uncRatio = uncorrectedPt/genPt;
  
  // Fill the histograms.
  h_ratioUncGen_genPt->Fill(uncRatio,genPt);
  h_ratioCorGen_genPt->Fill(corRatio,genPt);
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSPATJetCorrectionsAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSPATJetCorrectionsAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSPATJetCorrectionsAnalyzer);
