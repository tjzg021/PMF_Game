import numpy as np

import MCMC_solver
import GenerateRandomData as GenData


class GameRobot:
    PID = 0
    PMF = {}
    DATA = {}

    def __init__(self):
        self.PID = 0
        self.PMF = {}
        self.DATA = {}

    def GetPMF(self):
        print("PID:",self.PID,"PMF", self.PMF)
        return self.PMF

    def GetDATA(self):
        return self.DATA


def Robot(GR, Output, Iteration, TotalRobot):
    
    FCM = {}
    if Iteration < 500 :
        return np.random.randint(TotalRobot/2,TotalRobot)
    else:
        for i in range(1,TotalRobot+1):
            FCM[i] = 1
            for j in range(1,TotalRobot+1):
                FCM[i] += GR[j].PMF[i]

    Score = {}
    for i in range(1,TotalRobot):
        Score[i] = i/( FCM[i] * (np.log10(FCM[i]) + 1) )
    MaxScore,outputvalue = max(zip(Score.values().Score.keys()) )
    MCMC_solver.UpdatePMF(GR, Output, Iteration, TotalRobot)
    return MaxScore,outputvalue



def TestData(num, teams_num):
    numlist = []
    for i in range(1,num+1):
        numlist.append(GenOutput_randint(teams_num))
        numlist.append(GenOutput_normal(teams_num))
        numlist.append(GenOutput_beta(teams_num))
    print(numlist)
    return numlist

def TestDistrbution(teams_num):
    Y = TestData(20000, teams_num)
    MCMC_solver.PMF_solver(Y,teams_num)   
    

def TestRobot(teams_num):
    robot = {}
    Iteration = 20000
    for i in range(1, teams_num):
        robot[i] = GameRobot()
        robot[i].PID = i
        data = TestData(Iteration-1, teams_num)
        for j in range(1, Iteration):
            robot[i].DATA[Iteration] = data[j]
   
    currentiter = {}        
    for i in range(1, teams_num):
        currentiter[i] = TestData(1, teams_num)
        
    score,value = Robot(robot, currentiter, 20000, 12)
    print ("score: %d  value:%f" %(score,value))
    
    
if __name__ == "__main__":
    #TestDistrbution(12)
    TestRobot(12)
   


