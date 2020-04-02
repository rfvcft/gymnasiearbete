# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:50:53 2020

@author: ad58638
"""

from CreateWeightGrid import population_grid
from SortSverigeData import file_to_data_list
from SverigeColorGradient import create_gradient

path = 'SverigeDataOrigo.txt'

dataList = file_to_data_list(path)

popGrid = population_grid(dataList)

create_gradient(popGrid, save='')
