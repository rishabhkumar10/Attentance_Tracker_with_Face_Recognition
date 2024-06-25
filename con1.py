import csv
import mysql.connector

# connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="96096",
    database="employee_attendance_system"
)

# retrieve data from the database table
cursor = conn.cursor()
cursor.execute("SELECT * FROM `leave`")
rows = cursor.fetchall()

# write data to a CSV file
with open("con1.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["emp_id", "emp_name", "gender", "dep", "dob", "reasone", "dateleave"]) # write header row
    for row in rows:
        writer.writerow(row)

# close the database connection
conn.close()
