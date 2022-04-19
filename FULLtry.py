from distutils.log import info
import random
from multiprocessing.connection import wait
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from tkinter import *
root = Tk()
root.title('Processes Scheduler')
root.geometry("1000x600")
wel_label = Label(root,text='Please specify the type of the Scheduler',font='Arial',bg='#d1c7c7')
wel_label.pack(padx=10,pady=10)


colors = ['tab:red', 'tab:green', 'tab:blue', 'purple', 'black', 'orange', 'gray', 'pink', 'yellow', 'navy','violet', 'maroon']

class process_ins:
    def __init__(self,burstTime,arrival_time=0,priority=1):
        self.burstTime = burstTime
        self.arrival_time = arrival_time
        self.priority = priority

    def __lt__(self, other):
        return self.arrival_time < other.arrival_time

#FCFS Algorithm


def plottingNon(sequence_of_process, total_duration, start_time, burst_time):
# declaration
	global colors
	fig, gnt = plt.subplots()
	fig.canvas.set_window_title('Grantt Chart')
	gnt.set_title('Grantt Chart')

	gnt.set_ylim(0, 60)
	gnt.set_xlim(0, total_duration+2)

	gnt.set_xlabel('Process Time')
	gnt.set_ylabel('Processor')

	patch =[]

	for i in range(len(colors)):
		patch.append(mpatches.Patch(color=colors[i], label=f'Process #{i + 1}'))
	plt.legend(handles=patch, loc='upper right', borderaxespad=0., ncol = 3)

	# Setting ticks on y-axis
	gnt.set_yticks([0, 20, 40, 60])
	gnt.set_yticklabels(['', '', '', ''])

	gnt.grid(True)


	for i in range(len(sequence_of_process)):
		gnt.broken_barh([(start_time[i], burst_time[i])], (20,20),
							color = colors[sequence_of_process[i]])


	plt.show()

# Plotting gannt chart
def gannt_chart():
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    
    # Setting Y-axis limits
    gnt.set_ylim(0, 20+10*len(processes))
    
    # Setting X-axis limits
    gnt.set_xlim(0, 20+10*len(processes))
    
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Seconds')
    gnt.set_ylabel('Processes')
    
    # Setting ticks on y-axis
    ticks = []
    for i in range(int(number)):
        ticks.append(15+10*i)
    gnt.set_yticks(ticks)

    # Labelling tickes of y-axis
    tick_labels = []
    for i in range(int(number)):
        tick_labels.append('P'+str(i+1))
    gnt.set_yticklabels(tick_labels)
    
    # Setting graph attribute
    gnt.grid(True)
    
    # Declaring a bar in schedule
    wait_sum = 0

    for i in range(number):
        gnt.broken_barh([(wait_sum, processes[i].burstTime)], (ticks[i]-5, 10),facecolors =(colors[i]))
        wait_sum = wait_sum + int(processes[i].burstTime)
    
    plt.show()
        

def fcfs():
    timer = 0
    global processes
    processes = list()
    global number
    number = int(num0.get())
    duration = 0
    for single in info_list:
            process = process_ins(int(single[0].get()),int(single[1].get()))
            processes.append(process)
            duration += int(single[0].get())

    processes.sort()
    startseq = []
    wait_sum = 0
    for i in range(0,int(number)-1):
        wait_sum = wait_sum + int(processes[i].burstTime) + timer
        startseq.append(wait_sum)
        timer = timer + int(processes[i].burstTime)
    
    av_wait = wait_sum/int(number)
    wait_label1.config(text = 'average wait time is: '+ str(av_wait), bg= '#772020',fg='white',font=('Arial', 14))
    wait_label1.grid(row=number+4,column=1)

    gannt_chart()

