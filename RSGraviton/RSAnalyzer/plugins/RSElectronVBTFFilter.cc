// Shamelessly copied from Nikolaos code

#ifndef RSElectronVBTFFilter_H
#define RSElectronVBTFFilter_H
// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
//
#include <vector>
#include <iostream>
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/Common/interface/ValueMap.h"
//
#include "TString.h"
#include "TMath.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"

//

//
// class declaration
//

class RSElectronVBTFFilter : public edm::EDFilter {
   public:
      explicit RSElectronVBTFFilter(const edm::ParameterSet&);
      ~RSElectronVBTFFilter();

   private:
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      bool isInFiducial(double eta);
      bool isPositiveEnergy(double energy);
      
      // ----------member data ---------------------------
  edm::InputTag electronCollectionTag_;
  edm::InputTag electronIdTag_;

  double BarrelMaxEta_;
  double EndCapMaxEta_;
  double EndCapMinEta_;
  double electronIdMin_;
  double ETCut_;
  double ETCut2ndEle_;
  bool vetoSecondElectronEvents_;
  bool filter_;
};
#endif
//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
RSElectronVBTFFilter::RSElectronVBTFFilter(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed
  // *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
  // I N P U T      P A R A M E T E R S  *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
  // *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
  // Cuts
  double ETCut_D = 30.;
  ETCut_ = iConfig.getUntrackedParameter<double>("ETCut",ETCut_D);
  double ETCut2ndEle_D = 20.;
  ETCut2ndEle_ = iConfig.getUntrackedParameter<double>("ETCut2ndEle",ETCut2ndEle_D);
  vetoSecondElectronEvents_ = iConfig.getUntrackedParameter<bool>("vetoSecondElectronEvents",false);
  
  // Fiducial region
  double BarrelMaxEta_D = 1.4442;
  double EndCapMinEta_D = 1.56;
  double EndCapMaxEta_D = 2.5;
  BarrelMaxEta_ = iConfig.getUntrackedParameter<double>("BarrelMaxEta",
                                                        BarrelMaxEta_D);
  EndCapMaxEta_ = iConfig.getUntrackedParameter<double>("EndCapMaxEta",
                                                        EndCapMaxEta_D);
  EndCapMinEta_ = iConfig.getUntrackedParameter<double>("EndCapMinEta",
                                                        EndCapMinEta_D);

  // electrons
  edm::InputTag electronCollectionTag_D("selectedLayer1Electrons","","PAT");
  electronCollectionTag_=iConfig.getUntrackedParameter<edm::InputTag>
    ("electronCollectionTag",electronCollectionTag_D);
  // electronId
  edm::InputTag electronIdTag_D("simpleEleId80relIso","","");
  electronIdTag_=iConfig.getUntrackedParameter<edm::InputTag>
    ("electronIdTag",electronIdTag_D);
  int electronIdMin_D(7);
  electronIdMin_ = iConfig.getUntrackedParameter<double>
    ("electronIdMin",electronIdMin_D);
  
  // shall we filter or nor?
  filter_ = iConfig.getUntrackedParameter<bool>("filter",false);
  
  //
  // *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
  //
  // now print a summary with what exactly the filter does:
  std::cout << "RSElectronVBTFFilter: Running electron VBTF Filter..." << std::endl;
  std::cout << "RSElectronVBTFFilter: ET  > " << ETCut_ << std::endl;
  if (vetoSecondElectronEvents_) {
  std::cout << "RSElectronVBTFFilter: VETO 2nd electron with ET > " 
	    << ETCut2ndEle_ << std::endl;
  }
  else {
    std::cout << "RSElectronVBTFFilter: No veto for 2nd electron applied " 
	      << std::endl;
  }
  std::cout << "RSElectronVBTFFilter: Fiducial Cut: " << std::endl;
  std::cout << "RSElectronVBTFFilter:    BarrelMax: "<<BarrelMaxEta_<<std::endl;
  std::cout << "RSElectronVBTFFilter:    EndcapMin: " << EndCapMinEta_
	    << "  EndcapMax: " << EndCapMaxEta_
	    <<std::endl;
  std::cout << "RSElectronVBTFFilter: ElectronId: " << electronIdTag_
	    << std::endl;
  std::cout << "RSElectronVBTFFilter: ElectronIdMin: " << electronIdMin_
	    << std::endl;
  if(filter_)
    std::cout << "RSElectronVBTFFilter: Will work in filter mode" << std::endl;
  else
    std::cout << "RSElectronVBTFFilter: Will NOT work in filter mode" << std::endl;
  
  // extra info in the event
  produces< reco::GsfElectronCollection >
    ("selectedVBTFElectrons").setBranchAlias("selectedVBTFElectrons");
  produces < int >
    ("electronVBTFStatus").setBranchAlias("electronVBTFStatus");
}


