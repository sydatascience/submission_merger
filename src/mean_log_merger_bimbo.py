from __future__ import division
__author__ = 'Vladimir Iglovikov'
'''
Merges prediction for https://www.kaggle.com/c/grupo-bimbo-inventory-demand competition


Expm1(Mean([Log1p(x), Log1p(y)]))
'''

import os
import numpy as np
import sys
import pandas as pd
import time

files = sys.argv[1:]
try:
  files.remove('mean_log_merger_bimbo.py')
except:
  pass


data = [pd.read_csv(fName).sort_values(by='id') for fName in files]
ids = data[0]['id']

result = pd.DataFrame()
submission = pd.DataFrame()

ind = 0
for df in data:
  result[ind] = np.log1p(df['Demanda_uni_equil'])
  ind += 1

submission['Demanda_uni_equil'] = np.expm1(result.mean(axis=1))
submission['id'] = ids

submission.to_csv('{timestamp}.csv'.format(timestamp=time.time()), index=False)