# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:10:09 2022

@author: VIP
"""

class Priority_preemptive:

    def process(self, noOfProcesses):
        processData = []
        for i in range(noOfProcesses):
            temp= []
            processID = int(input("Enter the process ID: "))
            arrivalTime = int(input(f"Enter The Time of arrival for the process {processID}: "))
            priority = int(input("Enter the process priority: "))
            burstTime = int(input(f"Enter the process Burst Time  {processID}: "))
            temp.extend([processID, arrivalTime, burstTime, priority, 0, burstTime])
            processData.append(temp)
        Priority_preemptive.schedule_process(self, processData)
        
    def schedule_process(self, processData):
        startTime = []
        timer = 0
        exitTime = []
        process_seq = []
        processData.sort(key=lambda x: x[1])   #sort according to the arrival time
        while 1:
            nQueue = []
            readyQueue = []
            temporary = []
            for i in range(len(processData)):
                if processData[i][1] <= timer and processData[i][4] == 0:   #take the processes that have arrived and not completed and put them in the ready queue
                    temporary.extend([processData[i][0], processData[i][1], processData[i][2], processData[i][3],
                                 processData[i][5]])
                    readyQueue.append(temporary)
                    temporary = []
                elif processData[i][4] == 0:   #the processes which haven't arrived them put them in another queue
                    temporary .extend([processData[i][0], processData[i][1], processData[i][2], processData[i][4],
                                 processData[i][5]])
                    nQueue.append(temporary)
                    temporary = []
           
            if len(readyQueue) != 0:
                readyQueue.sort(key=lambda x: x[3])  #sort the raedy queue according to the priority in ascending order the smallest the number the higher the priority
                startTime.append(timer)
                timer = timer + 1
                eTime = timer
                exitTime.append(eTime)
                process_seq.append(readyQueue[0][0])
                for k in range(len(processData)):
                 if processData[k][0] == readyQueue[0][0]:
                        break
                processData[k][2] = processData[k][2] - 1  #remove 1 from the burst time 
                if processData[k][2] == 0:       #if burst time is zero, it means process is completed
                    processData[k][4] = 1        #mark the process as completed
                    processData[k].append(eTime) #give no 6 for the completion time  
           
            if len(readyQueue) == 0 and len(nQueue) == 0:  # if the two queues are empty this means that all the processes have been executed so break
                break
            
            if len(readyQueue) == 0:
                nQueue.sort(key=lambda x: x[1]) #sort it according to the arrival time
                if timer < nQueue[0][1]:  #if timer smaller than the arrival time of the first element in the normal queue
                    timer = nQueue[0][1]  #make the timer equal the arrival time of the first element
                startTime.append(timer)
                timer = timer + 1
                eTime = timer
                exitTime.append(eTime)
                process_seq.append(nQueue[0][0])
                for k in range(len(processData)):
                 if processData[k][0] == nQueue[0][0]:
                        break
                 processData[k][2] = processData[k][2] - 1  #remove 1 from the burst time 
                 if processData[k][2] == 0:                 #if burst time is zero, it means process is completed
                    processData[k][4] = 1                   #mark the process as completed
                    processData[k].append(eTime)            #give no 6 for the completion time
           
            
       
        waitingTime = Priority_preemptive.calculating_waiting_time(self, processData)
        turnAroundTime = Priority_preemptive.calculating_turn_around_time(self, processData)
        Priority_preemptive.print_data(self, processData,waitingTime,turnAroundTime,process_seq)


    def calculating_waiting_time(self, processData):
        totalWaitingTime = 0
        for i in range(len(processData)):
            waiting =  processData[i][6] - processData[i][1] - processData[i][5]  #waiting=completion time-arrival time-original burst time
            totalWaitingTime = totalWaitingTime + waiting
            processData[i].append(waiting)
        av_waiting_time = totalWaitingTime / len(processData)  #average=total/no of processes
        return av_waiting_time

    def calculating_turn_around_time(self, processData):
        totalTurnAroundTime = 0
        for i in range(len(processData)):
            turnAround = processData[i][6] - processData[i][1]  #turn around=completion-arrival
            totalTurnAroundTime = totalTurnAroundTime + turnAround
            processData[i].append(turnAround)
        av_turn_around_time = totalTurnAroundTime / len(processData)  #average=total turn around time/no of processes
        return av_turn_around_time
    
    def print_data(self, processData,av_waiting_time, av_turn_around_time,  process_seq):
        processData.sort(key=lambda x: x[0])   #sort according to the id
        print("ProcessID  ArrivalTime  RemBurstTime   Priority        Completed  OrigBurstTime CompletionTime  WaitingTime  turnAroundTime")
        for i in range(len(processData)):
            for j in range(len(processData[i])):
                   print(processData[i][j], end="				")
            print()
        print(f'The Average Waiting Time for all the processes: {av_waiting_time}')
        print(f'The Average Turn around Time for all the processes: {av_turn_around_time}')
        print(f'The Sequence of Process: {process_seq}')
if __name__ == "__main__":
    noOfProcesses = int(input("Enter number of processes: "))
    priority = Priority_preemptive()
    priority.process(noOfProcesses)