# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:39:50 2020

@author: ad58638
"""

import scipy.spatial as spatial
import numpy as np
from SortSverigeData import sort_data
import time

def d(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    
    return (dx ** 2 + dy ** 2) ** 0.5

file = 'SverigeDataOrigo.txt'

dataWithWeight = sort_data(file)

data = [(i[0], i[1]) for i in dataWithWeight]

startTime = time.time()

points = np.array(data)

print(time.time() - startTime)

point_tree = spatial.cKDTree(points)

p = [100, 100]

a = point_tree.data[point_tree.query_ball_point(p, 5)]


