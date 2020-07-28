# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:38:12 2019

@author: Matthew Murray
"""
##Imports
import math
import numpy as np
##Define the myroots function: gives the roots of a quadratic equation
def myroots(a,b,c):
    Roots = np.array([(-b-math.sqrt(b**2-4*a*c))/2*a,format((-b+math.sqrt(b**2-4*a*c))/2*a,'16')])
    return Roots
r = myroots(1,10**8,1)
print(r) ##Roots are given in the form [x-,x+]

##Numpy's default root finder
Roots_default = np.roots([1,10**8,1])
print(Roots_default) ##Roots are given in the form [x-,x+]

##Define the myrootsacc function: correct for catastrophic cancelation
def myrootsacc(a,b,c):
    Roots = np.array([(-b-math.sqrt(b**2-4*a*c))/2*a,-2*c/(b+math.sqrt(b**2-4*a*c))])
    return Roots
r_acc = myrootsacc(1,10**8,1)
print(r_acc) ##Roots are given in the form [x-,x+]

rel = (float(r_acc[1])-float(r[1]))/float(r_acc[1])##The relative error between the negative root(x+) of myroots and myrootsacc
print(rel)



