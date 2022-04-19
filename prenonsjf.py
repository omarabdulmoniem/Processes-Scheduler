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
    print(Name.upper())
    
    # This block prints data in an organized shape
    #print('| PROCESS | ARRIVAL | BURST | WAIT | TURNAROUND')
    for key,value in sorted(cData.items()):
        #print('{:>4}{:>10}{:>10}{:>10}'.format(key,gData[key][0],gData[key][1],value[0]))
        
        # This block prints data in order (use either blocks not both)
        #process data
        print('Process ID:',key)
        print('Arrival time:',gData[key][0])
        print('Burst time:',gData[key][1])
        print('waiting time: ',value[0])
        print('Turnaround time: ',value[1])
        
        #sum of waiting time, turnaround time
        sumWT += value[0]
        sumTT += value[1]
        
        #average waiting time
        avgwait= sumWT/len(cData)
       
        #average turnaround time
        avgturnaround=sumTT/len(cData)
        
    print('Average Wait Time = ',avgwait)
    print('Average Turnaround Time = ',avgturnaround)
    
    # Line similar to gantt chart
    for x in pLine:
        plinestr += ('{} -> {} -> '.format(x[0],x[1]))
    print('{}\n'.format(plinestr[:-3]))

    


