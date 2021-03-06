from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
This scripts merges several csv files that are used to perform Kaggle submission

It performs average
'''

import os
import sys
import pandas as pd
import time

files = sys.argv[1:]
try:
  files.remove('mean_merger_taxi.py')
except:
  pass


data = [pd.read_csv(fName) for fName in files]
ids = data[0]['TRIP_ID']

result  = pd.DataFrame()
submission = pd.DataFrame()

ind = 0
for df in data:
  result[ind] = df['TRAVEL_TIME']
  ind += 1

submission['TRAVEL_TIME'] = result.mean(axis=1)
submission['TRIP_ID'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)