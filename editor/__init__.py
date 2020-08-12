import os

def getPath(path,mode):
    if mode == 'w':
        with open(path, mode='w+') as to_be_edited:
            Edit_And_overwrite(to_be_edited)
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