RSElectronVBTFFilter::~RSElectronVBTFFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
RSElectronVBTFFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;

   // Electron collection
   edm::Handle<reco::GsfElectronCollection> gsfElectron;
   iEvent.getByLabel(electronCollectionTag_, gsfElectron);
   unsigned int electronCollectionSize = gsfElectron->size();

   bool weGotElectrons = true;
   if(electronCollectionSize == 0) {
    // Ok, there are no electrons in the event...
    weGotElectrons = false;
  }
   //std::cout << std::boolalpha;
   //std::cout << "weGotElectrons " << weGotElectrons << std::endl;

   const reco::GsfElectronCollection *pElecs = gsfElectron.product();

   // Get electron ID
   edm::Handle<edm::ValueMap<float> > eIDmap_handle;
   iEvent.getByLabel(electronIdTag_, eIDmap_handle);
   const edm::ValueMap<float> *eIDmap = eIDmap_handle.product();
   
   //  ------------------------------------------------------------------
   //  Order your electrons: first the ones with the higher ET
   //  ------------------------------------------------------------------

   // Check number of REASONABLE electrons in fiducial region.
   // Also save a vector of etas and phis for later usage.
   int  counter = 0;
   std::vector<int> indices;
   std::vector<double> ETs;
   reco::GsfElectronCollection myElectrons;
   std::vector<double> allEtas;
   std::vector<double> allPhis;
   reco::GsfElectronCollection::const_iterator elec;
   for (elec = pElecs->begin(); elec != pElecs->end(); ++elec) {
     allEtas.push_back(elec->p4().eta());
     allPhis.push_back(elec->p4().phi());
     bool isEleFiducial = isInFiducial(elec->caloPosition().eta());
     bool isEleReasonable  = isPositiveEnergy(elec->caloEnergy()); 
     if (isEleReasonable && isEleFiducial) {
       //std::cout << "This electron has caloenergy " << elec->caloEnergy() << std::endl;
       //std::cout << "This electron has caloPositionEta " << elec->caloPosition().eta() << std::endl;
       double sc_et = elec->caloEnergy()/cosh(elec->caloPosition().eta());
       //std::cout << "This electron has sc_et " << sc_et << std::endl;
       indices.push_back(counter); ETs.push_back(sc_et);
       myElectrons.push_back(*elec);
       ++counter;
     }
   }
   
   bool weGotFiducialElectrons = true;
   const int event_elec_number = (int) indices.size();
   if (event_elec_number == 0) {
     weGotFiducialElectrons = false;
   }
   //std::cout << "weGotFiducialElectrons " << weGotFiducialElectrons << std::endl;

   // Loop to reject/control Z->ee is done separately
   int nelesForZ1 = 0;
   int nelesForZ2 = 0;
   int leadingElectronIndex = -1;
   double leadingElectronSCET = 0.0;
   //std::cout << "event_elec_number " << event_elec_number << std::endl;
   for (int i=0; i<event_elec_number; i++) {
     double et = ETs.at(i);
     //std::cout << "This electron has SCET " << et << std::endl;
     if(et>ETCut_) nelesForZ1++;
     if(et>ETCut2ndEle_) nelesForZ2++;
     if(et > leadingElectronSCET) {
       leadingElectronSCET = et;
       leadingElectronIndex = i;
     }
   }

   int originalLeadingElectronIndex;
   if(leadingElectronIndex != -1)
     originalLeadingElectronIndex = indices.at(leadingElectronIndex);
   else
     originalLeadingElectronIndex = -1;
   // At this point, if originalLeadingElectronIndex == -1,
   // this means that no fiducial electrons were found.

   // Get the flags ready.
   bool passesEtCut = true;
   bool passes2ndElectronVeto = true;
   bool passesElectronID = true;

   // Get the collections ready;
   auto_ptr<reco::GsfElectronCollection>
     selectedVBTFElectrons(new reco::GsfElectronCollection);
   auto_ptr<int> electronVBTFStatus(new int);
   
   if(weGotFiducialElectrons) {
     //std::cout << "leadingElectronSCET " << leadingElectronSCET << std::endl;
     // get the most high-ET electron:
     const reco::GsfElectron maxETelec = myElectrons[leadingElectronIndex];
     // Shove the guy into the collection already
     reco::GsfElectron theChosenElectron = *(maxETelec.clone()); 
     selectedVBTFElectrons->push_back(theChosenElectron);
     
     // if the highest electron in the event has ET < ETCut_ return
     if (leadingElectronSCET < ETCut_)
       passesEtCut = false;
     
     // if more than one fiducial electron passes ET > ETCut2ndEle_ return
     if (nelesForZ2 > 1 && vetoSecondElectronEvents_)
       passes2ndElectronVeto = false;

     // get also a reference to it: This is complicated by the fact that 
     // the electrons leadingElectronIndex refers to a different collection!
     // So, we get the index saved in the std::vector<int> indices
     edm::Ref<reco::GsfElectronCollection> maxETelectronRef(gsfElectron,originalLeadingElectronIndex);

     //std::cout << "originalLeadingElectronIndex is " << originalLeadingElectronIndex << std::endl;
     //std::cout << "eIDmap->size() is " << eIDmap->size() << std::endl;

     double electronIdResult = double((*eIDmap)[maxETelectronRef]);
     if(electronIdResult < electronIdMin_)     
       passesElectronID = false;

     // The electron ID requirements
     // https://twiki.cern.ch/twiki/bin/viewauth/CMS/SimpleCutBasedEleID#Electron_ID_Implementation_in_Re
     /*
       The value map returns a double with the following meaning:
       
       0: fails
       1: passes electron ID only
       2: passes electron Isolation only
       3: passes electron ID and Isolation only
       4: passes conversion rejection
       5: passes conversion rejection and ID
       6: passes conversion rejection and Isolation
       7: passes the whole selection
     */
   }

   bool theFilterResult = (weGotElectrons && weGotFiducialElectrons &&
			   passesEtCut && passes2ndElectronVeto && 
			   passesElectronID);
   
   if(theFilterResult == true)
     *electronVBTFStatus = 1;
   else 
     *electronVBTFStatus = 0;

   //std::cout << "theFilterResult " << theFilterResult << std::endl;
   iEvent.put( selectedVBTFElectrons, "selectedVBTFElectrons");
   iEvent.put( electronVBTFStatus, "electronVBTFStatus");

   if (filter_ == true)
     return theFilterResult;
   else
     return true;
}

// ------------ method called once each job just after ending the event loop  -
void 
RSElectronVBTFFilter::endJob() {
}

bool RSElectronVBTFFilter::isInFiducial(double eta)
{
  if (fabs(eta) < BarrelMaxEta_) return true;
  else if (fabs(eta) < EndCapMaxEta_ && fabs(eta) > EndCapMinEta_)
    return true;
  return false;

}

bool RSElectronVBTFFilter::isPositiveEnergy(double energy)
{
  return (energy>0);
}
//define this as a plug-in
DEFINE_FWK_MODULE(RSElectronVBTFFilter);
