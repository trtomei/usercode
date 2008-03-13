TH1D* H_etaWplus;
TH1D* H_etaWminus;

// For W processes.
TH1D*       H_tnumJets_W;
TH1D*       H_tbarrel_W; // Number of jets: total, barrel, endcap.
TH1D*       H_tendcap_W;

TH1D*       H_pt_tJets_W;
TH1D*       H_Et_tJets_W;
TH1D*       H_eta_tJets_W; // Status of jets.
TH1D*       H_phi_tJets_W;
TH1D*       H_m_tJets_W;
TH1D*       H_mcalc_tJets_W;  

TH1D*       H_Etjets_barrel_W;
TH1D*       H_etajets_barrel_W; // Status of barrel jets.
TH1D*       H_phijets_barrel_W;

TH1D*       H_Etjets_endcap_W;
TH1D*       H_etajets_endcap_W; // Status of endcap jets.
TH1D*       H_phijets_endcap_W;

TH1D*       H_ptV_dir_1j_W;
TH1D*       H_ptV_dir_2j_W;
TH1D*       H_ptV_dir_3j_W;
TH1D*       H_ptV_dir_4j_W;
TH1D*       H_ptV_dirmu_1j_W;
TH1D*       H_ptV_dirmu_2j_W;
TH1D*       H_ptV_dirmu_3j_W;
TH1D*       H_ptV_dirmu_4j_W;
TH1D*       H_ptV_mu_1j_W;   // Boson pt: (2 copies of) true, reconstructed with
TH1D*       H_ptV_mu_2j_W;   // the two hardest muons in the events 
TH1D*       H_ptV_mu_3j_W;   // (as if it was a Z) and from the  
TH1D*       H_ptV_mu_4j_W;   // jet recoil.
TH1D*       H_ptV_jets_1j_W;
TH1D*       H_ptV_jets_2j_W;
TH1D*       H_ptV_jets_3j_W;
TH1D*       H_ptV_jets_4j_W;
TH1D*       H_ptV_mumet_W;   // Boson pt reconstructed with muon+MET (as if it was W).

TH1D*       H_pt1stmu_1j_W;
TH1D*       H_eta1stmu_1j_W;
TH1D*       H_pt2ndmu_1j_W;
TH1D*       H_eta2ndmu_1j_W;
TH1D*       H_pt1stmu_2j_W;
TH1D*       H_eta1stmu_2j_W;
TH1D*       H_pt2ndmu_2j_W;
TH1D*       H_eta2ndmu_2j_W;
TH1D*       H_pt1stmu_3j_W;
TH1D*       H_eta1stmu_3j_W;
TH1D*       H_pt2ndmu_3j_W;
TH1D*       H_eta2ndmu_3j_W;
TH1D*       H_pt1stmu_4j_W;
TH1D*       H_eta1stmu_4j_W;
TH1D*       H_pt2ndmu_4j_W;
TH1D*       H_eta2ndmu_4j_W;

TH1D*       H_transvmass_1j_W;
TH1D*       H_transvmass_2j_W;
TH1D*       H_transvmass_3j_W;
TH1D*       H_transvmass_4j_W;

TH1D*       H_invmass_mumet_W; // Invariant mass with muon and MET.  
TH1D*       H_invmass_2mu_W;   // Invariant mass of the only 2 muons found.
TH1D*       H_invmass_mu12_W;
TH1D*       H_invmass_mu13_W;  // Invariant mass of 1-2, 1-3, 2-3 muons.
TH1D*       H_invmass_mu23_W;

TH1D*       H_dphi_mu12_W;
TH1D*       H_dphi_mu13_W;     // Delta phi in between 1-2, 1-3, 2-3 muons
TH1D*       H_dphi_mu23_W;

TH1D*       H_ptnu_direct_W;   // Neutrino pt.
TH1D*       H_ptnu_dirl_W;   // Neutrino pt.
TH1D*       H_ptnu_jlep_W;     // Neutrino pt from jets and lepton. 
TH1D*       H_pt_met_W;        // Met pt.
TH1D*       H_eff_W;           // Stores if the 1st jet went into b, e, f.  
  
vector<TH1D*> H_Etjets_W; 
vector<TH1D*> H_etajets_W; // Statistics of the 1st, 2nd, 3rd... more energetic jet.
vector<TH1D*> H_phijets_W;
// *********************************************
// For Z processes.
TH1D*       H_tnumJets_Z;
TH1D*       H_tbarrel_Z; // Number of jets: total, barrel, endcap.
TH1D*       H_tendcap_Z;

