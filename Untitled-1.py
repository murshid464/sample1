from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("Clock")

def time():
    string=strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000, time
    
time()

mainloop()

ghhhgg