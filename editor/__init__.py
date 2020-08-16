import os
from time import sleep
def getPath(path,mode):
    if mode == 'w':
        with open(path, mode='w+') as to_be_edited:
            Edit_And_overwrite(to_be_edited)

    elif mode == 'ov':
        overwrite(path)

    else:
        with open(path, mode='r') as read:
            Readout(read)
def Edit_And_overwrite(file):
    print("you are ready to go! \n")
    lines = int(0)
    n = int(0)
    while True:
        p = str(input("c: "))
        lines = lines + 1
        if p == ".":
            file.close()
            x = (lines - n)-1
            print("lines:",x)
            break
        elif p == "/n":
            file.write('\n')
            n = n + 1
        elif p == " " :
            n = n+1
        elif p == "":
            n = n + 1
        else:
            file.write(p)

def Readout(file):
    for line in file:
        print(line)

def overwrite(file):
    x = input("Are you sure you want to do it?")
    if x == "y":
        f = open(file, 'r+')
        f.truncate(0)
    elif x == "n":
        sleep(2)
    else:
        print("error, please answer with y or n")
        overwrite(file)
