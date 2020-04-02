# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:40:21 2019

@author: ad58638
"""

import geopandas as gpd
from matplotlib import pyplot as plt
import time

startTime = time.time()

pathGPKG = r'H:\Documents\Gymnasiet\Gymnasiearbete\gadm36_SWE_gpkg\gadm36_SWE.gpkg'
pathSHP = r'H:\Documents\Gymnasiet\Gymnasiearbete\Befolkning Rutnät SCB\Inspire_TotPop_Sweref_region.shp'

# fig, ax = plt.subplots()

readData = gpd.read_file(pathGPKG)
print(readData)

# c = ax.pcolormesh(data)

readData.plot()

plt.axis('scaled')
plt.show()
print(time.time() - startTime)
