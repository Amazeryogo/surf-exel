from tkinter import *
import os

root = Tk()
root.title("Surf-exel terminal")
termf = Frame(root, height=400, width=500)
termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 600x400 -sb &' % wid)

root.mainloop() 