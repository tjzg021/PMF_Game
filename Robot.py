import numpy as np

import PMF_solver as Solver
import GenerateRandomData  as GenData


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
    if Iteration < 501 :
        if Iteration == 500:
            for i in range(0,TotalRobot-1):
                GR[i].PMF == Solver.PMF_solver(GR[i].DATA.values(),TotalRobot) 
                
        return np.random.randint(TotalRobot/2,TotalRobot)
    else:
    
        for i in range(0,TotalRobot):
            FCM[i] = 0
            for j in range(0,TotalRobot-1):
                #print("PMF: %f %d %d"  %(GR[j].PMF[i],j,i))
                #PMF_solver.UpdatePMF(GR, Output, Iteration, TotalRobot)
                FCM[i] += GR[j].PMF[i]

    Score = {}
    for i in range(0,TotalRobot):
        Score[i] = (i+1)/( FCM[i] * (np.log10(FCM[i]) + 1) )
    MaxScore,outputvalue = max(zip(Score.values(),Score.keys()) )
    Solver.UpdatePMF(GR, Output, Iteration, TotalRobot)
    return MaxScore,outputvalue



def TestData(num, teams_num):
    numlist = []
    for i in range(1,num+1):
        numlist.append(GenData.GenOutput_randint(teams_num))
        #numlist.append(GenData.GenOutput_normal(teams_num))
        #numlist.append(GenData.GenOutput_beta(teams_num))
    #print("TestData",numlist)
    return numlist

def TestDistrbution(teams_num):
    Y = TestData(20000, teams_num)
    MCMC_solver.PMF_solver(Y,teams_num)   
    

def TestRobot(teams_num):
    robot = {}
    Iteration = 20000
    for i in range(0, teams_num-1):
        robot[i] = GameRobot()
        robot[i].PID = i
        data = TestData(Iteration-1, teams_num)
        for j in range(0, Iteration-1):
            
            robot[i].DATA[j] = data[j]
            
    for i in range(0, teams_num-1):        
        #for j in range(0,teams_num-1):
            robot[i].PMF = Solver.PMF_solver(robot[i].DATA.values(),teams_num) 
    
   # for i in range(0, teams_num):        
   #     for j in range(0,teams_num-1):
            #print("PMF: %f %d %d"  %(robot[j].PMF[i],j,i))  
              
    currentiter = {}        
    for i in range(0, teams_num):
        currentiter[i] = TestData(1, teams_num)[0]
        print("TestData:%d"  %(currentiter[i]))
        
    score,value = Robot(robot, currentiter, 20000, 12)
    print ("score: %f  value:%d" %(score,value))
    
    
if __name__ == "__main__":
    #TestDistrbution(12)
    TestRobot(12)
   


