# What is surf-exel?

surf-exel is a silly editor.


It takes in an os path to a file, for example:

#### /Users/username/Dropbox/blueberry/hi.txt

and asks you to give one mode, r for reading and w for writing or ov to overwrite and destroy the contents of a file.

## When you give the mode w

It asks you to commit in a while loop.
to stop it asking, take a new line and write a full stop
.
## When you give the mode r

It prints the contents of a file and breaks.

## When you give the mode ov

Destroys the contents of a file

## How do I run Surf-exel?
### To use surf-exel , you need python 3.7 and above , and some terminal experience

go to your terminal
navigate to the directory where your surf-exel is kept using cd, for example:

$cd Downloads <br/>
$cd surf-exel


now use ls, if you find 2 files , main.py and editor (along with a bunch of files like README.md and LICENSE) then you are on the correct path.
next, write  
#### python3.7 main.py

and it should work!

You may find bugs, so if you find bugs,please report them in issues

## Updates:
to make a new line , please hit an enter ,
commit /n to create a new line
