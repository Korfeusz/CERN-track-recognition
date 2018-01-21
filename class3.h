//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sun Jan 14 20:10:15 2018 by ROOT version 5.34/36
// from TTree chi2Tuple/chi2Tuple
// found on file: Brunel_BdJPsiKs_Magu_30k.root
//////////////////////////////////////////////////////////

#ifndef class3_h
#define class3_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class class3 {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Double_t        p;
   UInt_t          nHits;
   Double_t        chi2;
   Bool_t          AcceptCandidate;
   Bool_t          AddOverlapRegions;
   Bool_t          AddUHits;
   Bool_t          AddVHits;
   Bool_t          BeampipeCut;
   Bool_t          FitAndRemove;
   Bool_t          Preselection;
   Bool_t          ReconstructibleAsDown;
   Bool_t          ReconstructibleAsLong;
   Bool_t          addUHits;
   Bool_t          fisher;
   Bool_t          fitXProjection;
   Bool_t          fitXprojection;
   Bool_t          initEvent;
   Bool_t          seedClassifier;

   // List of branches
   TBranch        *b_p;   //!
   TBranch        *b_nHits;   //!
   TBranch        *b_chi2;   //!
   TBranch        *b_AcceptCandidate;   //!
   TBranch        *b_AddOverlapRegions;   //!
   TBranch        *b_AddUHits;   //!
   TBranch        *b_AddVHits;   //!
   TBranch        *b_BeampipeCut;   //!
   TBranch        *b_FitAndRemove;   //!
   TBranch        *b_Preselection;   //!
   TBranch        *b_ReconstructibleAsDown;   //!
   TBranch        *b_ReconstructibleAsLong;   //!
   TBranch        *b_addUHits;   //!
   TBranch        *b_fisher;   //!
   TBranch        *b_fitXProjection;   //!
   TBranch        *b_fitXprojection;   //!
   TBranch        *b_initEvent;   //!
   TBranch        *b_seedClassifier;   //!

   class3(TTree *tree=0);
   virtual ~class3();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   //virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef class3_cxx
class3::class3(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("Brunel_BdJPsiKs_Magu_30k.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("Brunel_BdJPsiKs_Magu_30k.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("Brunel_BdJPsiKs_Magu_30k.root:/ToolSvc.PatDebugTTTruthTool");
      dir->GetObject("chi2Tuple",tree);

   }
   Init(tree);
}

class3::~class3()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t class3::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t class3::LoadTree(Long64_t entry)
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

void class3::Init(TTree *tree)
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

   fChain->SetBranchAddress("p", &p, &b_p);
   fChain->SetBranchAddress("nHits", &nHits, &b_nHits);
   fChain->SetBranchAddress("chi2", &chi2, &b_chi2);
   fChain->SetBranchAddress("AcceptCandidate", &AcceptCandidate, &b_AcceptCandidate);
   fChain->SetBranchAddress("AddOverlapRegions", &AddOverlapRegions, &b_AddOverlapRegions);
   fChain->SetBranchAddress("AddUHits", &AddUHits, &b_AddUHits);
   fChain->SetBranchAddress("AddVHits", &AddVHits, &b_AddVHits);
   fChain->SetBranchAddress("BeampipeCut", &BeampipeCut, &b_BeampipeCut);
   fChain->SetBranchAddress("FitAndRemove", &FitAndRemove, &b_FitAndRemove);
   fChain->SetBranchAddress("Preselection", &Preselection, &b_Preselection);
   fChain->SetBranchAddress("ReconstructibleAsDown", &ReconstructibleAsDown, &b_ReconstructibleAsDown);
   fChain->SetBranchAddress("ReconstructibleAsLong", &ReconstructibleAsLong, &b_ReconstructibleAsLong);
   fChain->SetBranchAddress("addUHits", &addUHits, &b_addUHits);
   fChain->SetBranchAddress("fisher", &fisher, &b_fisher);
   fChain->SetBranchAddress("fitXProjection", &fitXProjection, &b_fitXProjection);
   fChain->SetBranchAddress("fitXprojection", &fitXprojection, &b_fitXprojection);
   fChain->SetBranchAddress("initEvent", &initEvent, &b_initEvent);
   fChain->SetBranchAddress("seedClassifier", &seedClassifier, &b_seedClassifier);
   Notify();
}

Bool_t class3::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void class3::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t class3::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef class3_cxx
