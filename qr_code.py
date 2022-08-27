
from tkinter import *
from turtle import title
import qrcode

root= Tk()
root.title("Qr Generator")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False,False)

Label(root,text="Title" ,fg="white" ,bg="red", font=15).place(x=50,y=170)


root.mainloop()

