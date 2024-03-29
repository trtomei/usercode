// system include files
#include <cstdio>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/ServiceRegistry/interface/Service.h"


//
// class declaration
//

class RSPrimaryVertexCounter : public edm::EDFilter {
public:
  explicit RSPrimaryVertexCounter(const edm::ParameterSet&);
  ~RSPrimaryVertexCounter();

private:
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  edm::InputTag vertexSrc;        
  int minNumberOfVertices;
  int maxNumberOfVertices;
  // ----------member data ---------------------------
};

RSPrimaryVertexCounter::RSPrimaryVertexCounter(const edm::ParameterSet& iConfig)
{
  vertexSrc = iConfig.getParameter<edm::InputTag>("vertexCollection");
  minNumberOfVertices = iConfig.getParameter<int>("minNumberOfVertices");
  maxNumberOfVertices = iConfig.getParameter<int>("maxNumberOfVertices");
  std::printf("Will filter events with MORE THAN %i and LESS THAN OR EQUAL TO %i vertices\n",minNumberOfVertices,maxNumberOfVertices);
}


RSPrimaryVertexCounter::~RSPrimaryVertexCounter()
{
}

bool
RSPrimaryVertexCounter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  int numVertices = 0;
  edm::Handle<reco::VertexCollection> pvHandle; 
  iEvent.getByLabel(vertexSrc,pvHandle);
  numVertices = int(pvHandle->size());

  bool result;
  if((numVertices > minNumberOfVertices) && (numVertices <= maxNumberOfVertices))
    result = true;
  else
    result = false;

  return result;
}


//define this as a plug-in
DEFINE_FWK_MODULE(RSPrimaryVertexCounter);
