import editor

from editor import root
from editor import *


root.mainloop()


'''my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill = Y)


my_text = Text(my_frame,width=80,height=30,font=('Helvetica',14),selectbackground="grey",selectforeground='white',undo=True,yscrollcommand=text_scroll.set)


my_text.pack()

my_menu = Menu(root)
root.config(menu=my_menu)

about_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='About',menu=file_menu)
file_menu.add_command(label = "Version",command = version)

file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label = "Open",command = open_file)
file_menu.add_command(label = "Save", command = saveCurrentFile)
file_menu.add_command(label = "Save as",command = saveAsFile)
file_menu.add_command(label = "New file",command = new_file)

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
root.bind('<Control-Key-s>',saveCurrentFile)'''
#cool , will remove this if it works well on a mac without this

