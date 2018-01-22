#define class1_cxx
#include "class1.h"


using namespace std;

void write_to_file(){
	
	srand(time(NULL));
	cout<<"Hello World!"<<endl;
	
	TFile* f1 = new TFile("Brunel_BdJPsiKs_MagU_30k.root");

    TDirectoryFile* dir = (TDirectoryFile*)f1->Get("ToolSvc.PatDebugTTTruthTool");
    TTree* tree1 = (TTree*)dir->Get("DownstreamSeedDebugTuple");
  
    class1 c1(tree1);
    
    fstream f2;
    f2.open("dsdt.csv", ios::out|ios::trunc);
  
    for(int i =0; i<1000; i++){
    	tree1->GetEntry(rand()%2415201);
    	
    	
    	f2<<c1.seed_chi2PerDoF<<","<<c1.seed_nbIT<<","<<c1.seed_nLayers
		<<","<<c1.seed_nLHCbIDs<<","<<c1.seed_p<<","<<c1.seed_pt<<","<<c1.seed_tx<<","<<c1.seed_ty<<","<<c1.seed_x<<","<<c1.seed_y<<","<<c1.is_downstream_reconstructible<<endl;
		
				
    		
	}
    f2.close();

		
	
}
