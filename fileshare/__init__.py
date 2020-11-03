from socket import error
import tkinter
from tkinter import simpledialog 
import socket
import os
import tkinter
from tkinter import simpledialog
root = tkinter.Tk()
import platform
root.withdraw()

''' please read the README.md in the fileshare directory to learn more about this code '''
def share():
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096  
    code = simpledialog.askstring("Code", "Enter the code of the reciver")
    ip,port = code.split(':')
    s = socket.socket()
    try:
        s.connect((ip,port))
        # ASK FOR PASSWORD 
        file = tkinter.filedialog.askopenfilename(initialdir='', title="Open")
        with open(file, "rb") as f:
            for i in range(1,100):
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                else:
                    s.sendall(bytes_read)
            
                  
    except:
        tkinter.messagebox.showinfo("ERROR","ERROR, PLEASE TRY AGAIN LATER")

def recive():
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    if IP == "127.0.0.1":
        if platform.system() == "Darwin":
            IP = os.system("ipconfig getifaddr")
        elif platform.system() == "Linux":
            IP = os.system("hostname -I")
        else:
            # WE WILL ADD SUPPORT FOR WINDOWS in the next commit of this file 
            tkinter.messagebox.showinfo('PLATFORM NOT SUPPORTED', "PLATFORM NOT SUPPORTED")
            

    print(IP)
    print(platform.system())
    
recive()