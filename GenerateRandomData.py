# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:38:22 2019

@author: tjzg
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

import MCMC_solver

def GenerateRandomData(inputseed):
    np.random.seed(inputseed)
    #n = np.random.normal(loc=0.0, scale=1, size=(3,3,3))
    #RandomNum = np.random.normal(0.0, 0.1, 50)
    RandomNum = np.random.randint(1,31,30)
    print (RandomNum)
    
    
    return RandomNum
    
#Seed = 123
#GenerateRandomData(Seed)
    

def GenOutput_randint(teams_num):
    #np.random.seed(seed)
    RandomNum = np.random.randint(1,teams_num+1,1)
    return RandomNum[0]

def GenOutput_beta(teams_num):
   
    RandomNum = max(int(np.random.beta(0.2,0.3) * teams_num),1)
    return RandomNum

def GenOutput_normal(teams_num):
   
    RandomNum = int(np.random.normal(teams_num/2,0.5) )
    RandomNum = min(RandomNum,teams_num)
    RandomNum = max(RandomNum,1)
    
    return RandomNum


#def TestDistrbution(teams_num):
#    Y = []
#    for i in range(1,20000+1):
#        Y.append(GenScore_normal(teams_num))
#    print(Y)
#    MCMC_solver.PMF_solver(Y,teams_num)
    #fig1,ax1 = plt.subplots(1, 1, figsize=(10,4));
    #ax1.scatter(X, Y);ax1.set_xlabel('X');ax1.set_ylabel('Y'); 
 
#TestDistrbution(12)