from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import email_pass
import smtplib
import time


class login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE || Developed By Pooja Bhardwaj ")
        self.root.geometry("800x540+170+50")
        self.root.config(bg="#ffc046")

        main_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='white')
        main_Frame.place(x=70, y=70, width=650, height=410)
        self.var_stud_Email = StringVar()
        self.var_stud_password = StringVar()

        self.otp=''

        #================= image ========================
        image = Image.open('admin.png')
        print(f"Original size : {image.size}")  # 5464x3640

        self.img_image_resized = image.resize((180, 140))
        self.img_image_resized.save('admin.png')
        self.img_image = ImageTk.PhotoImage(file="admin.png")
        self.lb1_img_image = Label(
            main_Frame, image=self.img_image, bg="white").place(x=50, y=150)

        #============= logo ====================================
        image = Image.open('gndeclogo.png')
        print(f"Original size : {image.size}")  # 5464x3640

        self.logo_image_resized = image.resize((100, 80))
        self.logo_image_resized.save('gndeclogo.png')
        self.logo_image = ImageTk.PhotoImage(file="gndeclogo.png")
        self.lb1_logo_image = Label(main_Frame, image=self.logo_image, bg="white").place(x=400, y=10)

        #=================== text ==========================
        lb1_stud = Label(main_Frame, text="Student Login", font=(
            "time new roman", 22, 'bold'), bg="white").place(x=40, y=45)
        lb1_stud2 = Label(main_Frame, text=("Fill your details to login an account "), font=(
            "goudy old style", 13), fg="gray", bg="white").place(x=30, y=90)

        #======================= details ====================
        lb1_username = Label(main_Frame, text="Username", font=("Andalus", 15),fg="gray",bg="white").place(x=380, y=120)
        lb1_password = Label(main_Frame, text="Password", font=("Andalus", 15),fg="gray", bg="white").place(x=380, y=190)
        self.txt_Email = Entry(main_Frame, font=("times new roman", 15), bg="light yellow")
        self.txt_Email.place(x=380, y=150, width=200)
        
        self.txt_password = Entry(main_Frame, font=("times new roman", 15), bg="light yellow")
        self.txt_password.place(x=380, y=220, width=200)
       
        btn_login = Button(main_Frame, text="LOGIN", command=self.login, font=("times new roman", 15, 'bold'), bd=0, bg="#ffc046", fg='white').place(x=380, y=280, width=200, height=35)
        hr=Label(main_Frame,bg="lightgray").place(x=380,y=340,height=2,width=200)
        lb1_or = Label(main_Frame, text="OR", font=("time new roman", 15,"bold"),fg="gray").place(x=450, y=330)
        btn_forget_password = Button(main_Frame, command=self.forget_window,text="Forget password ?" ,font=("time new roman", 10),bd=0,fg="red", bg="white").place(x=380, y=355,width=200,height=35)
        btn_sign_in = Button(main_Frame, text="SignUp", command=self.signup, font=("times new roman", 15, 'bold'), bd=0, bg="blue", fg='white').place(x=60, y=320, width=150, height=25)
        btn_back = Button(self.root, text="Back", command=self.back,font=("times new roman", 15, 'bold'), bd=0, bg="gray", fg='black').place(x=10, y=10, width=100, height=25)
        
        
    def login(self):
        # print(self.txt_Email.get())
        if  self.txt_Email.get() == '' or  self.txt_password.get() == '':
            messagebox.showerror("Error","All Field are Required!!!",parent=self.root)
            
        else:
            try:
                con = mysql.connector.connect(user='root',
                                              password='Pooja@2015104',
                                              host='127.0.0.1',
                                              database='registration')
                mycursor = con.cursor()
                mycursor.execute("select * from student_info where email=%s and password=%s" , ( self.txt_Email.get(), self.txt_password.get()))
                row =mycursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                    
                else:
                    messagebox.showerror("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import branchpage.py
                mycursor.close()   
            except Exception as es:
                messagebox.showerror('error',f"Error Due to:{str(es)}",parent=self.root)
    def forget_window(self):
        con = mysql.connector.connect(user='root',
                                      password='Pooja@2015104',
                                      host='127.0.0.1',
                                      database='registration')
        mycursor = con.cursor()
        try:
            if self.txt_Email.get() == '' :
                messagebox.showerror("Error","Username must be Required!!!",parent=self.root)
            else:
                mycursor.execute("select email from student_info where email=%s" , ( self.txt_Email.get(),))
                email=mycursor.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid USERNAME",parent=self.root)
                else:
                    #=== forget window=============
                    self.var_otp=StringVar()
                    self.var_new_pass = StringVar()
                    self.var_conf_pass = StringVar()
                    chk=self.send_email(email[0])
                    if chk!='s':
                        messagebox.showerror("Error","Connection Error,try again",parent=self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("RESET PASSWORD")
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win,text='Reset Password',font=('goudy old style',15,'bold'),bg='red',fg='white').place(x=0,y=0,relwidth=1)
                        lb1_reset=Label(self.forget_win,text="Enter OTP Sent on Registered Email",font=("times new roman",15)).place(x=20,y=60)
                        txt_reset = Entry(self.forget_win, textvariable=self.var_otp, font=("times new roman", 15),bg='lightyellow').place(x=20, y=100,width=250,height=30)
                        self.btn_reset = Button(self.forget_win, command=self.validate_otp,text="SUBMIT", font=("times new roman", 15), bg='lightblue')
                        self.btn_reset.place(x=280, y=100, width=100, height=30)

                        lb1_new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                        txt_new_pass = Entry(self.forget_win, textvariable=self.var_new_pass, font=("times new roman", 15),bg='lightyellow').place(x=20, y=190,width=250,height=30)

                        lb1_conf_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                        txt_conf_pass = Entry(self.forget_win, textvariable=self.var_conf_pass, font=("times new roman", 15),bg='lightyellow').place(x=20, y=255,width=250,height=30)

                        # self.btn_reset = Button(self.forget_win, text="SUBMIT", font=("times new roman", 15), bg='lightblue')
                        # self.btn_reset.place(x=280, y=100, width=100, height=30)

                        self.btn_update = Button(self.forget_win, command=self.update_password,text="UPDATE", state=DISABLED, font=("times new roman", 15), bg='lightblue')
                        self.btn_update.place(x=150, y=300, width=100, height=30)
        except Exception as es:
            print("forgrt error")
            messagebox.showerror('error',f"Error Due to:{str(es)}",parent=self.root)
    
    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=='':
            messagebox.showerror("Error","Password is required",parent=self.forget_win)
        elif self.var_new_pass.get()!= self.var_conf_pass.get():
            messagebox.showerror("Error","New Password & confirm password should be same",parent=self.forget_win)
        else:
            con = mysql.connector.connect(user='root',
                                          password='Pooja@2015104',
                                          host='127.0.0.1',
                                          database='registration')
            mycursor = con.cursor()
            try:
                print(self.txt_Email.get())
                mycursor.execute('Update student_info SET password=%s where email=%s',(self.var_new_pass.get(),self.txt_Email.get()))
                con.commit()
                messagebox.showerror("Success","Password Updated Successfully!!",parent=self.forget_win)
                self.forget_win.destroy()

            except Exception as es:
                print("update error")
                messagebox.showerror('error',f"Error Due to:{str(es)}",parent=self.root)

    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP,Try again",parent=self.forget_win)


    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_ = email_pass.email_
        pass_ = email_pass.pass_

        s.login(email_,pass_)

        self.otp = int(time.strftime('%H%S%M'))+int(time.strftime('%S'))
        
        subj='IMS-Resect Password OTP'
        msg=f'Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nIMS Team'
        msg="subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return's'
        else:
            return'f'

    def signup(self):
        self.root.destroy()
        import signup.py
    
   
    
    def back(self):
        self.root.destroy()
        import signup.py


root = Tk()
obj = login_page(root)
root.mainloop()


