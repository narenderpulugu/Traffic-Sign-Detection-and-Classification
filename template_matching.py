# -*- coding: utf-8 -*-

import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import os
from scipy.signal import convolve2d as conv2
from skimage import color, data, restoration
import glob

template_path = "/home/narender/vision_templates/*ppm"
template_files = glob.glob(template_path)
template_list = [cv2.imread(filename, cv2.IMREAD_COLOR) for filename in template_files]

#for training Images.

circle_path = "/home/narender/spyder/test/circle"
triangle_path = "/home/narender/spyder/test/triangle"
rectangle_path = "/home/narender/spyder/test/rectangle"
inverse_triangle_path = "/home/narender/spyder/test/inverse_triangle"

images_path = [circle_path, triangle_path, rectangle_path, inverse_triangle_path]

#images_path = "/home/narender/Downloads/GTSRB/Final_Test/Images"

for path in images_path:
    image_list = glob.glob(path + "/*.ppm")
    
    for image in image_list:
        img_raw= cv2.imread(image, cv2.IMREAD_COLOR)
        img_raw = cv2.resize(img_raw, (32,32))
        img_gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)

        if np.mean(img_gray) < 40:
            img_gray = cv2.equalizeHist(img_gray)
            
        h,w = img_gray.shape
        
        best_value = None
        best_location = None
        best_particle_size_ratio = 0
        best_template_label = ""
        
        for ind, template in enumerate(template_list):
            templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
            templateGray = cv2.resize(templateGray, (32,32))
            template_height,template_width = templateGray.shape   
            #multi scale templates 
            for size in np.linspace(0.6,1,10)[::-1]:
                template_resize = cv2.resize(templateGray, (int(size * template_height), int(size*template_width)))
                #matching every template to the image and storing the best values    
                res = cv2.matchTemplate(img_gray,template_resize,cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                if best_value == None or best_value < max_val:
                    best_value = max_val
                    best_location = max_loc
                    best_particle_size_ratio = size
                    best_template_label = '_'.join(template_files[ind].split('/')[-1].split('_')[:-1])
                  
        
        print(best_location)
        top_left = best_location
        print(best_location)
        best_template = cv2.resize(templateGray, (int(template_width* best_particle_size_ratio) ,int(best_particle_size_ratio* template_height)))
        bottom_right = (top_left[0] + int(template_width * best_particle_size_ratio), top_left[1] + int(best_particle_size_ratio * template_height))
        # drawing the bounding box for the observed match
        cv2.rectangle(img_raw,top_left, bottom_right,(0,0,255),2)
#        cv2.imshow(best_template_label, best_template)
#        cv2.imshow(best_template_label, img_raw)
        output_path = './' + path.split('/')[-1]
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        cv2.imwrite(output_path + '/' + best_template_label + '_' + image.split('/')[-1], img_raw)
#        cv2.waitKey(0)






