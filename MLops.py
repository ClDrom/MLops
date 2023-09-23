# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:38:10 2023

@author: 142068
"""

import pandas as pd
import os
import glob

os.chdir(r'\\ad.univ-lille.fr\Etudiants\Homedir3\142068\Documents\DataMLops\MLops\batch')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


#combine all files in the list
for f in all_filenames:
    restoTemp = pd.read_csv(f)
    try :
        restoTemp['Order ID'] = restoTemp['Order Number']
    except KeyError:
        pass
    dbResto = pd.concat([restoTemp])
#export to csv
dbResto.to_csv( "combined_csv.csv", index=False)



