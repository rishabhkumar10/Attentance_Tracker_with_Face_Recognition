# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os 
# import csv
# from tkinter import filedialog
# # from upcls import AttendanceSystem

# my_data=[]

# class atten:
#     def __init__(self,root) :
#         self.root=root
#         self.root.geometry("1280x690+0+0")
#         self.root.title("Face Recognization System")

        


#          # first
#         img=Image.open(r"project photo\fi.jpg")
#         img=img.resize((650,180),Image.ANTIALIAS)
#         self.photoimg=ImageTk.PhotoImage(img)

#         firstlbl=Label(self.root,image=self.photoimg)
#         firstlbl.place(x=0,y=0,width=650,height=180)

#         # second
#         img1=Image.open(r"project photo\mi.jpg")
#         img1=img1.resize((650,180),Image.ANTIALIAS)
#         self.photoimg1=ImageTk.PhotoImage(img1)

#         firstlbl1=Label(self.root,image=self.photoimg1)
#         firstlbl1.place(x=650,y=0,width=650,height=180)

#         # background
#         img3=Image.open(r"project photo\background.jpg")
#         img3=img3.resize((1280,690),Image.ANTIALIAS)
#         self.photoimg3=ImageTk.PhotoImage(img3)

#         firstlbl3=Label(self.root,image=self.photoimg3)
#         firstlbl3.place(x=0,y=180,width=1280,height=590)

#         # title lable
#         title_lbl=Label(firstlbl3,text="Employee Attendance Details",font=("time new roman",35,"bold"),bg="white",fg="blue")
#         title_lbl.place(x=0,y=0,width=1310,height=45)

#         main_frame=Frame(firstlbl3,bd=2,bg="white")
#         main_frame.place(x=5,y=55,width=1260,height=500)

        
#         # right lable frame
#         right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee's Details",font=("times new roman",12,"bold"))
#         right_frame.place(x=5,y=5,width=1243,height=390)

#         # table frame
#         table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
#         table_frame.place(x=5,y=5,width=1220,height=360)
#         # scroll bar
#         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
#         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
#         self.AttendanceReportTable=ttk.Treeview(table_frame,column=("Emp_Id","Emp_Name","Dep","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM,fill=X)
#         scroll_y.pack(side=RIGHT,fill=Y)
#         scroll_x.config(command=self.AttendanceReportTable.xview)
#         scroll_y.config(command=self.AttendanceReportTable.yview)

#         self.AttendanceReportTable.heading("Emp_Id",text="Employee_ID")
#         self.AttendanceReportTable.heading("Emp_Name",text="Employee_NAME")
#         self.AttendanceReportTable.heading("Dep",text="Department")
#         self.AttendanceReportTable.heading("Time",text="Time")
#         self.AttendanceReportTable.heading("Date",text="Date")
#         self.AttendanceReportTable.heading("Attendance",text="Attendance")
#         self.AttendanceReportTable["show"]="headings"
#         # width
#         self.AttendanceReportTable.column("Emp_Id",width=100)
#         self.AttendanceReportTable.column("Emp_Name",width=100)
#         self.AttendanceReportTable.column("Dep",width=100)
#         self.AttendanceReportTable.column("Time",width=100)
#         self.AttendanceReportTable.column("Date",width=100)
#         self.AttendanceReportTable.column("Attendance",width=100)
    
#         self.AttendanceReportTable.pack(fill=BOTH,expand=1)
#         # self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        





# if __name__=="__main__":
#     root=Tk()
#     obj=atten(root)
#     # boj1=AttendanceSystem(root)
#     root.mainloop()