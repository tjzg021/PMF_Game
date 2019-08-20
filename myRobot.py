import numpy

class Robot:
    def __init__(self, id, robot_num):
        self.PID = id
        self.robot_num = robot_num
        self.history_data = []
        self.return_data = robot_num

    def cal_data(self):
        return self.return_data

    def update_data(self, vector):
        self.history_data.append(vector)
        return 0

class DummyRobot:
    def __init__(self, id, robot_num):
        self.PID = id
        self.robot_num = robot_num

    def cal_data(self):
        return numpy.random.randint(1, self.robot_num + 1)

    def update_data(self, vector):
        return 0