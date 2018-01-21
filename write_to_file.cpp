#include "class1.h"
#include "class2.h"
#include "class3.h"

using namespace std;

void write_to_file(){

	srand(time(NULL));
	cout<<"Hello World!"<<endl;
	
	TFile* f1 = new TFile("Brunel_BdJPsiKs_MagU_30k.root");

    TDirectoryFile* dir = (TDirectoryFile*)f1->Get("ToolSvc.PatDebugTTTruthTool");
    TTree* tree1 = (TTree*)dir->Get("DownstreamSeedDebugTuple");
    TTree* tree2 = (TTree*)dir->Get("DownstreamTrackDebugTuple");
    TTree* tree3 = (TTree*)dir->Get("chi2Tuple");

    class1 c1(tree1);
    class2 c2(tree2);
    class3 c3(tree3);

    
    fstream f2;
	fstream f3;
	fstream f4;	
    


    f2.open("dsdt.csv", ios::out|ios::trunc);
    f3.open("dtdt.csv",ios::out|ios::trunc);
    f4.open("chi2.csv",ios::out|ios::trunc );
    
    for(int i =0; i<1000; i++){
    	tree1->GetEntry(rand()%+2415201);
    	tree2->GetEntry(rand()%+3966795);
    	tree3->GetEntry(rand()%+1062635);
    	
    	f2<<c1.has_MCParticle<<","<<c1.is_downstream_reconstructible<<","<<c1.has_MCParticle_not_electron<<","
		<<c1.is_downstream_reconstructible_not_electron<<","<<c1.is_true_seed<<","<<c1.seed_chi2PerDoF<<","<<c1.seed_mva_value<<","<<c1.seed_nbIT<<","<<c1.seed_nLayers
		<<","<<c1.seed_nLHCbIDs<<","<<c1.seed_p<<","<<c1.seed_pt<<","<<c1.seed_tx<<","<<c1.seed_ty<<","<<c1.seed_x<<","<<c1.seed_y<<endl;
		
		f3<<c2.hasT<<","<<c2.hasTT<<","<<c2.hasVelo<<","<<c2.isMomentumOver5GeV<<","<<c2.is_true_seed<<","<<c2.is_true_track<<","<<c2.seed_chi2PerDoF<<","<<c2.seed_nbIT
		<<","<<c2.seed_nLHCbIDs<<","<<c2.seed_p<<","<<c2.seed_pt<<","<<c2.seed_tx<<","<<c2.seed_ty<<","<<c2.seed_x<<","<<c2.seed_y<<","<<c2.seed_z<<","<<c2.track_chi2
		<<","<<c2.track_displX<<","<<c2.track_displY<<","<<c2.track_errXMag<<","<<c2.track_errYMag<<","<<c2.track_isIgnored<<","<<c2.track_mvaValue<<","<<c2.track_nbHit
		<<","<<c2.track_p<<","<<c2.track_tx<<","<<c2.track_ty<<","<<c2.track_x<<","<<c2.track_y<<endl;
		
		f4<<c3.p<<","<<c3.nHits<<","<<c3.chi2<<","<<c3.AcceptCandidate<<","<<c3.AddOverlapRegions<<","<<c3.AddUHits
		<<","<<c3.AddVHits<<","<<c3.BeampipeCut<<","<<c3.FitAndRemove<<","<<c3.Preselection<<","
		<<c3.ReconstructibleAsDown<<","<<c3.ReconstructibleAsLong<<","<<c3.addUHits<<","<<c3.fisher<<","
		<<c3.fitXProjection<<","<<c3.fitXprojection<<","<<c3.initEvent<<","<<c3.seedClassifier<<endl;
		
		
    		
	}
    f2.close();
    f3.close();
    f4.close();
		
	
}
