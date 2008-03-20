const double minptboson = 0.;
const double maxptboson = 500.;
const double minptjet = 0.;
const double maxptjet = 250.;
const double minptlepton = 0.;
const double maxptlepton = 250.;
const int numbinsboson = 100;
const int numbinsjet = 50;
const int numbinslepton = 50; 

const int maxnumjets = 3;

char name[256];
ostringstream hEt_name;
ostringstream heta_name;
ostringstream hphi_name;

H_etaWplus  = new TH1D( "Wplus_eta", "Eta dist W+", 26, -5.2, 5.2);
H_etaWminus = new TH1D( "Wminus_eta", "Eta dist W-", 26, -5.2, 5.2);

H_tnumJets    = new TH1D( "jets_num", "Total number of jets", 10, 0, 10 );
H_tbarrel     = new TH1D( "jets_perc_barrel", "Perc. of jets in barrel", 55, 0., 1.1);
H_tendcap     = new TH1D( "jets_perc_endcap", "Perc. of jets in endcap", 55, 0., 1.1);

H_Et_tJets    = new TH1D( "jets_Et", "Et dist. of total jets", numbinsjet, minptjet, maxptjet);
H_eta_tJets   = new TH1D( "jets_eta", "Eta dist. of total jets", 26, -5.2, 5.2);
H_phi_tJets   = new TH1D( "jets_phi", "Phi dist. of total jets", 36, -M_PI, M_PI);

H_Etjets_barrel  = new TH1D( "jets_Et_barrel", "Et dist. of jets in barrel", numbinsjet, minptjet, maxptjet);
H_etajets_barrel = new TH1D( "jets_eta_barrel", "Eta dist. of jets in barrel", 26, -5.2, 5.2);
H_phijets_barrel = new TH1D( "jets_phi_barrel", "Phi dist. of jets in barrel", 36, -M_PI, M_PI);

H_Etjets_endcap  = new TH1D( "jets_Et_endcap", "Et dist. of jets in endcap", numbinsjet, minptjet, maxptjet);
H_etajets_endcap = new TH1D( "jets_eta_endcap", "Eta dist. of jets in endcap", 26, -5.2, 5.2);
H_phijets_endcap = new TH1D( "jets_phi_endcap", "Phi dist. of jets in endcap", 36, -M_PI, M_PI);

