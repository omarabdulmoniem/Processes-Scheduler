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


class prenonsjf:

    def mainsjf(self):
        num = int(num0.get())

        #define processes list
        proc = [[0]*3]*num

        # define data dictionary
        gData = {}

        # ask user for input
        y=int(0)
        for i in info_list:
            
            ID = 'P{y}'
            arrival = int(i[1].get())
            burst = int(i[0].get())

            #store process data
            proc[y][0]= arrival
            proc[y][1]= burst
            proc[y][2]= ID
            # put data in dictionary
            gData.update({proc[y][2]:[proc[y][0],proc[y][1]]})
            y=y+1

        #calling printData 
        if clicked.get() == 'SJF (Preemptive)':
            # calling sjf function, store return value (tt,wt,process line)
            sjfScheduling,sjfLine = prenonsjf.sjf(gData)
            prenonsjf.printData(gData,sjfScheduling,sjfLine,'Shortest Job First')
        else:
            # calling srtf function, store return value (tt,wt,process line)
            srtfScheduling,srtfLine = prenonsjf.srtf(gData)
            prenonsjf.printData(gData,srtfScheduling,srtfLine,'Shortest Remaning Time First')

        # Shortest Job First
    def sjf(dict):
        begHold,endHold = 0,0
        sjfdict,tempdict,sortdict,pLine ={},{},{},[]
        for key,value in dict.items():
            at,bt = value[0],value[1]
            if (begHold == 0):
                endHold += bt
                sjfdict[key] = [begHold-at,bt-at]
                pLine.append([key,endHold])
                begHold = bt
            else:
                tempdict[key] = value[0],value[1]
        for key,value in sorted(tempdict.items(), key = lambda x : x[1][1]):
            sortdict[key] = value[0],value[1]
        for key,value in sortdict.items():
            at,bt = value[0],value[1]
            if(begHold-at > 0):
                endHold += bt
                sjfdict[key] = [begHold-at,endHold-at]
                pLine.append([key,endHold])
                begHold += bt
            else:
                endHold += bt
                sjfdict[key] = [0,bt]
                pLine.append([key,endHold+1])
                begHold += bt

        return sjfdict,pLine

    #Shortest Remaining Time First Function
    def srtf(dict):
        begHold,endHold = 0,0
        srtfdict,tempdict,sortdict,pLine = {},{},{},[]
        for key,value in dict.items():
            at,bt = value[0],value[1]
            
            print(at,bt)
            if (begHold == 0):
                second = list(dict.values())[1]
                srtfdict[key] = [begHold-at, bt-second[0]-at]
                endHold += bt-second[0]
                begHold = bt-second[0]
                tempdict[key] = at, bt-begHold
                pLine.append([key,endHold])
            else:
                tempdict[key] = at,bt
        for key,value in reversed(sorted(tempdict.items(), key = lambda x : x[1][1],reverse=True)):
            sortdict[key] = value[0],value[1]
        for key,value in sortdict.items():
            at,bt = value[0], value[1]
            if key in srtfdict.keys():
                hold = srtfdict[key]
                endHold += bt
                srtfdict[key] = [begHold-hold[1],endHold-at]
                pLine.append([key,endHold])
                begHold += bt
            elif(begHold-at > 0):
                endHold += bt
                srtfdict[key] = [begHold-at,endHold-at]
                pLine.append([key,endHold])
                begHold += bt
            else:
                endHold += bt
                srtfdict[key] = [0,bt]
                pLine.append([key,endHold+1])
                begHold += bt
        return srtfdict, pLine

    def printData(gData, cData, pLine, Name):
        sumWT,sumTT =0,0
        plinestr= "0 -> "
        #print(Name.upper())
        
        # This block prints data in an organized shape
        #print('| PROCESS | ARRIVAL | BURST | WAIT | TURNAROUND')
        for key,value in sorted(cData.items()):
            #print('{:>4}{:>10}{:>10}{:>10}'.format(key,gData[key][0],gData[key][1],value[0]))
            
            # This block prints data in order (use either blocks not both)
            #process data
            #print('Process ID:',key)
            #print('Arrival time:',gData[key][0])
            #print('Burst time:',gData[key][1])
            #print('waiting time: ',value[0])
            #print('Turnaround time: ',value[1])
            
            #sum of waiting time, turnaround time
            sumWT += value[0]
            sumTT += value[1]
            
            #average waiting time
            avgwait= sumWT/len(cData)
        
            #average turnaround time
            avgturnaround=sumTT/len(cData)
        
        waitsjf_label.config(text = 'average wait time is: '+ str(avgwait), bg= '#772020',fg='white',font=('Arial', 14))
        waitsjf_label.grid(row=int(num0.get())+3,column=2,padx=10,pady=10)

        turnsjf_label.config(text = 'average turn around time is: '+ str(avgturnaround), bg= '#772020',fg='white',font=('Arial', 14))
        turnsjf_label.grid(row=int(num0.get())+4,column=2,padx=10,pady=10)


        #print('Average Wait Time = ',avgwait)
        #print('Average Turnaround Time = ',avgturnaround)
        
        # Line similar to gantt chart
        #for x in pLine:
        #    plinestr += ('{} -> {} -> '.format(x[0],x[1]))
        #print('{}\n'.format(plinestr[:-3]))

        #prenonsjf.prlabel(avgwait,avgturnaround)
    
    #def prlabel(avwait,avturn):
    #    waitsjf_label.config(text = 'av wait time is: '+ str(avwait), bg= '#772020',fg='white')
    #    waitsjf_label.grid(row=int(num0.get())+3,column=2,padx=10,pady=10)
    #
    #    turnsjf_label.config(text = 'turn around time is: '+ str(avturn), bg= '#772020',fg='white')
    #    turnsjf_label.grid(row=int(num0.get())+4,column=2,padx=10,pady=10)
    




def sjfprocess():
    x = prenonsjf()
    x.mainsjf()




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


    process_button = Button(new,text="Process",padx=10,pady=10,fg='black',command= sjfprocess)
    process_button.grid(row=int(num0.get()),column=1)

    exit_button = Button(new,text="Exit",padx=10,pady=10,fg='red',command= new.quit)
    exit_button.grid(row=int(num0.get())+1,column=2,padx=10,pady=10)


    global waitsjf_label
    waitsjf_label = Label(new,text='')

    global turnsjf_label
    turnsjf_label = Label(new,text='')



# SJF Non preemetive Algorithm

def sjfnon_window():
    sjfpre_window()


    
# Round Robin Algorithm


class RoundRobin:
    
    def Process(self):
        
        process_data = []
        ready_queue = []
        executed_process = []
        time = 0
        start_time = []
        exit_time = []
        
        
        n = rrnumber
        
        for i in info_list:
            
            temporary = []
            process_id = 0
            
            
            arrival_time = float(i[1].get())
            
            
            burst_time = float(i[0].get())
            
            
            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            process_data.append(temporary)
            
            
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

    def printrr(self,AvgTurn_time,AvgWait_time):
        waitrr_label.config(text = 'average wait time is: '+ str(AvgWait_time), bg= '#772020',fg='white',font=('Arial', 14))
        waitrr_label.grid(row=int(num0.get())+5,column=2,padx=10,pady=10)
    
        turnrr_label.config(text = 'average turn around time is: '+ str(AvgTurn_time), bg= '#772020',fg='white',font=('Arial', 14))
        turnrr_label.grid(row=int(num0.get())+6,column=2,padx=10,pady=10)





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