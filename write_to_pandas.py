import csv
import pandas as pd

df1 = pd.read_csv('dsdt.csv', names=['has_MCParticle', 'is_downstream_reconstructible', 'has_MCParticle_not_electron', 'is_downstream_reconstructible_not_electron', 'is_true_seed', 'seed_chi2PerDoF', 'seed_mva_value', 'seed_nbIT', 'seed_nLayers', 'seed_nLHCbIDs', 'seed_p', 'seed_pt', 'seed_tx', 'seed_ty', 'seed_x', 'seed_y'])
df2 = pd.read_csv('dtdt.csv', names=['hasT', 'hasTT', 'hasVelo', 'isMomentumOver5GeV', 'is_true_seed', 'is_true_track', 'seed_chi2PerDoF', 'seed_nbIT', 'seed_nLHCbIDs', 'seed_p', 'seed_pt', 'seed_tx', 'seed_ty', 'seed_x', 'seed_y', 'seed_z', 'track_chi2', 'track_displX', 'track_displY', 'track_errXMag', 'track_errYMag', 'track_isIgnored', 'track_mvaValue', 'track_nbHit', 'track_p', 'track_tx', 'track_ty', 'track_x', 'track_y'])
df3 = pd.read_csv('chi2.csv', names=['p', 'nHits', 'chi2', 'AcceptCandidate', 'AddOverlapRegions', 'AddUHits', 'AddVHits', 'BeampipeCut', 'FitAndRemove', 'Preselection', 'ReconstructibleAsDown', 'ReconstructibleAsLong', 'addUHits', 'fisher', 'fitXProjection', 'fitXprojection', 'initEvent', 'seedClassifier'])
