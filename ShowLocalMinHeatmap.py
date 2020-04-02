# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:23:02 2020

@author: ad58638
"""

import ast
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from CreateWeightGrid import population_grid
from SortSverigeData import file_to_data_list


def create_gradient(evaluation_data, save=''):
    fig, ax = plt.subplots()
     
    #evaluation_data = np.ma.masked_where(evaluation_data == 0, evaluation_data)
    
    hot = plt.cm.get_cmap('hot')
    #hot.set_bad(color='b')
    
    #new_colors = hot(np.linspace(0, 1, 256))
    
    pink = np.array([248/256, 24/256, 148/256, 1])
    #green = np.array([0, 1, 0, 1])
    
    #new_colors[-1:, :] = green
    
    #cmap = colors.ListedColormap(new_colors)
    
    color = plt.pcolormesh(evaluation_data, norm=colors.LogNorm(), cmap=hot)
    
    ax.set_aspect('equal', 'box')
    
    ax.set_title('n = 4')
    
    # plt.colorbar(color, ax=ax)
    
    ax.scatter(xList, yList, s=2,  c=pink)
    
    if save:
        plt.savefig(save, dpi=1000)
    
    plt.show()
    

def num_of_neighbors(n_list, num):
    count = 0
    for neighbor in n_list:
        if neighbor == 0:
            count += 1
    
    if count > num:
        return False
    else:
        return True


path1 = 'SverigeDataOrigo.txt'
path = 'SverigeGridData.txt'

dataList = file_to_data_list(path1)

popGrid = population_grid(dataList)

with open(path, 'r') as data:
    for line in data:
        # grid = ast.literal_eval(line)
        
        grid = popGrid
        
        numRows = len(grid)
        numColumns = len(grid[0])
        
        xList = []
        yList = []
        count = 0       
        for row in range(numRows):
            for col in range(numColumns):
                val = grid[row][col]
                
                if val != 0:
                    neighbors = []
                    
                    if row != 0:
                        neighbors.append(grid[row - 1][col])
                    
                    if row != numRows - 1:
                        neighbors.append(grid[row + 1][col])
                    
                    if col != 0:
                        neighbors.append(grid[row][col - 1])
                    
                    if col != numColumns - 1:
                        neighbors.append(grid[row][col + 1])
                    

                    if all(i < val for i in neighbors) and num_of_neighbors(neighbors, 0):
                        count += 1
                        # print(neighbors)
                        xList.append(col)
                        yList.append(row)
        print(count)
        create_gradient(grid, save='befLocMax4')
    