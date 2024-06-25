import csv
import mysql.connector

# connect to the database
conn = mysql.connector.connect(host="localhost", username="root", password="96096", database="employee_attendance_system")
# conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# execute a SELECT statement to fetch all the data from the table
c.execute("SELECT * FROM employee")
data = c.fetchall()

# write the data to a CSV file
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# close the database connection
conn.close()
