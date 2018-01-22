import pandas as pd


def read_data(filepath='dsdt.csv'):
    cols1 = ['has_MCParticle', 'is_downstream_reconstructible', 'has_MCParticle_not_electron', 'is_downstream_reconstructible_not_electron', 'is_true_seed', 'seed_chi2PerDoF', 'seed_mva_value', 'seed_nbIT', 'seed_nLayers', 'seed_nLHCbIDs', 'seed_p', 'seed_pt', 'seed_tx', 'seed_ty', 'seed_x', 'seed_y']
    result = pd.read_csv(filepath, names=cols1, index_col=False)
    result = result[['seed_chi2PerDoF', 'seed_p', 'seed_pt', 'seed_nLHCbIDs' , 'seed_nbIT'  , 'seed_nLayers', 'seed_x' , 'seed_y' , 'seed_tx', 'seed_ty', 'is_downstream_reconstructible']]
    return result

