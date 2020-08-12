import editor

print("Welcome to surf-exel command-line editor")
print("please make sure the file you are going to edit is pre-made and it can accessible to surf-exel")
print("please enter the path, \n if you don't know what path is,write --h{path} ")


def getPathandopeneditor():
    x = input("path: ")
    if x == "--h{path}":
        print("the path is where your file is located, for example")
        print("C:\\Users\\Admin\\Desktop\\results.txt'")
        print("C:\\Users\\suresh\\gopher\\go.py'")
    else:
        y = input("mode:")
        if y == "w":
            editor.getPath(x, "w")
        elif y == "r":
            editor.getPath(x, "r")
        else:
            print("ERROR: Invalid mode")

getPathandopeneditor()