import csv
from datetime import datetime

# Read the employee data from the data.csv file
with open("data.csv", "r", newline="\n") as f:
    reader = csv.reader(f)
    data = list(reader)

# Read the attendance data from the attendance.csv file
with open("attendance.csv", "r", newline="\n") as f:
    reader = csv.reader(f)
    attendance = list(reader)

# Get the list of IDs of employees who haven't marked attendance yet
# ids = [entry[0] for entry in data if entry[0] not in [a[0] for a in attendance]]
ids = [entry[0] for entry in data if len(entry) > 0 and entry[0] not in [a[0] for a in attendance]]




# Mark absent for the employees who haven't marked attendance yet
now = datetime.now()
dat = now.strftime("%d/%m/%Y")
dtstring = now.strftime("%H:%M:%S")
for id in ids:
    for entry in data:
        if entry[0] == id:
            name = entry[1]
            dep=entry[6]
            break
    else:
        continue
    
    attendance.append([id, name, dep,dtstring, dat, "absent"])

# Write the updated attendance data to the attendance.csv file
with open("attendance.csv", "w", newline="\n") as f:
    writer = csv.writer(f)
    writer.writerows(attendance)

