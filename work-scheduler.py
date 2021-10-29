import json
from datetime import datetime, timedelta


with open('config.json', 'r') as config_file:
    configurations = json.load(config_file)

print("start time (h:m) -", end=" ")
start_hour, start_minute = map(int, input().split(":"))

print("number of work periods -", end=" ")
work_periods = int(input())

time = datetime(datetime.today().year, datetime.today().month, datetime.today().day, start_hour, start_minute)

#-------------------------

path = configurations["pathToSchedules"]
strtime = time.strftime("%Y.%m.%d")

with open("{0}/{1} - schedule.txt".format(path, strtime), "w") as schedule_file:
    schedule_file.write("{} ({}):\n".format(time.strftime("%m/%d"), time.strftime("%A")[:2]))
    schedule_file.write("\nTasks:\n-\n\n")
    schedule_file.write("\nPlans:\n-\n\n")
    schedule_file.write("\nTime ({}):\n".format(work_periods))

    workDuration = int(configurations["workDuration"])
    breakDuration = int(configurations["breakDuration"])

    for i in range(1, work_periods + 1):
        schedule_file.write("{0:2}) {1} - {2} | \n".format(i, time.strftime("%I:%M"), (time + timedelta(minutes = workDuration)).strftime("%I:%M")))
        time += timedelta(minutes = workDuration + breakDuration)

    schedule_file.write("\nProductivity: _%")
