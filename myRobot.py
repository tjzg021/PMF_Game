import numpy

from Robot import  OurRobot



class SRobot:

    def __init__(self, id, robot_num):

        self.PID = id

        self.robot_num = robot_num

        self.history_data = []

        self.return_data = robot_num



    def cal_data(self,robot,currentiter,Iteration,TotalRobot):



        value = OurRobot(robot, currentiter, Iteration, TotalRobot-1)

        return value   #self.return_data



    def update_data(self, vector):

        self.history_data.append(vector)

        return 0



class DummyRobot:

    def __init__(self, id, robot_num):

        self.PID = id

        self.robot_num = robot_num



    def cal_data(self,robot,currentiter,Iteration,TotalRobot):
        if self.PID == TotalRobot -1 and Iteration >500:
            return TotalRobot
        else:
            return numpy.random.randint(1, self.robot_num + 1)



    def update_data(self, vector):

        return 0
