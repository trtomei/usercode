// For W processes.

TH1D* H_etaWplus;
TH1D* H_etaWminus;

// Count jets.
TH1D*       H_tnumJets;
TH1D*       H_tbarrel; // Number of jets: total, barrel, endcap.
TH1D*       H_tendcap;

TH1D*       H_Et_tJets;
TH1D*       H_eta_tJets; // Status of jets.
TH1D*       H_phi_tJets;

TH1D*       H_Etjets_barrel;
TH1D*       H_etajets_barrel; // Status of barrel jets.
TH1D*       H_phijets_barrel;

TH1D*       H_Etjets_endcap;
TH1D*       H_etajets_endcap; // Status of endcap jets.
TH1D*       H_phijets_endcap;

TH1D*       H_ptV_dir_1j;
TH1D*       H_ptV_dir_2j;
TH1D*       H_ptV_dir_3j;
TH1D*       H_ptV_dir_4j;
TH1D*       H_ptV_mu_1j;   // Boson pt: true, reconstructed with
TH1D*       H_ptV_mu_2j;   // the two hardest muons in the events 
TH1D*       H_ptV_mu_3j;   // (as if it was Z), reconstructed and from the  
TH1D*       H_ptV_mu_4j;   // with mu+MET (as if it was W) and from jets.
TH1D*       H_ptV_mumet_1j;
TH1D*       H_ptV_mumet_2j;
TH1D*       H_ptV_mumet_3j;
TH1D*       H_ptV_mumet_4j;
TH1D*       H_ptV_jets_1j; 
TH1D*       H_ptV_jets_2j;
TH1D*       H_ptV_jets_3j;
TH1D*       H_ptV_jets_4j;

TH1D*       H_tnumMuons;

TH1D*       H_pt1stmu_1j;
TH1D*       H_eta1stmu_1j;
TH1D*       H_pt2ndmu_1j;
TH1D*       H_eta2ndmu_1j;
TH1D*       H_pt1stmu_2j;
TH1D*       H_eta1stmu_2j;
TH1D*       H_pt2ndmu_2j;
TH1D*       H_eta2ndmu_2j;
TH1D*       H_pt1stmu_3j;
TH1D*       H_eta1stmu_3j;
TH1D*       H_pt2ndmu_3j;
TH1D*       H_eta2ndmu_3j;
TH1D*       H_pt1stmu_4j;
TH1D*       H_eta1stmu_4j;
TH1D*       H_pt2ndmu_4j;
TH1D*       H_eta2ndmu_4j;

TH1D*       H_transvmass_1j;
TH1D*       H_transvmass_2j; // Transverse mass
TH1D*       H_transvmass_3j;
TH1D*       H_transvmass_4j;

TH1D*       H_invmass_2mu_1j;   
TH1D*       H_invmass_2mu_2j;   // Invariant mass of the only 2 muons found.
TH1D*       H_invmass_2mu_3j;   
TH1D*       H_invmass_2mu_4j;   

TH1D*       H_ptnu_direct;   // Neutrino pt.
TH1D*       H_ptnu_jlep;     // Neutrino pt from jets and lepton. 
TH1D*       H_pt_met;        // Met pt.
TH1D*       H_eff;           // Stores if the 1st jet went into b, e, f.  

TH1D*       H_eventcounter;  // Counts events. 
  
vector<TH1D*> H_Etjets; 
vector<TH1D*> H_etajets; // Statistics of the 1st, 2nd, 3rd... more energetic jet.
vector<TH1D*> H_phijets;

