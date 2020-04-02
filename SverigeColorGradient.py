# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:51:03 2020

@author: ad58638
"""
from SortSverigeData import file_to_data_list
from matplotlib import pyplot as plt
from matplotlib import colors
from scipy import spatial
import numpy as np
import time

RADIUS = 100


def create_pop_dict_and_np_array(data_list):
    population_dict = dict()
    placement_list = []
    
    for point in np.array(data_list):
        placement = (point[0], point[1])
        population_dict[placement] = point[2]
        placement_list.append(placement)
    
    return population_dict, np.array(placement_list)
    

def point_eval(distance, radius):
    # returns a number (score)
    score = (radius - distance) / radius
    return score


def distance_to_point(my_point, eval_point):
    # returns a number (distance)
    distance = ((eval_point[0] - my_point[0]) ** 2 + (eval_point[1] - my_point[1]) ** 2) ** 0.5
    return distance


def find_in_range(my_point, all_points, radius):
    # all_points måste komma som en numpy array!
    
    point_tree = spatial.cKDTree(np.array(all_points))
    
    return point_tree.data[point_tree.query_ball_point(my_point, radius)]


def evaluate_single_point(my_point, all_points, radius):
    
    evaluation = 0
    points_in_distance = find_in_range(my_point, all_points, radius)
    
    for point in points_in_distance:
        '''
        print(point, my_point)
        
        # weight = POP_DICT[point]
        
        distance = distance_to_point(my_point, point)
        
        
        evaluation += point_eval(distance, radius) #* weight
        
        '''
        p = (point[0], point[1])
        weight = POP_DICT[p]
        distance = distance_to_point(my_point, p)
        
        if distance < radius:
            evaluation += point_eval(distance, radius) * weight
        
    return evaluation
            


def evaluate_over_all(all_points, radius):
    
    # eval_list = []
    
    count = 1
    start_time = time.time()
    for point in all_points:
        if count % 100 == 0:
            print(count)
            print(time.time() - start_time)
        count += 1
        # point = (x, y, weight)
        point_eval = evaluate_single_point((point[0], point[1]), all_points, radius)
        
        yield (point[0], point[1], point_eval)
        # eval_list.append((point[0], point[1], point_eval))
    
    # Return all points in the form p = (x, y, eval)
    # return eval_list


def create_gradient(evaluation_data, save=''):
    fig, ax = plt.subplots()
     
    #evaluation_data = np.ma.masked_where(evaluation_data == 0, evaluation_data)
    
    hot = plt.cm.get_cmap('hot')
    #hot.set_bad(color='black')
    
    new_colors = hot(np.linspace(0, 1, 256))
    
    pink = np.array([248/256, 24/256, 148/256, 1])
    green = np.array([0, 1, 0, 1])
    
    new_colors[-1:, :] = green
    
    cmap = colors.ListedColormap(new_colors)
    
    color = plt.pcolormesh(evaluation_data, norm=colors.LogNorm(), cmap=hot)
    
    ax.set_aspect('equal', 'box')
    
    plt.colorbar(color, ax=ax)
    
    if save:
        plt.savefig(save, dpi=1000)
    
    plt.show()


def fill_gaps(all_points, x_length, y_length):
    
    # Skapa listor med 0, och fyll sedan ut de ställen som ska ha värden
    
    fill_list = []
    
    for row in range(y_length):
        row_list = [0] * x_length
        fill_list.append(row_list)
    
    for point in evaluate_over_all(all_points, RADIUS):
        try:
            x_point = point[1]
            y_point = point[0]
            eval_point = point[2]
            fill_list[y_point][x_point] = eval_point
        except IndexError:
            print('IndexError')
            print(x_point, y_point)
            print()
        
    return fill_list


if __name__ == '__main__':
    
    startTime = time.time()
    
    file = 'SverigeDataOrigo.txt'
    
    data = file_to_data_list(file)
    
    print(len(data))
    
    POP_DICT, data_array = create_pop_dict_and_np_array(data)
    # print(POP_DICT)
    
    print('Data sorted')
    print('Time:', time.time() - startTime)
    print()
    
    # evaluationList = evaluate_over_all(data, RADIUS)
    
    
    filledList = fill_gaps(data_array, 647 + 1, 1512 + 1)
    
    print('Data evaluated')
    print('Time:', time.time() - startTime)
    print()
    
    create_gradient(filledList, save=True)
    
    print('Total time:', time.time() - startTime)
