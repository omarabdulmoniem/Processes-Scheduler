# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 06:34:46 2022

@author: VIP
"""

class Priority_non_preemptive:

    def process(self, noOfProcesses):
        processData = []
        for i in range(noOfProcesses):
            temp = []
            processID = int(input("Enter the process ID  : "))
            arrivalTime = float(input(f"Enter The Time of arrival for the process {processID}: "))
            priority = int(input(f"Enter the Process priority {processID}: "))
            burstTime = float(input(f"Enter the process Burst Time  {processID}: "))
            temp.extend([processID, arrivalTime, burstTime, priority,0])
            processData.append(temp)
        Priority_non_preemptive.schedule_process(self, processData)
    def schedule_process(self, processData):
        timer = 0
        startTime = []
        exitTime = []
        process_seq = []
        processData.sort(key=lambda x: x[1])   #sort according to the arrival time
        while 1:
            nQueue = []
            readyQueue = []
            temporary = []
            for i in range(len(processData)):
                if processData[i][1] <= timer and processData[i][4] == 0:    #take the processes that have arrived and not completed and put them in the ready queue
                    temporary.extend([processData[i][0], processData[i][1], processData[i][2], processData[i][3], processData[i][4]])
                    readyQueue.append(temporary)
                    temporary = []
                elif processData[i][4] == 0:  #the processes which haven't arrived  put them in another queue
                    temporary.extend([processData[i][0], processData[i][1], processData[i][2], processData[i][3], processData[i][4]])
                    nQueue.append(temporary)
                    temporary = []
            if len(readyQueue) != 0:
                readyQueue.sort(key=lambda x: x[3])  #sort the raedy queue according to the priority in ascending order the smallest the number the higher the priority
                startTime.append(timer)
                process_seq.append(readyQueue[0][0])
                for k in range(len(processData)):
                    if processData[k][0] == readyQueue[0][0]:
                        break
                processData[k][4] = 1    #mark the process as completed
                timer = timer + processData[k][2]   #increase the timer by the burst time of the process
                eTime = timer
                exitTime.append(eTime)
                processData[k].append(eTime)        #give no 5 for the completion time 
            if len(readyQueue) == 0 and len(nQueue) == 0:   # if the two queues are empty this means that all the processes have been executed so break
                break
            if len(readyQueue) == 0:
                nQueue.sort(key=lambda x: x[1])   #sort it according to the arrival time
                if timer < nQueue[0][1]:          #if timer smaller than the arrival time of the first element in the normal queue
                    timer = nQueue[0][1]          #make the timer equal the arrival time of the first element
                startTime.append(timer)
                process_seq.append(nQueue[0][0])
                for k in range(len(processData)):
                    if processData[k][0] == nQueue[0][0]:
                        break
                processData[k][4] = 1           #mark the process as completed by giving 1 instead of zero
                timer = timer + processData[k][2] #increase the timer by the burst time of the process
                eTime = timer
                exitTime.append(eTime)
                processData[k].append(eTime)   #give no 5 for the completion time
        waitingTime = Priority_non_preemptive.calculating_waiting_time(self, processData)
        turnAroundTime = Priority_non_preemptive.calculating_turn_around_time(self, processData)
        Priority_non_preemptive.print_data(self, processData, waitingTime, turnAroundTime, process_seq)

    def calculating_waiting_time(self, processData):
        totalWaitingTime = 0
        for i in range(len(processData)):
            waiting = processData[i][5] - processData[i][1] - processData[i][2]  #waiting=completion time-arrival time- burst time
            totalWaitingTime = totalWaitingTime + waiting
            processData[i].append(waiting)
        av_waiting_time = totalWaitingTime / len(processData)   #average=total/no of processes
        return av_waiting_time
    def calculating_turn_around_time(self, processData):
        totalTurnAroundTime = 0
        for i in range(len(processData)):
            turnAround = processData[i][5] - processData[i][1]          #turn around=completion-arrival
            totalTurnAroundTime =  totalTurnAroundTime +turnAround
            processData[i].append(turnAround)
        av_turn_around_time =  totalTurnAroundTime / len(processData)    #average=total turn around time/no of processes
        return av_turn_around_time

    def print_data(self, processData, av_waiting_time, av_turn_around_time, process_seq):
        processData.sort(key=lambda x: x[0])   #sort according to the id
        print("ProcessID  ArrivalTime   BurstTime       Priority        Completed    CompletionTime   waitingTime   TurnAroundTime")
        for i in range(len(processData)):
            for j in range(len(processData[i])):
                print(processData[i][j], end="				")
            print()
        print(f'The Average Waiting Time for all the processes: {av_waiting_time}')
        print(f'The Average Turn around Time for all the processes: {av_turn_around_time}')
        print(f'The Sequence of Process: {process_seq}')


if __name__ == "__main__":
    noOfProcesses = int(input("Enter number of processes: "))
    priority = Priority_non_preemptive()
    priority.process(noOfProcesses)
        


