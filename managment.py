from tkinter import*
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
from tkinter import ttk, messagebox
# import pymysql
import mysql.connector


class managment:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+50+50")
        self.root.title("Student managment system |Developed By Pooja Bhardwaj")
        self.root.resizable(False, False)
        
        self.sub1 = StringVar()
        self.sub2 = StringVar()
        self.sub3 = StringVar()
        self.sub4 = StringVar()
        self.sub5 = StringVar()
        self.ob_marks = StringVar()
        self.total_marks = StringVar()
        self.percent = StringVar()
        self.URN = StringVar()
        self.CRN = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.contact = StringVar()
        self.address = StringVar()
        self.branch = StringVar()
        self.section = StringVar()
        self.session = StringVar()
        self.search_t = StringVar()
        self.search_by = StringVar()
        self.obtained_marks = StringVar()
        self.Total_marks=StringVar()
        self.percentage=StringVar()



        bg_color = ("#008F7A")
        title = Label(self.root, text="Student Managment System", bd=12, bg=bg_color,relief=GROOVE, fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Student Details", font=("times new roman", 15, "bold"), fg="red", bg=bg_color)
        F1.place(x=5, y=70, width=370, height=260)
        URN = Label(F1, text="URN", bg=bg_color, fg="black", font=("times new roman", 14, "bold")).place(x=10, y=10)
        self.URN_txt = Entry(F1, width=12, textvariable=self.URN, font="arial 10 bold",bd=5, relief=SUNKEN)
        self.URN_txt.place(x=70, y=10)
        CRN = Label(F1, text="CRN", bg=bg_color, fg="black", font=("times new roman", 14, "bold")).place(x=180, y=10)
        self.CRN_txt = Entry(F1, width=12, textvariable=self.CRN, font="arial 10 bold",bd=6, relief=SUNKEN)
        self.CRN_txt.place(x=240, y=10)
        name_lbl = Label(F1, text="Name", font=("times new roman ", 14, "bold"),bg=bg_color, fg="lightgreen").place(x=10, y=50)
        self.name_txt = Entry(F1, width=20, textvariable=self.name, font=("times new roman ", 12, "bold"), bd=5, relief=SUNKEN)
        self.name_txt.place(x=143, y=50)
        Email_lbl = Label(F1, text="Email", font=("times new roman ", 14, "bold"),bg=bg_color, fg="lightgreen").place(x=10, y=90)
        self.Email_txt = Entry(F1, width=20, textvariable=self.email, font=("times new roman ", 12, "bold"), bd=5, relief=SUNKEN)
        self.Email_txt.place(x=143, y=90)
        contact_lbl = Label(F1, text="Contact no", font=("times new roman ", 14, "bold"),bg=bg_color, fg="lightgreen").place(x=10, y=130)
        self.contact_txt = Entry(F1, width=20, textvariable=self.contact, font=("times new roman ", 12, "bold"), bd=5, relief=SUNKEN)
        self.contact_txt.place(x=143, y=130)
        address_lbl = Label(F1, text="Address", font=("times new roman ", 14, "bold"),bg=bg_color, fg="lightgreen").place(x=10, y=170)
        self.address_txt = Entry(F1, width=20, textvariable=self.address, font=("times new roman ", 12, "bold"), bd=5, relief=SUNKEN)
        self.address_txt.place(x=143, y=170, height=45)

        

        #================== subject marks ==========================================================
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Marks", font=(
            "times new roman", 15, "bold"), fg="red", bg=bg_color)
        F2.place(x=5, y=310, width=370, height=260)

        sub1_lbl = Label(F2, text="Operating System", font=("times new roman ", 16, "bold"),bg=bg_color, fg="lightgreen").place(x=10,y=10)
        self.sub1_txt = Entry(F2, width=10, textvariable=self.sub1, font=("times new roman ", 12, "bold"), bd=5, relief=SUNKEN)
        self.sub1_txt.place(x=240, y=10)

        sub2_lbl = Label(F2, text="Math ", font=("times new roman ", 16, "bold"),bg=bg_color, fg="lightgreen").place(x=10, y=50)
        self.sub2_txt = Entry(F2, width=10, textvariable=self.sub2, font=("times new roman ", 12, "bold"), bd=5, relief=SUNKEN)
        self.sub2_txt.place(x=240, y=50)

        sub3_lbl = Label(F2, text="Data Structure", font=("times new roman ", 16, "bold"),bg=bg_color, fg="lightgreen").place(x=10, y=90)
        self.sub3_txt = Entry(F2, width=10, textvariable=self.sub3, font=("times new roman ", 12, "bold"), bd=5, relief=SUNKEN)
        self.sub3_txt.place(x=240, y=90)

        sub4_lbl = Label(F2, text="Machine learning ", font=("times new roman ", 16, "bold"),bg=bg_color, fg="lightgreen").place(x=10, y=130)
        self.sub4_txt = Entry(F2, width=10, textvariable=self.sub4, font=("times new roman ", 12, "bold"), bd=5, relief=SUNKEN)
        self.sub4_txt.place(x=240, y=130)

        sub5_lbl = Label(F2, text="PPS", font=("times new roman ", 16, "bold"),bg=bg_color, fg="lightgreen").place(x=10, y=170)
        self.sub5_txt = Entry(F2, width=10, textvariable=self.sub5, font=("times new roman ", 12, "bold"), bd=5, relief=SUNKEN)
        self.sub5_txt.place(x=240, y=170)
        #==================== total marks ================================================================

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Total", font=("times new roman", 15, "bold"), fg="red", bg=bg_color)
        F3.place(x=5, y=540, width=370, height=160)
        Ob = Label(F3, text="Otained Marks", bg=bg_color, fg="black", font=("times new roman", 14, "bold")).place(x=10,y=10)
        self.Ob_txt = Entry(F3, width=17, textvariable=self.ob_marks, font="arial 10 bold",bd=6, relief=SUNKEN)
        self.Ob_txt.place(x=210, y=0)

        Total_marks = Label(F3, text="Total marks", bg=bg_color, fg="black", font=("times new roman", 14, "bold")).place(x=10, y=50)
        self.Tm_txt = Entry(F3, width=17,text="500", textvariable=self.total_marks, font="arial 10 bold",bd=6, relief=SUNKEN)
        self.Tm_txt.place(x=210, y=50)


        percent= Label(F3, text="Percentage", bg=bg_color, fg="black", font=("times new roman", 14, "bold")).place(x=10, y=90)
        self.percent_txt = Entry(F3, width=17, textvariable=self.percent,font="arial 10 bold", bd=6, relief=SUNKEN)
        self.percent_txt.place(x=210, y=90)

        #===================== Branch details =================================================================
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Branch Details", font=("times new roman", 15, "bold"), fg="red", bg=bg_color)
        F4.place(x=370, y=70,relwidth=1)
        branch_lbl = Label(F4, text="Branch", bg=bg_color, font=("time new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        # branch2_lbl = Label(F4, text="CSE", bd=6, relief=SUNKEN, bg=bg_color, font=("time new roman", 18, "bold")).grid(row=0, column=1, padx=20, pady=5)
        self.branch_txt = Entry(F4, width=15, textvariable=self.branch, fg="black",font="arial 15", bd=6, relief=SUNKEN)
        self.branch_txt.grid(row=0, column=1, pady=5, padx=10)
        section_lbl = Label(F4, text="Section", bg=bg_color, font=("time new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        self.section_txt = Entry(F4, width=15, textvariable=self.section, fg="black",font="arial 15", bd=6, relief=SUNKEN)
        self.section_txt.grid(row=0, column=3, pady=5, padx=10)
        session_lbl = Label(F4, text="Session", bg=bg_color, font=("time new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        self.session_txt = Entry(F4, width=15, textvariable=self.session, fg="black",font="arial 15", bd=6, relief=SUNKEN)
        self.session_txt.grid(row=0, column=5, pady=5, padx=10)
        
        #============= QR frame or button frame ========================
        F5 = LabelFrame(self.root, bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="red", bg=bg_color)
        F5.place(x=375, y=480, relwidth=1, height=290)

        #============= Qr code =========================
        QR_Frame = Frame(F5, bd=7, bg='white', relief=GROOVE)
        QR_Frame.place(x=20, y=20, width=200, height=170)
        self.qr_code = Label(QR_Frame, text='No QR \nAvaliable', font=(
            "times new roman", 20), bg='cadetblue', fg='dark blue', bd=0, relief=RIDGE)
        self.qr_code.place(x=2, y=3, width=180, height=150)


         #============ button frame ================
        
        btn_F = Frame(F5, bd=7,bg='gray', relief=GROOVE)
        btn_F.place(x=290,y=60, width=650, height=105)

        self.total_btn = Button(btn_F, text="total",command=self.obt_marks, bg="cadetblue", fg="white",
                           bd=5, pady=15, width=8, font="arial 12").grid(row=0, column=0, padx=5, pady=10)
        self.add_btn = Button(btn_F, text="Add", command=self.add_data, bg="cadetblue", fg="white",
                                bd=5, pady=15, width=9, font="arial 12").grid(row=0, column=1, padx=5, pady=10)
        self.update_btn = Button(btn_F, text="Update", command=self.update_data ,bg="cadetblue", fg="white",
                              bd=5, pady=15, width=9, font="arial 12").grid(row=0, column=2, padx=5, pady=10)
        self.Gcode_btn = Button(btn_F, text="Gcode",command=self.QR_generate, bg="cadetblue", fg="white",
                           bd=5, pady=15, width=9, font="arial 12").grid(row=0, column=3, padx=5, pady=10)
        self.Clear_btn = Button(btn_F, text="Clear",command=self.clear, bg="cadetblue", fg="white", bd=5,
                           pady=15, width=9, font="arial 12").grid(row=0, column=4, padx=5, pady=10)
        self.Exit_btn = Button(btn_F, text="Exit", bg="cadetblue", fg="white", bd=5,
                          pady=15, width=9, font="arial 12",command=self.Exit).grid(row=0, column=5, padx=5, pady=10)
        
        


        #============= database frame ========================
        data_Frame = Frame(self.root, bd=7, bg=bg_color, relief=GROOVE)
        data_Frame.place(x=370, y=150, width=980, height=330)
        
        
        Table_Frame = Frame(data_Frame, bd=7, bg='white', relief=GROOVE)
        Table_Frame.place(x=10, y=10, width=940, height=290)
        
        
        #================ scrollbar =========================================================
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=("branch", "section", "session", "URN", "CRN", "name","email", "contact", "Address", "sub1", "sub2", "sub3", "sub4", "sub5","obt_masks","tot_masks","percent"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("branch", text="Branch")
        self.Student_table.heading("section", text="Section")
        self.Student_table.heading("session", text="Session")
        self.Student_table.heading("URN", text="URN")
        self.Student_table.heading("CRN", text="CRN")
        self.Student_table.heading("name", text="NAME")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("Address", text="Address")
        self.Student_table.heading("sub1", text="Operating System")
        self.Student_table.heading("sub2", text="Math")
        self.Student_table.heading("sub3", text="Data structure")
        self.Student_table.heading("sub4", text="Machine Learning")
        self.Student_table.heading("sub5", text="PPS")
        self.Student_table.heading("obt_masks", text="Obtained Masks")
        self.Student_table.heading("tot_masks", text="Total Masks")
        self.Student_table.heading("percent", text="percentage")

        self.Student_table['show'] ='headings'
        self.Student_table.column("branch", width=100)
        self.Student_table.column("section", width=100)
        self.Student_table.column("session", width=100)
        self.Student_table.column("URN", width=60)
        self.Student_table.column("CRN", width=60)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=180)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("Address", width=150)
        self.Student_table.column("sub1", width=120)
        self.Student_table.column("sub2", width=100)
        self.Student_table.column("sub3", width=100)
        self.Student_table.column("sub4", width=120)
        self.Student_table.column("sub5", width=100)
        self.Student_table.column("obt_masks", width=100)
        self.Student_table.column("tot_masks", width=100)
        self.Student_table.column("percent", width=100)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()
        self.clear()

        
        
    #================== another fuctions =====================================
    def add_data(self):
        
        try:
                con = mysql.connector.connect(user='root',
                                               password='Pooja@2015104',
                                               host='127.0.0.1',
                                               port='3306',
                                               database='registration')
                mycursor = con.cursor()
                print(mycursor)
                mycursor.execute("insert into cse_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.branch_txt.get(), self.section_txt.get(), self.session_txt.get(
                    ), self.URN_txt.get(), self.CRN_txt.get(), self.name_txt.get(),
                        self.Email_txt.get(), self.contact_txt.get(),  self.address_txt.get(), self.sub1_txt.get(), self.sub2_txt.get(), self.sub3_txt.get(), self.sub4_txt.get(), self.sub5_txt.get(),
                        self.Ob_txt.get(), self.Tm_txt.get(), self.percent_txt.get()))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('error', "Register Successful")
        except Exception as es:
                print(es)
                messagebox.showerror('error', es)
    
        
    def fetch_data(self):
        try:
            con = mysql.connector.connect(user='root',
                                      password='Pooja@2015104',
                                      host='127.0.0.1',
                                      port='3306',
                                      database='registration')
            mycursor = con.cursor()
            mycursor.execute("select * from cse_info ")
            rows=mycursor.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows :
                    self.Student_table.insert('', END, values=row)
                con.commit()
            con.close()
        except Exception as es:
            print(es)
            messagebox.showerror('error', es)




    def clear(self):
        self.branch.set('')
        self.section.set('')
        self.session.set('')
        self.URN.set('')
        self.CRN.set('')
        self.name.set('')
        self.email.set('')
        self.contact.set('')
        self.address.set('')
        self.sub1.set('')
        self.sub2.set('')
        self.sub3.set('')
        self.sub4.set('')
        self.sub5.set('')
        self.ob_marks.set('')
        self.total_marks.set('')
        self.percent.set('')

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.branch.set(row[0])
        self.section.set(row[1])
        self.session.set(row[2])
        self.URN.set(row[3])
        self.CRN.set(row[4])
        self.name.set(row[5])
        self.email.set(row[6])
        self.contact.set(row[7])
        self.address.set(row[8])
        self.sub1.set(row[9])
        self.sub2.set(row[10])
        self.sub3.set(row[11])
        self.sub4.set(row[12])
        self.sub5.set(row[13])
        self.ob_marks.set(row[14])
        self.total_marks.set(row[15])
        self.percent.set(row[16])

    def update_data(self):
        try:
                con = mysql.connector.connect(user='root',
                                      password='Pooja@2015104',
                                      host='127.0.0.1',
                                      port='3306',
                                      database='registration')
                mycursor = con.cursor()
    
                mycursor.execute("update cse_info SET branch=%s,section=%s,session=%s,URN=%s,CRN=%s,name=%s,email=%s,contact=%s,address=%s,OS=%s,math=%s,DS=%s,ML=%s ,PPS=%s,obt_marks=%s,tot_marks=%s where percent=%s", (
                                                            self.branch_txt.get(), self.section_txt.get(), self.session_txt.get(), 
                                                            self.URN_txt.get(), self.CRN_txt.get(), self.name_txt.get(),self.Email_txt.get(), 
                                                            self.contact_txt.get(),  self.address_txt.get(), self.sub1_txt.get(), self.sub2_txt.get(), 
                                         self.sub3_txt.get(), self.sub4_txt.get(), self.sub5_txt.get(), self.Ob_txt.get(), self.Tm_txt.get(), self.percent_txt.get()))
               
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('error', "Updated Successfully!!!")
        except Exception as es:
                print(es)
        messagebox.showerror('error', es)



      


    def QR_generate(self):
        if self.branch_txt.get() == '' or self.section_txt.get() == '' or self.session_txt.get() == '' or self.URN_txt.get() == '' or self.CRN_txt.get() == '' or self.name_txt.get() == '' or self.Email_txt.get() == '' or self.contact_txt.get() == '' or self.address_txt.get() == '' or self.sub1_txt.get() == '' or self.sub2_txt.get() == '' or self.sub3_txt.get() == '' or self.sub4_txt.get() == '' or self.sub5_txt.get() == '' or self.Ob_txt.get() == '' or self.Tm_txt.get() == '' or self.percent_txt.get() == '':
            messagebox.showinfo('error', "All Feild Are Required!!!")
        
        else:
            qr_data = (f"branch:{self.branch.get()}\n\nSection:{self.section_txt.get()}\n\nSession:{self.session.get()}\n\nURN:{self.URN.get()}\n\nCRN:{self.CRN_txt.get()}\n\nName:{self.name_txt.get()}\n\nEmail:{self.Email_txt.get()}\n\nContact No:{self.contact_txt.get()}\n\nAddress:{self.address_txt.get()}\n\nOS Marks:{self.sub1_txt.get()}\n\nMath marks:{self.sub2_txt.get()}\n\nDS marks:{self.sub3_txt.get()}\n\nMachine Learning marks:{self.sub4_txt.get()}\n\nPPS marks:{self.sub5_txt.get()}\n\nObtained marks:{self.Ob_txt.get()}\n\nTotal marks:{self.Tm_txt.get()}\n\nPercentage:{self.percent_txt.get()}")
            qr_code = qrcode.make(qr_data)
            qr_code = resizeimage.resize_cover(qr_code, [150, 150])
            qr_code.save("student_QR/Stud_" +str(self.URN_txt.get())+'.png')
        # #========QR code image updating===========
            self.im = ImageTk.PhotoImage(file="student_QR/Stud_"+str(self.URN_txt.get())+'.png')
            self.qr_code.config(image=self.im)
    
        
    def obt_marks(self):     
        self.obtained_marks=StringVar()
        self.Total_marks = StringVar()
        self.s1 = (self.sub1.get())
        self.s1=int(self.s1)
        self.s2 = (self.sub2.get())
        self.s2 = int(self.s2)
        self.s3 = (self.sub3.get())
        self.s3 = int(self.s3)
        self.s4 = (self.sub4.get())
        self.s4 = int(self.s4)
        self.s5 = (self.sub5.get())
        self.s5 = int(self.s5)
        self.sb1 = 100
        self.sb1 = int(self.sb1)
        self.sb2 = 100
        self.sb2 = int(self.sb2)
        self.sb3 = 100
        self.sb3 = int(self.sb3)
        self.sb4 = 100
        self.sb4 = int(self.sb4)
        self.sb5 = 100
        self.sb5 = int(self.sb5)
        
        self.obtained_marks= float(
            self.s1 +
            self.s2 +self.s3+self.s4+self.s5
          )
        self.ob_marks.set(str(self.obtained_marks))
        
        
        self.Total_marks = int(self.sb1 +self.sb2 + self.sb3+self.sb4+self.sb5)
        self.total_marks.set(str(self.Total_marks))

        self.percentage=float( (self.obtained_marks/self.Total_marks)*100)
        self.percent.set(str(self.percentage))
 
           
    def Exit(self):
        op=messagebox.askyesno("exit","do you want to exit")
        if op>0:
            self.root.destroy()

    
root = Tk()
obj = managment(root)
root.mainloop()
