from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from editor.colourx import backgroundcolor as bc
from editor.colourx import forgroundcolor  as fc
from editor.colourx import back as b
from editor.colourx import fore as f
from editor.colourx import size
from gtts import gTTS
import playsound
import re
import os

global ev
ev = 'surf-exel v5.6'
base_title = "Surf-exel"

root = Tk()
root.title(base_title)
root.geometry("600x400")
global file_status
file_status = False

global selected
selected = False

frame = Frame(root, background=bc)
Label(frame, text='Find').pack(side=LEFT)
edit = Entry(frame)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()

Find = Button(frame, text='Find')
Find.pack(side=LEFT)

edit2 = Entry(frame)
edit2.pack(side=LEFT, fill=BOTH, expand=1)
edit2.focus_set()

replaceall = Button(frame, text='Replace All')
replaceall.pack(side=LEFT)

frame.pack(side=TOP)

text = Text(root, undo=True, foreground=f, background=b, font=("Helvetica", size))
text.config(insertbackground='white')


def update():
    messagebox.showinfo('update', 'updating your surf-exel , please check the terminal to see the changes')
    os.system('sh update.sh')
    messagebox.showinfo('updated', 'updated , please relaunch surf-exel')
    quit()


def tsversion():
    tts = gTTS('version 5.6')
    tts.save('version.mp3')
    playsound.playsound('version.mp3')


def find():
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    if (s):
        spyder = '1.0'
        while 1:
            spyder = text.search(s, spyder, stopindex=END, regexp=True)

            if not spyder: break
            lastspyder = '% s+% dc' % (spyder, len(s))

            text.tag_add('found', spyder, lastspyder)
            spyder = lastspyder

        text.tag_config('found', foreground="red")
    edit.focus_set()

def replacex():
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    r = edit2.get()
    if (s and r):
        spyder = '1.0'
        while 1:
            spyder = text.search(s, spyder, stopindex=END, regexp=True)

            print(spyder)
            if not spyder: break
            lastspyder = '% s+% dc' % (spyder, len(s))

            text.delete(spyder, lastspyder)
            text.insert(spyder, r)

            lastspyder = '% s+% dc' % (spyder, len(r))

            text.tag_add('found', spyder, lastspyder)
            spyder = lastspyder

        text.tag_config('found', foreground=fc, background=bc)
    edit.focus_set()


Find.config(command=find)
replaceall.config(command=replacex)


def tsat():
    goat = text.get('1.0', END)
    tts = gTTS(goat)
    tts.save('texttospeech.mp3')
    playsound.playsound('texttospeech.mp3')


def version(e):
    messagebox.showinfo('version', ev)


def select_all(event):
    text.tag_add(SEL, "1.0", END)
    text.mark_set(INSERT, "1.0")
    text.see(INSERT)
    return 'break'


def cuttext(e):
    global selected
    if text.selection_get():
        selected = text.selection_get()
        text.delete("sel.first", "sel.last")


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
        text.insert(pos, selected)


def saveCurrentFile_wrapper(args):
    saveCurrentFile()


def saveCurrentFile():
    global file_status
    if file_status:
        textr = open(file_status, 'w')
        textr.write(text.get(1.0, END))
        textr.close()
        root.title(textr.name)
    else:
        saveAsFile()


def new_file_wrapper(args):
    new_file()


def new_file():
    text.delete("1.0", END)
    global file_status
    file_status = False
    root.title(base_title)


def open_file_wrapper(args):
    open_file()


def open_file():
    text.delete("1.0", END)
    file = filedialog.askopenfilename(initialdir='', title="Open")
    if file:
        global file_status
        file_status = file
    file = open(file, mode='r')
    spyders = file.read()
    root.title(file.name)
    text.insert(END, spyders)


def saveAsFile():
    textr = filedialog.asksaveasfilename(defaultextension=".txt", initialdir='', title="Save")
    textr = open(textr, 'w')
    textr.write(text.get(1.0, END))
    root.title(textr.name)
    textr.close()


global menu
menu = Menu(root)
root.config(menu=menu)

global about_menu
about_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label="Version", command=version('e'))
about_menu.add_command(label='Text-to-speech Version', command=tsversion)
about_menu.add_command(label="Update", command=update)

global file_menu
file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="text-to-speech-contents", command=tsat)
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+o")
file_menu.add_command(label="Save", command=saveCurrentFile, accelerator="Ctrl+s")
file_menu.add_command(label="Save as", command=saveAsFile)
file_menu.add_command(label="New file", command=new_file, accelerator="Ctrl+n")

global edit_menu
edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cuttext(False), accelerator="Ctrl+x")
edit_menu.add_command(label="Copy", command=lambda: copytext(False), accelerator="Ctrl+c")
edit_menu.add_command(label="Paste", command=lambda: pastetext(False), accelerator="Ctrl+v")
edit_menu.add_command(label="Redo", command=text.edit_redo, accelerator="Ctrl+y")
edit_menu.add_command(label="Undo", command=text.edit_undo, accelerator="Ctrl+z")


frame.pack(pady=5)
text.pack(fill=BOTH, side=BOTTOM, expand=True)
root.bind('<Control-Key-a>', select_all)
root.bind('<Control-Key-x>', cuttext)
root.bind('<Control-Key-c>', copytext)
root.bind('<Control-Key-v>', pastetext)
root.bind('<Control-Key-n>', new_file_wrapper)
root.bind('<Control-Key-s>', saveCurrentFile_wrapper)
root.bind('<Control-Key-q>', version)
root.bind('<Control-Key-o>', open_file_wrapper)
root.mainloop()

# Written in pycharm on a free open source license, Thanks @Jetbrains!
#  https://www.jetbrains.com/?from=surf-exel
# - Amazeryogo