TH1D*       H_pt_tJets_Z;
TH1D*       H_Et_tJets_Z;
TH1D*       H_eta_tJets_Z; // Status of jets.
TH1D*       H_phi_tJets_Z;
TH1D*       H_m_tJets_Z;
TH1D*       H_mcalc_tJets_Z;  

TH1D*       H_Etjets_barrel_Z;
TH1D*       H_etajets_barrel_Z; // Status of barrel jets.
TH1D*       H_phijets_barrel_Z;

TH1D*       H_Etjets_endcap_Z;
TH1D*       H_etajets_endcap_Z; // Status of endcap jets.
TH1D*       H_phijets_endcap_Z;

TH1D*       H_ptV_dir_1j_Z;
TH1D*       H_ptV_dir_2j_Z;
TH1D*       H_ptV_dir_3j_Z;
TH1D*       H_ptV_dir_4j_Z;
TH1D*       H_ptV_dirmu_1j_Z;
TH1D*       H_ptV_dirmu_2j_Z;
TH1D*       H_ptV_dirmu_3j_Z;
TH1D*       H_ptV_dirmu_4j_Z;
TH1D*       H_ptV_mu_1j_Z;   // Boson pt: true, reconstructed with
TH1D*       H_ptV_mu_2j_Z;   // the two hardest muons in the events 
TH1D*       H_ptV_mu_3j_Z;   // (as if it was a Z) and from the  
TH1D*       H_ptV_mu_4j_Z;   // jet recoil.
TH1D*       H_ptV_jets_1j_Z;
TH1D*       H_ptV_jets_2j_Z;
TH1D*       H_ptV_jets_3j_Z;
TH1D*       H_ptV_jets_4j_Z;
TH1D*       H_ptV_mumet_Z;   // Boson pt reconstructed with muon+MET (as if it was W).

TH1D*       H_pt1stmu_1j_Z;
TH1D*       H_eta1stmu_1j_Z;
TH1D*       H_pt2ndmu_1j_Z;
TH1D*       H_eta2ndmu_1j_Z;
TH1D*       H_pt1stmu_2j_Z;
TH1D*       H_eta1stmu_2j_Z;
TH1D*       H_pt2ndmu_2j_Z;
TH1D*       H_eta2ndmu_2j_Z;
TH1D*       H_pt1stmu_3j_Z;
TH1D*       H_eta1stmu_3j_Z;
TH1D*       H_pt2ndmu_3j_Z;
TH1D*       H_eta2ndmu_3j_Z;
TH1D*       H_pt1stmu_4j_Z;
TH1D*       H_eta1stmu_4j_Z;
TH1D*       H_pt2ndmu_4j_Z;
TH1D*       H_eta2ndmu_4j_Z;

TH1D*       H_transvmass_1j_Z;
TH1D*       H_transvmass_2j_Z;
TH1D*       H_transvmass_3j_Z;
TH1D*       H_transvmass_4j_Z;  

TH1D*       H_invmass_mumet_Z; // Invariant mass with muon and MET.  
TH1D*       H_invmass_2mu_Z;   // Invariant mass of the only 2 muons found.
TH1D*       H_invmass_mu12_Z;
TH1D*       H_invmass_mu13_Z;  // Invariant mass of 1-2, 1-3, 2-3 muons.
TH1D*       H_invmass_mu23_Z;

TH1D*       H_dphi_mu12_Z;
TH1D*       H_dphi_mu13_Z;     // Delta phi in between 1-2, 1-3, 2-3 muons
TH1D*       H_dphi_mu23_Z;

TH1D*       H_ptnu_direct_Z;   // Neutrino pt.
TH1D*       H_ptnu_dirl_Z;   // Neutrino pt.
TH1D*       H_ptnu_jlep_Z;     // Neutrino pt from jets and lepton. 
TH1D*       H_pt_met_Z;        // Met pt.
TH1D*       H_eff_Z;           // Stores if the 1st jet went into b, e, f.  
  
vector<TH1D*> H_Etjets_Z; 
vector<TH1D*> H_etajets_Z; // Statistics of the 1st, 2nd, 3rd... more energetic jet.
vector<TH1D*> H_phijets_Z;
// *********************************************
// For tt processes.
TH1D*       H_tnumJets_tt;
TH1D*       H_tbarrel_tt; // Number of jets: total, barrel, endcap.
TH1D*       H_tendcap_tt;

