import tkinter
import tkinter.tix as tix
from ttkbootstrap.widgets import Meter



root = tkinter.Tk()
root.geometry('400x400')


meter = Meter(master=root)

meter.grid(row=0 , column=0)



root.mainloop()