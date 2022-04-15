class RoundRobin:
    
    def Process(self):
        
        process_data = []
        ready_queue = []
        executed_process = []
        time = 0
        start_time = []
        exit_time = []
        
        
        n=int(input("Enter number of process: "))
        
        for i in range(n):
            
            temporary = []
            process_id = i
            
            
            arrival_time = float(input(f"Enter Arrival Time for P{i}: " ))
            
            
            burst_time = float(input(f"Enter Burst Time for P{i}: " ))
            
            
            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            process_data.append(temporary)
            
            
        quantum = int(input("Enter Time quantum: "))
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
        
        print("Process_ID  Arrival_Time  Rem_Burst_Time   Completed  Original_Burst_Time     Completion_Time     Turnaround_Time     Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                
                print(process_data[i][j], end="				")
                
            print()
            
        print(f'Average Turnaround Time: {AvgT_time}')
        
        print(f'Average Waiting Time: {AvgW_time}')
            
        print(f'Sequence of Processes: {executed_process}')


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
        
        


if __name__ == "__main__":
    
    rr = RoundRobin()
    rr.Process()
