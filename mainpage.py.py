from tkinter import*
from PIL import Image, ImageTk



class main_page:
    def __init__(self, root):
        self.root = root
        self.root.title("MAIN PAGE || Developed By Pooja Bhardwaj ")
        self.root.geometry("900x600+170+50")
        self.root.config(bg="#ffc046")

        self.root.resizable(False, False)

        self.var_option_login = StringVar()
        self.var_option_sign_up = StringVar()
       
        # #====== images ==========================
       

        main_Frame = Frame(self.root, bd=1, relief=RIDGE, bg='white', highlightbackground="black",highlightthickness=1)
        main_Frame.place(x=100,y=80,width=710,height=450)
       
        image = Image.open('mainpage1.png')
        print(f"Original size : {image.size}")
        self.img_image_resized = image.resize((250, 250))
        self.img_image_resized.save('mainpage1.png')
        self.main_image = ImageTk.PhotoImage(file="mainpage1.png")
        self.lb1_main_image = Label(main_Frame, image=self.main_image, bg="white").place(x=50, y=170)
       
        lb1_stud=Label(main_Frame,text="Student Login",font=("time new roman",30,'bold'),bg="white").place (x=50,y=45)
        lb1_stud2=Label(main_Frame,text=("Welcome to Student Managment System \nDeveloped by Pooja Bhardwaj "),font=("goudy old style",13),bg="white").place (x=55,y=100)
        #============= image frame 2 ==============================
        img_Frame = Frame(self.root, bd=2, bg='white')
        img_Frame.place(x=600, y=150, width=140, height=160)
        image = Image.open('gndeclogo.png')
        print(f"Original size : {image.size}")  # 5464x3640

        self.logo_image_resized = image.resize((120, 90))
        self.logo_image_resized.save('gndeclogo.png')
        self.logo_image=ImageTk.PhotoImage(file="gndeclogo.png")
        self.lb1_logo_image=Label(img_Frame,image=self.logo_image,bg="white").place(x=10,y=0)
       

        #============ option2 frame================
        option_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='white')
        option_Frame.place(x=460, y=245, width=300, height=250)

        # title=Label(option_Frame,text="MAIN SCREEN",font=("goudy old style",20),bg="#009999",fg='black').place (x=0,y=0,relwidth=1)
         
        #=============== login button ===================
        btn_login = Button(option_Frame, text="LOGIN", command=self.login,font=("times new roman", 15, 'bold'),bd=0, bg="#2196f3", fg='white').place(x=100, y=70, width=180, height=35)
        btn_signup = Button(option_Frame, text="SIGNUP", command=self.signup,font=("times new roman", 15, 'bold'), bg="#990000", bd=0, fg='white').place(x=100, y=120, width=180, height=35)
        # btn_fpassword= Button(option_Frame, text="FORGET PASSWORD",font=("times new roman", 12,'bold'), bg="navy blue",bd=0, fg='white').place(x=100, y=170,width=180,height=35)
 
        
    def login(self):
        self.root.destroy()
        import forget_pass.py




















































































































































































































































































        
    
    def signup(self):
        self.root.destroy()
        import signup.py





root = Tk()
obj = main_page(root)
root.mainloop()
