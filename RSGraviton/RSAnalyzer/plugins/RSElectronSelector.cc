// -*- C++ -*-
//
// Package:    RSJetAnalyzerV2
// Class:      RSJetAnalyzerV2
// 
/**\class RSElectronSelector RSElectronSelector.cc RSGraviton/RSElectronSelector/src/RSElectronSelector.cc

Description: Class to select electrons based on HEEP in RS->electrons events.

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Wed Apr 23 17:48:37 CEST 2008
// $Id: RSElectronSelector.cc,v 1.1 2010/06/09 13:52:52 tomei Exp $
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
#include "FWCore/ParameterSet/interface/InputTag.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "SHarper/HEEPAnalyzer/interface/HEEPAnalyzerBarePAT.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
//
// class decleration
//

class RSElectronSelector : public edm::EDFilter {
public:
  explicit RSElectronSelector(const edm::ParameterSet&);
  ~RSElectronSelector();

private:
  virtual void beginJob();
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  // ----------member data ---------------------------

  edm::InputTag eleLabel_;
  heep::EleSelector cuts_;

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
RSElectronSelector::RSElectronSelector(const edm::ParameterSet& iConfig) :
  eleLabel_(iConfig.getParameter<edm::InputTag>("eleLabel") ),
  cuts_(iConfig)
{
  edm::Service<TFileService> fs;
}


RSElectronSelector::~RSElectronSelector()
{
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.
}


//
// member functions
//

// ------------ method called to for each event  ------------
bool
RSElectronSelector::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  // electrons
  edm::Handle<reco::GsfElectronCollection> eleHandle;
  iEvent.getByLabel(eleLabel_,eleHandle);
  const reco::GsfElectronCollection& electrons = *(eleHandle.product());

  // Pretty simple thing at the beginning: just pass/fail the event if the leading electron doesn't pass the HEEP cuts.
  bool passed = true;
  passed = cuts_.passCuts(electrons.at(0));
  
  return passed;
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSElectronSelector::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSElectronSelector::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSElectronSelector);
