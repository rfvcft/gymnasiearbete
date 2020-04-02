# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:00:54 2019

@author: ad58638
"""

import geopandas as gpd

path = r'C:\Users\ad58638\Downloads\befolkning_upplatelseform_20181231_tab\Bef_Upplatform.MAP'

f = gpd.read_file(path)
print(f)
