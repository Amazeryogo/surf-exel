# What is Surf-exel?

Surf-exel is a simple editor built on top of Tkinter and written entirely in Python3 (along with some shell files).
It is lightweight and easily customizable to suit your needs. 
The non-GUI version was inspired by ed , a simple GNU text editor.

# How fast does it get updated ?
A new version of surf-exel is released in the time space of 18 hours to 18 days.
You have to update it manually though. 

# Can I contribute in it? Will a PR be counted in the Hacktoberfest?
Yes, Absolutely , All contributions are welcome and accepted! (As long as they make sense to be added).
All PR contributions are counted in the Hacktoberfest.
# Can my computer run it?
See the supportedplatforms.md in docs to find out if your computer can run surf-exel.

# Prerequisites

git, xterm for linux or iterm2 for MacOS 

# NOTE 
## 5.7 and Above
Surf-exel is not supported on Windows, please use a build below v5.7

## Below v5.7
Surf-exel may not work on Microsoft Windows , if thats the case, please try running main.py only and not building it using run.sh , sorry for the trouble. 

# How to run it ?
## Linux/MacOS
1) Download the source code by clicking the .zip file of the latest release and unzip it. 
2) Navigate to it using the cd command (it will most probably be in your Downloads. directory , so enter this your terminal: `cd Downloads/surf-exel-version-number`.
3) write `make`
4) `./surf-exel`
### Just run `./surf-exel` if your pwd is in surf-exel directory
### Please note that the terminal in surf-exel works on linux only because it uses xterm as it's terminal, if you want to use it on a mac , change xterm to iterm2
### if you like the bleeding edge of surf-exel, you can download it using 
 `sudo git clone https://github.com/Amazeryogo/surf-exel && cd surf-exel && mkdir .cache && make
`
### Warning!: We do not recommend going to the bleeding edge 


## Windows 
please see the NOTE above (sorry for the trouble).



