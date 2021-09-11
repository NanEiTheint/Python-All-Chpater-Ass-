# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 21:49:19 2021

@author: Acer

Exercise 5.10
"""
import sys
from numpy import *
import matplotlib.pyplot as plt

v0 = eval(input("Enter value of v0:"))
g = 9.81

t = linspace(0,2*v0/g,1000)

def f(t):
    return  v0*t - 0.5*g*t**2

result = f(t)

print(result)
plt.plot(t,result)
plt.xlabel('time (s)')
plt.ylabel('height (m)')


