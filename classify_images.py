#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: ANITER Hichame
# DATE CREATED: 08/08/2020                    
# REVISED DATE: 09/02/2020
from classifier import classifier 

def classify_images(images_dir, results_dic, model):    
    for key in results_dic:       
        temp = classifier(images_dir+key, model).lower().strip()
        if results_dic[key][0] in temp:
            results_dic[key].extend([temp,1])
        else:
            results_dic[key].extend([temp,0])                             
    None 