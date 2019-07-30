



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


def Robot(R,Output, Iteration, TotalRobot):
    # TotalRobot = 30

    FCM = {}


    if Iteration < 500 :
        return np.random.randint(TotalRobot/2,TotalRobot)
    else:
        for i in range(1,TotalRobot+1):
            FCM[i] = 1
            for j in range(1,TotalRobot+1):
                FCM[i] += R[j].PMF[i]


    Score = {}
    for i in range(1,TotalRobot+1):
        Score[i] = i/(FCM[i]* (np.log10(FCM[i]*) + 1) )
    MaxScore = max(zip(Score.values().Score.keys()) )

    UpdatePMF(R, Output, Iteration, TotalRobot):
    return MaxScore[1]

def Game():



