import prenonsjf

num = int(input('Enter number of processes '))

#define processes list
proc = [[0]*3]*num

# define data dictionary
gData = {}

# ask user for input
for i in range(num):
    
    ID = input('Enter  process ID ')
    print('For process '+ID)
    arrival = int(input('Enter arrival time '))
    burst = int(input('Enter CPU burst time '))

    #store process data
    proc[i][0]= arrival
    proc[i][1]= burst
    proc[i][2]= ID
    
    # put data in dictionary
    gData.update({proc[i][2]:[proc[i][0],proc[i][1]]})

# calling sjf function, store return value (tt,wt,process line)
sjfScheduling,sjfLine = prenonsjf.sjf(gData)

# calling srtf function, store return value (tt,wt,process line)
srtfScheduling,srtfLine = prenonsjf.srtf(gData)

#calling printData 
prenonsjf.printData(gData,sjfScheduling,sjfLine,'Shortest Job First')
prenonsjf.printData(gData,srtfScheduling,srtfLine,'Shortest Remaning Time First')
