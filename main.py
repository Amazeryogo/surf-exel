import editor
import platform 
from editor import root
from editor import *
from editor.colourx import *

if platform.system() == 'Windows':
    print('Your OS is not supported,please install an older version of surf-exel ')
else:
    root.mainloop()
    