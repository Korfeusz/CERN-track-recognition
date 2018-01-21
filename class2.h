//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sun Jan 14 20:09:30 2018 by ROOT version 5.34/36
// from TTree DownstreamTrackDebugTuple/DownstreamTrackDebugTuple
// found on file: Brunel_BdJPsiKs_Magu_30k.root
//////////////////////////////////////////////////////////

#ifndef class2_h
#define class2_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class class2 {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Bool_t          is_true_track;
   Double_t        track_chi2;
   Double_t        track_displX;
   Double_t        track_displY;
   Double_t        track_errXMag;
   Double_t        track_errYMag;
   Double_t        track_isIgnored;
   Double_t        track_mvaValue;
   Double_t        track_nbHit;
   Double_t        track_p;
   Double_t        track_tx;
   Double_t        track_ty;
   Double_t        track_x;
   Double_t        track_y;
   Bool_t          is_true_seed;
   Double_t        seed_chi2PerDoF;
   Double_t        seed_p;
   Double_t        seed_pt;
   Double_t        seed_nLHCbIDs;
   Double_t        seed_nbIT;
   Double_t        seed_x;
   Double_t        seed_y;
   Double_t        seed_z;
   Double_t        seed_tx;
   Double_t        seed_ty;
   Bool_t          hasT;
   Bool_t          hasTT;
   Bool_t          hasVelo;
   Bool_t          isMomentumOver5GeV;

   // List of branches
   TBranch        *b_is_true_track;   //!
   TBranch        *b_track_chi2;   //!
   TBranch        *b_track_displX;   //!
   TBranch        *b_track_displY;   //!
   TBranch        *b_track_errXMag;   //!
   TBranch        *b_track_errYMag;   //!
   TBranch        *b_track_isIgnored;   //!
   TBranch        *b_track_mvaValue;   //!
   TBranch        *b_track_nbHit;   //!
   TBranch        *b_track_p;   //!
   TBranch        *b_track_tx;   //!
   TBranch        *b_track_ty;   //!
   TBranch        *b_track_x;   //!
   TBranch        *b_track_y;   //!
   TBranch        *b_is_true_seed;   //!
   TBranch        *b_seed_chi2PerDoF;   //!
   TBranch        *b_seed_p;   //!
   TBranch        *b_seed_pt;   //!
   TBranch        *b_seed_nLHCbIDs;   //!
   TBranch        *b_seed_nbIT;   //!
   TBranch        *b_seed_x;   //!
   TBranch        *b_seed_y;   //!
   TBranch        *b_seed_z;   //!
   TBranch        *b_seed_tx;   //!
   TBranch        *b_seed_ty;   //!
   TBranch        *b_hasT;   //!
   TBranch        *b_hasTT;   //!
   TBranch        *b_hasVelo;   //!
   TBranch        *b_isMomentumOver5GeV;   //!

   class2(TTree *tree=0);
   virtual ~class2();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef class2_cxx
class2::class2(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("Brunel_BdJPsiKs_Magu_30k.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("Brunel_BdJPsiKs_Magu_30k.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("Brunel_BdJPsiKs_Magu_30k.root:/ToolSvc.PatDebugTTTruthTool");
      dir->GetObject("DownstreamTrackDebugTuple",tree);

   }
   Init(tree);
}

class2::~class2()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t class2::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t class2::LoadTree(Long64_t entry)
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

void class2::Init(TTree *tree)
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

   fChain->SetBranchAddress("is_true_track", &is_true_track, &b_is_true_track);
   fChain->SetBranchAddress("track_chi2", &track_chi2, &b_track_chi2);
   fChain->SetBranchAddress("track_displX", &track_displX, &b_track_displX);
   fChain->SetBranchAddress("track_displY", &track_displY, &b_track_displY);
   fChain->SetBranchAddress("track_errXMag", &track_errXMag, &b_track_errXMag);
   fChain->SetBranchAddress("track_errYMag", &track_errYMag, &b_track_errYMag);
   fChain->SetBranchAddress("track_isIgnored", &track_isIgnored, &b_track_isIgnored);
   fChain->SetBranchAddress("track_mvaValue", &track_mvaValue, &b_track_mvaValue);
   fChain->SetBranchAddress("track_nbHit", &track_nbHit, &b_track_nbHit);
   fChain->SetBranchAddress("track_p", &track_p, &b_track_p);
   fChain->SetBranchAddress("track_tx", &track_tx, &b_track_tx);
   fChain->SetBranchAddress("track_ty", &track_ty, &b_track_ty);
   fChain->SetBranchAddress("track_x", &track_x, &b_track_x);
   fChain->SetBranchAddress("track_y", &track_y, &b_track_y);
   fChain->SetBranchAddress("is_true_seed", &is_true_seed, &b_is_true_seed);
   fChain->SetBranchAddress("seed_chi2PerDoF", &seed_chi2PerDoF, &b_seed_chi2PerDoF);
   fChain->SetBranchAddress("seed_p", &seed_p, &b_seed_p);
   fChain->SetBranchAddress("seed_pt", &seed_pt, &b_seed_pt);
   fChain->SetBranchAddress("seed_nLHCbIDs", &seed_nLHCbIDs, &b_seed_nLHCbIDs);
   fChain->SetBranchAddress("seed_nbIT", &seed_nbIT, &b_seed_nbIT);
   fChain->SetBranchAddress("seed_x", &seed_x, &b_seed_x);
   fChain->SetBranchAddress("seed_y", &seed_y, &b_seed_y);
   fChain->SetBranchAddress("seed_z", &seed_z, &b_seed_z);
   fChain->SetBranchAddress("seed_tx", &seed_tx, &b_seed_tx);
   fChain->SetBranchAddress("seed_ty", &seed_ty, &b_seed_ty);
   fChain->SetBranchAddress("hasT", &hasT, &b_hasT);
   fChain->SetBranchAddress("hasTT", &hasTT, &b_hasTT);
   fChain->SetBranchAddress("hasVelo", &hasVelo, &b_hasVelo);
   fChain->SetBranchAddress("isMomentumOver5GeV", &isMomentumOver5GeV, &b_isMomentumOver5GeV);
   Notify();
}

Bool_t class2::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void class2::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t class2::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef class2_cxx
