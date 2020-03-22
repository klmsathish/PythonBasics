
from tkinter import Tk,Label,Button
root = Tk()
root.title("MY GRAPHICS")
msg = Label(root,text = "WELCOME TO SRET")
msg.config(font = ("Cloister Black",50,"underline","italic","bold"))
msg.pack()
msg_button = Button(root,text = "EXIT",command = root.destroy)
msg_button.config(font = ("Cloister Black",18,"underline","bold"))
def ask():
    print("WELCOME TO PYTHON CLASS")
msg_button1 = Button(root,text = "SIGN UP ",command = ask)
msg_button1.config(font = ("Notre Dame",18,"underline","bold"))
msg_button1.pack()
msg_button.pack()
root.mainloop()
