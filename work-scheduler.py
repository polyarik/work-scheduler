from datetime import datetime, timedelta

print("start time (h:m) -", end=" ")
start_hour, start_minute = map(int, input().split(":"))

print("number of work periods -", end=" ")
work_periods = int(input())

time = datetime(datetime.today().year, datetime.today().month, datetime.today().day, start_hour, start_minute)

#-------------------------

file = open(time.strftime("%Y.%m.%d")+".txt", "w")

file.write("{} ({}):\n".format(time.strftime("%m/%d"), time.strftime("%A")[:2]))
file.write("\nTasks:\n-\n\n")
file.write("\nPlans:\n-\n\n")
file.write("\nTime ({}):\n".format(work_periods))

for i in range(1, work_periods + 1):
    file.write("{0:2}) {1} - {2} | \n".format(i, time.strftime("%I:%M"), (time + timedelta(minutes = 52)).strftime("%I:%M")))
    time += timedelta(minutes = 52 + 17)

file.write("\nProductivity: _%")