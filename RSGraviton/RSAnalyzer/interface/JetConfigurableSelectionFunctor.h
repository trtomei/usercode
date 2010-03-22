#include "DataFormats/JetReco/interface/CaloJet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "PhysicsTools/Utilities/interface/Selector.h"

#include <iostream>

class JetConfigurableSelectionFunctor : public Selector<reco::CaloJet> {

public: // interface

  JetConfigurableSelectionFunctor( double ptMin = 0.0,
				   double etaMax = 9999.9,
				   double emfMin = 0.0,
				   double massMin = 0.0 )
  {
    push_back("ptMin",      ptMin);
    push_back("etaMax",     etaMax);
    push_back("emFraction", emfMin);
    push_back("mass",       massMin);

    set("ptMin");
    set("etaMax");
    set("emfMin");
    set("massMin");
  }

  bool operator()( const reco::CaloJet & jet, std::strbitset & ret ) 
  { 
    return doTheCuts( jet, ret );
  }

  bool doTheCuts( const reco::CaloJet & jet, std::strbitset & ret ) 
  {
    double jetPt = jet.pt();
    double jetEta = jet.eta();
    double jetEMF = jet.emEnergyFraction();
    double jetMass = jet.mass();

    if (jetPt > cut("ptMin",double()) || ignoreCut("ptMin")) 
      passCut(ret, "ptMin");
    if (std::abs(jetEta) < cut("etaMax",double()) || ignoreCut("etaMax")) 
      passCut(ret, "etaMax");
    if (jetEMF > cut("emfMin",double()) || ignoreCut("emfMin")) 
      passCut(ret, "emfMin");
    if (jetMass > cut("massMin",double()) || ignoreCut("massMin")) 
      passCut(ret, "massMin");
    
    return (bool)ret;
  }
  
private: // member variables
};