def fcfs_window():
    new = Toplevel()
    new.title('FCFS INFO')
    new.geometry("1000x600")
    new.config(bg= '#772020')

    #processes info
    global info_list
    info_list = []
    #vertical
    for y in range(int(num0.get())):
        info_list.append([])
        burst_label  = Label(new,text = 'P'+ str(y+1) +' burst time: ', bg= '#772020',fg='white')
        burst_label.grid(row=y,column=0)
        global burst
        burst = Entry(new,width=50,fg='black')
        burst.grid(row=y,column=1,padx=10,pady=10)
        info_list[y].append(burst)

        arrival_label  = Label(new,text = 'Arrival Time: ', bg= '#772020',fg='white')
        arrival_label.grid(row=y,column=2)
        global arrival
        arrival = Entry(new,width=50,fg='black')
        arrival.grid(row=y,column=3,padx=10,pady=10)
        info_list[y].append(arrival)


    process_button = Button(new,text="Process",padx=10,pady=10,fg='black',command= fcfs)
    process_button.grid(row=int(num0.get()),column=1)

    exit_button = Button(new,text="Exit",padx=10,pady=10,fg='red',command= new.quit)
    exit_button.grid(row=int(num0.get())+1,column=2,padx=10,pady=10)


    global wait_label1
    wait_label1 = Label(new,text='')

            

# Priority (preemative) Algorithm

def pnongannt_chart():
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    
    # Setting Y-axis limits
    gnt.set_ylim(0, 20+10*len(info_list))
    
    # Setting X-axis limits
    gnt.set_xlim(0, 20+3*len(info_list))
    
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Seconds')
    gnt.set_ylabel('Processes')
    
    # Setting ticks on y-axis
    ticks = []
    for i in range(int(num0.get())):
        ticks.append(15+10*i)
    gnt.set_yticks(ticks)

    # Labelling tickes of y-axis
    tick_labels = []
    for i in range(int(num0.get())):
        tick_labels.append('P'+str(i+1))
    gnt.set_yticklabels(tick_labels)
    
    # Setting graph attribute
    gnt.grid(True)
    
    # Declaring a bar in schedule
    wait_sum = 0

    for i in range(int(num0.get())):
        index = int(sq[i])-1
        bur = burlist[index]
        gnt.broken_barh([(wait_sum, bur)], (ticks[index]-5, 10),facecolors =(colors[i]))
        wait_sum = wait_sum + bur
    
    plt.show()

class Priority_preemptive:

    def process(self, noOfProcesses):
        processData = []
        for i in info_list:
            temp = []
            processID = 'P'+str(i)
            arrivalTime = int(i[1].get())
            priority = int(i[2].get())
            burstTime = int(i[0].get())
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

        wait_label.config(text = 'average wait time is: '+ str(av_waiting_time), bg= '#772020',fg='white',font=('Arial', 14))
        wait_label.grid(row=int(num0.get())+3,column=2,padx=10,pady=10)

        turn_label.config(text = 'average turn around time is: '+ str(av_turn_around_time), bg= '#772020',fg='white',font=('Arial', 14))
        turn_label.grid(row=int(num0.get())+4,column=2,padx=10,pady=10)
        
        



def ppre():
    noOfProcesses = int(num0.get())
    priority = Priority_preemptive()
    priority.process(noOfProcesses)

def prioritypre_window():
    new = Toplevel()
    new.title('Priority (preemative)')
    new.geometry("1400x600")
    new.config(bg= '#772020')

    #processes info
    global info_list
    info_list = []
    #vertical
    for y in range(int(num0.get())):
        info_list.append([])
        burst_label  = Label(new,text = 'P'+ str(y+1) +' burst time: ', bg= '#772020',fg='white')
        burst_label.grid(row=y,column=0)
        global burst
        burst = Entry(new,width=50,fg='black')
        burst.grid(row=y,column=1,padx=10,pady=10)
        info_list[y].append(burst)

        arrival_label  = Label(new,text = 'Arrival Time: ', bg= '#772020',fg='white')
        arrival_label.grid(row=y,column=2)
        global arrival
        arrival = Entry(new,width=50,fg='black')
        arrival.grid(row=y,column=3,padx=10,pady=10)
        info_list[y].append(arrival)

        priority_label  = Label(new,text = 'Priority: ', bg= '#772020',fg='white')
        priority_label.grid(row=y,column=4)
        global priority
        priority = Entry(new,width=50,fg='black')
        priority.grid(row=y,column=5,padx=10,pady=10)
        info_list[y].append(priority)


    process_button = Button(new,text="Process",padx=10,pady=10,fg='black',command= ppre)
    process_button.grid(row=int(num0.get()),column=1)

    exit_button = Button(new,text="Exit",padx=10,pady=10,fg='red',command= new.quit)
    exit_button.grid(row=int(num0.get())+1,column=2,padx=10,pady=10)

    global wait_label
    wait_label = Label(new,text='')

    global turn_label
    turn_label = Label(new,text='')




