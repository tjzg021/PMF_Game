# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:38:22 2019

@author: tjzg
"""

import numpy as np
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