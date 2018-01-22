import numpy as np
from pymongo import MongoClient
import pprint

filt = {}
client = MongoClient()
runs = client.sacred.runs.find(filt)[client.sacred.runs.find(filt).count()-1]
for i in range( pprint.pprint (runs['info']['runs_info'] ):
    pprint.pprint (runs['info']['runs_info'][i])