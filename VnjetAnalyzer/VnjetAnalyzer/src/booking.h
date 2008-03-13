const double minptboson = 0.;
const double maxptboson = 500.;
const double minptjet = 0.;
const double maxptjet = 250.;
const double minptlepton = 0.;
const double maxptlepton = 250.;
const int numbinsboson = 100;
const int numbinsjet = 50;
const int numbinslepton = 50; 

char name[256];
ostringstream hEt_name;
ostringstream heta_name;
ostringstream hphi_name;

H_etaWplus  = new TH1D( "etaWplus", "Eta dist W+", 26, -5.2, 5.2);
H_etaWminus = new TH1D( "etaWminus", "Eta dist W-", 26, -5.2, 5.2);

hOutputFile->cd("Wjets");
H_tnumJets_W    = new TH1D( "njets_total_W", "Total number of jets", 10, 0, 10 );
H_tbarrel_W     = new TH1D( "perc_barrel_W", "Perc. of jets in barrel", 55, 0., 1.1);
H_tendcap_W     = new TH1D( "perc_endcap_W", "Perc. of jets in endcap", 55, 0., 1.1);

H_pt_tJets_W    = new TH1D( "pt_tJets_W", "Pt dist. of total jets", numbinsjet, minptjet, maxptjet);
H_Et_tJets_W    = new TH1D( "Et_tJets_W", "Et dist. of total jets", numbinsjet, minptjet, maxptjet);
H_eta_tJets_W   = new TH1D( "eta_tJets_W", "Eta dist. of total jets", 26, -5.2, 5.2);
H_phi_tJets_W   = new TH1D( "phi_tJets_W", "Phi dist. of total jets", 36, -M_PI, M_PI);
H_m_tJets_W     = new TH1D( "m_tJets_W", "Mass dist. of total jets", 200, 0., 20.);
H_mcalc_tJets_W = new TH1D( "mcalc_tJets_W", "Calc. mass dist. of total jets", 210, -1., 20.);

H_Etjets_barrel_W  = new TH1D( "Et_barrel_W", "Et dist. of jets in barrel", numbinsjet, minptjet, maxptjet);
H_etajets_barrel_W = new TH1D( "eta_barrel_W", "Eta dist. of jets in barrel", 26, -5.2, 5.2);
H_phijets_barrel_W = new TH1D( "phi_barrel_W", "Phi dist. of jets in barrel", 36, -M_PI, M_PI);

H_Etjets_endcap_W  = new TH1D( "Et_endcap_W", "Et dist. of jets in endcap", numbinsjet, minptjet, maxptjet);
H_etajets_endcap_W = new TH1D( "eta_endcap_W", "Eta dist. of jets in endcap", 26, -5.2, 5.2);
H_phijets_endcap_W = new TH1D( "phi_endcap_W", "Phi dist. of jets in endcap", 36, -M_PI, M_PI);

