# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 08:23:09 2020

@author: ad58638
"""
import matplotlib.pyplot as plt

path = 'SverigeData.txt'

with open(path, 'r') as data:
    northList = []
    eastList = []
    popList = []
    
    for line in data:
        north, east, pop = [int(i) for i in line.split()]
        

        northList.append(north)
        eastList.append(east)
        popList.append(pop)
        
    print(len(popList))
    
    northMin = min(northList)
    eastMin = min(eastList)
    
    print(northMin, eastMin)
    print(max(northList), max(eastList))
    
    northList = [(i - northMin) // 1000 for i in northList]
    eastList = [(i - eastMin) // 1000 for i in eastList]
    sizeList = [i/10000 for i in popList]
    
    print(min(northList), min(eastList))
    print(max(northList), max(eastList), max(northList) * max(eastList))
    
    plt.scatter(northList, eastList, s=sizeList)
    
    plt.axis('equal')
    
    # plt.savefig('sverige_pyplot.png', dpi=1000)
    
    plt.show()
