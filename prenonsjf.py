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
    avgWT,avgTT =0,0
    plinestr= "0 -> "
    print(Name.upper())
    print('| PROCESS | ARRIVAL | BURST | WAIT |')
    for key,value in sorted(cData.items()):
        print('{:>4}{:>10}{:>10}{:>10}'.format(key,gData[key][0],gData[key][1],value[0]))
        avgWT += value[0]
        avgTT += value[1]
    print('Average Wait Time = {}'.format(avgWT/len(cData)))
    for x in pLine:
        plinestr += ('{} -> {} -> '.format(x[0],x[1]))
    print('{}\n'.format(plinestr[:-3]))




