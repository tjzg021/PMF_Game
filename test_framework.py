import argparse
import math
from myRobot import Robot
from myRobot import DummyRobot

def get_score(index, vector):
    cm = vector.count(vector[index])
    score = vector[index]/(cm * (math.log10(cm) + 1))
    return score

def main(robot_num, round_num):
    robot_list = []
    cur_robot = Robot(0, robot_num)
    robot_list.append(cur_robot)
    for ii in range(robot_num-1):
        cur_robot = DummyRobot(ii + 1, robot_num)
        robot_list.append(cur_robot)

    return_data = [0] * robot_num
    cur_score = [0] * robot_num 
    tot_score = [0] * robot_num
    for ii in range(round_num):
        for jj in range(robot_num):
            return_data[jj] = robot_list[jj].cal_data()
        for jj in range(robot_num):
            cur_score[jj] = get_score(jj, return_data)
            tot_score[jj] += cur_score[jj] 
            robot_list[jj].update_data(return_data)
        print(return_data)
        print([round(i, 2) for i in cur_score])
    print([round(i, 2) for i in tot_score])
    my_score = tot_score[0]
    tot_score.sort(reverse=True)
    my_rank = tot_score.index(my_score) + 1
    print("rank {}".format(my_rank))
    return 0

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--robot_num', default=12)
    parser.add_argument('-r', '--round_num', default=100)
    args = parser.parse_args()
    main(args.robot_num, args.round_num)