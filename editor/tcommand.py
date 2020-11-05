import os
import platform

def terminal(e):
    if platform.system() != 'Windows': 
        os.system("bash terminal.sh")
    else:
        os.system("sh terminal.sh")
