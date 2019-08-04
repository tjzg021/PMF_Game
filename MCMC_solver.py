import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def PMF_solver(data, teams_num):

    total = len(data)
    datacounter = Counter(data)
    print("len: %d" %(total))

    pmf = {}
    Y = []
    for i in range(1,teams_num+1) :
        pmf[i] = datacounter[i]/total
        Y.append(pmf[i])
        print ( "i= %d    %d times" %(i,datacounter[i]) )    #sum(data == i)) )
        print ("PMF for %d   %f" %(i,pmf[i]))

#    Y = []
#    for i in range(1,teams_num+1) :
#        print ("PMF for %d   %f" %(i,pmf[i]))
#        Y.append(pmf[i])

    X1 = range(1, teams_num+1)
    print (X1)
    print (len(Y),Y)
    fig1, ax1 = plt.subplots(1, 1, figsize=(10, 4))

    ax1.scatter(X1,Y)
    ax1.set_xlabel('X1')
    ax1.set_ylabel('Y')
    plt.show()
    
    return pmf


def UpdatePMF(R, Output, Iteration, TotalRobot):

    for i in range(1,TotalRobot+1):
        R[i].DATA[Iteration] = Output[i]
    R[i].PMF = PMF_solver( list( R[i].DATA.values() ), TotalRobot)


