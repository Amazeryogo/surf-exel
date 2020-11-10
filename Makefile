CWD = ${PWD}
surf-exel: gtts pls pyi 
	pyinstaller --onefile --name surf-exel  main.py 
	mv $(CWD)/dist/surf-exel $(CWD)/
		
gtts: pp3 
	pip3 install gTTS
	echo "done!" > $(CWD)/.cache/gtts

pls: pp3
	pip3 install playsound
	echo "done!" > $(CWD)/.cache/pls

pyi: pp3 
	pip3 install pyinstaller
	echo "done!" > $(CWD)/.cache/pyi

pp3: 
	echo "done!" > $(CWD)/cache/pp3

