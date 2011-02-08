void backgroundDataDriven (char* controlName, char* selectionName) {
  TFile* controlFile = TFile::Open(controlName); 
  TFile* selectionFile = TFile::Open(selectionName);
  TH1F* controlMETHisto = (TH1F*)controlFile->Get("plotMET/MET");
  TH1F* selectedMETHisto = (TH1F*)selectionFile->Get("plotMET/MET");
  double numControl = controlMETHisto->Integral();
  double numSelection = selectedMETHisto->Integral();
 
  double branchingRatioTauMu = 0.1736;
  double efficiencyVBTFTrueMuRecoMu = 0.76;
  double efficiencyVBTFTrueTauRecoMu = 0.45;
  double ratioWmuOverZInvisible = 1.387;
  double ratioElecOverTauSignal = 0.36;
  double ratioMuOverTauSignal = 0.45;

  
  double numWMuControl = numControl/(1.0+branchingRatioTauMu);
  double numWMuKinematicRegion = numWMuControl/efficiencyVBTFTrueMuRecoMu;
  double numZInvisibleSignal = numWMuKinematicRegion/ratioWmuOverZInvisible;
  double numWTauControl = numControl - numWMuControl;
  double numWTauSignal = numWTauControl/efficiencyVBTFTrueTauRecoMu;
  double numWElecSignal = numWTauSignal*ratioElecOverTauSignal;
  double numWMuSignal = numWTauSignal*ratioMuOverTauSignal;
  double totalBackground = numZInvisibleSignal + numWElecSignal + numWMuSignal + numWTauSignal;
  
  printf("Number of events in Signal Region: %g\n", numSelection);
  printf("Number of events in Control Region: %g\n", numControl);
  printf("Total background calculated from control is %g\n",totalBackground);
  printf("Total Z invisible = %g\n",numZInvisibleSignal);
  selectionFile->Close();
  controlFile->Close();
}

void backgroundDataDriven (char* controlAndSelectionName) {
  TFile* theFile = TFile::Open(controlAndSelectionName); 
  TH1F* controlMETHisto = (TH1F*)theFile->Get("plotMETControl/MET");
  TH1F* selectedMETHisto = (TH1F*)theFile->Get("plotMET/MET");
  double numControl = controlMETHisto->Integral();
  double numSelection = selectedMETHisto->Integral();
 
  double branchingRatioTauMu = 0.1736;
  double efficiencyVBTFTrueMuRecoMu = 0.70;
  double efficiencyVBTFTrueTauRecoMu = 0.42;
  double ratioWmuOverZInvisible = 1.807;
  double ratioElecOverTauSignal = 0.36;
  double ratioMuOverTauSignal = 0.45;

  
  double numWMuControl = numControl/(1.0+branchingRatioTauMu);
  double numWMuKinematicRegion = numWMuControl/efficiencyVBTFTrueMuRecoMu;
  double numZInvisibleSignal = numWMuKinematicRegion/ratioWmuOverZInvisible;
  double numWTauControl = numControl - numWMuControl;
  double numWTauSignal = numWTauControl/efficiencyVBTFTrueTauRecoMu;
  double numWElecSignal = numWTauSignal*ratioElecOverTauSignal;
  double numWMuSignal = numWTauSignal*ratioMuOverTauSignal;
  double totalBackground = numZInvisibleSignal + numWElecSignal + numWMuSignal + numWTauSignal;
  
  double errorNZinv = 1/TMath::Sqrt(numControl)*numZInvisibleSignal;

  printf("Number of events in Signal Region: %g\n", numSelection);
  printf("Number of events in Control Region: %g\n", numControl);
  printf("Total background calculated from control is %g\n",totalBackground);
  printf("Total Z invisible = %g +- %g\n",numZInvisibleSignal,errorNZinv);
  theFile->Close();
}
