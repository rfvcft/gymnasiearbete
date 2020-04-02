# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 08:58:42 2020

@author: ad58638
"""

path = 'SverigeData.txt'

with open(path, 'r') as data:
    writeFile = open('SverigeDataOrigo.txt', 'w')
    
    # northMin = 6133000
    # eastMin = 269000
    
    for line in data:
        north, east, pop = [int(i) for i in line.split()]
        
        if pop != 0:
        
            northShift = (north - 6133000) // 1000
            eastShift = (east - 269000) // 1000
            
            text = str(northShift) + ' ' + str(eastShift) + ' ' + str(pop) + '\n'
            
            writeFile.write(text)

writeFile.close()
        