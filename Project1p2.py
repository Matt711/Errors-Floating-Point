# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:18:51 2019

@author: Matthew Murray
"""
#Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

##Variables
h = 1e-2
x = np.arange(0,1+h,h) ##Interval [0,1] w/ 100 evenly spaced points

##f'(x) Functions
def f_1(x):
    return (np.exp(x+h)-np.exp(x))/h
def f_2(x):
    return (np.exp(x+h)-np.exp(x-h))/(2*h)
def f_prime(x):
    return np.exp(x)

## Plot 1
f = plt.figure(1)
plt.plot(x,f_prime(x),color=(0,0,0),markersize=10,linewidth=4)
plt.plot(x,f_1(x),color=(1,0,0),markersize=10,linewidth=3)
plt.plot(x,f_2(x),color=(0,0,1),markersize=10,linewidth=2)
plt.title('Derivative of the The Exponential Function',fontsize=20)
plt.xlabel('x',fontsize=18)
plt.ylabel('y', fontsize = 18) 
plt.rcParams['xtick.labelsize']= 18
plt.rcParams['ytick.labelsize']= 18
black_patch = mpatches.Patch(color='black', label='exp(x)')
red_patch = mpatches.Patch(color='red', label='f1(x)')
blue_patch = mpatches.Patch(color='blue', label = 'f2(x)')

plt.legend(handles=[black_patch,red_patch,blue_patch],bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)

f.show()
# save as PDF
f.savefig("project1graph1.pdf", bbox_inches='tight')

##Relative Errors
hs = np.array([1e-15,1e-14,1e-13,1e-12,1e-11,1e-10,1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1])
def rel_1(hs):
    return np.abs(f_prime(0.5)- np.divide((np.exp(0.5+hs)-np.exp(0.5)),hs))/np.exp(0.5)
def rel_2(hs):
    return np.abs(f_prime(0.5)- np.divide((np.exp(0.5+hs)-np.exp(0.5-hs)),2*hs))/np.exp(0.5)


##Plot 2
g = plt.figure(2)
plt.loglog(hs,rel_1(hs),color=(1,0,0),markersize=10,linewidth=4)
plt.loglog(hs,rel_2(hs),color=(0,0,1),markersize=10,linewidth=3)
plt.title('Relative Errors',fontsize=20)
plt.xlabel('h',fontsize=18)
plt.ylabel('rel', fontsize = 18) 
plt.rcParams['xtick.labelsize']= 18
plt.rcParams['ytick.labelsize']= 18
red_patch = mpatches.Patch(color='red', label='rel1(h)')
blue_patch = mpatches.Patch(color='blue', label = 'rel2(h)')

plt.legend(handles=[red_patch,blue_patch],bbox_to_anchor=(1.05,1),loc=4,borderaxespad=0.)
g.show()
# save as PDF
g.savefig("project1graph2.pdf", bbox_inches='tight')