#!/bin/bash


echo "Installing all the libraries..... \n"


pip3 install gTTS
pip3 install playsound

git init 



git fetch --all && git checkout --force "origin/master"


echo "surf-exel should work now , there is a problem if surf-exel is not working properly"
python3 main.py