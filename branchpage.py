from tkinter import*
from PIL import Image, ImageTk

class branch_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Department PAGE || Developed By Pooja Bhardwaj ")
        self.root.geometry("500x560+170+50")
        self.root.config(bg="#ffc046")
    

        department_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white',highlightbackground="black", highlightthickness=1)
        department_Frame.place(x=50, y=50, width=400, height=450)

        lb1_details = Label(department_Frame, text="Choose Your Department..", font=("Elephant", 20), bg="white").place(x=20, y=170)
        lb1_details = Label(department_Frame, text="", font=("Elephant", 30, 'bold'), bg="white").place(x=80, y=20) 
        
        image = Image.open('mainpage.png')
        print(f"Original size : {image.size}")  # 5464x3640

        self.img_image_resized = image.resize((190, 150))
        self.img_image_resized.save('mainpage.png')
        self.img_image = ImageTk.PhotoImage(file="mainpage.png")
        self.lb1_img_image = Label(department_Frame, image=self.img_image, bg="white").place(x=90, y=0)

        btn_CSE = Button(department_Frame, text="CSE",command=self.managment_page, font=("Arial Rounded MT Bold", 15,'bold'), bg="#008F7A", fg='white').place(x=90, y=240, width=200, height=30)
        btn_IT = Button(department_Frame, text="IT", command=self.managment_page,font=("Arial Rounded MT Bold", 15,'bold'), bg="light blue", fg='white').place(x=90, y=280, width=200, height=30)
        btn_ECE = Button(department_Frame, text="ECE",command=self.managment_page, font=("Arial Rounded MT Bold", 15,'bold'), bg="#845EC2", fg='white').place(x=90, y=320, width=200, height=30)
        btn_CE = Button(department_Frame, text="CE",command=self.managment_page, font=("Arial Rounded MT Bold", 15,'bold'), bg="#053246", fg='white').place(x=90, y=360, width=200, height=30)
        btn_ME = Button(department_Frame, text="ME",command=self.managment_page, font=("Arial Rounded MT Bold", 15,'bold'), bg="#FF6F91", fg='white').place(x=90, y=400, width=200, height=30)
    

    def managment_page(self):
        self.root.destroy()
        import managment.py


root = Tk()
obj = branch_page(root)
root.mainloop()