# Priority (non Preemative)


class Priority_non_preemptive:

    def process(self, noOfProcesses):
        processData = []
        global burlist
        burlist = []
        y=1
        for i in info_list:
            temp = []
            processID = y
            arrivalTime = int(i[1].get())
            priority = int(i[2].get())
            burstTime = int(i[0].get())
            temp.extend([processID, arrivalTime, burstTime, priority,0])
            processData.append(temp)
            burlist.append(burstTime)
            y+=1
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
        global sq
        sq = process_seq
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
        waitpnon_label.config(text = 'average wait time is: '+ str(av_waiting_time), bg= '#772020',fg='white',font=('Arial', 14))
        waitpnon_label.grid(row=int(num0.get())+3,column=2,padx=10,pady=10)

        turnpnon_label.config(text = 'average turn around time is: '+ str(av_turn_around_time), bg= '#772020',fg='white',font=('Arial', 14))
        turnpnon_label.grid(row=int(num0.get())+4,column=2,padx=10,pady=10)
        pnongannt_chart()



def pnon():
    noOfProcesses = int(num0.get())
    priority = Priority_non_preemptive()
    priority.process(noOfProcesses)


def prioritynon_window():
    new = Toplevel()
    new.title('Priority (Non preemative)')
    new.geometry("1400x600")
    new.config(bg= '#772020')

    #processes info
    global info_list
    info_list = []
    #vertical
    for y in range(int(num0.get())):
        info_list.append([])
        burst_label  = Label(new,text = 'P'+ str(y+1) +' burst time: ', bg= '#772020',fg='white')
        burst_label.grid(row=y,column=0)
        global burst
        burst = Entry(new,width=50,fg='black')
        burst.grid(row=y,column=1,padx=10,pady=10)
        info_list[y].append(burst)

        arrival_label  = Label(new,text = 'Arrival Time: ', bg= '#772020',fg='white')
        arrival_label.grid(row=y,column=2)
        global arrival
        arrival = Entry(new,width=50,fg='black')
        arrival.grid(row=y,column=3,padx=10,pady=10)
        info_list[y].append(arrival)

        priority_label  = Label(new,text = 'Priority: ', bg= '#772020',fg='white')
        priority_label.grid(row=y,column=4)
        global priority
        priority = Entry(new,width=50,fg='black')
        priority.grid(row=y,column=5,padx=10,pady=10)
        info_list[y].append(priority)


    process_button = Button(new,text="Process",padx=10,pady=10,fg='black',command= pnon)
    process_button.grid(row=int(num0.get()),column=1)

    exit_button = Button(new,text="Exit",padx=10,pady=10,fg='red',command= new.quit)
    exit_button.grid(row=int(num0.get())+1,column=2,padx=10,pady=10)

    global waitpnon_label
    waitpnon_label = Label(new,text='')

    global turnpnon_label
    turnpnon_label = Label(new,text='')




# SJF preemetive Algorithm


class SJF:

    def processData(self, no_of_processes):
      process_data = []
      y =0
      for i in info_list:
            temp = []
            processID = y
            arrivalTime = int(i[1].get())
            
            burstTime = int(i[0].get())
            temp.extend([processID, arrivalTime, burstTime, 0, burstTime])
            process_data.append(temp)
            y+=1
      SJF.schedule_process(self, process_data)
      
      
    def schedule_process(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])
        
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                    
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
        t_time = SJF.calculateTurnaroundTime(self, process_data)
        w_time = SJF.calculateWaitingTime(self, process_data)
        SJF.printData(self, process_data, t_time, w_time, sequence_of_process)
        
        
        
    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        
        return average_turnaround_time


    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        
        return average_waiting_time                
                    
    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
        
        waitsjf_label.config(text = 'average wait time is: '+ str(average_waiting_time), bg= '#772020',fg='white',font=('Arial', 14))
        waitsjf_label.grid(row=int(num0.get())+3,column=2,padx=10,pady=10)

        turnsjf_label.config(text = 'average turn around time is: '+ str(average_turnaround_time), bg= '#772020',fg='white',font=('Arial', 14))
        turnsjf_label.grid(row=int(num0.get())+4,column=2,padx=10,pady=10)
        
            

