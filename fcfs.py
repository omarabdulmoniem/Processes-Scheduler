
from collections import deque

class process_ins:
    def __init__(self,name,burstTime,arrival_time=0,priority=1):
        self.name = name
        self.burstTime = burstTime
        self.arrival_time = arrival_time
        self.priority = priority

    def __lt__(self, other):
        return self.arrival_time < other.arrival_time


def fcfs():
    timer = 0
    processes = list()
    number = input("Please enter number of processes: ")
    for i in range(0,int(number)):
        name = input("enter process name: \n")
        burstTime = input("enter it's burst time: \n")
        arrival_time = input("enter it's arrival time: \n")
        process = process_ins(name,burstTime,arrival_time)
        processes.append(process)
    processes.sort()
    wait_sum = 0
    for i in range(0,int(number)-1):
        wait_sum = wait_sum + int(processes[i].burstTime) + timer
        timer = timer + int(processes[i].burstTime)

    av_wait = wait_sum/int(number)
    for i in range(len(processes)):
        print(processes[i].name)
    print(av_wait)

fcfs()
