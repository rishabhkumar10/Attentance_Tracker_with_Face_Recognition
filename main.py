from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter

from PIL import Image,ImageTk
from employee import Employee
import os
from time import strftime
from datetime import datetime
from tain import Train
from facerecognization import detect
from att import attend
from leave import Leave
from hepl import Help


class Face_recognization_system:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1280x690+0+0")
        self.root.title("Face Recognization System")
        
        # first
        img=Image.open(r"project photo\fr-1200.png")
        img=img.resize((450,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        firstlbl=Label(self.root,image=self.photoimg)
        firstlbl.place(x=0,y=0,width=450,height=130)

        # second
        img1=Image.open(r"project photo\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        firstlbl1=Label(self.root,image=self.photoimg1)
        firstlbl1.place(x=450,y=0,width=500,height=130)

        # third
        img2=Image.open(r"project photo\USC-ISI-1200x600-29.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        firstlbl2=Label(self.root,image=self.photoimg2)
        firstlbl2.place(x=900,y=0,width=500,height=130)

        # background
        img3=Image.open(r"project photo\background.jpg")
        img3=img3.resize((1280,690),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        firstlbl3=Label(self.root,image=self.photoimg3)
        firstlbl3.place(x=0,y=130,width=1280,height=590)


        # title lable
        title_lbl=Label(firstlbl3,text="Employee Attendance System Software",font=("time new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1330,height=45)

        #time===
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=('time new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        # employee button
        img4=Image.open(r"project photo\emp.jpg")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(firstlbl3,image=self.photoimg4,command=self.employee_details,cursor="hand2")
        b1.place(x=80,y=80,width=150,height=150)

        b1_1=Button(firstlbl3,text="Employee Details",command=self.employee_details,cursor="hand2",font=("time new roman",10 ,"bold"),bg="blue",fg="white")
        b1_1.place(x=80,y=210,width=150,height=30)


        # detect button
        img5=Image.open(r"project photo\images.jpg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(firstlbl3,image=self.photoimg5,cursor="hand2",command=self.face_recognization)
        b1.place(x=410,y=80,width=150,height=150)

        b1_1=Button(firstlbl3,text="Face Detector",cursor="hand2",command=self.face_recognization,font=("time new roman",10 ,"bold"),bg="blue",fg="white")
        b1_1.place(x=410,y=210,width=150,height=30)

        # attendance button
        img6=Image.open(r"project photo\atte.png")
        img6=img6.resize((160,160),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(firstlbl3,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=710,y=80,width=185,height=150)

        b1_1=Button(firstlbl3,text="Generate Attendance Sheet",cursor="hand2",command=self.attendance_data,font=("time new roman",10 ,"bold"),bg="blue",fg="white")
        b1_1.place(x=710,y=210,width=185,height=30)

        # help button
        img7=Image.open(r"project photo\Pers.png")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(firstlbl3,image=self.photoimg7,cursor="hand2",command=self.help)
        b1.place(x=1010,y=80,width=150,height=150)

        b1_1=Button(firstlbl3,text="Help Desk",cursor="hand2",command=self.help,font=("time new roman",10 ,"bold"),bg="blue",fg="white")
        b1_1.place(x=1010,y=210,width=150,height=30)

        # Train button
        img8=Image.open(r"project photo\rsz.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(firstlbl3,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=80,y=280,width=150,height=150)

        b1_1=Button(firstlbl3,text="Train Data",cursor="hand2",command=self.train_data,font=("time new roman",10 ,"bold"),bg="blue",fg="white")
        b1_1.place(x=80,y=410,width=150,height=30)

        # Photos button
        img9=Image.open(r"project photo\photosss.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(firstlbl3,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b1.place(x=410,y=280,width=150,height=150)

        b1_1=Button(firstlbl3,text="Photos",cursor="hand2",command=self.open_image,font=("time new roman",10 ,"bold"),bg="blue",fg="white")
        b1_1.place(x=410,y=410,width=150,height=30)

        # Developer button
        img10=Image.open(r"project photo\dev.jpg")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(firstlbl3,image=self.photoimg10,cursor="hand2",command=self.leave_data)
        b1.place(x=710,y=280,width=150,height=150)

        b1_1=Button(firstlbl3,text="Leave ",cursor="hand2",command=self.leave_data,font=("time new roman",10 ,"bold"),bg="blue",fg="white")
        b1_1.place(x=710,y=410,width=150,height=30)

        # Exits button
        img11=Image.open(r"project photo\exx.png")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(firstlbl3,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1010,y=280,width=150,height=150)

        b1_1=Button(firstlbl3,text="Exit",cursor="hand2",command=self.iExit,font=("time new roman",10 ,"bold"),bg="blue",fg="white")
        b1_1.place(x=1010,y=410,width=150,height=30)

    # 
    def open_image(self):
        os.startfile("data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognization","Are you sure exit this project ",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    # ================Function buttons===============

    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_recognization(self):
        self.new_window=Toplevel(self.root)
        self.app=detect(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        att_sys = attend(self.new_window,host="localhost", username="root", password="96096", database="employee_attendance_system")
        att_sys.mark_absentees()
        att_sys.close_connections()
        self.app=attend(att_sys)
    
    def leave_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Leave(self.new_window)
        
        
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        

        
        
        







if __name__=="__main__":
    root=Tk()
    obj=Face_recognization_system(root)
    root.mainloop()