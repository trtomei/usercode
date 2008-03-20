// -*- C++ -*-
//
// Package:    CalibrationCurve
// Class:      CalibrationCurve
// 
/**\class CalibrationCurve CalibrationCurve.cc VnjetAnalyzer/CalibrationCurve/src/CalibrationCurve.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Thiago Fernandez Perez
//         Created:  Thu Nov 22 22:11:49 CET 2007
// $Id$
//
//


// system include files
#include <memory>
#include <cstddef>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// My includes                                                                                                                                            
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Common/interface/Ref.h"
#include <TFile.h>
#include <TH1.h>
#include <TH2.h>
#include <TProfile.h>
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

using namespace std;
using namespace reco;
using namespace edm;

//
// class decleration
//

class CalibrationCurve : public edm::EDAnalyzer {
   public:
      explicit CalibrationCurve(const edm::ParameterSet&);
      ~CalibrationCurve();


   private:
      virtual void beginJob(const edm::EventSetup&) ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      // ----------member data ---------------------------

  InputTag source_;
  InputTag matched_;
  double coneradius_;
  bool debugmode_;
  string fOutputFileName_;

  int nevents_;

  // ROOT stuff.
  TFile* hOutputFile;
  TH1I* H_eff;
  TH1D* H_amax;
  TH1D* H_bmax;
  TH2D* H_abmax;
  TH1D* H_separation;
  TProfile* calibcurve;
  //  TH2D* H_good;
};
 
//
// constants, enums and typedefs
//
const int passed = 1;
const int dropped = 0;
const double wellmatched = 0.3;
//
// static data member definitions
//

//
// constructors and destructor
//
CalibrationCurve::CalibrationCurve(const edm::ParameterSet& iConfig):
  source_(iConfig.getParameter<InputTag>("src") ),
  matched_(iConfig.getParameter<InputTag>("matched") ),
  coneradius_(iConfig.getParameter<double>("coneRadius") ),
  debugmode_(iConfig.getParameter<bool>("debugmode") ),
  fOutputFileName_(iConfig.getUntrackedParameter<string>("HistOutFile", "output.root") )
{
  //now do what ever initialization is needed
  hOutputFile = new TFile(fOutputFileName_.c_str(), "RECREATE" );
  H_eff       = new TH1I( "efficiency", "Passing and failing events", 2, 0, 2);
  H_amax      = new TH1D( "alpha_max", "Dist. of alpha_max", 50, 0., 1.);
  H_bmax      = new TH1D( "beta_max", "Dist. of beta_max", 70, 0., 7.);
  H_abmax     = new TH2D( "a_b_max", "Dist of a_max and b_max", 50, 0., 1., 70, 0., 7.);
  H_separation = new TH1D( "separation", "Separation", 20, 0., 10.);
  calibcurve  = new TProfile( "calibcurve", "Calib. curve", 20, 0., 200.,0.,1.5 ,"s"); 
  nevents_ = 0;
}


CalibrationCurve::~CalibrationCurve()
{
  
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  hOutputFile->Write() ;
  hOutputFile->Close() ;
  return;
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
CalibrationCurve::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace std;
  using namespace edm;
  
  Handle<CandidateCollection> source;
  iEvent.getByLabel(source_, source);
  Handle<CandidateCollection> matched;
  iEvent.getByLabel(matched_, matched);

  nevents_++;
  if((nevents_%100)==0)
    LogInfo("Information") << "Event number " << nevents_ << endl;
  
  int srcsize = source->size();
  int mtcsize = matched->size();
  
  if(debugmode_) {
    LogInfo("Information") << "ATTENTION: source size is " << srcsize 
	    << " and matched size is " << mtcsize << endl;
  }

  if(mtcsize < srcsize) {
    if(debugmode_) {
      LogInfo("Information") << "Source size (" << srcsize << ") < matched size (" <<
	mtcsize << ")." << endl;
      LogInfo("Information") << "-------------------------" << endl;
    }
    H_eff->Fill(dropped);
    return;
  }
  // We want only to have events in which there are, at least,
  // as many reconstructed jets as hard partons.
  // To be very general, I will call the partons
  // SOURCES and the jets MATCHED.
  
  H_eff->Fill(passed);
  
  vector <vector<double> > vecsource;
  vector <vector<double> > vecmatched;
  
  for(CandidateCollection::const_iterator iSr  = source->begin();
      iSr != source->end();
      iSr++) {
    vector <double> thissource;
    double Et_temp = iSr->et();
    double E_temp = iSr->energy();
    double px_temp = iSr->px();
    double py_temp = iSr->py();
    double pz_temp = iSr->pz();
    double eta_temp = iSr->eta();
    double phi_temp = iSr->phi();
    thissource.push_back(Et_temp);
    thissource.push_back(E_temp);
    thissource.push_back(px_temp);
    thissource.push_back(py_temp);
    thissource.push_back(pz_temp);
    thissource.push_back(eta_temp);
    thissource.push_back(phi_temp);
    vecsource.push_back(thissource);
    thissource.clear();
  }

  for(CandidateCollection::const_iterator iMt  = matched->begin();
      iMt != matched->end();
      iMt++) {
    vector <double> thismatched;
    double Et_temp = iMt->et();
    double E_temp = iMt->energy();
    double px_temp = iMt->px();
    double py_temp = iMt->py();
    double pz_temp = iMt->pz();
    double eta_temp = iMt->eta();
    double phi_temp = iMt->phi();
    thismatched.push_back(Et_temp);
    thismatched.push_back(E_temp);
    thismatched.push_back(px_temp);
    thismatched.push_back(py_temp);
    thismatched.push_back(pz_temp);
    thismatched.push_back(eta_temp);
    thismatched.push_back(phi_temp);
    vecmatched.push_back(thismatched);
    thismatched.clear();
  }
  // Ok, vecsource and vecmatched have all the source and matched.
  
  double bestdeltaR = 99999.;
  double amax = 0.;
  double bmax = 0.;
  int bestsource;
  int bestmatched;
  vector< pair < vector<double>, vector<double> > > couplemap;

  while(vecsource.size() != 0) {
    
    bestdeltaR = 99999.;
    
    for(int ivsrc = 0;
	ivsrc != vecsource.size();
	ivsrc++) {
      for(int ivmat = 0;
	  ivmat != vecmatched.size();
	  ivmat++) {
	double temp_eta_src = vecsource[ivsrc][5];
	double temp_phi_src = vecsource[ivsrc][6];
	double temp_eta_mat = vecmatched[ivmat][5];
	double temp_phi_mat = vecmatched[ivmat][6];
	double tempdeltaR = deltaR(temp_eta_src, temp_phi_src,
				   temp_eta_mat, temp_phi_mat);
	if(tempdeltaR < bestdeltaR) {
	  bestdeltaR = tempdeltaR;
	  bestsource = ivsrc;
	  bestmatched = ivmat;
	}
      }
    }
    // Ok, now we have the best delta R for the current selection.
    // Let's save it if it is the biggest one (amax).
      
    if(bestdeltaR > amax)
      amax = bestdeltaR;

    // Let's create a pair of vector<double> to represent that matching.

    // First we create the two vectors themselves.
    vector<double> chosensource = vecsource[bestsource];
    vector<double> chosenmatched = vecmatched[bestmatched];
    
    // Enhance these vectors with the deltaR information.
    chosensource.push_back(bestdeltaR);
    chosenmatched.push_back(bestdeltaR);

    // Let us calculate the pull from the generator pt, and
    // enhance the vectors with this info.
    //    double resolution;
    //    resolution = 1.2*sqrt(chosenmatched[0]) + 0.07*chosenmatched[0];
    // This is totally adhoc - but it is a first guess.
    //    double pull;
    //    pull = (fabs(chosenmatched[0]-chosensource[0])/resolution);
    //    chosensource.push_back(pull);
    //    chosenmatched.push_back(pull);
    // Let's save it if it is the biggest one (bmax).
    //    if(pull > bmax)
    //      bmax = pull;

    // Create the pair, and push it to the vector<pair(vector,vector)>.
    pair <vector<double>, vector<double> > couple(chosensource, chosenmatched);
    couplemap.push_back(couple);
    
  // Remove the chosen couple from the vectors.
    vecsource.erase(vecsource.begin()+bestsource);
    //LogInfo("Information") << "Removed the source with pt = " << chosensource[0] << endl;
    vecmatched.erase(vecmatched.begin()+bestmatched);
    //LogInfo("Information") << "Removed the matched with pt = " << chosenmatched[0] << endl;
  }
  // Closes while(vecsource.size()!=0)
  
  // Ok, we have matched all the sources to some matches.
  // The remaining matches, we pair them with an empty vector.
  
  for(int ileft = 0; ileft != vecmatched.size(); ileft++) {
    vector<double> leftmatched = vecmatched[ileft];
    vector<double> nullvector;
    nullvector.clear();
    
    pair <vector<double>, vector<double> > lonejet(nullvector, leftmatched);
    couplemap.push_back(lonejet);
  }

  // Now, we analyze all jets, and find well-matched, well-separated
  // ones to create the calibration curve.
  
  for (int imap = 0; imap!=couplemap.size(); ++imap) {
    vector<double> testsource = (couplemap[imap]).first;
    vector<double> testmatched = (couplemap[imap]).second;

    bool goodmatch;
    // Check well-matched.
     if( !(testsource.empty()) ) {
      double thisdeltaR;
      thisdeltaR = testmatched[7];
      goodmatch = (thisdeltaR < wellmatched);
     }
     else
       goodmatch = false;

     //Check well-separated.
     double minseparation = 99999;
     bool separated = true;
     for (int jmap = 0; jmap!=couplemap.size(); ++jmap) {
      vector<double> secondmatched = (couplemap[jmap]).second;
     
      // Don't try to separate a jet from itself!
      if(imap == jmap)
	continue;
      
      double eta1 = testmatched[5];
      double phi1 = testmatched[6];
      double eta2 = secondmatched[5];
      double phi2 = secondmatched[6];
    
      double separation;
      separation = deltaR(eta1, phi1, eta2, phi2);
      if(debugmode_) {
	LogInfo("Information") << "Eta phi: " << eta1 << ", " << phi1 << ", " 
		     << eta2 << ", " << phi2 << endl;
	LogInfo("Information") << "Separation is " << separation << endl;
      }
      if(separation < 2*coneradius_)
	separated = false;
      if(separation < minseparation)
	minseparation = separation;
     }

     // Just to keep track of separation;
     H_separation->Fill(minseparation);

     if(separated && goodmatch) {
       if(debugmode_) 
	 LogInfo("Information") << "Separated and well-matched." << endl;
       double recofraction = (testmatched[4])/(testsource[4]);
       double jetEt = testmatched[0];
       calibcurve->Fill(jetEt, recofraction);  
     }
  }
  // Finished checking well-matching & separation.
  
  // Ok, now let us do something USEFUL with this.
  // First, we fill the histogram for amax with the largest 
  // deltaR of a matched couple in the event (amax).
  H_amax->Fill(amax);
  
}

// ------------ method called once each job just before starting event loop  ------------
void 
CalibrationCurve::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CalibrationCurve::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(CalibrationCurve);
