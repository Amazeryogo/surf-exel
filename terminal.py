from tkinter import *
import os

root = Tk()
root.title("Surf-exel terminal")
term = Frame(root, height=400, width=500)
term.pack(fill=BOTH, expand=YES)
wid = term.winfo_id()
os.system('xterm -into %d -geometry 600x400 -sb &' % wid)

root.mainloop()