import numpy as np

import PMF_solver as Solver

import GenerateRandomData  as GenData


##########################################class of robot

class GameRobot:
    PID = 0

    PMF = {}

    DATA = {}

    def __init__(self):
        self.PID = 0

        self.PMF = {}

        self.DATA = {}

    def GetPMF(self):
        print("PID:", self.PID, "PMF", self.PMF)

        return self.PMF

    def GetDATA(self):
        return self.DATA


##############################################caculte my output base on PMF

def OurRobot(GR, Output, Iteration, TotalRobot):
    FCM = {}

    if Iteration < 501:

        #if Iteration == 500:

        #    for i in range(0, TotalRobot ):
        #        GR[i].PMF == Solver.PMF_solver(GR[i].DATA.values(), TotalRobot)
        Solver.UpdatePMF(GR, Output, Iteration, TotalRobot)
        return np.random.randint((TotalRobot+1) / 2, TotalRobot+1)

    else:

        for i in range(0, TotalRobot+1):

            FCM[i] = 0.000001

            for j in range(0, TotalRobot ):
                FCM[i] += GR[j].PMF[i]

    Score = {}

    for i in range(0, TotalRobot+1):
        Score[i] = (i + 1) / ((FCM[i] + 1) * (np.log10(FCM[i] + 1) + 1))

        #print("Score caculate:%d %f %f score:%f" % (i, FCM[i], np.log10(FCM[i]), Score[i]))

    MaxScore, outputvalue = max(zip(Score.values(), Score.keys()))

    Solver.UpdatePMF(GR, Output, Iteration, TotalRobot)

    return outputvalue+1


##########################################generate test data for testing

def TestData(num, teams_num):
    numlist = []

    for i in range(1, num + 1):
        # numlist.append(GenData.GenOutput_randint(teams_num))

        numlist.append(GenData.GenOutput_normal(teams_num))

        # numlist.append(GenData.GenOutput_beta(teams_num))

    return numlist


########################################## test PMF solver

def TestDistrbution(teams_num):
    Y = TestData(20000, teams_num)

    Solver.PMF_solver(Y, teams_num)


##########################################   init robot
def initRobot(robot,teams_num):

    for i in range(0, teams_num):

        robot[i] = GameRobot()

        robot[i].PID = i

        #data = TestData(Iteration - 1, teams_num)


##########################################   test robot

def TestRobot(teams_num):
    robot = {}

    Iteration = 20000

    for i in range(0, teams_num ):

        robot[i] = GameRobot()

        robot[i].PID = i

        data = TestData(Iteration - 1, teams_num)

        for j in range(0, Iteration - 1):
            robot[i].DATA[j] = data[j]

    for i in range(0, teams_num ):
        robot[i].PMF = Solver.PMF_solver(robot[i].DATA.values(), teams_num)

    currentiter = {}

    for i in range(0, teams_num):
        currentiter[i] = TestData(1, teams_num)[0]

        print("TestData:%d" % (currentiter[i]))

    score, value = OurRobot(robot, currentiter, 20000, 12)

    print ("score: %f  value:%d" % (score, value + 1))


if __name__ == "__main__":
    # TestDistrbution(12)

    TestRobot(12)
