import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import date, datetime, timedelta

class Attendd:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x690+0+0")
        self.root.title("Face Recognition System")

        # ... Rest of the code ...

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.count_leave_absence()
        self.fetch_data()

    def count_leave_absence(self):
        # Connect to the attendance database
        attendance_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="96096",
            database="employee_attendance_system"
        )

        # Connect to the leaveandabs database
        leaveandabs_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="96096",
            database="employee_attendance_system"
        )

        # Get the current date and the next date
        today = date.today()
        next_date = today + timedelta(days=1)

        # Get the list of employees with their names and departments
        cursor = attendance_db.cursor()
        cursor.execute("SELECT DISTINCT Emp_Id, Emp_Name, Department FROM attendance")
        employees = cursor.fetchall()
        cursor.close()

        # Count leaves and absences for each employee
        leave_abs_data = []
        for emp_id, emp_name, department in employees:
            cursor = attendance_db.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM attendance WHERE Emp_Id = %s AND Status LIKE 'leave%%' AND Date = %s",
                (emp_id, next_date)
            )
            leave_count = cursor.fetchone()[0]
            cursor.close()

            cursor = attendance_db.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM attendance WHERE Emp_Id = %s AND Status = 'absent' AND Date = %s",
                (emp_id, next_date)
            )
            absence_count = cursor.fetchone()[0]
            cursor.close()

            leave_abs_data.append((emp_id, emp_name, department, absence_count, leave_count))

        # Check if data already exists for the next date in the leaveandabs table
        cursor = leaveandabs_db.cursor()
        cursor.execute("SELECT COUNT(*) FROM leaveandabs WHERE Date = %s", (next_date,))
        data_exists = cursor.fetchone()[0] > 0
        cursor.close()

        if data_exists:
            # Update the leave and absence counts for the next date
            cursor = leaveandabs_db.cursor()
            for emp_id, emp_name, department, absence_count, leave_count in leave_abs_data:
                cursor.execute(
                    "UPDATE leaveandabs SET TotalNoOfAbsence = %s, TotalNoOfLeave = %s WHERE Emp_Id = %s AND Date = %s",
                    (absence_count, leave_count, emp_id, next_date)
                )
            leaveandabs_db.commit()
            cursor.close()
        else:
            # Insert the leave and absence counts for the next date
            cursor = leaveandabs_db.cursor()
            for emp_id, emp_name, department, absence_count, leave_count in leave_abs_data:
                cursor.execute(
                    "INSERT INTO leaveandabs (Emp_Id, Emp_Name, Department, TotalNoOfAbsence, TotalNoOfLeave, Date) VALUES (%s, %s, %s, %s, %s, %s)",
                    (emp_id, emp_name, department, absence_count, leave_count, next_date)
                )
            leaveandabs_db.commit()
            cursor.close()

        # Close database connections
        attendance_db.close()
        leaveandabs_db.close()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="96096", database="employee_attendance_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM leaveandabs")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("", END, values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Attendd(root)
    root.mainloop()
