void calculateTriggerEfficiency(char* filename, char* histoname1, char* histoname2)
{
  TFile* f = TFile::Open(filename);
  TH1F* histo1 = (TH1F*)f->Get(histoname1);
  TH1F* histo2 = (TH1F*)f->Get(histoname1);
  TH1F* histoIntegral1 = (TH1F*)histo1->Clone();
  TH1F* histoIntegral2 = (TH1F*)histo2->Clone();
  int nbins = histo1->GetNbinsX();
  
  for(int i=1; i<=nbins; ++i) {
    histoIntegral1->SetBinContent(i,histo1->Integral(i,nbins));
    histoIntegral2->SetBinContent(i,histo2->Integral(i,nbins));
  }
  
  TEfficiency* theEfficiency = new TEfficiency(*histoIntegral2,*histoIntegral1);

  theEfficiency->Draw();
}