TH1D*       H_pt_tJets_tt;
TH1D*       H_Et_tJets_tt;
TH1D*       H_eta_tJets_tt; // Status of jets.
TH1D*       H_phi_tJets_tt;
TH1D*       H_m_tJets_tt;
TH1D*       H_mcalc_tJets_tt;  

TH1D*       H_Etjets_barrel_tt;
TH1D*       H_etajets_barrel_tt; // Status of barrel jets.
TH1D*       H_phijets_barrel_tt;

TH1D*       H_Etjets_endcap_tt;
TH1D*       H_etajets_endcap_tt; // Status of endcap jets.
TH1D*       H_phijets_endcap_tt;

TH1D*       H_ptV_dir_1j_tt;
TH1D*       H_ptV_dir_2j_tt;
TH1D*       H_ptV_dir_3j_tt;
TH1D*       H_ptV_dir_4j_tt;
TH1D*       H_ptV_dirmu_1j_tt;
TH1D*       H_ptV_dirmu_2j_tt;
TH1D*       H_ptV_dirmu_3j_tt;
TH1D*       H_ptV_dirmu_4j_tt;
TH1D*       H_ptV_mu_1j_tt;   // Boson pt: true, reconstructed with
TH1D*       H_ptV_mu_2j_tt;   // the two hardest muons in the events 
TH1D*       H_ptV_mu_3j_tt;   // (as if it was a Z) and from the  
TH1D*       H_ptV_mu_4j_tt;   // jet recoil.
TH1D*       H_ptV_jets_1j_tt;
TH1D*       H_ptV_jets_2j_tt;
TH1D*       H_ptV_jets_3j_tt;
TH1D*       H_ptV_jets_4j_tt;
TH1D*       H_ptV_mumet_tt;   // Boson pt reconstructed with muon+MET (as if it was W).

TH1D*       H_pt1stmu_1j_tt;
TH1D*       H_eta1stmu_1j_tt;
TH1D*       H_pt2ndmu_1j_tt;
TH1D*       H_eta2ndmu_1j_tt;
TH1D*       H_pt1stmu_2j_tt;
TH1D*       H_eta1stmu_2j_tt;
TH1D*       H_pt2ndmu_2j_tt;
TH1D*       H_eta2ndmu_2j_tt;
TH1D*       H_pt1stmu_3j_tt;
TH1D*       H_eta1stmu_3j_tt;
TH1D*       H_pt2ndmu_3j_tt;
TH1D*       H_eta2ndmu_3j_tt;
TH1D*       H_pt1stmu_4j_tt;
TH1D*       H_eta1stmu_4j_tt;
TH1D*       H_pt2ndmu_4j_tt;
TH1D*       H_eta2ndmu_4j_tt;

TH1D*       H_transvmass_1j_tt;
TH1D*       H_transvmass_2j_tt;
TH1D*       H_transvmass_3j_tt;
TH1D*       H_transvmass_4j_tt;  

TH1D*       H_invmass_mumet_tt; // Invariant mass with muon and MET.  
TH1D*       H_invmass_2mu_tt;   // Invariant mass of the only 2 muons found.
TH1D*       H_invmass_mu12_tt;
TH1D*       H_invmass_mu13_tt;  // Invariant mass of 1-2, 1-3, 2-3 muons.
TH1D*       H_invmass_mu23_tt;

TH1D*       H_dphi_mu12_tt;
TH1D*       H_dphi_mu13_tt;     // Delta phi in between 1-2, 1-3, 2-3 muons
TH1D*       H_dphi_mu23_tt;

TH1D*       H_ptnu_direct_tt;   // Neutrino pt.
TH1D*       H_ptnu_dirl_tt;   // Neutrino pt.
TH1D*       H_ptnu_jlep_tt;     // Neutrino pt from jets and lepton. 
TH1D*       H_pt_met_tt;        // Met pt.
TH1D*       H_eff_tt;           // Stores if the 1st jet went into b, e, f.  
  
vector<TH1D*> H_Etjets_tt; 
vector<TH1D*> H_etajets_tt; // Statistics of the 1st, 2nd, 3rd... more energetic jet.
vector<TH1D*> H_phijets_tt;
// *********************************************
