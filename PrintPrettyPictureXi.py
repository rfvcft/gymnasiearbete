# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 04:01:10 2020

@author: ad58638
"""

# import numpy as n
from math import sqrt
import random as r
from matplotlib import pyplot as plt


def distance_to_point(my_point, eval_point):
    dx = my_point[0] - eval_point[0]
    dy = my_point[1] - eval_point[1]
    distance = sqrt(dx ** 2 + dy ** 2)
    return distance


def point_eval(radius, distance):
    score = 1 - (distance / radius)
    return score


def find_pid(point, radius, point_list):
    points_in_distance = []
    pp = point[0]
    for q in point_list:
        qq = q[0]
        d = distance_to_point(pp, qq)
        if d < radius:
            q_score = point_eval(radius, d)
            points_in_distance.append(q_score)
            
    return points_in_distance
            
            
        

# Givet en lista punkter med vikter på formatet p = ((x, y), w), ge RGM-utvärdering
    
def find_RGM(point_list, radius):
    score_list = []
    
    for p in point_list:
        points_in_distance = find_pid(p, radius, point_list)
        total_score = sum(points_in_distance)
        score_list.append((p, total_score))
    
    return score_list

def create_random_points(number_of_points, random_seed):
    random_points = []
    
    r.seed(random_seed)
    
    for z in range(number_of_points):
        x = r.random()
        y = r.random()
        w = r.randint(1, 10)
        random_points.append(((x, y), w))
    
    return random_points


def picture(score_list, best_point, radius):
    x_list = [i[0][0][0] for i in score_list]
    y_list = [i[0][0][1] for i in score_list]
    w_list = [i[0][1] for i in score_list]
    
    plt.scatter(x_list, y_list, c='black')
    for i, j, k in zip(x_list, y_list, w_list):
        plt.text(i + 0.02 , j, str(k))
    
    # plt.scatter(x_list, y_list, c='black')
    plt.scatter(best_point[0][0][0], best_point[0][0][1], c='red')
    
    # Ritar cirkel
    circle_point = plt.Circle((best_point[0][0][0], best_point[0][0][1]), radius, color='blue', fill=False)
    plt.gcf().gca().add_artist(circle_point)
    
    plt.axis('equal')
    plt.axis('off')
    plt.show()
    

N = 10
R = 0.3
seed = 5

randomPoints = create_random_points(N, seed)

scoreList = find_RGM(randomPoints, R)

print(scoreList)

bestPoint = max(scoreList, key=lambda x: x[1])

print('\n', bestPoint)

picture(scoreList, bestPoint, R)