H_ptV_dir_1j_W  = new TH1D( "ptV_true_1j_W", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_2j_W  = new TH1D( "ptV_true_2j_W", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_3j_W  = new TH1D( "ptV_true_3j_W", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_4j_W  = new TH1D( "ptV_true_4j_W", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_1j_W  = new TH1D( "ptV_true_2mu_1j_W", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_2j_W  = new TH1D( "ptV_true_2mu_2j_W", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_3j_W  = new TH1D( "ptV_true_2mu_3j_W", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_4j_W  = new TH1D( "ptV_true_2mu_4j_W", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);

H_ptV_mu_1j_W  = new TH1D( "ptV_2mu_1j_W", "Pt dist. V - 2mu >= 1j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_2j_W  = new TH1D( "ptV_2mu_2j_W", "Pt dist. V - 2mu >= 2j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_3j_W  = new TH1D( "ptV_2mu_3j_W", "Pt dist. V - 2mu >= 3j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_4j_W  = new TH1D( "ptV_2mu_4j_W", "Pt dist. V - 2mu >= 4j", numbinsboson, minptboson, maxptboson);

H_ptV_jets_1j_W = new TH1D( "ptV_jets_1j_W", "Pt dist. V - >= 1 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_2j_W = new TH1D( "ptV_jets_2j_W", "Pt dist. V - >= 2 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_3j_W = new TH1D( "ptV_jets_3j_W", "Pt dist. V - >= 3 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_4j_W = new TH1D( "ptV_jets_4j_W", "Pt dist. V - >= 4 jet", numbinsboson, minptboson, maxptboson);

H_ptV_mumet_W   = new TH1D( "ptV_mumet_W", "Pt dist. V - mu+MET", numbinsboson, minptboson, maxptboson);

H_pt1stmu_1j_W  = new TH1D( "pt1stmu_1j_W", "Pt dist. 1stmu >= 1j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_1j_W = new TH1D( "eta1stmu_1j_W", "Eta dist. 1stmu >= 1j", 26, -5.2, 5.2);
H_pt2ndmu_1j_W  = new TH1D( "pt2ndmu_1j_W", "Pt dist. 2ndmu >= 1j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_1j_W = new TH1D( "eta2ndmu_1j_W", "Eta dist. 2ndmu >= 1j", 26, -5.2, 5.2);
H_pt1stmu_2j_W  = new TH1D( "pt1stmu_2j_W", "Pt dist. 1stmu >= 2j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_2j_W = new TH1D( "eta1stmu_2j_W", "Eta dist. 1stmu >= 2j", 26, -5.2, 5.2);
H_pt2ndmu_2j_W  = new TH1D( "pt2ndmu_2j_W", "Pt dist. 2ndmu >= 2j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_2j_W = new TH1D( "eta2ndmu_2j_W", "Eta dist. 2ndmu >= 2j", 26, -5.2, 5.2);
H_pt1stmu_3j_W  = new TH1D( "pt1stmu_3j_W", "Pt dist. 1stmu >= 3j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_3j_W = new TH1D( "eta1stmu_3j_W", "Eta dist. 1stmu >= 3j", 26, -5.2, 5.2);
H_pt2ndmu_3j_W  = new TH1D( "pt2ndmu_3j_W", "Pt dist. 2ndmu >= 3j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_3j_W = new TH1D( "eta2ndmu_3j_W", "Eta dist. 2ndmu >= 3j", 26, -5.2, 5.2);
H_pt1stmu_4j_W  = new TH1D( "pt1stmu_4j_W", "Pt dist. 1stmu >= 4j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_4j_W = new TH1D( "eta1stmu_4j_W", "Eta dist. 1stmu >= 4j", 26, -5.2, 5.2);
H_pt2ndmu_4j_W  = new TH1D( "pt2ndmu_4j_W", "Pt dist. 2ndmu >= 4j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_4j_W = new TH1D( "eta2ndmu_4j_W", "Eta dist. 2ndmu >= 4j", 26, -5.2, 5.2);

H_transvmass_1j_W = new TH1D( "transvmass_1j_W", "Transv. mass >= 1j", 50, 0., 150.);
H_transvmass_2j_W = new TH1D( "transvmass_2j_W", "Transv. mass >= 2j", 50, 0., 150.);
H_transvmass_3j_W = new TH1D( "transvmass_3j_W", "Transv. mass >= 3j", 50, 0., 150.);
H_transvmass_4j_W = new TH1D( "transvmass_4j_W", "Transv. mass >= 4j", 50, 0., 150.);

H_invmass_mumet_W  = new TH1D( "invmass_mumet_W", "Inv. mass V mu MET", 100, 0., 200.);
H_invmass_2mu_W  = new TH1D( "invmass_2mu_W", "Inv. mass V 2 mu", 100, 0., 200.);
H_invmass_mu12_W = new TH1D( "invmass_mu12_W", "Inv. mass V mu12", 100, 0., 200.);
H_invmass_mu13_W = new TH1D( "invmass_mu13_W", "Inv. mass V mu13", 100, 0., 200.);
H_invmass_mu23_W = new TH1D( "invmass_mu23_W", "Inv. mass V mu23", 100, 0., 200.);

H_dphi_mu12_W   = new TH1D( "dphi_mu12_W", "Delta phi V mu12", 36, -M_PI, M_PI);
H_dphi_mu13_W   = new TH1D( "dphi_mu13_W", "Delta phi V mu13", 36, -M_PI, M_PI);
H_dphi_mu23_W   = new TH1D( "dphi_mu23_W", "Delta phi V mu23", 36, -M_PI, M_PI);
  
H_ptnu_direct_W = new TH1D( "ptnu_true_W", "Pt dist. nu - true", numbinslepton, minptlepton, maxptlepton);
H_ptnu_dirl_W   = new TH1D( "ptnu_true_1mu_W", "Pt dist. nu - true", numbinslepton, minptlepton, maxptlepton);
H_ptnu_jlep_W   = new TH1D( "ptnu_jet_1mu_W", "Pt dist. nu - jets and l", numbinslepton, minptlepton, maxptlepton);
H_pt_met_W      = new TH1D( "pt_met_W", "Pt dist. nu - MET", numbinslepton, minptlepton, maxptlepton);
H_eff_W         = new TH1D( "efficiency_W", "0=bar, 1=end, 2=fwd", 3, 0, 3);

H_Etjets_W.resize(maxnumjets);
H_etajets_W.resize(maxnumjets);
H_phijets_W.resize(maxnumjets);

for (int i=0; i!=maxnumjets; ++i) {
  hEt_name.str("");
  heta_name.str("");
  hphi_name.str("");
  hEt_name << "jet_Et_" << (i+1) << "o_W";
  heta_name << "jet_eta_" << (i+1) << "o_W";
  hphi_name << "jet_phi_" << (i+1) << "o_W";
  H_Etjets_W[i] = new TH1D(hEt_name.str().c_str(),hEt_name.str().c_str(), numbinsjet, minptjet, maxptjet);
  H_etajets_W[i] = new TH1D(heta_name.str().c_str(),heta_name.str().c_str(),26, -5.2, 5.2);
  H_phijets_W[i] = new TH1D(hphi_name.str().c_str(),hphi_name.str().c_str(),36, -M_PI, M_PI);
}

// Bin labels.
for(int i=1; i!=11; ++i) {
  sprintf(name,"%i",i-1);
  H_tnumJets_W->GetXaxis()->SetBinLabel(i, name);
 }
// *********************************************

hOutputFile->cd("Zjets");
H_tnumJets_Z    = new TH1D( "njets_total_Z", "Total number of jets", 10, 0, 10 );
H_tbarrel_Z     = new TH1D( "perc_barrel_Z", "Perc. of jets in barrel", 55, 0., 1.1);
H_tendcap_Z     = new TH1D( "perc_endcap_Z", "Perc. of jets in endcap", 55, 0., 1.1);

H_pt_tJets_Z    = new TH1D( "pt_tJets_Z", "Pt dist. of total jets", numbinsjet, minptjet, maxptjet);
H_Et_tJets_Z    = new TH1D( "Et_tJets_Z", "Et dist. of total jets", numbinsjet, minptjet, maxptjet);
H_eta_tJets_Z   = new TH1D( "eta_tJets_Z", "Eta dist. of total jets", 26, -5.2, 5.2);
H_phi_tJets_Z   = new TH1D( "phi_tJets_Z", "Phi dist. of total jets", 36, -M_PI, M_PI);
H_m_tJets_Z     = new TH1D( "m_tJets_Z", "Mass dist. of total jets", 200, 0., 20.);
H_mcalc_tJets_Z = new TH1D( "mcalc_tJets_Z", "Calc. mass dist. of total jets", 210, -1., 20.);

H_Etjets_barrel_Z  = new TH1D( "Et_barrel_Z", "Et dist. of jets in barrel", numbinsjet, minptjet, maxptjet);
H_etajets_barrel_Z = new TH1D( "eta_barrel_Z", "Eta dist. of jets in barrel", 26, -5.2, 5.2);
H_phijets_barrel_Z = new TH1D( "phi_barrel_Z", "Phi dist. of jets in barrel", 36, -M_PI, M_PI);

H_Etjets_endcap_Z  = new TH1D( "Et_endcap_Z", "Et dist. of jets in endcap", numbinsjet, minptjet, maxptjet);
H_etajets_endcap_Z = new TH1D( "eta_endcap_Z", "Eta dist. of jets in endcap", 26, -5.2, 5.2);
H_phijets_endcap_Z = new TH1D( "phi_endcap_Z", "Phi dist. of jets in endcap", 36, -M_PI, M_PI);

H_ptV_dir_1j_Z  = new TH1D( "ptV_true_1j_Z", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_2j_Z  = new TH1D( "ptV_true_2j_Z", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_3j_Z  = new TH1D( "ptV_true_3j_Z", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_4j_Z  = new TH1D( "ptV_true_4j_Z", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_1j_Z  = new TH1D( "ptV_true_2mu_1j_Z", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_2j_Z  = new TH1D( "ptV_true_2mu_2j_Z", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_3j_Z  = new TH1D( "ptV_true_2mu_3j_Z", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_4j_Z  = new TH1D( "ptV_true_2mu_4j_Z", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);

H_ptV_mu_1j_Z  = new TH1D( "ptV_2mu_1j_Z", "Pt dist. V - 2mu >= 1j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_2j_Z  = new TH1D( "ptV_2mu_2j_Z", "Pt dist. V - 2mu >= 2j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_3j_Z  = new TH1D( "ptV_2mu_3j_Z", "Pt dist. V - 2mu >= 3j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_4j_Z  = new TH1D( "ptV_2mu_4j_Z", "Pt dist. V - 2mu >= 4j", numbinsboson, minptboson, maxptboson);

H_ptV_jets_1j_Z = new TH1D( "ptV_jets_1j_Z", "Pt dist. V - >= 1 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_2j_Z = new TH1D( "ptV_jets_2j_Z", "Pt dist. V - >= 2 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_3j_Z = new TH1D( "ptV_jets_3j_Z", "Pt dist. V - >= 3 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_4j_Z = new TH1D( "ptV_jets_4j_Z", "Pt dist. V - >= 4 jet", numbinsboson, minptboson, maxptboson);

H_ptV_mumet_Z   = new TH1D( "ptV_mumet_Z", "Pt dist. V - mu+MET", numbinsboson, minptboson, maxptboson);

H_pt1stmu_1j_Z  = new TH1D( "pt1stmu_1j_Z", "Pt dist. 1stmu >= 1j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_1j_Z = new TH1D( "eta1stmu_1j_Z", "Eta dist. 1stmu >= 1j", 26, -5.2, 5.2);
H_pt2ndmu_1j_Z  = new TH1D( "pt2ndmu_1j_Z", "Pt dist. 2ndmu >= 1j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_1j_Z = new TH1D( "eta2ndmu_1j_Z", "Eta dist. 2ndmu >= 1j", 26, -5.2, 5.2);
H_pt1stmu_2j_Z  = new TH1D( "pt1stmu_2j_Z", "Pt dist. 1stmu >= 2j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_2j_Z = new TH1D( "eta1stmu_2j_Z", "Eta dist. 1stmu >= 2j", 26, -5.2, 5.2);
H_pt2ndmu_2j_Z  = new TH1D( "pt2ndmu_2j_Z", "Pt dist. 2ndmu >= 2j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_2j_Z = new TH1D( "eta2ndmu_2j_Z", "Eta dist. 2ndmu >= 2j", 26, -5.2, 5.2);
H_pt1stmu_3j_Z  = new TH1D( "pt1stmu_3j_Z", "Pt dist. 1stmu >= 3j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_3j_Z = new TH1D( "eta1stmu_3j_Z", "Eta dist. 1stmu >= 3j", 26, -5.2, 5.2);
H_pt2ndmu_3j_Z  = new TH1D( "pt2ndmu_3j_Z", "Pt dist. 2ndmu >= 3j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_3j_Z = new TH1D( "eta2ndmu_3j_Z", "Eta dist. 2ndmu >= 3j", 26, -5.2, 5.2);
H_pt1stmu_4j_Z  = new TH1D( "pt1stmu_4j_Z", "Pt dist. 1stmu >= 4j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_4j_Z = new TH1D( "eta1stmu_4j_Z", "Eta dist. 1stmu >= 4j", 26, -5.2, 5.2);
H_pt2ndmu_4j_Z  = new TH1D( "pt2ndmu_4j_Z", "Pt dist. 2ndmu >= 4j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_4j_Z = new TH1D( "eta2ndmu_4j_Z", "Eta dist. 2ndmu >= 4j", 26, -5.2, 5.2);

H_transvmass_1j_Z = new TH1D( "transvmass_1j_Z", "Transv. mass >= 1j", 50, 0., 150.);
H_transvmass_2j_Z = new TH1D( "transvmass_2j_Z", "Transv. mass >= 2j", 50, 0., 150.);
H_transvmass_3j_Z = new TH1D( "transvmass_3j_Z", "Transv. mass >= 3j", 50, 0., 150.);
H_transvmass_4j_Z = new TH1D( "transvmass_4j_Z", "Transv. mass >= 4j", 50, 0., 150.);

H_invmass_mumet_Z  = new TH1D( "invmass_mumet_Z", "Inv. mass V mu MET", 100, 0., 200.);
H_invmass_2mu_Z  = new TH1D( "invmass_2mu_Z", "Inv. mass V 2 mu", 100, 0., 200.);
H_invmass_mu12_Z = new TH1D( "invmass_mu12_Z", "Inv. mass V mu12", 100, 0., 200.);
H_invmass_mu13_Z = new TH1D( "invmass_mu13_Z", "Inv. mass V mu13", 100, 0., 200.);
H_invmass_mu23_Z = new TH1D( "invmass_mu23_Z", "Inv. mass V mu23", 100, 0., 200.);

H_dphi_mu12_Z   = new TH1D( "dphi_mu12_Z", "Delta phi V mu12", 36, -M_PI, M_PI);
H_dphi_mu13_Z   = new TH1D( "dphi_mu13_Z", "Delta phi V mu13", 36, -M_PI, M_PI);
H_dphi_mu23_Z   = new TH1D( "dphi_mu23_Z", "Delta phi V mu23", 36, -M_PI, M_PI);
  
H_ptnu_direct_Z = new TH1D( "ptnu_true_Z", "Pt dist. nu - true", numbinslepton, minptlepton, maxptlepton);
H_ptnu_dirl_Z   = new TH1D( "ptnu_true_1mu_Z", "Pt dist. nu - true", numbinslepton, minptlepton, maxptlepton);
H_ptnu_jlep_Z   = new TH1D( "ptnu_jet_1mu_Z", "Pt dist. nu - jets and l", numbinslepton, minptlepton, maxptlepton);
H_pt_met_Z      = new TH1D( "pt_met_Z", "Pt dist. nu - MET", numbinslepton, minptlepton, maxptlepton);
H_eff_Z         = new TH1D( "efficiency_Z", "0=bar, 1=end, 2=fwd", 3, 0, 3);

H_Etjets_Z.resize(maxnumjets);
H_etajets_Z.resize(maxnumjets);
H_phijets_Z.resize(maxnumjets);

for (int i=0; i!=maxnumjets; ++i) {
  hEt_name.str("");
  heta_name.str("");
  hphi_name.str("");
  hEt_name << "jet_Et_" << (i+1) << "o_Z";
  heta_name << "jet_eta_" << (i+1) << "o_Z";
  hphi_name << "jet_phi_" << (i+1) << "o_Z";
  H_Etjets_Z[i] = new TH1D(hEt_name.str().c_str(),hEt_name.str().c_str(), numbinsjet, minptjet, maxptjet);
  H_etajets_Z[i] = new TH1D(heta_name.str().c_str(),heta_name.str().c_str(),26, -5.2, 5.2);
  H_phijets_Z[i] = new TH1D(hphi_name.str().c_str(),hphi_name.str().c_str(),36, -M_PI, M_PI);
}

// Bin labels.
for(int i=1; i!=11; ++i) {
  sprintf(name,"%i",i-1);
  H_tnumJets_Z->GetXaxis()->SetBinLabel(i, name);
}
// *********************************************

hOutputFile->cd("ttjets");
H_tnumJets_tt    = new TH1D( "njets_total_tt", "Total number of jets", 10, 0, 10 );
H_tbarrel_tt     = new TH1D( "perc_barrel_tt", "Perc of jets in barrel", 55, 0., 1.1);
H_tendcap_tt     = new TH1D( "perc_endcap_tt", "Perc of jets in endcap", 55, 0., 1.1);

H_pt_tJets_tt    = new TH1D( "pt_tJets_tt", "Pt dist. of total jets", numbinsjet, minptjet, maxptjet);
H_Et_tJets_tt    = new TH1D( "Et_tJets_tt", "Et dist. of total jets", numbinsjet, minptjet, maxptjet);
H_eta_tJets_tt   = new TH1D( "eta_tJets_tt", "Eta dist. of total jets", 26, -5.2, 5.2);
H_phi_tJets_tt   = new TH1D( "phi_tJets_tt", "Phi dist. of total jets", 36, -M_PI, M_PI);
H_m_tJets_tt     = new TH1D( "m_tJets_tt", "Mass dist. of total jets", 200, 0., 20.);
H_mcalc_tJets_tt = new TH1D( "mcalc_tJets_tt", "Calc. mass dist. of total jets", 210, -1., 20.);

H_Etjets_barrel_tt  = new TH1D( "Et_barrel_tt", "Et dist. of jets in barrel", numbinsjet, minptjet, maxptjet);
H_etajets_barrel_tt = new TH1D( "eta_barrel_tt", "Eta dist. of jets in barrel", 26, -5.2, 5.2);
H_phijets_barrel_tt = new TH1D( "phi_barrel_tt", "Phi dist. of jets in barrel", 36, -M_PI, M_PI);

H_Etjets_endcap_tt  = new TH1D( "Et_endcap_tt", "Et dist. of jets in endcap", numbinsjet, minptjet, maxptjet);
H_etajets_endcap_tt = new TH1D( "eta_endcap_tt", "Eta dist. of jets in endcap", 26, -5.2, 5.2);
H_phijets_endcap_tt = new TH1D( "phi_endcap_tt", "Phi dist. of jets in endcap", 36, -M_PI, M_PI);

H_ptV_dir_1j_tt  = new TH1D( "ptV_true_1j_tt", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_2j_tt  = new TH1D( "ptV_true_2j_tt", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_3j_tt  = new TH1D( "ptV_true_3j_tt", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_4j_tt  = new TH1D( "ptV_true_4j_tt", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_1j_tt  = new TH1D( "ptV_true_2mu_1j_tt", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_2j_tt  = new TH1D( "ptV_true_2mu_2j_tt", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_3j_tt  = new TH1D( "ptV_true_2mu_3j_tt", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dirmu_4j_tt  = new TH1D( "ptV_true_2mu_4j_tt", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);

H_ptV_mu_1j_tt  = new TH1D( "ptV_2mu_1j_tt", "Pt dist. V - 2mu >= 1j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_2j_tt  = new TH1D( "ptV_2mu_2j_tt", "Pt dist. V - 2mu >= 2j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_3j_tt  = new TH1D( "ptV_2mu_3j_tt", "Pt dist. V - 2mu >= 3j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_4j_tt  = new TH1D( "ptV_2mu_4j_tt", "Pt dist. V - 2mu >= 4j", numbinsboson, minptboson, maxptboson);

H_ptV_jets_1j_tt = new TH1D( "ptV_jets_1j_tt", "Pt dist. V - >= 1 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_2j_tt = new TH1D( "ptV_jets_2j_tt", "Pt dist. V - >= 2 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_3j_tt = new TH1D( "ptV_jets_3j_tt", "Pt dist. V - >= 3 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_4j_tt = new TH1D( "ptV_jets_4j_tt", "Pt dist. V - >= 4 jet", numbinsboson, minptboson, maxptboson);

H_ptV_mumet_tt   = new TH1D( "ptV_mumet_tt", "Pt dist. V - mu+MET", numbinsboson, minptboson, maxptboson);

H_pt1stmu_1j_tt  = new TH1D( "pt1stmu_1j_tt", "Pt dist. 1stmu >= 1j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_1j_tt = new TH1D( "eta1stmu_1j_tt", "Eta dist. 1stmu >= 1j", 26, -5.2, 5.2);
H_pt2ndmu_1j_tt  = new TH1D( "pt2ndmu_1j_tt", "Pt dist. 2ndmu >= 1j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_1j_tt = new TH1D( "eta2ndmu_1j_tt", "Eta dist. 2ndmu >= 1j", 26, -5.2, 5.2);
H_pt1stmu_2j_tt  = new TH1D( "pt1stmu_2j_tt", "Pt dist. 1stmu >= 2j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_2j_tt = new TH1D( "eta1stmu_2j_tt", "Eta dist. 1stmu >= 2j", 26, -5.2, 5.2);
H_pt2ndmu_2j_tt  = new TH1D( "pt2ndmu_2j_tt", "Pt dist. 2ndmu >= 2j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_2j_tt = new TH1D( "eta2ndmu_2j_tt", "Eta dist. 2ndmu >= 2j", 26, -5.2, 5.2);
H_pt1stmu_3j_tt  = new TH1D( "pt1stmu_3j_tt", "Pt dist. 1stmu >= 3j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_3j_tt = new TH1D( "eta1stmu_3j_tt", "Eta dist. 1stmu >= 3j", 26, -5.2, 5.2);
H_pt2ndmu_3j_tt  = new TH1D( "pt2ndmu_3j_tt", "Pt dist. 2ndmu >= 3j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_3j_tt = new TH1D( "eta2ndmu_3j_tt", "Eta dist. 2ndmu >= 3j", 26, -5.2, 5.2);
H_pt1stmu_4j_tt  = new TH1D( "pt1stmu_4j_tt", "Pt dist. 1stmu >= 4j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_4j_tt = new TH1D( "eta1stmu_4j_tt", "Eta dist. 1stmu >= 4j", 26, -5.2, 5.2);
H_pt2ndmu_4j_tt  = new TH1D( "pt2ndmu_4j_tt", "Pt dist. 2ndmu >= 4j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_4j_tt = new TH1D( "eta2ndmu_4j_tt", "Eta dist. 2ndmu >= 4j", 26, -5.2, 5.2);

H_transvmass_1j_tt = new TH1D( "transvmass_1j_tt", "Transv. mass >= 1j", 50, 0., 150.);
H_transvmass_2j_tt = new TH1D( "transvmass_2j_tt", "Transv. mass >= 2j", 50, 0., 150.);
H_transvmass_3j_tt = new TH1D( "transvmass_3j_tt", "Transv. mass >= 3j", 50, 0., 150.);
H_transvmass_4j_tt = new TH1D( "transvmass_4j_tt", "Transv. mass >= 4j", 50, 0., 150.);

H_invmass_mumet_tt  = new TH1D( "invmass_mumet_tt", "Inv. mass V mu MET", 100, 0., 200.);
H_invmass_2mu_tt  = new TH1D( "invmass_2mu_tt", "Inv. mass V 2 mu", 100, 0., 200.);
H_invmass_mu12_tt = new TH1D( "invmass_mu12_tt", "Inv. mass V mu12", 100, 0., 200.);
H_invmass_mu13_tt = new TH1D( "invmass_mu13_tt", "Inv. mass V mu13", 100, 0., 200.);
H_invmass_mu23_tt = new TH1D( "invmass_mu23_tt", "Inv. mass V mu23", 100, 0., 200.);

H_dphi_mu12_tt   = new TH1D( "dphi_mu12_tt", "Delta phi V mu12", 36, -M_PI, M_PI);
H_dphi_mu13_tt   = new TH1D( "dphi_mu13_tt", "Delta phi V mu13", 36, -M_PI, M_PI);
H_dphi_mu23_tt   = new TH1D( "dphi_mu23_tt", "Delta phi V mu23", 36, -M_PI, M_PI);
  
H_ptnu_direct_tt = new TH1D( "ptnu_true_tt", "Pt dist. nu - true", numbinslepton, minptlepton, maxptlepton);
H_ptnu_dirl_tt   = new TH1D( "ptnu_true_1mu_tt", "Pt dist. nu - true", numbinslepton, minptlepton, maxptlepton);
H_ptnu_jlep_tt   = new TH1D( "ptnu_jet_1mu_tt", "Pt dist. nu - jets and l", numbinslepton, minptlepton, maxptlepton);
H_pt_met_tt      = new TH1D( "pt_met_tt", "Pt dist. nu - MET", numbinslepton, minptlepton, maxptlepton);
H_eff_tt         = new TH1D( "efficiency_tt", "0=bar, 1=end, 2=fwd", 3, 0, 3);

H_Etjets_tt.resize(maxnumjets);
H_etajets_tt.resize(maxnumjets);
H_phijets_tt.resize(maxnumjets);

for (int i=0; i!=maxnumjets; ++i) {
  hEt_name.str("");
  heta_name.str("");
  hphi_name.str("");
  hEt_name << "jet_Et_" << (i+1) << "o_tt";
  heta_name << "jet_eta_" << (i+1) << "o_tt";
  hphi_name << "jet_phi_" << (i+1) << "o_tt";
  H_Etjets_tt[i] = new TH1D(hEt_name.str().c_str(),hEt_name.str().c_str(), numbinsjet, minptjet, maxptjet);
  H_etajets_tt[i] = new TH1D(heta_name.str().c_str(),heta_name.str().c_str(),26, -5.2, 5.2);
  H_phijets_tt[i] = new TH1D(hphi_name.str().c_str(),hphi_name.str().c_str(),36, -M_PI, M_PI);
}

// Bin labels.
for(int i=1; i!=11; ++i) {
  sprintf(name,"%i",i-1);
  H_tnumJets_tt->GetXaxis()->SetBinLabel(i, name);
}
// *********************************************