H_ptV_dir_1j  = new TH1D( "V_pt_true_1j", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_2j  = new TH1D( "V_pt_true_2j", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_3j  = new TH1D( "V_pt_true_3j", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);
H_ptV_dir_4j  = new TH1D( "V_pt_true_4j", "Pt dist. V - true", numbinsboson, minptboson, maxptboson);

H_ptV_mumet_1j   = new TH1D( "V_pt_mumet_1j", "Pt dist. V - mu+MET >= 1j", numbinsboson, minptboson, maxptboson);
H_ptV_mumet_2j   = new TH1D( "V_pt_mumet_2j", "Pt dist. V - mu+MET >= 2j", numbinsboson, minptboson, maxptboson);
H_ptV_mumet_3j   = new TH1D( "V_pt_mumet_3j", "Pt dist. V - mu+MET >= 3j", numbinsboson, minptboson, maxptboson);
H_ptV_mumet_4j   = new TH1D( "V_pt_mumet_4j", "Pt dist. V - mu+MET >= 4j", numbinsboson, minptboson, maxptboson);

H_ptV_mu_1j  = new TH1D( "V_pt_2mu_1j", "Pt dist. V - 2mu >= 1j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_2j  = new TH1D( "V_pt_2mu_2j", "Pt dist. V - 2mu >= 2j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_3j  = new TH1D( "V_pt_2mu_3j", "Pt dist. V - 2mu >= 3j", numbinsboson, minptboson, maxptboson);
H_ptV_mu_4j  = new TH1D( "V_pt_2mu_4j", "Pt dist. V - 2mu >= 4j", numbinsboson, minptboson, maxptboson);

H_ptV_jets_1j = new TH1D( "V_pt_jets_1j", "Pt dist. V - >= 1 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_2j = new TH1D( "V_pt_jets_2j", "Pt dist. V - >= 2 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_3j = new TH1D( "V_pt_jets_3j", "Pt dist. V - >= 3 jet", numbinsboson, minptboson, maxptboson);
H_ptV_jets_4j = new TH1D( "V_pt_jets_4j", "Pt dist. V - >= 4 jet", numbinsboson, minptboson, maxptboson);

H_pt1stmu_1j  = new TH1D( "mu_pt1st_1j", "Pt dist. 1stmu >= 1j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_1j = new TH1D( "mu_eta1st_1j", "Eta dist. 1stmu >= 1j", 26, -5.2, 5.2);
H_pt2ndmu_1j  = new TH1D( "mu_pt2nd_1j", "Pt dist. 2ndmu >= 1j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_1j = new TH1D( "mu_eta2nd_1j", "Eta dist. 2ndmu >= 1j", 26, -5.2, 5.2);
H_pt1stmu_2j  = new TH1D( "mu_pt1st_2j", "Pt dist. 1stmu >= 2j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_2j = new TH1D( "mu_eta1st_2j", "Eta dist. 1stmu >= 2j", 26, -5.2, 5.2);
H_pt2ndmu_2j  = new TH1D( "mu_pt2nd_2j", "Pt dist. 2ndmu >= 2j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_2j = new TH1D( "mu_eta2nd_2j", "Eta dist. 2ndmu >= 2j", 26, -5.2, 5.2);
H_pt1stmu_3j  = new TH1D( "mu_pt1st_3j", "Pt dist. 1stmu >= 3j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_3j = new TH1D( "mu_eta1st_3j", "Eta dist. 1stmu >= 3j", 26, -5.2, 5.2);
H_pt2ndmu_3j  = new TH1D( "mu_pt2nd_3j", "Pt dist. 2ndmu >= 3j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_3j = new TH1D( "mu_eta2nd_3j", "Eta dist. 2ndmu >= 3j", 26, -5.2, 5.2);
H_pt1stmu_4j  = new TH1D( "mu_pt1st_4j", "Pt dist. 1stmu >= 4j", numbinslepton, minptlepton, maxptlepton);
H_eta1stmu_4j = new TH1D( "mu_eta1st_4j", "Eta dist. 1stmu >= 4j", 26, -5.2, 5.2);
H_pt2ndmu_4j  = new TH1D( "mu_pt2nd_4j", "Pt dist. 2ndmu >= 4j", numbinslepton, minptlepton, maxptlepton);
H_eta2ndmu_4j = new TH1D( "mu_eta2nd_4j", "Eta dist. 2ndmu >= 4j", 26, -5.2, 5.2);

H_transvmass_1j = new TH1D( "transvmass_1j", "Transv. mass >= 1j", 50, 0., 150.);
H_transvmass_2j = new TH1D( "transvmass_2j", "Transv. mass >= 2j", 50, 0., 150.);
H_transvmass_3j = new TH1D( "transvmass_3j", "Transv. mass >= 3j", 50, 0., 150.);
H_transvmass_4j = new TH1D( "transvmass_4j", "Transv. mass >= 4j", 50, 0., 150.);

H_invmass_2mu_1j  = new TH1D( "invmass_2mu_1j", "Inv. mass V 2 mu >= 1j", 100, 0., 200.);
H_invmass_2mu_2j  = new TH1D( "invmass_2mu_2j", "Inv. mass V 2 mu >= 1j", 100, 0., 200.);
H_invmass_2mu_3j  = new TH1D( "invmass_2mu_3j", "Inv. mass V 2 mu >= 1j", 100, 0., 200.);
H_invmass_2mu_4j  = new TH1D( "invmass_2mu_4j", "Inv. mass V 2 mu >= 1j", 100, 0., 200.);
  
H_ptnu_direct = new TH1D( "ptnu_true", "Pt dist. nu - true", numbinslepton, minptlepton, maxptlepton);
H_pt_met      = new TH1D( "pt_met", "Pt dist. nu - MET", numbinslepton, minptlepton, maxptlepton);
H_eff         = new TH1D( "efficiency", "0=bar, 1=end, 2=fwd", 3, 0, 3);

H_eventcounter = new TH1D("eventcounter", "Event counter", 1, 0., 1.);

H_Etjets.resize(maxnumjets);
H_etajets.resize(maxnumjets);
H_phijets.resize(maxnumjets);

for (int i=0; i!=maxnumjets; ++i) {
  hEt_name.str("");
  heta_name.str("");
  hphi_name.str("");
  hEt_name << "jet_Et_" << (i+1) << "o";
  heta_name << "jet_eta_" << (i+1) << "o";
  hphi_name << "jet_phi_" << (i+1) << "o";
  H_Etjets[i] = new TH1D(hEt_name.str().c_str(),hEt_name.str().c_str(), numbinsjet, minptjet, maxptjet);
  H_etajets[i] = new TH1D(heta_name.str().c_str(),heta_name.str().c_str(),26, -5.2, 5.2);
  H_phijets[i] = new TH1D(hphi_name.str().c_str(),hphi_name.str().c_str(),36, -M_PI, M_PI);
}

// Bin labels.
for(int i=1; i!=11; ++i) {
  sprintf(name,"%i",i-1);
  H_tnumJets->GetXaxis()->SetBinLabel(i, name);
 }
