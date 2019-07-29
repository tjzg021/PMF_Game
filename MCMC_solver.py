import numpy as np
import matplotlib.pyplot as plt

import GenerateRandomData as GenData

def PMF_solver(): #data, pid, teams_num):
    
    Data = GenData.GenerateRandomData(123)
    teams_num = 30
    
    data = Data

    #X1=np.random.randn(1000)
    X1 = range(1,31)
    fig1,ax1 = plt.subplots(1, 1, figsize=(10,4));
    ax1.scatter(X1, Data);ax1.set_xlabel('X1');ax1.set_ylabel('Y'); 
    
    total = len(data)
    print("len: %d" %(total))
    pmf = {}
    for i in range(1,teams_num+1) :
        pmf[i]=[]
        pmf[i].append([data.count(i)/float(total)])
    
    
PMF_solver()