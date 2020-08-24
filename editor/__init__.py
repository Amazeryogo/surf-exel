from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import editor

root = Tk()
root.title('surf-exel')
root.geometry("1200x600")
global file_status
file_status = False

global selected
selected = False



def version():
    messagebox.showinfo('version',editor.version)

def cuttext(e):
    global selected
    if my_text.selection_get():
        selected = my_text.selection_get()
        my_text.delete("sel.first","sel.last")
def copytext(e):
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
def pastetext(e):
    if selected:
        pos = my_text.index(INSERT)
        my_text.insert(pos,selected)

def saveCurrentFile(e):
    global file_status
    if file_status:
        textr = open(file_status, 'w')
        textr.write(my_text.get(1.0,END))
        textr.close()
        root.title('file saved')
    else:
        saveAsFile()


def new_file(e):
    my_text.delete("1.0",END)
    root.title('A new file')
    global file_status
    file_status = False

def open_file():
    my_text.delete("1.0",END)
    file = filedialog.askopenfilename(initialdir='',title="opening a file")
    if file:
        global file_status
        file_status = file
    file = open(file, mode='r')
    spyders = file.read()
    my_text.insert(END,spyders)

def saveAsFile():
    textr = filedialog.asksaveasfilename(defaultextension=".txt",initialdir='',title="saving the file")
    textr = open(textr, 'w')
    textr.write(my_text.get(1.0,END))
    textr.close()




my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill = Y)


my_text = Text(my_frame,width=80,height=30,font=('Helvetica',14),selectbackground="grey",selectforeground='white',undo=True,yscrollcommand=text_scroll.set)

my_text.pack()



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
edit_menu.add_command(label = "Cut" , command = lambda: cuttext(False))
edit_menu.add_command(label = "Copy", command = lambda: copytext(False))
edit_menu.add_command(label = "Paste",command = lambda: pastetext(False))
edit_menu.add_command(label = "Redo")
edit_menu.add_command(label = "Undo")







text_scroll.config(command= my_text.yview)




root.bind('<Control-Key-x>',cuttext)
root.bind('<Control-Key-c>',copytext)
root.bind('<Control-Key-v>',pastetext)
root.bind('<Control-Key-n>',new_file)
root.bind('<Control-Key-s>',saveCurrentFile)
root.mainloop()
