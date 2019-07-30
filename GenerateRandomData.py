# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:38:22 2019

@author: tjzg
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def GenerateRandomData(inputseed):
    np.random.seed(inputseed)
    #n = np.random.normal(loc=0.0, scale=1, size=(3,3,3))
    #RandomNum = np.random.normal(0.0, 0.1, 50)
    RandomNum = np.random.randint(1,31,30)
    print (RandomNum)
    
    
    return RandomNum
    
#Seed = 123
#GenerateRandomData(Seed)
    

def GenScore_randint(seed, teams_num):
    np.random.seed(seed)
    RandomNum = np.random.randint(1,teams_num+1,1)
    return RandomNum

def GenScore_beta(teams_num):
   
    RandomNum = int(np.random.beta(0.2,0.3) * teams_num)
    return RandomNum

def GenScore_normal(teams_num):
   
    RandomNum = int(np.random.normal(teams_num/2,0.3) * teams_num)
    return RandomNum
