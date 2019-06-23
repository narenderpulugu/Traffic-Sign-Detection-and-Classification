# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:23:31 2019

@author: narender
"""

import pandas as pd
import os
from shutil import copyfile

csv_path = '/home/narender/Downloads/GT-final_test'
test_data_path = '/home/narender/Downloads/GTSRB/Final_Test/Images/'

test_labels_df = pd.read_csv(csv_path, delimiter=';')

class_dict = {3:'circle', 11:'triangle', 12:'rectangle', 13:'inverse_triangle'}

for ind in test_labels_df.index:
    sample = test_labels_df.iloc[ind]
    if sample['ClassId'] in [3, 11, 12, 13]:
        if not os.path.exists('./test'):
            os.mkdir('./test')
            
        if not os.path.exists('./test/{0}'.format(class_dict[sample['ClassId']])):
            os.mkdir('./test/{0}'.format(class_dict[sample['ClassId']]))
            
        filename = sample['Filename']
        
        filepath = test_data_path + filename
        
        dst = './test/{0}'.format(class_dict[sample['ClassId']]) + '/' + filename
        
        copyfile(filepath, dst)
            
        
            
    

ass