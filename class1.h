//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sun Jan 14 20:07:13 2018 by ROOT version 5.34/36
// from TTree DownstreamSeedDebugTuple/DownstreamSeedDebugTuple
// found on file: Brunel_BdJPsiKs_Magu_30k.root
//////////////////////////////////////////////////////////

#ifndef class1_h
#define class1_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TRandom3.h>
#include <TNtuple.h>
#include <TH1F.h>
#include <TLegend.h>
#include <TF1.h>
#include <TTree.h>
#include <TH1D.h>
#include <TLorentzVector.h>s
#include<TDirectoryFile.h>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class class1 {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Bool_t          has_MCParticle;
   Bool_t          is_downstream_reconstructible;
   Bool_t          has_MCParticle_not_electron;
   Bool_t          is_downstream_reconstructible_not_electron;
   Bool_t          is_true_seed;
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
   Double_t        seed_mva_value;

   // List of branches
   TBranch        *b_has_MCParticle;   //!
   TBranch        *b_is_downstream_reconstructible;   //!
   TBranch        *b_has_MCParticle_not_electron;   //!
   TBranch        *b_is_downstream_reconstructible_not_electron;   //!
   TBranch        *b_is_true_seed;   //!
   TBranch        *b_seed_chi2PerDoF;   //!
   TBranch        *b_seed_p;   //!
   TBranch        *b_seed_pt;   //!
   TBranch        *b_seed_nLHCbIDs;   //!
   TBranch        *b_seed_nbIT;   //!
   TBranch        *b_seed_nLayers;   //!
   TBranch        *b_seed_x;   //!
   TBranch        *b_seed_y;   //!
   TBranch        *b_seed_tx;   //!
   TBranch        *b_seed_ty;   //!
   TBranch        *b_seed_mva_value;   //!

   class1(TTree *tree=0);
   virtual ~class1();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
  // virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef class1_cxx
class1::class1(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("Brunel_BdJPsiKs_Magu_30k.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("Brunel_BdJPsiKs_Magu_30k.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("Brunel_BdJPsiKs_Magu_30k.root:/ToolSvc.PatDebugTTTruthTool");
      dir->GetObject("DownstreamSeedDebugTuple",tree);

   }
   Init(tree);
}

class1::~class1()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t class1::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t class1::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void class1::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("has_MCParticle", &has_MCParticle, &b_has_MCParticle);
   fChain->SetBranchAddress("is_downstream_reconstructible", &is_downstream_reconstructible, &b_is_downstream_reconstructible);
   fChain->SetBranchAddress("has_MCParticle_not_electron", &has_MCParticle_not_electron, &b_has_MCParticle_not_electron);
   fChain->SetBranchAddress("is_downstream_reconstructible_not_electron", &is_downstream_reconstructible_not_electron, &b_is_downstream_reconstructible_not_electron);
   fChain->SetBranchAddress("is_true_seed", &is_true_seed, &b_is_true_seed);
   fChain->SetBranchAddress("seed_chi2PerDoF", &seed_chi2PerDoF, &b_seed_chi2PerDoF);
   fChain->SetBranchAddress("seed_p", &seed_p, &b_seed_p);
   fChain->SetBranchAddress("seed_pt", &seed_pt, &b_seed_pt);
   fChain->SetBranchAddress("seed_nLHCbIDs", &seed_nLHCbIDs, &b_seed_nLHCbIDs);
   fChain->SetBranchAddress("seed_nbIT", &seed_nbIT, &b_seed_nbIT);
   fChain->SetBranchAddress("seed_nLayers", &seed_nLayers, &b_seed_nLayers);
   fChain->SetBranchAddress("seed_x", &seed_x, &b_seed_x);
   fChain->SetBranchAddress("seed_y", &seed_y, &b_seed_y);
   fChain->SetBranchAddress("seed_tx", &seed_tx, &b_seed_tx);
   fChain->SetBranchAddress("seed_ty", &seed_ty, &b_seed_ty);
   fChain->SetBranchAddress("seed_mva_value", &seed_mva_value, &b_seed_mva_value);
   Notify();
}

Bool_t class1::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void class1::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t class1::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef class1_cxx
