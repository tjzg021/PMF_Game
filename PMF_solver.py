import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def PMF_solver(data, teams_num):

    total = len(data)
    datacounter = Counter(data)
    print("len: %d" %(total))

    pmf = {}
    Y = []
    for i in range(0,teams_num) :
        pmf[i] = datacounter[i+1]/total
        Y.append(pmf[i])
    #for i in range(0,teams_num) :
        #print("PMF_solver.PMF:%f %d" %(pmf[i],i))

#    X1 = range(1, teams_num+1)
#    print (X1)
#    print (len(Y),Y)
#    fig1, ax1 = plt.subplots(1, 1, figsize=(10, 4))
#
#    ax1.scatter(X1,Y)
#    ax1.set_xlabel('X1')
#    ax1.set_ylabel('Y')
#    plt.show()
    
    return pmf


def UpdatePMF(R, Output, Iteration, TotalRobot):

    for i in range(0,TotalRobot-1):
        R[i].DATA[Iteration] = Output[i]
        
    for i in range(0,TotalRobot-1):
        for j in range(0,TotalRobot):
            #R[i].PMF[j] = PMF_solver( list( R[i].DATA.values() ), TotalRobot)
            #print("PMF_solver.DATA",R[i].DATA.values())
            R[i].PMF[j] = PMF_solver(  R[i].DATA.values() , TotalRobot)


