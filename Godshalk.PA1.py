# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 21:02:02 2024

@author: KJGodshalk
"""
import random
import time
from tabulate import tabulate
 
global EXPERIMENT_AMOUNT
EXPERIMENT_AMOUNT = 100

def dimension1(x):
    counter = 0
    for n in range(EXPERIMENT_AMOUNT):
        steps = x
        origin = 0
        while steps != 0:
            steps -= 1
            step = random.choice([-1,1])
            origin += step
            if origin == 0:
                counter += 1
                break
    return counter

def dimension2(x):
    counter = 0
    for n in range(EXPERIMENT_AMOUNT):
        steps = x
        origin_x = 0
        origin_y = 0
        while steps != 0 :
            steps -= 1
            direction = random.choice(['x', 'y'])
            step = random.choice([-1,1])
            if direction == 'x':
                origin_x += step
            else:
                origin_y += step
            if origin_x == 0 and origin_y == 0:
                counter += 1
                break
    return counter

def dimension3(x):
    counter = 0
    for n in range(EXPERIMENT_AMOUNT):
        steps = x
        origin_x = 0
        origin_y = 0
        origin_z = 0
        while steps != 0 :
            steps -= 1
            direction = random.choice(['x', 'y','z'])
            step = random.choice([-1,1])
            if direction == 'x':
                origin_x += step
            elif direction == 'y':
                origin_y += step
            else:
                origin_z += step
            if origin_x == 0 and origin_y == 0 and origin_z == 0:
                counter += 1
                break
    return counter
        
def main():
    headers = ['Number of steps:', '20', '200', '2,000', '20,000', '200,000', '2,000,000']
    data = [['1D', dimension1(20), dimension1(200), dimension1(2000), dimension1(20000), dimension1(200000), dimension1(2000000)],
            ['2D', dimension2(20), dimension2(200), dimension2(2000), dimension2(20000), dimension2(200000), dimension2(2000000)],
            ['3D', dimension3(20), dimension3(200), dimension3(2000), dimension3(20000), dimension3(200000), dimension3(2000000)]]
    print("Percentages of time particle returned to origin:")
    table = tabulate(data, headers, tablefmt= 'grid')
    print(table)
    
    starttime = time.time()
   
    dimension3(20)
    dimension3(200), 
    dimension3(2000), 
    dimension3(20000), 
    dimension3(200000), 
    dimension3(2000000)
   
    endtime=time.time()
    elapsed_time=endtime-starttime
    
    print('Time took to run 3D: %10.5f' % elapsed_time)

main()

        