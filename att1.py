from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog
from datetime import datetime

my_data=[]

class attend:
    def __init__(self,root,host, username, password, database) :
        self.root=root
        self.root.geometry("1280x690+0+0")
        self.root.title("Face Recognization System")

        self.employee_db = mysql.connector.connect(
            host=host, username=username, password=password, database=database
        )

        self.attendance_db = mysql.connector.connect(
            host=host, username=username, password=password, database=database
        )

        self.leave_db = mysql.connector.connect(
            host=host, username=username, password=password, database=database
        )

        


         # first
        img=Image.open(r"project photo\fi.jpg")
        img=img.resize((650,180),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        firstlbl=Label(self.root,image=self.photoimg)
        firstlbl.place(x=0,y=0,width=650,height=180)

        # second
        img1=Image.open(r"project photo\mi.jpg")
        img1=img1.resize((650,180),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        firstlbl1=Label(self.root,image=self.photoimg1)
        firstlbl1.place(x=650,y=0,width=650,height=180)

        # background
        img3=Image.open(r"project photo\background.jpg")
        img3=img3.resize((1280,690),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        firstlbl3=Label(self.root,image=self.photoimg3)
        firstlbl3.place(x=0,y=180,width=1280,height=590)

        # title lable
        title_lbl=Label(firstlbl3,text="Employee Attendance Details",font=("time new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1310,height=45)

        main_frame=Frame(firstlbl3,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1260,height=500)

        
        # right lable frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee's Details",font=("times new roman",12,"bold"))
        right_frame.place(x=5,y=5,width=1243,height=390)

        # table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=1220,height=300)
        # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("Emp_Id","Emp_Name","Dep","Date","Time","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Emp_Id",text="Employee_ID")
        self.AttendanceReportTable.heading("Emp_Name",text="Employee_NAME")
        self.AttendanceReportTable.heading("Dep",text="Department")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"
        # width
        self.AttendanceReportTable.column("Emp_Id",width=100)
        self.AttendanceReportTable.column("Emp_Name",width=100)
        self.AttendanceReportTable.column("Dep",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)
    
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        # self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

         # button frame
        bth_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        bth_frame.place(x=520,y=310,width=160,height=35)
        # save
        save_btn=Button(bth_frame,text="Convert To Csv File",command=self.convert_database_to_csv_and_delete_db,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
    
    @staticmethod
    def convert_database_to_csv_and_delete_db():

        try:
        # connect to the database
            conn = mysql.connector.connect(host="localhost", username="root", password="96096", database="employee_attendance_system")
            c = conn.cursor()

        # execute a SELECT statement to fetch all the data from the table
            c.execute("SELECT * FROM attendance")
            data = c.fetchall()

        # write the data to a CSV file
            with open('data.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)

        # close the database connection
            conn.close()

        # connect to the MySQL server
            conn = mysql.connector.connect(host="localhost", username="root", password="96096",database="employee_attendance_system")

        # create a cursor object
            c = conn.cursor()

        # execute the DROP DATABASE statement to delete the database
            c.execute("TRUNCATE TABLE attendance")

        # close the database connection
            conn.close()
            messagebox.showinfo("Sucess","Attendance Converted to  Csv File  Sucessfully")
        except mysql.connector.Error as error:
            print(f"Error: {error}")



    def mark_absentees(self):
    # Get the list of IDs of employees who haven't marked attendance yet
        cursor = self.attendance_db.cursor()
        cursor.execute("SELECT DISTINCT Emp_Id FROM attendance")
        marked_ids = [row[0] for row in cursor.fetchall()]
        cursor.close()

    # Get the list of employees who haven't marked attendance yet
        cursor = self.employee_db.cursor()
        cursor.execute(
            "SELECT Emp_Id, Emp_Name, dep FROM employee WHERE Emp_Id NOT IN (%s)"
            % ",".join(["%s"] * len(marked_ids)),
            marked_ids,
        )
        unmarked_employees = cursor.fetchall()
        cursor.close()

    # Check if employees are on leave during the current date and time
        now = datetime.now()
        dat = now.strftime("%d/%m/%Y")
        dtstring = now.strftime("%H:%M:%S")
        attendance_data = []
        for employee in unmarked_employees:
            emp_id, emp_name, dep = employee
            cursor = self.leave_db.cursor()
            cursor.execute(
                "SELECT * FROM `leave` WHERE Emp_Id = %s AND DateLeaveFrom <= %s AND DateLeaveTo >= %s",
                (emp_id, dat, dat),
            )
            leave = cursor.fetchone()
            cursor.close()
            if leave:
                # Employee is on leave, mark as leave in the attendance database
                attendance_data.append((emp_id, emp_name, dep, dat, dtstring, leave[5]))
            else:
                # Employee is absent, mark as absent in the attendance database
                attendance_data.append((emp_id, emp_name, dep, dat, dtstring, "absent"))

        # Update the attendance database with the new attendance data
        cursor = self.attendance_db.cursor()
        cursor.executemany(
            "INSERT INTO attendance (Emp_Id, Emp_Name, Department, Date, Time, Status) VALUES (%s, %s, %s, %s, %s, %s)",
            attendance_data,
        )
        self.attendance_db.commit()
        self.fetch_data()
        cursor.close()

    def close_connections(self):
        self.employee_db.close()
        self.attendance_db.close()
        self.leave_db.close()

    


    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="96096",database="employee_attendance_system")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from attendance")
        data=my_cursur.fetchall()

        if len(data)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close()
    

if __name__ == "__main__":
  
    root=Tk()
    # Connect to the employee and attendance databases
    att_sys = attend(root,host="localhost", username="root", password="96096", database="employee_attendance_system")

    # Mark absent for the employees who haven't marked attendance yet
    att_sys.mark_absentees()

    # Close the database connections
    att_sys.close_connections()
    # att_sys.fetch_data()
    
    # obj=atten(root)
    # boj1=AttendanceSystem(root)
    root.mainloop()