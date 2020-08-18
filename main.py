import editor

print("Surf-exel")
print("please enter the path, \n if you don't know what path is,write --h")


def getPathandopeneditor():
    x = input("p: ")
    if x == "--h":
        with open("help.txt",'r') as file:
            for line in file:
                print(line)
        getPathandopeneditor()
    else:
        y = input("m:")
        if y == "w":
            editor.getPath(x, "w")
        elif y == "r":
            editor.getPath(x, "r")
        elif y == "ov":
            editor.getPath(x,"ov")
        else:
            print("ERROR: Invalid mode")

getPathandopeneditor()
