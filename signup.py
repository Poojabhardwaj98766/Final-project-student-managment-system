
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
# import pymysql 
import mysql.connector


class login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("SIGNUP PAGE || Developed By Pooja Bhardwaj ")
        self.root.geometry("800x540+170+50")
        self.root.config(bg="#ffc046")

        main_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='white')
        main_Frame.place(x=70,y=70,width=650,height=410)
        
        self.var_stud_name = StringVar()
        self.var_stud_Email = StringVar()
        self.var_stud_contact = StringVar()
        self.var_stud_password = StringVar()
        self.var_stud_conf_pass= StringVar()

        #================= image ========================
        image = Image.open('signup1.png')
        print(f"Original size : {image.size}")  # 5464x3640

        self.img_image_resized = image.resize((220, 180))
        self.img_image_resized.save('signup1.png')
        self.img_image = ImageTk.PhotoImage(file="signup1.png")
        self.lb1_img_image = Label(main_Frame, image=self.img_image, bg="white").place(x=30, y=170)

        
        #============= logo ====================================
        image = Image.open('gndeclogo.png')
        print(f"Original size : {image.size}")  # 5464x3640

        self.logo_image_resized = image.resize((100, 80))
        self.logo_image_resized.save('gndeclogo.png')
        self.logo_image=ImageTk.PhotoImage(file="gndeclogo.png")
        self.lb1_logo_image=Label(main_Frame,image=self.logo_image,bg="white").place(x=400,y=10)
        
        #=================== text ==========================
        lb1_stud=Label(main_Frame,text="Student Signup",font=("time new roman",22,'bold'),bg="white").place (x=40,y=45)
        lb1_stud2=Label(main_Frame,text=("Fill your details to create an account "),font=("goudy old style",13),fg="gray",bg="white").place (x=30,y=90)

        #======================= details ====================
        lb1_name = Label(main_Frame, text="Student Name", font=("times new roman", 15,'bold'), bg="white").place(x=310, y=120)
        lb1_Email=Label(main_Frame,text="Email",font=("times new roman",15,'bold'),bg="white").place (x=310,y=160)
        lb1_contact=Label(main_Frame,text="Contact No",font=("times new roman",15,'bold'),bg="white").place (x=310,y=200)
        lb1_pasword=Label(main_Frame,text="Password",font=("times new roman",15,'bold'),bg="white").place (x=310,y=240)
        lb1_conf_pass=Label(main_Frame,text="Confirm Password",font=("times new roman",15,'bold'),bg="white").place (x=310,y=280)
       
        self.txt_name = Entry(main_Frame, font=("times new roman", 15),bg="light yellow")
        self.txt_name.place(x=480, y=120,width=150)
        self.txt_Email = Entry(main_Frame, font=("times new roman", 15) , bg="light yellow")
        self.txt_Email.place(x=480, y=160,width=150)
        self.txt_contact = Entry(main_Frame, font=("times new roman", 15),bg="light yellow")
        self.txt_contact.place(x=480, y=200,width=150)
        self.txt_password = Entry(main_Frame, font=("times new roman", 15),bg="light yellow")
        self.txt_password.place(x=480, y=240,width=150)
        self.txt_conf_pass= Entry(main_Frame, font=("times new roman", 15) ,bg="light yellow")
        self.txt_conf_pass.place(x=480, y=280,width=150)
        btn_sign_up= Button(main_Frame, text="Signup",command=self.register,font=("times new roman", 15, 'bold'), bd=0,bg="#ffc046", fg='white').place(x=360, y=350, width=180, height=35)
        

       

        # #============= check box ================================
        # chk=Checkbutton(main_Frame,text="I Agree The Terms & Conditions",bg="white",font=("time new roman",10)).place(x=310,y=320)

    #============== register funtion ========================
    def register(self):
        print(self.txt_name.get())
        if self.txt_name.get() == '' or self.txt_Email.get() == '' or self.txt_contact.get() == '' or self.txt_password.get() == '' or self.txt_conf_pass.get() == '':
            
            messagebox.showinfo('error',"All Field are Required!!!")
        elif self.txt_password.get() != self.txt_conf_pass.get():
            
            messagebox.showinfo('error'," Password or Confirm Password\n should be same!!")
        else:
            try:    
                con = mysql.connector.connect(user='root',
                                               password='Pooja@2015104',
                                               host='127.0.0.1',
                                               port='3306',
                                               database='registration')
                mycursor = con.cursor()
                print(mycursor)
                mycursor.execute("insert into student_info values(%s,%s,%s,%s)", (self.txt_name.get(), self.txt_Email.get() ,self.txt_contact.get() ,self.txt_password.get()))
                con.commit()
                
                messagebox.showinfo('error', "Register Successful")
                self.root.destroy()
                import forget_pass.py
            except Exception as es:
                print(es)
                messagebox.showerror('error', es)

    





root = Tk()
obj = login_page(root)
root.mainloop()       
