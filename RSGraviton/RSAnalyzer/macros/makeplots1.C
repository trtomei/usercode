#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <utility>
#include "TH1.h"
#include "TH2.h"
#include "TProfile.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TStyle.h"

void makeplots1(string fname) {

  using namespace std;

  gROOT->SetStyle("Plain");      // Switches off the ROOT default style
  gStyle->SetMarkerStyle(20);
  gStyle->SetMarkerSize(0.7);
  gStyle->SetHistLineWidth(2);
  //  gStyle->SetOptStat(0);
  gROOT->ForceStyle();
  gStyle->SetStatH(0.8*gStyle->GetStatH());
  gStyle->SetStatH(0.8*gStyle->GetStatH());

  char name[256];
  sprintf(name, "%s", fname.c_str());
  
  string strippedfname;
  strippedfname = fname.substr(0,fname.size()-5);
  
  TFile* f = TFile::Open(name);
  
  TH1F* histo;
  TProfile* profile;
  TH2F* histo2d;
  TCanvas* cv = new TCanvas("cv","",200,10,700,500);

  histo = (TH1F*) f->Get("dR");
  histo->GetXaxis()->SetRangeUser(0.,6.);
  histo->GetXaxis()->SetTitle("dR");
  histo->Draw();
  sprintf(name, "%s/dR.png", strippedfname.c_str());
  cv->SaveAs(name);

  histo = (TH1F*) f->Get("jet1Particles");
  histo->GetXaxis()->SetRangeUser(0.,150.);
  histo->GetXaxis()->SetTitle("Number of particles");
  histo->Draw();
  sprintf(name, "%s/jet1Particles.png", strippedfname.c_str());
  cv->SaveAs(name);
  
  histo = (TH1F*) f->Get("jet2Particles");
  histo->GetXaxis()->SetRangeUser(0.,150.);
  histo->GetXaxis()->SetTitle("Number of particles");
  histo->Draw();
  sprintf(name, "%s/jet2Particles.png", strippedfname.c_str());
  cv->SaveAs(name);
  
  histo = (TH1F*) f->Get("Jet1dRTwoParticles");
  histo->GetXaxis()->SetTitle("dR");
  histo->Draw();
  sprintf(name, "%s/Jet1dRTwoParticles.png", strippedfname.c_str());
  cv->SaveAs(name);
  
  histo = (TH1F*) f->Get("Jet1dRJetParticle");
  histo->GetXaxis()->SetTitle("dR");
  histo->Draw();
  sprintf(name, "%s/jet1dRJetParticle.png", strippedfname.c_str());
  cv->SaveAs(name);
  
  histo = (TH1F*) f->Get("Jet2dRTwoParticles");
  histo->GetXaxis()->SetTitle("dR");
  histo->Draw();
  sprintf(name, "%s/Jet2dRTwoParticles.png", strippedfname.c_str());
  cv->SaveAs(name);
  
  histo = (TH1F*) f->Get("Jet2dRJetParticle");
  histo->GetXaxis()->SetTitle("dR");
  histo->Draw();
  sprintf(name, "%s/jet2dRJetParticle.png", strippedfname.c_str());
  cv->SaveAs(name);

  profile = (TProfile*) f->Get("jet1Density");
  profile->GetXaxis()->SetTitle("radius");
  profile->GetYaxis()->SetTitle("Sum E_{T} / (E_{T}*radius)");
  profile->Draw();
  sprintf(name, "%s/jet1Density.png", strippedfname.c_str());
  cv->SaveAs(name);

  profile = (TProfile*) f->Get("jet2Density");
  profile->GetXaxis()->SetTitle("radius");
  profile->GetYaxis()->SetTitle("Sum E_{T} / (E_{T}*radius)");
  profile->Draw();
  sprintf(name, "%s/jet2Density.png", strippedfname.c_str());
  cv->SaveAs(name);

  gStyle->SetPalette(1);

  gStyle->SetStatX(0.85);
  histo2d = (TH2F*) f->Get("etaCorrelation");
  histo2d->GetXaxis()->SetTitle("#eta jet 1");
  histo2d->GetYaxis()->SetTitle("#eta jet 2");
  histo2d->Rebin2D();
  histo2d->Draw("contz");
  sprintf(name, "%s/etaCorrelation.png", strippedfname.c_str());
  cv->SaveAs(name);

  gStyle->SetStatX(0.5);
  histo2d = (TH2F*) f->Get("etCorrelation");
  histo2d->GetXaxis()->SetTitle("E_{T} jet 1");
  histo2d->GetYaxis()->SetTitle("E_{T} jet 2");
  histo2d->Rebin2D();
  histo2d->GetXaxis()->SetRangeUser(0.,600.);
  histo2d->GetYaxis()->SetRangeUser(0.,600.);
  histo2d->Draw("contz");
  sprintf(name, "%s/etCorrelation.png", strippedfname.c_str());
  cv->SaveAs(name);
  
  gStyle->SetStatX(0.5);
  profile = (TProfile*) f->Get("jet1Etprofile");
  profile->GetXaxis()->SetTitle("radius");
  profile->GetYaxis()->SetTitle("Sum E_{T} / E_{T}");
  profile->Draw();
  sprintf(name, "%s/jet1Etprofile.png", strippedfname.c_str());
  cv->SaveAs(name);

  gStyle->SetStatX(0.5);
  profile = (TProfile*) f->Get("jet2Etprofile");
  profile->GetXaxis()->SetTitle("radius");
  profile->GetYaxis()->SetTitle("Sum E_{T} / E_{T}");
  profile->Draw();
  sprintf(name, "%s/jet2Etprofile.png", strippedfname.c_str());
  cv->SaveAs(name);

  gStyle->SetStatX(0.75);
  histo = (TH1F*) f->Get("dPhi");
  histo->GetXaxis()->SetTitle("d#phi");
  histo->Draw();
  sprintf(name, "%s/dPhi.png", strippedfname.c_str());
  cv->SaveAs(name);

  gStyle->SetStatX(0.85);
  histo2d = (TH2F*) f->Get("phiCorrelation");
  histo2d->GetXaxis()->SetTitle("#phi jet 1");
  histo2d->GetYaxis()->SetTitle("#phi jet 2");
  histo2d->Rebin2D();
  histo2d->Rebin2D();
  histo2d->Draw("contz");
  sprintf(name, "%s/phiCorrelation.png", strippedfname.c_str());
  cv->SaveAs(name);

  gStyle->SetStatX(0.5);
  histo2d = (TH2F*) f->Get("massCorrelation");
  histo2d->GetXaxis()->SetTitle("mass jet 1");
  histo2d->GetYaxis()->SetTitle("mass jet 2");
  histo2d->Rebin2D();
  histo2d->GetXaxis()->SetRangeUser(0.,140.);
  histo2d->GetYaxis()->SetRangeUser(0.,140.);
  histo2d->Draw("contz");
  sprintf(name, "%s/massCorrelation.png", strippedfname.c_str());
  cv->SaveAs(name);
  
  delete cv;
}
