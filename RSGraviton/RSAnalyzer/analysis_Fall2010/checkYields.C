void checkYields(char* fname) {
  TFile* f = TFile::Open(fname);
  TH1F* h_electrons = (TH1F*)f->Get("plotMETelectrons/MET");
  TH1F* h_muons = (TH1F*)f->Get("plotMETmuons/MET");
  TH1F* h_taus = (TH1F*)f->Get("plotMETtaus/MET");
  printf("Electrons:\t%i\nMuons:\t\t%i\nTaus:\t\t%i\n",h_electrons->GetEntries(),h_muons->GetEntries(),h_taus->GetEntries());
  f->Close();
}
