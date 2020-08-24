from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import editor.version as ev
import time

root = Tk()
root.title('Surf-exel')
root.geometry("800x500")
global file_status
file_status = False

global selected
selected = False

frame = Frame(root)


text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT,fill = Y)

bottom_scroll = Scrollbar(frame,orient="horizontal")
bottom_scroll.pack(side = BOTTOM,fill = X)


text = Text(frame,width=80,height=30,font=('Helvetica',14),selectbackground="grey",selectforeground='white',undo=True,yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=bottom_scroll.set)


def version():
    messagebox.showinfo('version',ev.v)

def cuttext(e):
    global selected
    if text.selection_get():
        selected = text.selection_get()
        text.delete("sel.first","sel.last")
def copytext(e):
    if e:
        selected = root.clipboard_get()

    if text.selection_get():
        selected = text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
def pastetext(e):
    if selected:
        pos = text.index(INSERT)
        text.insert(pos,selected)

def saveCurrentFile():
    global file_status
    if file_status:
        textr = open(file_status, 'w')
        textr.write(text.get(1.0,END))
        textr.close()
        root.title('file saved')
    else:
        saveAsFile()


def new_file():
    text.delete("1.0",END)
    global file_status
    file_status = False

def open_file():
    text.delete("1.0",END)
    file = filedialog.askopenfilename(initialdir='',title="Open")
    if file:
        global file_status
        file_status = file
    file = open(file, mode='r')
    spyders = file.read()
    text.insert(END,spyders)

def saveAsFile():
    textr = filedialog.asksaveasfilename(defaultextension=".txt",initialdir='',title="Save")
    textr = open(textr, 'w')
    textr.write(text.get(1.0,END))
    textr.close()


global my_menu
my_menu = Menu(root)
root.config(menu=my_menu)

global file_menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label = "Open",command = open_file,accelerator="Ctrl+o")
file_menu.add_command(label = "Save", command = saveCurrentFile,accelerator="Ctrl+s")
file_menu.add_command(label = "Save as",command = saveAsFile)
file_menu.add_command(label = "New file",command = new_file,accelerator="Ctrl+n")
file_menu.add_command(label = "Version",command = version,accelerator="Ctrl+q")

global edit_menu
edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label = "Cut" , command = lambda: cuttext(False), accelerator="Ctrl+x")
edit_menu.add_command(label = "Copy", command = lambda: copytext(False),accelerator="Ctrl+c")
edit_menu.add_command(label = "Paste",command = lambda: pastetext(False),accelerator="Ctrl+v")
edit_menu.add_command(label = "Redo",command = text.edit_redo,accelerator="Ctrl+y")
edit_menu.add_command(label = "Undo",command = text.edit_undo,accelerator="Ctrl+z")







text_scroll.config(command= text.yview)
bottom_scroll.config(command= text.xview)

frame.pack(pady=5)
text.pack()
root.bind('<Control-Key-x>',cuttext)
root.bind('<Control-Key-c>',copytext)
root.bind('<Control-Key-v>',pastetext)
root.bind('<Control-Key-n>',new_file)
root.bind('<Control-Key-s>',saveCurrentFile)
root.bind('<Control-Key-q>',version)
root.bind('<Control-Key-o>',open_file)
root.bind('<Control-Key-n>',new_file)
root.mainloop()
