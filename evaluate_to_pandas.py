import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import math

def read_data(filepath='dsdt.csv'):
    cols1 = ['seed_chi2PerDoF', 'seed_nbIT', 'seed_nLayers', 'seed_nLHCbIDs', 'seed_p', 'seed_pt', 'seed_tx', 'seed_ty', 'seed_x', 'seed_y', 'is_downstream_reconstructible']
    result = pd.read_csv(filepath, names=cols1, index_col=False)
    #print(result)
    return result



def normalize_data(dat):
    x = dat.values
    cols = dat.columns.values.tolist()
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    dat_scaled = pd.DataFrame(x_scaled, columns=cols)
    return dat_scaled

def standardize_data(dat):
    x = dat.values
    cols = dat.columns.values.tolist()
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
    standarized = pd.DataFrame(x, columns=cols)
    return standarized