def psjf():
    noOfProcesses = int(num0.get())
    sjf = SJF()
    sjf.processData(noOfProcesses)




def sjfpre_window():

    new = Toplevel()
    new.title('INFO')
    new.geometry("1000x600")
    new.config(bg= '#772020')

    #processes info
    global info_list
    info_list = []
    #vertical
    for y in range(int(num0.get())):
        info_list.append([])
        burst_label  = Label(new,text = 'P'+ str(y+1) +' burst time: ', bg= '#772020',fg='white')
        burst_label.grid(row=y,column=0)
        global burst
        burst = Entry(new,width=50,fg='black')
        burst.grid(row=y,column=1,padx=10,pady=10)
        info_list[y].append(burst)

        arrival_label  = Label(new,text = 'Arrival Time: ', bg= '#772020',fg='white')
        arrival_label.grid(row=y,column=2)
        global arrival
        arrival = Entry(new,width=50,fg='black')
        arrival.grid(row=y,column=3,padx=10,pady=10)
        info_list[y].append(arrival)


    process_button = Button(new,text="Process",padx=10,pady=10,fg='black',command= psjf)
    process_button.grid(row=int(num0.get()),column=1)

    exit_button = Button(new,text="Exit",padx=10,pady=10,fg='red',command= new.quit)
    exit_button.grid(row=int(num0.get())+1,column=2,padx=10,pady=10)


    global waitsjf_label
    waitsjf_label = Label(new,text='')

    global turnsjf_label
    turnsjf_label = Label(new,text='')



# SJF Non preemetive Algorithm



class NONPSJF:
    
    def processData(self, no_of_processes):
        process_data = []
        for i in info_list:
              temp = []
              processID = 'P'+str(i)
              arrivalTime = int(i[1].get())
              
              burstTime = int(i[0].get())
              temp.extend([processID, arrivalTime, burstTime, 0, burstTime])
              process_data.append(temp)
        NONPSJF.schedulingProcess(self, process_data)
        
    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            
            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []
                    
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
                
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
        
        t_time = NONPSJF.calculateTurnaroundTime(self, process_data)
        w_time = NONPSJF.calculateWaitingTime(self, process_data)
        NONPSJF.printData(self, process_data, t_time, w_time)
        
    
    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]
            
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        
        return average_turnaround_time


    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]
            
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        
        return average_waiting_time    
    
    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        waitsjfnon_label.config(text = 'average wait time is: '+ str(average_waiting_time), bg= '#772020',fg='white',font=('Arial', 14))
        waitsjfnon_label.grid(row=int(num0.get())+3,column=2,padx=10,pady=10)

        turnsjfnon_label.config(text = 'average turn around time is: '+ str(average_turnaround_time), bg= '#772020',fg='white',font=('Arial', 14))
        turnsjfnon_label.grid(row=int(num0.get())+4,column=2,padx=10,pady=10)
        
        
def nonpsjf():
    noOfProcesses = int(num0.get())
    nonsjf = NONPSJF()
    nonsjf.processData(noOfProcesses)







def sjfnon_window():
    new = Toplevel()
    new.title('sjf non preemative INFO')
    new.geometry("1200x600")
    new.config(bg= '#772020')

    #processes info
    global info_list
    info_list = []
    #vertical
    for y in range(int(num0.get())):
        info_list.append([])
        burst_label  = Label(new,text = 'P'+ str(y+1) +' burst time: ', bg= '#772020',fg='white')
        burst_label.grid(row=y,column=0)
        global burst
        burst = Entry(new,width=50,fg='black')
        burst.grid(row=y,column=1,padx=10,pady=10)
        info_list[y].append(burst)

        arrival_label  = Label(new,text = 'Arrival Time: ', bg= '#772020',fg='white')
        arrival_label.grid(row=y,column=2)
        global arrival
        arrival = Entry(new,width=50,fg='black')
        arrival.grid(row=y,column=3,padx=10,pady=10)
        info_list[y].append(arrival)


    process_button = Button(new,text="Process",padx=10,pady=10,fg='black',command= nonpsjf)
    process_button.grid(row=int(num0.get()),column=1)

    exit_button = Button(new,text="Exit",padx=10,pady=10,fg='red',command= new.quit)
    exit_button.grid(row=int(num0.get())+1,column=2,padx=10,pady=10)


    global waitsjfnon_label
    waitsjfnon_label = Label(new,text='')

    global turnsjfnon_label
    turnsjfnon_label = Label(new,text='')


    
