from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Dangerous Malware Found!")

button = Button(root, text="Scan PC", command=msg)
button.place(x=75, y=80)

root.mainloop()