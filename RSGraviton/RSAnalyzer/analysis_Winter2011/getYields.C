void getYields(char* fileName) {
  TFile* f = TFile::Open(fileName);
  TH1F* numeros = (TH1F*)f->Get("eventCounterOne/eventcounter");
  TH1F* h =(TH1F*)f->Get("plotMET/METpt");
  TH1F* h2 =(TH1F*)f->Get("plotMETControl/METpt");
  int numInitial = numeros->GetEntries();
  int num1 = h->GetEntries();
  int num2 = h2->GetEntries();
  printf("Starting from %i entries\n",numInitial);
  printf("%i entries in search and %i entries in control\n",num1,num2);
  f->Close();
}
