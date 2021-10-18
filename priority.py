#TAT = CT - AT => CT = AT + TAT
#WT = TAT - BT => TAT = BT + WT
#TAT = BT + WT => BT = TAT - WT
#CT = ST + BT => CT = ST + TAT - WT

#for creating a 2D Array

n = 5
process = []
for i in range(5):
	l = []
	for j in range(4):
		l.append(0)
	process.append(l)

def findWaitingTime( waitingTime):
	cumulativeBurstTime = [0] * 5
	cumulativeBurstTime[0] = 0
	waitingTime[0] = 0

	for i in range(1, n):
		cumulativeBurstTime[i] = process[i - 1][1] + cumulativeBurstTime[i - 1]
		waitingTime[i] = cumulativeBurstTime[i] - process[i][0]
		if(waitingTime[i] < 0) :	
			waitingTime[i] = 0
		
def findTurnAroundTime(turnAroundTime, waitingTime):

	for i in range(n):
		turnAroundTime[i] = process[i][1] + waitingTime[i]

def findGanttChart():
	waitingTime = [0] * 5
	turnAroundTime = [0] * 5

	avgWaitingTime = 0
	avgTurnAroundTime = 0
	
	findWaitingTime(waitingTime)
	findTurnAroundTime(turnAroundTime, waitingTime)

	startTime = [0] * 5
	completionTime = [0] * 5
	startTime[0] = 1
	completionTime[0] = startTime[0] + turnAroundTime[0]
	
	for i in range(1, n):
		startTime[i] = completionTime[i - 1]
		completionTime[i] = startTime[i] + turnAroundTime[i] - waitingTime[i]

	print("Process ID\tStart Time\tCompletetion Time",
			"\tTurn Around Time\tWaiting Time\t Priority")
	for i in range(n):
		avgWaitingTime += waitingTime[i]
		avgTurnAroundTime += turnAroundTime[i]
		
		print(process[i][3], "\t\t", startTime[i],"\t\t", end = " ")
		print(completionTime[i], "\t\t\t", turnAroundTime[i], "\t\t\t", waitingTime[i], "\t\t\t", priority[i])

	print("Average waiting time is : ", end = " ")
	print(avgWaitingTime / n)
	
	print("Average turnaround time : " , end = " ")
	print(avgTurnAroundTime / n)


if __name__ =="__main__":
	arrivalTime = [1, 2, 3, 4, 5]
	burstTime = [3, 5, 1, 7, 4]
	priority = [3, 4, 1, 7, 8]
	
	for i in range(n):

		process[i][0] = arrivalTime[i]
		process[i][1] = burstTime[i]
		process[i][2] = priority[i]
		process[i][3] = i + 1

	#for sorting in priority order	
	process = sorted (process, key = lambda x:x[2])
	process = sorted (process)

	findGanttChart()

