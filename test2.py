import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

class Attendd:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x690+0+0")
        self.root.title("Face Recognition System")

        # Load and resize the first image
        img = Image.open(r"project photo\fi.jpg")
        img = img.resize((650, 180), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        firstlbl = Label(self.root, image=self.photoimg)
        firstlbl.place(x=0, y=0, width=650, height=180)

        # Load and resize the second image
        img1 = Image.open(r"project photo\mi.jpg")
        img1 = img1.resize((650, 180), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        firstlbl1 = Label(self.root, image=self.photoimg1)
        firstlbl1.place(x=650, y=0, width=650, height=180)

        # Load and resize the background image
        img3 = Image.open(r"project photo\background.jpg")
        img3 = img3.resize((1280, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        firstlbl3 = Label(self.root, image=self.photoimg3)
        firstlbl3.place(x=0, y=180, width=1280, height=590)

        # Title label
        title_lbl = Label(firstlbl3, text="Employee Leave Details", font=("time new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1310, height=45)

        # Main frame
        main_frame = Frame(firstlbl3, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1260, height=500)

        # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Employee's Leave Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=5, y=5, width=1243, height=390)

        # Table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=1220, height=300)

        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("Emp_Id", "Emp_Name", "Department",
                                                                       "TotalNoOfAbsence", "TotalNoOfLeave"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Emp_Id", text="Employee ID")
        self.AttendanceReportTable.heading("Emp_Name", text="Employee Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("TotalNoOfAbsence", text="Total No. of Absence")
        self.AttendanceReportTable.heading("TotalNoOfLeave", text="Total No. of Leave")

        self.AttendanceReportTable["show"] = "headings"

        # Set column widths
        self.AttendanceReportTable.column("Emp_Id", width=100)
        self.AttendanceReportTable.column("Emp_Name", width=150)
        self.AttendanceReportTable.column("Department", width=150)
        self.AttendanceReportTable.column("TotalNoOfAbsence", width=150)
        self.AttendanceReportTable.column("TotalNoOfLeave", width=150)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.check_and_update_leave_absence()
        self.fetch_data()

    def check_and_update_leave_absence(self):
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

        # Check if leaveandabs table is empty
        cursor = leaveandabs_db.cursor()
        cursor.execute("SELECT COUNT(*) FROM leaveandabs")
        result = cursor.fetchone()[0]
        cursor.close()

        if result == 0:  # Table is empty, count leaves and absences for all records
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
                    "SELECT COUNT(*) FROM attendance WHERE Emp_Id = %s AND Status LIKE '%%Leave%%'",
                    (emp_id,)
                )
                leave_count = int(cursor.fetchone()[0])
                cursor.close()

                cursor = attendance_db.cursor()
                cursor.execute(
                    "SELECT COUNT(*) FROM attendance WHERE Emp_Id = %s AND Status = 'absent'",
                    (emp_id,)
                )
                absence_count = int(cursor.fetchone()[0])
                cursor.close()

                leave_abs_data.append((emp_id, emp_name, department, absence_count, leave_count))

            # Insert the leave and absence counts into the leaveandabs database
            cursor = leaveandabs_db.cursor()
            cursor.executemany(
                "INSERT INTO leaveandabs (Emp_Id, Emp_Name, Department, TotalNoOfAbsence, TotalNoOfLeave) VALUES (%s, %s, %s, %s, %s)",
                leave_abs_data
            )
            leaveandabs_db.commit()
            cursor.close()

        # else:  # Table is not empty, update leave and absence counts
        #     # Get the TotalNoOfLeave and TotalNoOfAbsence from leaveandabs database
        #     cursor = leaveandabs_db.cursor()
        #     cursor.execute("SELECT Emp_Id, TotalNoOfAbsence, TotalNoOfLeave FROM leaveandabs")
        #     employees = cursor.fetchall()
        #     cursor.close()

        #     # Update leave and absence counts for each employee
        #     for emp_id, total_absence_count, total_leave_count in employees:
        #         # Get the leave and absence counts from attendance table
        #         cursor = attendance_db.cursor()
        #         cursor.execute(
        #             "SELECT COUNT(*) FROM attendance WHERE Emp_Id = %s AND Status LIKE '%%Leave%%'",
        #             (emp_id,)
        #         )
        #         leave_count = int(cursor.fetchone()[0])
        #         cursor.close()

        #         cursor = attendance_db.cursor()
        #         cursor.execute(
        #             "SELECT COUNT(*) FROM attendance WHERE Emp_Id = %s AND Status = 'absent'",
        #             (emp_id,)
        #         )
        #         absence_count = int(cursor.fetchone()[0])
        #         cursor.close()

        #         # Calculate the updated leave and absence counts
        #         updated_leave_count = leave_count + total_leave_count
        #         updated_absence_count = absence_count + total_absence_count

        #         # Update the leave and absence counts in leaveandabs table
        #         cursor = leaveandabs_db.cursor()
        #         cursor.execute(
        #             "UPDATE leaveandabs SET TotalNoOfAbsence = %s, TotalNoOfLeave = %s WHERE Emp_Id = %s",
        #             (updated_absence_count, updated_leave_count, emp_id)
        #         )
        #         leaveandabs_db.commit()
        #         cursor.close()

        # Close the database connections
        attendance_db.close()
        leaveandabs_db.close()

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="96096",
            database="employee_attendance_system"
        )
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
