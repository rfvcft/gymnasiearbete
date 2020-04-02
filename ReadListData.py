# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:21:41 2020

@author: ad58638
"""

from SverigeColorGradient import create_gradient
import ast
import numpy as np

path = 'SverigeGridData.txt'

with open(path, 'r') as data:
    
    for i, line in enumerate(data):
        
        if i == 0:
            grid_list = ast.literal_eval(line)
            
            grid_array = np.array(grid_list)
            
            create_gradient(grid_array, save='')

