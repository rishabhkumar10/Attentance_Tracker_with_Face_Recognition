import mysql.connector
from datetime import datetime

class AttendanceSystem:
    def __init__(self, host, username, password, database):
        self.employee_db = mysql.connector.connect(
            host=host, username=username, password=password, database=database
        )

        self.attendance_db = mysql.connector.connect(
            host=host, username=username, password=password, database=database
        )

    def mark_absentees(self):
        # Get the list of IDs of employees who haven't marked attendance yet
        cursor = self.attendance_db.cursor()
        cursor.execute("SELECT DISTINCT Emp_Id FROM attendance")
        marked_ids = [row[0] for row in cursor.fetchall()]
        cursor.close()

        cursor = self.employee_db.cursor()
        cursor.execute(
            "SELECT Emp_Id, Emp_Name, dep FROM employee WHERE Emp_Id NOT IN (%s)"
            % ",".join(["%s"] * len(marked_ids)),
            marked_ids,
        )
        unmarked_employees = cursor.fetchall()
        cursor.close()

        # Mark absent for the employees who haven't marked attendance yet
        now = datetime.now()
        dat = now.strftime("%d/%m/%Y")
        dtstring = now.strftime("%H:%M:%S")
        attendance_data = [
            (e[0], e[1], e[2], dtstring, dat, "absent") for e in unmarked_employees
        ]

        cursor = self.attendance_db.cursor()
        cursor.executemany(
            "INSERT INTO attendance (Emp_Id, Emp_Name, Department, Date, Time, Status) VALUES (%s, %s, %s, %s, %s, %s)",
            attendance_data,
        )
        self.attendance_db.commit()
        cursor.close()

    def close_connections(self):
        self.employee_db.close()
        self.attendance_db.close()

def main():
    # Connect to the employee and attendance databases
    att_sys = AttendanceSystem(host="localhost", username="root", password="96096", database="employee_attendance_system")

    # Mark absent for the employees who haven't marked attendance yet
    att_sys.mark_absentees()

    # Close the database connections
    att_sys.close_connections()

if __name__ == "__main__":
    main()
