from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class detect:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1280x690+0+0")
        self.root.title("Face Recognization System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("time new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1310,height=45)

        # image 1
        img_top=Image.open(r"project photo\images.jpg")
        img_top=img_top.resize((600,650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        firstlbl2=Label(self.root,image=self.photoimg_top)
        firstlbl2.place(x=0,y=55,width=600,height=550)

        # second image
        img_bottom=Image.open(r"project photo\loading.jpg")
        img_bottom=img_bottom.resize((900,550),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        firstlbl3=Label(self.root,image=self.photoimg_bottom)
        firstlbl3.place(x=600,y=55,width=800,height=550)
        
        # button

        b1_1=Button(firstlbl3,text="Face Recognition",cursor="hand2",command=self.face_reco,font=("time new roman",15 ,"bold"),bg="blue",fg="white")
        b1_1.place(x=270,y=496,width=260,height=30)



    # # attendance
    # def mark_attendance(self, d1, en, d):
    #     with open("Attendance.csv", "r+", newline="\n") as f:
    #         my_data_list = f.readlines()
    #         name_list = []
    #         for line in my_data_list:
    #             entry = line.split(",")
    #             name_list.append(entry[0])

    #         if d1 not in name_list and en not in name_list and d not in name_list:
    #             now = datetime.now()
    #             dat = now.strftime("%d/%m/%Y")
    #             dtstring = now.strftime("%H:%M:%S")
    #             # if employee is on time
    #             if dtstring <= "09:00:00":
    #                 f.writelines(f"\n{d1},{en},{d},{dtstring},{dat},present")
    #          # if employee is late
    #             elif "09:00:00" < dtstring < "12:00:00":
    #                 f.writelines(f"\n{d1},{en},{d},{dtstring},{dat},late present")
    #          # if employee comes after 12:00 PM or is absent
    #             elif dtstring >= "12:00:00":
    #                 f.writelines(f"\n{d1},{en},{d},{dtstring},{dat},half day")
    #         else:
    #             print("Employee already marked present.")
    

    def mark_attendance(self, d1, en, d):
        now = datetime.now()
        dat = now.strftime("%d/%m/%Y")
        dtstring = now.strftime("%H:%M:%S")

        conn = mysql.connector.connect(host="localhost", username="root", password="96096", database="employee_attendance_system")
        cursor = conn.cursor()

        if dtstring <= "10:00:00":
            status = "present"
        elif "10:00:00" < dtstring < "12:00:00":
            status = "late present"
        else:
            status = "half day"

        query = "INSERT INTO attendance (Emp_Id, Emp_Name, Department, Date, Time, Status) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (d1, en, d, dat, dtstring, status)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()


            

  






    # =========face recognition

    def face_reco(self):
        def draw_bound(img, classifier, scaleFactor, minSize, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minSize)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="96096", database="employee_attendance_system")
                my_cursur = conn.cursor()

                my_cursur.execute("select Emp_Name from employee where Emp_Id=" + str(id))
                en = my_cursur.fetchone()
                en = "+".join(en)

                my_cursur.execute("select Dep from employee where Emp_Id=" + str(id))
                d = my_cursur.fetchone()
                d = "+".join(d)

                my_cursur.execute("select Emp_id from employee where Emp_Id=" + str(id))
                d1 = my_cursur.fetchone()
                d1 = "+".join(d1)

                if confidence > 77:
                    cv2.putText(img, f"ID:{d1}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Employee Name:{en}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department:{d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(d1, en, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recog(img, clf, faceCascade):
            coord = draw_bound(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        cap = cv2.VideoCapture(0)

        while True:
            ret, img = cap.read()
            img = recog(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognization", img)

            if cv2.waitKey(1000) == 13:
                cap.release()
                cv2.destroyAllWindows()
                break

                


if __name__=="__main__":
    root=Tk()
    obj=detect(root)
    root.mainloop()