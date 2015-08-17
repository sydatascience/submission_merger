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
import math
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

files = sys.argv[1:]
try:
  files.remove('ICDM_merger.py')
except:
  pass

data = [pd.read_csv(fName) for fName in files]
ids = data[0]['device_id']

result = pd.DataFrame()
submission = pd.DataFrame()

ind = 0
for df in data:
  result[ind] = df['cookie_id'].apply(lambda x: x + ' ')
  ind += 1

def helper(x):
  result = list(set(x.strip().split()))
  result = ' '.join(result)
  return result

submission['cookie_id'] = result.sum()
submission['cookie_id'] = submission['cookie_id'].apply(helper, 1)

submission['device_id'] = ids

submission.to_csv('ICDM_{timestamp}.csv'.format(timestamp=time.time()), index=False)