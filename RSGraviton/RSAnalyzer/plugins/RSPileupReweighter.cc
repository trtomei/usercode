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
// $Id: RSPileupReweighter.cc,v 1.1 2011/11/14 14:47:18 tomei Exp $
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
#include "PhysicsTools/Utilities/interface/Lumi3DReWeighting.h"

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
  edm::Lumi3DReWeighting LumiWeights_;
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

  //  std::vector<float> TrueDist2011;
  //  std::vector<float> GenDist;
  //  for( int i=0; i<25; ++i) {
  //    TrueDist2011.push_back(DataDist[i]);
  //   GenDist.push_back(PoissonIntDist[i]);
  //  }    
  //  LumiWeights_ = edm::LumiReWeighting(GenDist,TrueDist2011);
  LumiWeights_ = edm::Lumi3DReWeighting(generatedFile_.c_str(), dataFile_.c_str(), genHistName_.c_str(), dataHistName_.c_str());
  LumiWeights_.weight3D_init( 1.0 );
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
  double myWeight3D = LumiWeights_.weight3D( (*iEventB) );
  
  //std::cout << "This event has weight " << myWeight << std::endl;
  
  // Get the weight, and put it into the event.
  std::auto_ptr<double> weightToPut(new double);
  
  *weightToPut = myWeight3D;
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
