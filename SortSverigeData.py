# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:18:50 2020

@author: ad58638
"""
 

def file_to_data_list(path):
    with open(path, 'r') as data:
        data_list = []
        
        for line in data:
            north, east, pop = [int(i) for i in line.split()]
            
            if pop != 0:
                data_list.append((north, east, pop))
        
        return data_list


def sort_data(data_list, sorting_focus='north'):      
    if sorting_focus == 'north':
        data_list.sort(key=lambda x: x[0])
    
    elif sorting_focus == 'east':
        data_list.sort(key=lambda x: x[1])
    
    elif sorting_focus == 'pop':
        data_list.sort(key=lambda x: x[2])
        
    return data_list


if __name__ == '__main__':
    file = 'SverigeDataOrigo.txt'
    dataList = file_to_data_list(file)
    print(sort_data(dataList, sorting_focus='north')[-10:])
        