import editor

print("Welcome to surf-exel command-line editor")
print("please enter the path, \n if you don't know what path is,write --h{path} ")


def getPathandopeneditor():
    x = input("path: ")
    if x == "--h{path}":
        print("the path is where your file is located, for example")
        print("C:\\Users\\Admin\\Desktop\\results.txt'")
        print("C:\\Users\\suresh\\gopher\\go.py'")
        getPathandopeneditor()
    else:
        y = input("mode:")
        if y == "w":
            editor.getPath(x, "w")
        elif y == "r":
            editor.getPath(x, "r")
        elif y == "ov":
            editor.getPath(x,"ov")
        else:
            print("ERROR: Invalid mode")

getPathandopeneditor()
