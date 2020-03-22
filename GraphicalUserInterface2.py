from tkinter import Tk,Label,Button,messagebox
root = Tk()
root.title("MY GRAPHICS")
msg = Label(root,text = "WELCOME TO SRET")
msg.config(font = ("callibri",50,"underline","italic","bold"))
msg.pack()
Title = "STUDENT FEEDBACK"
text = "DO YOU WANT TO ENROLL IN PYTHON CLASS ?"
reply = messagebox.askquestion(Title,text)
if reply == "yes":
    def ask():
        print("WELCOME TO PYTHON CLASS")
    msg_button1 = Button(root, text="SIGN UP ", command=ask)
    msg_button1.config(font=("Notre Dame", 18, "underline", "bold"))
    msg_button1.pack()
    NAME = input("ENTER YOUR NAME : ")
    MAIL = input("ENTER YOUR MAIL ID : ")
else:
    print("Who Cares")
    print("Thank You So Much")
    msg_button = Button(root, text="EXIT", command=root.destroy)
    msg_button.config(font=("Cloister Black", 18, "underline", "bold"))
    msg_button.pack()
root.mainloop()
