import csv

class midterm:

    def __init__(self, SubmissionID, StudentID, Problem, Status, Score, CodeLength, SubmissionTime):
        self.SubmissionID = SubmissionID
        self.StudentID = StudentID
        self.Problem = Problem
        self.Status = Status
        self.Score = Score
        self.CodeLength = CodeLength
        self.SubmissionTime = SubmissionTime

file = open('midterm2.csv', 'r')
data = csv.reader(file)
next(data)

allData = []
for row in data:
    allData.append(midterm(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

#input
startTime, endTime = input("Start time, End time (hh:mm:ss hh:mm:ss): ").split(" ")
sepStartTime = startTime.split(":")
sepEndTime = endTime.split(":")
ans = [[0 for x in range(5)] for y in range(4)]
ProbStatus = ["Accepted", "Compile Error", "Runtime Error", "Time Limit Exceed", "Wrong Answer"]
#Accepted, Compile Error, Runtime Error, Time Limit Exceed, Wrong Answer
for x in allData:
    time = x.SubmissionTime.split(":")
    if (int(sepStartTime[0])*3600+int(sepStartTime[1])*60+int(sepStartTime[2])
        >int(time[0])*3600+int(time[1])*60+int(time[2])):
        break;
    if (int(sepEndTime[0])*3600+int(sepEndTime[1])*60+int(sepEndTime[2])
        <int(time[0])*3600+int(time[1])*60+int(time[2])):
        continue;

    ans[int(x.Problem)-1][ProbStatus.index(x.Status)] += 1

for x in range(4):
    for y in range(5):
        if y!=4:
            print(ans[x][y], end=" ")
        else:
            print(ans[x][y], end="")
    print(end=";")