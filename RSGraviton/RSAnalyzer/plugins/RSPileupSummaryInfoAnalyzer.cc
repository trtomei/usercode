// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

//
// class declaration
//

class RSPileupSummaryInfoAnalyzer : public edm::EDFilter {
public:
  explicit RSPileupSummaryInfoAnalyzer(const edm::ParameterSet&);
  ~RSPileupSummaryInfoAnalyzer();

private:
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  edm::InputTag pileupInfo_;        
  TH1F* inTimeHisto;
  TH1F* minus50nsHisto;
  TH1F* plus50nsHisto;
  // ----------member data ---------------------------
};

RSPileupSummaryInfoAnalyzer::RSPileupSummaryInfoAnalyzer(const edm::ParameterSet& iConfig)
{
  edm::Service<TFileService> fs;
  inTimeHisto = fs->make<TH1F>("inTimeHisto","inTimeHisto",51,-0.5,50.5);
  minus50nsHisto = fs->make<TH1F>("minus50nsHisto","minus50nsHisto",51,-0.5,50.5);
  plus50nsHisto = fs->make<TH1F>("plus50nsHisto","plus50nsHisto",51,-0.5,50.5);

  pileupInfo_ = iConfig.getParameter<edm::InputTag>("pileupInfo");
}


RSPileupSummaryInfoAnalyzer::~RSPileupSummaryInfoAnalyzer()
{
}

bool
RSPileupSummaryInfoAnalyzer::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  edm::Handle<std::vector< PileupSummaryInfo > >  PupInfo;
  iEvent.getByLabel(pileupInfo_, PupInfo);
  std::vector<PileupSummaryInfo>::const_iterator PVI;

  int npvInTime = -1;
  int npv50nsEarly = -1;
  int npv50nsLate = -1;
  for(PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI) {
    int BX = PVI->getBunchCrossing();
    
    if(BX == 0)
      npvInTime = PVI->getPU_NumInteractions();
    if(BX == -1)
      npv50nsEarly = PVI->getPU_NumInteractions();
    if(BX == 1)
      npv50nsLate = PVI->getPU_NumInteractions();
    
  }

  if(npvInTime < 0) { 
    std::cerr << "No in-time beam crossing found? WTF?" << std::endl;
  }

  inTimeHisto->Fill(npvInTime);
  minus50nsHisto->Fill(npv50nsEarly);
  plus50nsHisto->Fill(npv50nsLate);
  
  return true;
}


//define this as a plug-in
DEFINE_FWK_MODULE(RSPileupSummaryInfoAnalyzer);
