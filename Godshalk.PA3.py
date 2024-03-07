# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:57:08 2024

@author: KJGodshalk
"""

import numpy as np

#Part 1
p1 = np.poly1d([2,3,0,1])
print(p1)
print(np.polyval(p1, 2))

p2 = np.poly1d([1,0,1])
p2_der = np.polyder(p2)
print(np.polyval(p2_der, 1))

#Part 2
coeff_in = input('Provide the coeffecients would like for your polynomial with commes separating them (ex: 1,0,4 gives x^2+4): ')
x1 = float(input('Provide the x1 values that you want to use for Newtons Method: '))
coeff_string = coeff_in.split(',')
coeff_list = []
#converts string values to floats and adds them to list
for i in coeff_string:
    coeff_list.append(float(i))

def newtons_method(a,c,counter = 0):
    #sets polynomial
    poly = np.poly1d(a)
    #sets derivative
    poly_der = np.polyder(poly)
    #equation for newton's formula
    new_x = c - (np.polyval(poly, c)/np.polyval(poly_der, c))
    #base case where if the new x value is the same as the previous x value to the thousandths place, the value is printed along with the roots
    if abs(new_x -c) < 0.001:
        print(f'The final value with stabilized thousandths place is: {new_x:.3f}')
        print(f'The roots of the polynomial are: {np.roots(a)}')
        return new_x
    else:
        #recursion case where the new x value is used now for the formula
        counter += 1
        print(f'x_{counter} = {new_x:.3f}')
        newtons_method(a, new_x, counter)

newtons_method(coeff_list,x1)



       

    
    

