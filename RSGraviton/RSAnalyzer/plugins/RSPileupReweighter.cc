// -*- C++ -*-
//
// Package:    RSPileupReweighter
// Class:      RSPileupReweighter
// 
/**\class RSPileupReweighter RSPileupReweighter.cc RSGraviton/RSPileupReweighter/src/RSPileupReweighter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Thiago Tomei
//         Created:  Thu Mar  4 16:26:36 BRT 2010
// $Id: RSPileupReweighter.cc,v 1.3 2011/02/09 12:31:19 tomei Exp $
//
//


// system include files
#include <memory>
#include <algorithm>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

//
// class declaration
//

class RSPileupReweighter : public edm::EDFilter {
   public:
      explicit RSPileupReweighter(const edm::ParameterSet&);
      ~RSPileupReweighter();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
  edm::LumiReWeighting LumiWeights_;
  std::string generatedFile_;
  std::string dataFile_;
  std::string genHistName_;
  std::string dataHistName_;
  bool useROOThistos_;
  // 
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
RSPileupReweighter::RSPileupReweighter(const edm::ParameterSet& iConfig) :
  generatedFile_(iConfig.getParameter<std::string>("generatedFile")),
  dataFile_(iConfig.getParameter<std::string>("dataFile")),
  genHistName_(iConfig.getParameter<std::string>("genHistName")),
  dataHistName_(iConfig.getParameter<std::string>("dataHistName")),
  useROOThistos_(iConfig.getParameter<bool>("useROOThistos"))
{

  Double_t PoissonIntDist[25] = {
    0.104109,
    0.0703573,
    0.0698445,
    0.0698254,
    0.0697054,
    0.0697907,
    0.0696751,
    0.0694486,
    0.0680332,
    0.0651044,
    0.0598036,
    0.0527395,
    0.0439513,
    0.0352202,
    0.0266714,
    0.019411,
    0.0133974,
    0.00898536,
    0.0057516,
    0.00351493,
    0.00212087,
    0.00122891,
    0.00070592,
    0.000384744,
    0.000219377
  };

  Double_t DataDist[25] = {
    14541678.75140,
    34774289.38287,
    78924690.82741,
    126467305.04758,
    159328519.15030,
    167603454.44536,
    152683760.94960,
    123793506.45609,
    90946208.64652,
    61397298.32203,
    38505025.66459,
    22628034.29717,
    12550315.25869,
    6610507.05491,
    3324027.56536,
    1602862.62060,
    743920.15564,
    333476.86203,
    144860.60592,
    61112.68817,
    25110.18360,
    10065.11630,
    3943.97901,
    1513.53536,
    896.16051
  };

  std::vector<float> TrueDist2011;
  std::vector<float> GenDist;
  for( int i=0; i<25; ++i) {
    TrueDist2011.push_back(DataDist[i]);
    GenDist.push_back(PoissonIntDist[i]);
  }    
  LumiWeights_ = edm::LumiReWeighting(GenDist,TrueDist2011);
    
  produces<double>();
}


RSPileupReweighter::~RSPileupReweighter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
RSPileupReweighter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  // Pray
  edm::EventBase* iEventB = dynamic_cast<edm::EventBase*>(&iEvent);
  double myWeight = LumiWeights_.weight( (*iEventB) );
  
  //std::cout << "This event has weight " << myWeight << std::endl;
  
  // Get the weight, and put it into the event.
  std::auto_ptr<double> weightToPut(new double);
  
  *weightToPut = myWeight;
  iEvent.put(weightToPut);

  return true;
}

// ------------ method called once each job just before starting event loop  ------------
void 
RSPileupReweighter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RSPileupReweighter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RSPileupReweighter);
