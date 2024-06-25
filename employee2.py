from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import filedialog



class Employee:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1280x690+0+0")
        self.root.title("Face Recognization System")


        # =======variables==========
        self.var_dep=StringVar()
        self.var_emp_id=StringVar()
        self.var_emp_name=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()



     # first
        img=Image.open(r"C:\Users\soham\Desktop\eeeeeaa\project photo\fi.jpg")
        img=img.resize((450,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        firstlbl=Label(self.root,image=self.photoimg)
        firstlbl.place(x=0,y=0,width=450,height=130)

        # second
        img1=Image.open(r"C:\Users\soham\Desktop\eeeeeaa\project photo\mi.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        firstlbl1=Label(self.root,image=self.photoimg1)
        firstlbl1.place(x=450,y=0,width=500,height=130)

        # third
        img2=Image.open(r"C:\Users\soham\Desktop\eeeeeaa\project photo\em.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        firstlbl2=Label(self.root,image=self.photoimg2)
        firstlbl2.place(x=900,y=0,width=500,height=130)


        # background
        img3=Image.open(r"C:\Users\soham\Desktop\eeeeeaa\project photo\background.jpg")
        img3=img3.resize((1280,690),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        firstlbl3=Label(self.root,image=self.photoimg3)
        firstlbl3.place(x=0,y=130,width=1280,height=590)


        # title lable
        title_lbl=Label(firstlbl3,text="Employee Details",font=("time new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1310,height=45)

        main_frame=Frame(firstlbl3,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1260,height=500)

        # left lable frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee's Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=5,width=670,height=440)

        img_left=Image.open(r"C:\Users\soham\Desktop\eeeeeaa\project photo\ni.png")
        img_left=img_left.resize((658,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        firstlbl2=Label(left_frame,image=self.photoimg_left)
        firstlbl2.place(x=5,y=0,width=658,height=130)


        # Details
        Details=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Registor",font=("times new roman",12,"bold"))
        Details.place(x=5,y=135,width=655,height=280)

        # #employee id
        Employee_id=Label(Details,text="Employee_Id:",font=("times new roman",12,"bold"),bg="white")
        Employee_id.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        EmployeeId_entry=ttk.Entry(Details,textvariable=self.var_emp_id,width=15,font=("times new roman",12,"bold"))
        EmployeeId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Employee Name
        Employee_Name=Label(Details,text="Employee_Name:",font=("times new roman",12,"bold"),bg="white")
        Employee_Name.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        EmployeeName_entry=ttk.Entry(Details,textvariable=self.var_emp_name,width=15,font=("times new roman",12,"bold"))
        EmployeeName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Department
        dep_lable=Label(Details,text="Department",font=("times new roman",12,"bold"),bg="white") 
        dep_lable.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Details,width=15,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly")    
        dep_combo["values"]=("Select Department","Analyst","Manager","Human Resource","Technical")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=6)

        # Doj
        DOJ=Label(Details,text="Date Of Birth",font=("times new roman",12,"bold"),bg="white") 
        DOJ.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(Details,textvariable=self.var_dob,width=15,font=("times new roman",12,"bold"))
        date_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # year_combo=ttk.Combobox(Details,width=15,font=("times new roman",10,"bold"),state="readonly")    
        # year_combo["values"]=("Select Year","2017","2018","2019","2020","2021","2022","2023","2024")
        # year_combo.current(0)
        # year_combo.grid(row=1,column=3,padx=2,pady=6)


        # Email
        Email_label=Label(Details,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(Details,textvariable=self.var_email,width=15,font=("times new roman",12,"bold"))
        Email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Phone
        Phone_label=Label(Details,text="Phone:",font=("times new roman",12,"bold"),bg="white")
        Phone_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Phone_entry=ttk.Entry(Details,textvariable=self.var_phone,width=15,font=("times new roman",12,"bold"))
        Phone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Address
        Address_label=Label(Details,text="Address:",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(Details,textvariable=self.var_address,width=15,font=("times new roman",12,"bold"))
        Address_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Gender
        gen_lable=Label(Details,text="Gender",font=("times new roman",12,"bold"),bg="white") 
        gen_lable.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        gen_combo=ttk.Combobox(Details,textvariable=self.var_gender,width=15,font=("times new roman",10,"bold"),state="readonly")    
        gen_combo["values"]=("Select Gender","Male","Female","Other")
        gen_combo.current(0)
        gen_combo.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # #  Radio_button
        # self.var_radio1=StringVar()
        # radiobtn1=ttk.Radiobutton(Details,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        # radiobtn1.grid(row=5,column=0)

        # #  Radio_button
        
        # radiobtn2=ttk.Radiobutton(Details,variable=self.var_radio1,text="No Photo Sample",value="No")
        # radiobtn2.grid(row=5,column=2)


        # button frame
        bth_frame=Frame(Details,bd=2,relief=RIDGE,bg="white")
        bth_frame.place(x=0,y=170,width=650,height=35)
        # save
        save_btn=Button(bth_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        # update
        up_btn=Button(bth_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        up_btn.grid(row=0,column=1,padx=2)

        # delete
        del_btn=Button(bth_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        del_btn.grid(row=0,column=2,padx=2)

        # reset
        re_btn=Button(bth_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        re_btn.grid(row=0,column=3,padx=2)


        # button frame
        bth_frame1=Frame(Details,bd=2,relief=RIDGE,bg="white")
        bth_frame1.place(x=0,y=205,width=650,height=35)
        # take photo sample
        # take_btn=Button(bth_frame1,text="Take Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # take_btn.grid(row=0,column=0)
        # update photo sample
        n_btn=Button(bth_frame1,command=self.generate_data,text="Upload Photo Sample",width=72,font=("times new roman",12,"bold"),bg="blue",fg="white")
        n_btn.grid(row=0,column=1,padx=2)

        
        # right lable frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee's Details",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=5,width=560,height=440)
        # ANTIALIAS
        img_right=Image.open(r"C:\Users\soham\Desktop\eeeeeaa\project photo\se.png")
        img_right=img_right.resize((550,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        firstlbl2=Label(right_frame,image=self.photoimg_right)
        firstlbl2.place(x=5,y=0,width=550,height=130)

        # ___________________serching system________________

        # searching=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        # searching.place(x=5,y=135,width=550,height=60)

        # Serach_label=Label(searching,text="Serach by:",font=("times new roman",12,"bold"),bg="blue",fg="white")
        # Serach_label.grid(row=0,column=0,padx=10,pady=0,sticky=W)

        # # combo box
        # search_combo=ttk.Combobox(searching,width=15,font=("times new roman",10,"bold"),state="readonly")    
        # search_combo["values"]=("Select","Employee_ID","Phone_No")
        # search_combo.current(0)
        # search_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # # entry field
        # field_entry=ttk.Entry(searching,width=15,font=("times new roman",12,"bold"))
        # field_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)



        # # serach btn
        # sr_btn=Button(searching,text="Search",width=6,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # sr_btn.grid(row=0,column=3,padx=4)

        # # show all
        # sh_btn=Button(searching,text="Show All",width=6,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # sh_btn.grid(row=0,column=4,padx=4)

        # ================table frame============
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=135,width=550,height=280)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.Employee_Table=ttk.Treeview(table_frame,column=("Emp_Id","Emp_Name","Gen","DOB","Phone","Email","Dep","Add","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Employee_Table.xview)
        scroll_y.config(command=self.Employee_Table.yview)
        


        self.Employee_Table.heading("Emp_Id",text="Employee_ID")
        self.Employee_Table.heading("Emp_Name",text="Employee_NAME")
        self.Employee_Table.heading("Gen",text="Gender")
        self.Employee_Table.heading("DOB",text="Dtae OF Birth")
        self.Employee_Table.heading("Phone",text="Phone")
        self.Employee_Table.heading("Email",text="Email")
        self.Employee_Table.heading("Dep",text="Department")
        self.Employee_Table.heading("Add",text="Address")
        self.Employee_Table.heading("photo",text="PhotoSampleStatus")
        self.Employee_Table["show"]="headings"
        # width
        self.Employee_Table.column("Emp_Id",width=100)
        self.Employee_Table.column("Emp_Name",width=100)
        self.Employee_Table.column("Gen",width=100)
        self.Employee_Table.column("DOB",width=100)
        self.Employee_Table.column("Phone",width=100)
        self.Employee_Table.column("Email",width=100)
        self.Employee_Table.column("Dep",width=100)
        self.Employee_Table.column("Add",width=100)
        self.Employee_Table.column("photo",width=150)

        self.Employee_Table.pack(fill=BOTH,expand=1)
        self.Employee_Table.bind("<ButtonRelease>",self.get_cursur)
        self.fetch_data()

        

    # ====================Function Declaration=============
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_emp_name.get()=="" or self.var_emp_id.get()=="":
            messagebox.showerror("Error","All Field Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="96096",database="employee_attendance_system")
                my_cursur=conn.cursor()

                
                
                my_cursur.execute("insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                            self.var_emp_id.get(),
                                                                                                            self.var_emp_name.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            
                                                                                                        
                                                                                                        
                                                                                                    )) 
                
               
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                
                
               
                messagebox.showinfo("Sucess","Employee Details has been added Sucessfully",parent=self.root)
                 
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)     
                


    # ============fetch data ==========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="96096",database="employee_attendance_system")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from employee1")
        data=my_cursur.fetchall()

        if len(data)!=0:
            self.Employee_Table.delete(*self.Employee_Table.get_children())
            for i in data:
                self.Employee_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    # ==========get cursur=========
    def get_cursur(self,event=""):
        cursur_focus=self.Employee_Table.focus()
        content=self.Employee_Table.item(cursur_focus)
        data=content["values"]

        self.var_emp_id.set(data[0]),
        self.var_emp_name.set(data[1]),
        self.var_gender.set(data[2]),
        self.var_dob.set(data[3]),
        self.var_phone.set(data[4]),
        self.var_email.set(data[5]),
        self.var_dep.set(data[6]),
        self.var_address.set(data[7]),
        self.var_radio1.set(data[8])


    # =========update========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_emp_name.get()=="" or self.var_emp_id.get()=="":
            messagebox.showerror("Error","All Field Are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this Employee details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="96096",database="employee_attendance_system")
                    my_cursur=conn.cursor()
                    my_cursur.execute("update employee1 set Emp_Name=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Dep=%s,Address=%s,Photo=%s where Emp_Id=%s",(
                                                                                                                                                          
                                                                                                                                                            self.var_emp_name.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_emp_id.get()

                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Sucess","Employee details sucessfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)


    # delete function
    def delete_data(self):
        if self.var_emp_id.get()=="":
            messagebox.showerror("Error","Employee id should we required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee Delete Page","Do you wnt to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="96096",database="employee_attendance_system")
                    my_cursur=conn.cursor()
                    sql="delete from employee where Emp_Id=%s"
                    val=(self.var_emp_id.get(),)
                    my_cursur.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully deleted Employee",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)   


        #==========reste function
    def reset_data(self):
        self.var_emp_id.set(""),
        self.var_emp_name.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_dep.set("Select Department"),
        self.var_address.set(""),
        self.var_radio1.set("")

    # =========take photo sample======
    def generate_data(self):
        if self.var_dep.get() == "Select Department" or self.var_emp_name.get() == "" or self.var_emp_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="96096", database="employee_attendance_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from employee1")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1
                # self.update_data()
                
                

               
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # minimum ne=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Data Set Completed!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)


   

   
                







if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()