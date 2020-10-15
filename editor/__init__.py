from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox,simpledialog
import time
from editor.colourx import backgroundcolor as bc
from editor.colourx import forgroundcolor  as fc
from editor.colourx import back as b
from editor.colourx import fore as f
from gtts import gTTS
import playsound
import re

global ev
ev = 'surf-exel v5.3'

root = Tk()
root.title('Surf-exel')
root.geometry("800x600")
global file_status
file_status = False

global selected
selected = False

frame = Frame(root, background= bc)
Label(frame, text ='Find').pack(side = LEFT)
edit = Entry(frame)
edit.pack(side = LEFT, fill = BOTH, expand = 1)
edit.focus_set()

Find = Button(frame, text ='Find')
Find.pack(side = LEFT)


Label(frame, text = "Replace With ").pack(side = LEFT)

edit2 = Entry(frame)
edit2.pack(side = LEFT, fill = BOTH, expand = 1)
edit2.focus_set()

replace = Button(frame, text = 'Replace')
replace.pack(side = LEFT)

frame.pack(side = TOP)

text = Text(root,undo=True,foreground = f, background = b,height= 20)

def tsversion():
    tts = gTTS('version 5.4')
    tts.save('version.mp3')
    playsound.playsound('version.mp3')
    


def find():
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    if (s):
        spyder = '1.0'
        while 1:
            spyder = text.search(s, spyder, nocase = 1,
                            stopindex = END)

            if not spyder: break
            lastspyder = '% s+% dc' % (spyder, len(s))

            text.tag_add('found', spyder, lastspyder)
            spyder = lastspyder

        text.tag_config('found', foreground = "red")
    edit.focus_set()

def findNreplace():
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    r = edit2.get()
    if (s and r):
        spyder = '1.0'
        while 1:
            spyder = text.search(s, spyder, nocase = 1,
                            stopindex = END)
            print(spyder)
            if not spyder: break
            lastspyder = '% s+% dc' % (spyder, len(s))

            text.delete(spyder, lastspyder)
            text.insert(spyder, r)

            lastspyder = '% s+% dc' % (spyder, len(r))

            text.tag_add('found', spyder, lastspyder)
            spyder = lastspyder

        text.tag_config('found', foreground = fc, background = bc)
    edit.focus_set()


Find.config(command = find)
replace.config(command = findNreplace)


def tsat():
    goat = text.get('1.0',END)
    tts = gTTS(goat)
    tts.save('texttospeech.mp3')
    playsound.playsound('texttospeech.mp3')


def version():
    messagebox.showinfo('version',ev)

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

def saveCurrentFile(o):
    global file_status
    if file_status:
        textr = open(file_status, 'w')
        textr.write(text.get(1.0,END))
        textr.close()
        root.title('file saved')
    else:
        saveAsFile()

def new_file(o):
    text.delete("1.0",END)
    global file_status
    file_status = False

def open_file(o):
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


global about_menu
about_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='About',menu=about_menu)
about_menu.add_command(label = "Version",command = version)
about_menu.add_command(label='Text-to-speech Version',command = tsversion)


global file_menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label="text-to-speech-contents",command=tsat)
file_menu.add_command(label = "Open",command = open_file,accelerator="Ctrl+o")
file_menu.add_command(label = "Save", command = saveCurrentFile,accelerator="Ctrl+s")
file_menu.add_command(label = "Save as",command = saveAsFile)
file_menu.add_command(label = "New file",command = new_file,accelerator="Ctrl+n")


global edit_menu
edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label = "Cut" , command = lambda: cuttext(False), accelerator="Ctrl+x")
edit_menu.add_command(label = "Copy", command = lambda: copytext(False),accelerator="Ctrl+c")
edit_menu.add_command(label = "Paste",command = lambda: pastetext(False),accelerator="Ctrl+v")
edit_menu.add_command(label = "Redo",command = text.edit_redo,accelerator="Ctrl+y")
edit_menu.add_command(label = "Undo",command = text.edit_undo,accelerator="Ctrl+z")



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