# Round Robin Algorithm

def rrgannt_chart():
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    
    # Setting Y-axis limits
    gnt.set_ylim(0, 20+10*len(info_list))
    
    # Setting X-axis limits
    gnt.set_xlim(0, 20+3*len(info_list))
    
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Seconds')
    gnt.set_ylabel('Processes')
    
    # Setting ticks on y-axis
    ticks = []
    for i in range(int(num0.get())):
        ticks.append(15+10*i)
    gnt.set_yticks(ticks)

    # Labelling tickes of y-axis
    tick_labels = []
    for i in range(int(num0.get())):
        tick_labels.append('P'+str(i+1))
    gnt.set_yticklabels(tick_labels)
    
    # Setting graph attribute
    gnt.grid(True)
    
    # Declaring a bar in schedule
    wait_sum = 0
    qua = int(quantumm.get())
    for i in range(int(num0.get())):
        startlist = []
        for j in range(len(executed_process)):
            starttime=0
            if int(executed_process[j])==i:
                for z in range(j):
                    starttime += int(extime[z])
                startlist.append((starttime,int(extime[j])))

        gnt.broken_barh(startlist, (ticks[i]-5, 10),facecolors =(colors[i]))
    
    plt.show()

class RoundRobin:
    
    def Process(self):
        
        process_data = []
        ready_queue = []
        global executed_process
        executed_process = []
        global extime
        extime = []
        time = 0
        start_time = []
        exit_time = []
        
        
        n=int(num0.get())
        y=0
        for i in info_list:
            
            temporary = []
            process_id = y
            
            
            arrival_time = float(i[1].get())
            
            
            burst_time = float(i[0].get())
            
            
            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            process_data.append(temporary)
            y+=1
            
            
        quantum = int(quantumm.get())
        process_data.sort(key=lambda x: x[1])
        
        
        while 1:
            
            normal_queue = []
            temp = []
            
            for i in range(n):
                if process_data[i][1] <= time and process_data[i][3] == 0:
                    
                    present = 0
                    
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            
                            if process_data[i][0] == ready_queue[k][0]:
                                
                                present = 1
                                
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)        
                        temp = []
                        
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                                
                
                                
                elif process_data[i][3] == 0:    
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
                        
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
                
            if len(ready_queue) !=0:
                
                if ready_queue[0][2] > quantum:
                    
                    start_time.append(time)
                    time = time + quantum
                    e_time = time
                    exit_time.append(e_time)
                        
                    executed_process.append(ready_queue[0][0])
                    extime.append(quantum)
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                            
                    process_data[j][2] = process_data[j][2] - quantum
                    ready_queue.pop(0)
                        
                        
                elif ready_queue[0][2] <= quantum:
                        
                    start_time.append(time)
                    time = time + ready_queue[0][2]
                    e_time = time
                    exit_time.append(e_time)
                        
                    executed_process.append(ready_queue[0][0])
                    extime.append(ready_queue[0][2])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                            
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)
                        
                        
            elif len(ready_queue) == 0:
                    
                if time < normal_queue[0][1]:
                    time = normal_queue[0][1]
                        
                if normal_queue[0][2] > quantum:
                    
                    start_time.append(time)
                    time = time + quantum
                    e_time = time
                    exit_time.append(e_time)
                        
                    executed_process.append(normal_queue[0][0])
                    extime.append(quantum)
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                        
                    process_data[j][2] = process_data[j][2] - quantum
                    
                elif normal_queue[0][2] <= quantum:
                    
                    start_time.append(time)
                    time = time + normal_queue[0][2]
                    e_time = time
                    exit_time.append(e_time)
                        
                    executed_process.append(normal_queue[0][0])
                    extime.append(normal_queue[0][2])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                        
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    
                    
                    
        AvgT_time = RoundRobin.calcTurnaroundTime(self, process_data)
        AvgW_time = RoundRobin.calcWaitingTime(self, process_data)    
                    
            
        process_data.sort(key=lambda x: x[0])
        
        RoundRobin.printrr(self,AvgT_time,AvgW_time)


    def calcTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            
            total_turnaround_time = total_turnaround_time + turnaround_time
            
            process_data[i].append(turnaround_time)
            
        average_turnaround_time = total_turnaround_time / len(process_data)
        
        return average_turnaround_time
        
        
        
    def calcWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            
            total_waiting_time = total_waiting_time + waiting_time
            
            process_data[i].append(waiting_time)
            
        average_waiting_time = total_waiting_time / len(process_data)
        
        return average_waiting_time

    def printrr(self,turn_time,wait_time):
            waitrr_label.config(text = 'average wait time is: '+ str(wait_time), bg= '#772020',fg='white',font=('Arial', 14))
            waitrr_label.grid(row=int(num0.get())+4,column=2,padx=10,pady=10)

            turnrr_label.config(text = 'average turn around time is: '+ str(turn_time), bg= '#772020',fg='white',font=('Arial', 14))
            turnrr_label.grid(row=int(num0.get())+5,column=2,padx=10,pady=10)
            rrgannt_chart()



