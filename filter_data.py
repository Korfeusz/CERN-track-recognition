import csv
import pandas as pd
import sys
import json
cols1 = ['has_MCParticle', 'is_downstream_reconstructible', 'has_MCParticle_not_electron', 'is_downstream_reconstructible_not_electron', 'is_true_seed', 'seed_chi2PerDoF', 'seed_mva_value', 'seed_nbIT', 'seed_nLayers', 'seed_nLHCbIDs', 'seed_p', 'seed_pt', 'seed_tx', 'seed_ty', 'seed_x', 'seed_y']
cols2 = ['hasT', 'hasTT', 'hasVelo', 'isMomentumOver5GeV', 'is_true_seed', 'is_true_track', 'seed_chi2PerDoF', 'seed_nbIT', 'seed_nLHCbIDs', 'seed_p', 'seed_pt', 'seed_tx', 'seed_ty', 'seed_x', 'seed_y', 'seed_z', 'track_chi2', 'track_displX', 'track_displY', 'track_errXMag', 'track_errYMag', 'track_isIgnored', 'track_mvaValue', 'track_nbHit', 'track_p', 'track_tx', 'track_ty', 'track_x', 'track_y']
cols3 = ['p', 'nHits', 'chi2', 'AcceptCandidate', 'AddOverlapRegions', 'AddUHits', 'AddVHits', 'BeampipeCut', 'FitAndRemove', 'Preselection', 'ReconstructibleAsDown', 'ReconstructibleAsLong', 'addUHits', 'fisher', 'fitXProjection', 'fitXprojection', 'initEvent', 'seedClassifier']

df1 = pd.read_csv('dsdt.csv', names=cols1, index_col=False)
df2 = pd.read_csv('dtdt.csv', names=cols2, index_col=False)
df3 = pd.read_csv('chi2.csv', names=cols3, index_col=False)

print ('You have three dataframes to access.')
print ('Dataframe number 1 (DownstreamSeedDebugTuple): ')
print (cols1)
print ('Dataframe number 2 (DownstreamTrackDebugTuple): ')
print (cols2)
print ('Dataframe number 3 (chi2Tuple): ')
print (cols3)
number = int(input('Please insert the number of the dataframe you want to filter: '))
if number == 1:
    dataframe = df1
elif number == 2:
    dataframe = df2
elif number == 3:
    dataframe = df3
else:
    print('This dataframe does not exist. Please input another number.')
    sys.exit()



json_data = input('Please input a dictionary of the variables you want to filter for and their values: ')
my_dict=json.loads(json_data)

for key,value in my_dict.items():
    print(key + str(value))


for index, row in dataframe.iterrows():
   criterion = True
   for key, value in my_dict:
       if row[key] != value:
           criterion = False
   if criterion == True:
       print(index)


