from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1280x690+0+0")
        self.root.title("Face Recognization System")
    
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("time new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1310,height=45)

        # Top image
    
        img_top=Image.open(r"project photo\facialrecognition.png")
        img_top=img_top.resize((1280,250),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        firstlbl2=Label(self.root,image=self.photoimg_top)
        firstlbl2.place(x=0,y=55,width=1280,height=250)

        # button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("time new roman",20 ,"bold"),bg="green",fg="white")
        b1_1.place(x=0,y=300,width=1280,height=50)
        
        
        # bottom img
        img_bottom=Image.open(r"project photo\photosss.jpg")
        img_bottom=img_bottom.resize((1280,350),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        firstlbl2=Label(self.root,image=self.photoimg_bottom)
        firstlbl2.place(x=0,y=350,width=1280,height=350)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #gray scale convert
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # ================train the clasifier and save
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("Result","Training datasets completed")
         



        

















if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()