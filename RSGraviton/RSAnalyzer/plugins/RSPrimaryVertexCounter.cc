// system include files
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
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"

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
  unsigned int minNDOF;
  double maxAbsZ;
  double maxd0;
  int maxNumberOfVertices;
  TH1F* histo;
  // ----------member data ---------------------------
};

RSPrimaryVertexCounter::RSPrimaryVertexCounter(const edm::ParameterSet& iConfig)
{
  edm::Service<TFileService> fs;
  histo = fs->make<TH1F>("num_vertices","num_vertices",10,-0.5,9.5);
  vertexSrc = iConfig.getParameter<edm::InputTag>("vertexCollection");
  minNDOF = iConfig.getParameter<unsigned int>("minimumNDOF");
  maxAbsZ = iConfig.getParameter<double>("maxAbsZ");
  maxd0 = iConfig.getParameter<double>("maxd0");
  maxNumberOfVertices = iConfig.getParameter<int>("maxNumberOfVertices");
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
  const reco::VertexCollection & vertices = *pvHandle.product();
  for(reco::VertexCollection::const_iterator it=vertices.begin() ; it!=vertices.end() ; ++it)
    {
      if(it->ndof() > minNDOF && 
         ( (maxAbsZ <=0 ) || fabs(it->z()) <= maxAbsZ ) &&
         ( (maxd0 <=0 ) || fabs(it->position().rho()) <= maxd0 )
	 ) 
	numVertices++;
    }

  histo->Fill(numVertices);

  bool result;
  if(numVertices == maxNumberOfVertices)
    result = true;
  else
    result = false;

  return result;
}


//define this as a plug-in
DEFINE_FWK_MODULE(RSPrimaryVertexCounter);
