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
    while True:
        p = str(input("commit: "))
        if p == ".":
            file.close()
            break
        elif p == "/n":
            file.write('\n')
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
