// -*- C++ -*-
//
// Package:    RSDistortedJetsProducer
// Class:      RSDistortedJetsProducer
// 
/**\class RSDistortedJetsProducer RSDistortedJetsProducer.cc RSGraviton/RSDistortedJetsProducer/src/RSDistortedJetsProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Thiago Tomei
//         Created:  Thu Mar  4 16:26:36 BRT 2010
// $Id: RSDistortedJetsProducer.cc,v 1.2 2011/03/17 09:28:58 tomei Exp $
//
//


// system include files
#include <memory>
#include <vector>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Common/interface/View.h" 
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

//
// class declaration
//

class RSDistortedJetsProducer : public edm::EDProducer {
   public:
      explicit RSDistortedJetsProducer(const edm::ParameterSet&);
      ~RSDistortedJetsProducer();

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
  edm::InputTag src_;
  double calibrationChanges_;
  double ePU_;
  double JA_;
  double AvgPu_;
  double Constant_;
  bool upScale_;
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
RSDistortedJetsProducer::RSDistortedJetsProducer(const edm::ParameterSet& iConfig) :
  src_(iConfig.getParameter<edm::InputTag>("src")),
  calibrationChanges_(iConfig.getParameter<double>("calibrationChanges")),
  ePU_(iConfig.getParameter<double>("ePU")),
  JA_(iConfig.getParameter<double>("JA")),
  AvgPu_(iConfig.getParameter<double>("AvgPu")),
  Constant_(iConfig.getParameter<double>("Constant")),
  upScale_(iConfig.getParameter<bool>("upScale"))
{
  produces<std::vector<pat::Jet> >();
}


RSDistortedJetsProducer::~RSDistortedJetsProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
RSDistortedJetsProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<edm::View<pat::Jet> > jetsHandle;
  iEvent.getByLabel(src_,jetsHandle);

  std::string JEC_PATH("CondFormats/JetMETObjects/data/");
  edm::FileInPath fip(JEC_PATH+"Spring10_Uncertainty_AK7PF.txt");
  // edm::FileInPath fip(JEC_PATH+"Spring10_Uncertainty_AK5PF.txt");
  // edm::FileInPath fip(JEC_PATH+"Spring10_Uncertainty_AK5JPT.txt");
  JetCorrectionUncertainty *jecUnc = new JetCorrectionUncertainty(fip.fullPath());

  const size_t size = jetsHandle->size();
  std::auto_ptr<std::vector<pat::Jet> > jetsPointer(new std::vector<pat::Jet>);
  jetsPointer->reserve(size);

  for(size_t i=0;i!=size;++i) {
    double eta = jetsHandle->at(i).eta();
    double ptCor = jetsHandle->at(i).pt();
    jecUnc->setJetEta(eta); // Give rapidity of jet you want uncertainty on
    jecUnc->setJetPt(ptCor);// Also give the corrected pt of the jet you want the uncertainty on
    double uncer = jecUnc->getUncertainty(true); // Uncertainty (pt,eta)
    double PUuncer = ePU_ * JA_ * AvgPu_ * Constant_ / ptCor;

    double totalUncertaintySquare = uncer*uncer +
      calibrationChanges_*calibrationChanges_ + 
      PUuncer * PUuncer;
    double totalUncertainty = sqrt(totalUncertaintySquare);
    double ptScaled = 0.0;
    if(upScale_)
      ptScaled = (1.0 + totalUncertainty) * ptCor;
    else
      ptScaled = (1.0 - totalUncertainty) * ptCor;
    
    math::PtEtaPhiMLorentzVector polar = jetsHandle->at(i).polarP4();
    pat::Jet newJet = (jetsHandle->at(i));
    polar.SetPt(ptScaled);
    newJet.setP4(polar);
    jetsPointer->push_back(newJet);
  }

  iEvent.put(jetsPointer);
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSDistortedJetsProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSDistortedJetsProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSDistortedJetsProducer);
