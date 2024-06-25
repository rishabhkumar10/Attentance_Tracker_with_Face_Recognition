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
from test2 import Attendd

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x690+0+0")
        self.root.title("Face Recognization System")

        title_lbl=Label(self.root,text="HELP DESK",font=("time new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1310,height=45)

        # Top image
    
        img_top=Image.open(r"project photo\help.jpeg")
        img_top=img_top.resize((1280,550),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        firstlbl2=Label(self.root,image=self.photoimg_top)
        firstlbl2.place(x=0,y=55,width=1280,height=550)



        # main_frame=Frame(firstlbl2,bd=2,bg="white")
        # main_frame.place(x=1000,y=0,width=500,height=500)


        # img_top1=Image.open(r"project photo\gmail.png")
        # img_top1=img_top1.resize((250,200),Image.ANTIALIAS)
        # self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        # firstlbl2=Label(main_frame,image=self.photoimg_top1)
        # firstlbl2.place(x=0,y=0,width=250,height=200)
        # #help
        # hel_btn=Label(main_frame,text="Contact",font=("times new roman",12,"bold"),bg="white")
        # hel_btn.place(x=40,y=200)

        hel_btn=Label(firstlbl2,text="Email:Sohammaity123@gmail.com",font=("times new roman",12,"bold"),bg="white")
        hel_btn.place(x=550,y=340) 

        hel_btn=Label(firstlbl2,text="Contact:+91-9534278812",font=("times new roman",12,"bold"),bg="white")
        hel_btn.place(x=590,y=390)


        # img_top2=Image.open(r"project photo\th.jpeg")
        # img_top2=img_top2.resize((250,100),Image.ANTIALIAS)
        # self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        # firstlbl2=Label(main_frame,image=self.photoimg_top2)
        # firstlbl2.place(x=35,y=350,width=250,height=100) 



        
















if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()