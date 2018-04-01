import ROOT
import csv

nEvents = 100000

def read_file():
    #Open input file.
    input_file = ROOT.TFile("Brunel_BdJPsiKs_MagU_30k.root")
    dir = input_file.Get("ToolSvc.PatDebugTTTruthTool")
    tree = dir.Get("DownstreamSeedDebugTuple")
    #Open output file.
    with open("dsdt.csv", "wb") as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #Read data from tree.
        for i, event in enumerate(tree):
            writer.writerow([event.seed_chi2PerDoF, event.seed_nbIT, event.seed_nLayers, event.seed_nLHCbIDs, event.seed_p,
            event.seed_pt, event.seed_tx, event.seed_ty, event.seed_x, event.seed_y, event.is_downstream_reconstructible])
            if i > nEvents:
                break
if __name__ == "__main__":
    read_file()
