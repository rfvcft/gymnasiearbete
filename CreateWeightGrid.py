# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:59:29 2020

@author: ad58638
"""

from SortSverigeData import file_to_data_list


def population_grid(data_list):
    grid =[]
    x_max = max(data_list, key=lambda x: x[1])[1] + 1
    y_max = max(data_list, key=lambda x: x[0])[0] + 1
    
    
    for row in range(y_max):
        row_list = [0] * x_max
        grid.append(row_list)
    
    
    for point in data_list:
        y_point = point[0]
        x_point = point[1]
        weight = point[2]
        
        grid[y_point][x_point] = weight

    return grid


if __name__ == '__main__':
    file = 'SverigeDataOrigo.txt'
    
    data = file_to_data_list(file)
    
    g = population_grid(data)
    
    print(len(g))
    
