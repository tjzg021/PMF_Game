import numpy as np

import matplotlib.pyplot as plt

from collections import Counter


##################################to caculate PMF of input data

def PMF_solver(data, teams_num):
    total = len(data)

    datacounter = Counter(data)

    # print("len: %d" %(total))



    pmf = {}

    Y = []

    for i in range(0, teams_num+1):
        pmf[i] = datacounter[i + 1] / float(total)

        Y.append(pmf[i])

    ################################show figure

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


##################################update PMF every round

def UpdatePMF(R, Output, Iteration, TotalRobot):
    for i in range(0, TotalRobot):
        R[i].DATA[Iteration] = Output[i]

    if Iteration >=500:
        for i in range(0, TotalRobot ):
                R[i].PMF = PMF_solver(list(R[i].DATA.values()), TotalRobot)
