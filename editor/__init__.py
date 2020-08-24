from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import editor.version as ev

root = Tk()
root.title('Surf-exel')
root.geometry("800x500")
global file_status
file_status = False

global selected
selected = False



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

def saveCurrentFile(e):
    global file_status
    if file_status:
        textr = open(file_status, 'w')
        textr.write(text.get(1.0,END))
        textr.close()
        root.title('file saved')
    else:
        saveAsFile()


def new_file(e):
    text.delete("1.0",END)
    root.title('A new file')
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




frame = Frame(root)
frame.pack(pady=5)

text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT,fill = Y)

bottom_scroll = Scrollbar(frame,orient="horizontal")
bottom_scroll.pack(side = BOTTOM,fill = X)

text = Text(frame,width=80,height=30,font=('Helvetica',14),selectbackground="grey",selectforeground='white',undo=True,yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=bottom_scroll.set)
text.pack()



global my_menu
my_menu = Menu(root)
root.config(menu=my_menu)

global file_menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label = "Open",command = open_file)
file_menu.add_command(label = "Save", command = saveCurrentFile)
file_menu.add_command(label = "Save as",command = saveAsFile)
file_menu.add_command(label = "New file",command = new_file)
file_menu.add_command(label = "Version",command = version)

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



root.bind('<Control-Key-x>',cuttext)
root.bind('<Control-Key-c>',copytext)
root.bind('<Control-Key-v>',pastetext)
root.bind('<Control-Key-n>',new_file)
root.bind('<Control-Key-s>',saveCurrentFile)
root.mainloop()
