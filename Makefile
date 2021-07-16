CWD = ${PWD}
surf-exel: gtts pls pyi
	pyinstaller --onefile --name surf-exel  main.py 
	mv $(CWD)/dist/surf-exel /bin/

gtts: pp3 
	pip3 install gTTS
	touch $(CWD)/.cache/gtts
	echo "done!" > $(CWD)/.cache/gtts

pls: pp3
	pip3 install playsound
	touch $(CWD)/.cache/pls
	echo "done!" > $(CWD)/.cache/pls

pyi: pp3 
	pip3 install pyinstaller
	touch $(CWD)/.cache/pyi
	echo "done!" > $(CWD)/.cache/pyi

pp3:
	touch $(CWD)/.cache/pp3
	echo "done!" > $(CWD)/.cache/pp3


