# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:38:22 2019

@author: tjzg
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#import PMF_solver

def RandomData(inputseed):
    np.random.seed(inputseed)
    RandomNum = np.random.randint(0,10,1)
    return RandomNum
    


def GenOutput_randint(teams_num):
    #np.random.seed(seed)
    RandomNum = np.random.randint(1,teams_num+1,1)
    return RandomNum[0]

def GenOutput_beta(teams_num):
   
    RandomNum = max(int(np.random.beta(5,1) * teams_num),1)
    return RandomNum

def GenOutput_normal(teams_num):
   
    RandomNum = int(np.random.normal(teams_num*3/4.0,0.3) )
    RandomNum = min(RandomNum,teams_num)
    RandomNum = max(RandomNum,1)
    
    return RandomNum

