/**********************************************************************************************************************
COMP: g++ -std=c++1z -I `root-config --incdir` writeToFile.cpp -o writeToFile `root-config --libs` -l TreePlayer
Still works very slow, here's why:
"The TTree stores the entries each branch in baskets that contain usually many entries. Those baskets are compressed.
At regular interval, the TTree will need to read a new basket (for a given branch) and decompress it. The only way to
get rid of this ‘slow’ down is to disable the compression when creating the file (but the file will be larger). "
~ https://root-forum.cern.ch/t/getentry-slow-readout-single-entry/14924
**********************************************************************************************************************/

#include <iostream>
#include <fstream>

#include <TFile.h>
#include <TTree.h>


void writeToFile(){

  srand(time(NULL));
  TFile* rootFile = new TFile("Brunel_BdJPsiKs_MagU_30k.root");
  TDirectoryFile* dir = (TDirectoryFile*)rootFile->Get("ToolSvc.PatDebugTTTruthTool");
  TTree* tree = (TTree*)dir->Get("DownstreamSeedDebugTuple");

  Bool_t          is_downstream_reconstructible;
  Double_t        seed_chi2PerDoF;
  Double_t        seed_p;
  Double_t        seed_pt;
  UInt_t          seed_nLHCbIDs;
  UInt_t          seed_nbIT;
  UInt_t          seed_nLayers;
  Double_t        seed_x;
  Double_t        seed_y;
  Double_t        seed_tx;
  Double_t        seed_ty;

  //Set up branches.
  tree->SetBranchAddress("is_downstream_reconstructible", &is_downstream_reconstructible);
  tree->SetBranchAddress("seed_chi2PerDoF", &seed_chi2PerDoF);
  tree->SetBranchAddress("seed_p", &seed_p);
  tree->SetBranchAddress("seed_pt", &seed_pt);
  tree->SetBranchAddress("seed_nLHCbIDs", &seed_nLHCbIDs);
  tree->SetBranchAddress("seed_nbIT", &seed_nbIT);
  tree->SetBranchAddress("seed_nLayers", &seed_nLayers);
  tree->SetBranchAddress("seed_x", &seed_x);
  tree->SetBranchAddress("seed_y", &seed_y);
  tree->SetBranchAddress("seed_tx", &seed_tx);
  tree->SetBranchAddress("seed_ty", &seed_ty);

  //Output file.
  std::fstream outputFile;
  outputFile.open("dsdt.csv");

  //Read all entries.
  Long64_t nEntries = tree->GetEntries();
  for(int i=0; i<nEntries; i++){
    std::cout << i << std::endl;
    tree->GetEntry(rand()%nEntries);
    outputFile << seed_chi2PerDoF << ',' << seed_nbIT << ',' << seed_nLayers << seed_nLHCbIDs << seed_p << ',' \
    << seed_pt << seed_tx << seed_ty << seed_x << seed_y << is_downstream_reconstructible << std::endl;
  }
  rootFile->Close();
  outputFile.close();
}

int main(){
  writeToFile();
}