def rrr():
    global rrnumber
    rrnumber = int(num0.get())
    rr = RoundRobin()
    rr.Process()


def rr_window():
    new = Toplevel()
    new.title('Round Robin')
    new.geometry("800x600")
    new.config(bg= '#772020')

    #processes info
    global info_list
    info_list = []
    #vertical
    for y in range(int(num0.get())):
        info_list.append([])
        burst_label  = Label(new,text = 'P'+ str(y+1) +' burst time: ', bg= '#772020',fg='white')
        burst_label.grid(row=y,column=0)
        global burst
        burst = Entry(new,width=50,fg='black')
        burst.grid(row=y,column=1,padx=10,pady=10)
        info_list[y].append(burst)

        arrival_label  = Label(new,text = 'Arrival Time: ', bg= '#772020',fg='white')
        arrival_label.grid(row=y,column=2)
        global arrival
        arrival = Entry(new,width=50,fg='black')
        arrival.grid(row=y,column=3,padx=10,pady=10)
        info_list[y].append(arrival)


    quantumm_label  = Label(new,text = 'Quantum: ', bg= '#772020',fg='white')
    quantumm_label.grid(row=int(num0.get()),column=0)
    global quantumm
    quantumm = Entry(new,width=50,fg='black')
    quantumm.grid(row=int(num0.get()),column=1,padx=10,pady=10)


    process_button = Button(new,text="Process",padx=10,pady=10,fg='black',command= rrr)
    process_button.grid(row=int(num0.get())+1,column=1)

    exit_button = Button(new,text="Exit",padx=10,pady=10,fg='red',command= new.quit)
    exit_button.grid(row=int(num0.get())+2,column=2,padx=10,pady=10)

    global waitrr_label
    waitrr_label = Label(new,text='')

    global turnrr_label
    turnrr_label = Label(new,text='')









def click():
    if clicked.get() == 'FCFS':
        fcfs_window()
    elif clicked.get() == 'SJF (Preemptive)':
        sjfpre_window()
    elif clicked.get() == 'SJF (Non Preemptive)':
        sjfnon_window()
    elif clicked.get() == 'Priority (Preemptive)':
        prioritypre_window()
    elif clicked.get() == 'Priority (Non Preemptive)':
        prioritynon_window()
    elif clicked.get() == 'Round Robin':
        rr_window()
    
    
    #my_label  = Label(root,text = 'Hello '+clicked.get())
    #my_label.pack()


# Algorithms options menu
options = [
    'FCFS',
    'SJF (Preemptive)',
    'SJF (Non Preemptive)',
    'Priority (Preemptive)',
    'Priority (Non Preemptive)',
    'Round Robin',

]

clicked=StringVar()
clicked.set(options[0])

drop_menu = OptionMenu(root,clicked,*options)
drop_menu.pack(padx=10,pady=10)

my_label0  = Label(root,text = 'Enter the number of processes: ')
my_label0.pack(padx=10,pady=10)

global num0
num0 = Entry(root,width=50,fg='black')
num0.pack(padx=10,pady=10)
# en.grid(row=0,column=1)

but = Button(root,text="Select",padx=10,pady=10,bg='white',fg='black',command=click)
but.pack(padx=10,pady=10)

exit_button = Button(root,text="Exit",padx=10,pady=10,bg='white',fg='red',command= root.quit)
exit_button.pack(padx=10,pady=10)
#but['state'] = DISABLED

root.mainloop()
