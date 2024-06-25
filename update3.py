# import mysql.connector
# from datetime import datetime

# # Connect to the employee and attendance databases
# employee_db = mysql.connector.connect(
#  host="localhost", username="root", password="96096", database="employee_attendance_system"
# )

# attendance_db = mysql.connector.connect(
#   host="localhost", username="root", password="96096", database="employee_attendance_system"
# )

# # Get the list of IDs of employees who haven't marked attendance yet
# cursor = attendance_db.cursor()
# cursor.execute("SELECT DISTINCT Emp_Id FROM attendance")
# marked_ids = [row[0] for row in cursor.fetchall()]
# cursor.close()

# cursor = employee_db.cursor()
# cursor.execute("SELECT Emp_Id, Emp_Name, dep FROM employee WHERE Emp_Id NOT IN (%s)" % ",".join(["%s"] * len(marked_ids)), marked_ids)
# unmarked_employees = cursor.fetchall()
# cursor.close()

# # Mark absent for the employees who haven't marked attendance yet
# now = datetime.now()
# dat = now.strftime("%d/%m/%Y")
# dtstring = now.strftime("%H:%M:%S")
# attendance_data = [(e[0], e[1], e[2], dtstring, dat, "absent") for e in unmarked_employees]

# cursor = attendance_db.cursor()
# cursor.executemany("INSERT INTO attendance (Emp_Id, Emp_Name, Department, Date, Time, Status) VALUES (%s, %s, %s, %s, %s, %s)", attendance_data)
# attendance_db.commit()
# cursor.close()

# # Close the database connections
# employee_db.close()
# attendance_db.close()
