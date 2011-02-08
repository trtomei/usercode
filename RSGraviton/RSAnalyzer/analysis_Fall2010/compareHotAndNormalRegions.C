void comparison(char* name) {
  char buffer[256];
    
  TCanvas* cv = new TCanvas("cv","cv",600,600);

  sprintf (buffer,"plotHotJets/%s",name);
  TH1F* hot = (TH1F*)_file0->Get(buffer);
  hot->SetLineWidth(2);
  hot->SetLineColor(kRed);
  //hot->Rebin(2);
  hot->Scale(1.0/hot->Integral());
  
  hot->Draw();
  gPad->Update();
  TPaveStats* ps1 = (TPaveStats*)hot->FindObject("stats");
  ps1->SetX1NDC(0.4); ps1->SetX2NDC(0.6);
  ps1->SetTextColor(kRed);

  sprintf(buffer,"plotNormalJets/%s",name);
  TH1F* normal = (TH1F*)_file0->Get(buffer);
  normal->SetLineWidth(2);
  //normal->Rebin(2);
  normal->Scale(1.0/normal->Integral());
  normal->Draw("sames");
  gPad->Update();
  TPaveStats* ps2 = (TPaveStats*)normal->FindObject("stats");
  ps2->SetX1NDC(0.65); ps2->SetX2NDC(0.85);
  gPad->Update();
  cv->Modified();
}
  
