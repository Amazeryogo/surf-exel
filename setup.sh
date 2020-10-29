#!/bin/bash


echo "Installing all the libraries..... \n"


pip3 install gTTS
pip3 install playsound
pip3 install pyinstaller

git init 

git remote set-url origin git@github.com:Amazeryogo/surf-exel.git

git fetch --all && git checkout --force "origin/master"

echo "surf-exel should work now , there is a problem if surf-exel is not working properly"
pyinstaller --onefile main.py 
cd dist 
./main