# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 07:49:38 2020

@author: ad58638
"""

import fiona

shape = fiona.open('Befolkning Rutnät SCB\\Inspire_TotPop_Sweref_region.shp')

writeFile = open('SverigeData.txt', 'w')

count = 1
for line in shape:
    properties = line['properties']
    
    place = int(properties['Ruta'])
    north = str(place % (10 ** 7))
    east = str(place // (10 ** 7))
    
    pop = str(properties['Pop'])
    
    write = north + ' ' + east + ' ' + pop + '\n'
    writeFile.write(write)
    
    print(count)
    count += 1

writeFile.close()
    