#!/bin/bash


echo "Installing all the libraries..... \n"


pip3 install gTTS
pip3 install playsound
pip3 install pyinstaller


echo "surf-exel should work now , there is a problem if surf-exel is not working properly"
pyinstaller --onefile  main.py  --distpath /usr/local
cd dist 
./main
cd ..
