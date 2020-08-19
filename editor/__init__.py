import os
from time import sleep
def addfav(path):
    with open("FavPath.txt" ,'r') as file:
        for line in file:
            x = list[line]
            if path in x :
                pass
            else:
                add__p = input("Do you want to add path in your favourites?")
                print('answer with y or n')
                if add__p == 'y':
                    with open("FavPath.txt",'a') as file:
                        file.write(path)
                        file.write(\n)
                        


def getPath(path,mode):
    if mode == 'w':
        addfav(path)
        with open(path, mode='w+') as to_be_edited:
            Edit_And_overwrite(to_be_edited)

    elif mode == 'ov':
        addfav(path)
        overwrite(path)


    else:
        with open(path, mode='r') as read:
            addfav(path)
            Readout(read)

def Edit_And_overwrite(file):
    print("you are ready to go! \n")
    lines = int(0)
    n = int(0)
    t_char = int(0)
    while True:
        p = str(input("c: "))
        lines = lines + 1
        if p == ".":
            file.close()
            x = (lines - n)-1
            print("lines:",x)
            print("total characters:",t_char)
            break
        elif p == "/n":
            file.write('\n')
            n = n + 1
        elif p == " " :
            n = n+1
        elif p == "":
            n = n + 1
        elif p == "--h" :
            with open("help.txt",'r') as file:
                for line in file:
                    print(line)
        else:
            file.write(p)
            file.write('\n')
            x = len(p)
            t_char = x + t_char

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
