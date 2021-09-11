# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 21:26:46 2021

@author: Acer

Exercise 5.9
"""
from numpy import *
import matplotlib.pyplot as plt

v0 = 10
g = 9.81

start = 0
stop = 2*v0/g
t = linspace(start,stop,1000)

def f(t):
    return v0*t - 0.5*g*t**2
result = f(t)

print(result)
plt.plot(t,result)
plt.xlabel('time (s)')
plt.ylabel('height (m)')


