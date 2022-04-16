# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 14:11:53 2022

@author: east asia
"""

import prenonsjf
num = int(input('Enter number of processes '))
proc = [[0]*3]*num
gData = {}
for i in range(num):
    id = input('Enter  process ID ')
    print('For process '+id)
    arrival = int(input('Enter arrival time '))
    burst = int(input('Enter CPU burst time '))
    #completed=0
    # waiting time
    proc[i][0]= arrival
    proc[i][1]= burst
    #completed =proc[i][2]
    proc[i][2]= id
    gData.update({proc[i][2]:[proc[i][0],proc[i][1]]})
#gData = {'P1': [0,10], 'P2': [1,2], 'P3': [4,4], 'P4':[5,1], 'P5': [10,3], 'P6':[21,12]}
gQuant = 4
gContSwitch = 0.4
sjfScheduling,sjfLine = prenonsjf.sjf(gData)
srtfScheduling,srtfLine = prenonsjf.srtf(gData)
prenonsjf.printData(gData,sjfScheduling,sjfLine,'Shortest Job First')
prenonsjf.printData(gData,srtfScheduling,srtfLine,'Shortest Remaning Time First')
