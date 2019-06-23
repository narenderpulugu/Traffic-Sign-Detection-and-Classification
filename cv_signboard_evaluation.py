# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:14:20 2019

@author: narender
"""


import glob
import os 

path = "/home/narender/spyder/vision_project"

complete_files = glob.glob(path + "/*")

class_list = ["circle", "triangle", "inverse_triangle","rectangle"]

folder_list = [file for file in complete_files if ".py" not in file] 

for cls in class_list:
    true_positives = 0
    true_negatives = 0
    false_positives = 0 
    false_negatives = 0
    
    for file in folder_list:
        label = file.split("/")[-1]
        image_files = os.listdir(file)
        for images in image_files:
            if images.startswith(cls):
                if images.startswith(label):
                    true_positives = true_positives + 1
                else :
                    false_positives = false_positives + 1
            else : 
                if images.startswith(label):
                    true_negatives = true_negatives + 1 
                    
                if cls == label and not images.startswith(label):
                    false_negatives =false_negatives + 1
                    
                    
    print(cls)                
    print('Precision: ', true_positives / float(true_positives + false_positives))
    print('Recall: ', true_positives / float(true_positives + false_negatives))
          