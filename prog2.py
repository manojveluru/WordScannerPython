#!/usr/bin/python3
import sys
import re
import os
def checkArgs():
	if len(sys.argv)<3 or len(sys.argv)>3:
		sys.stderr.write("enter correct usage")
		sys.exit()
	else:
		return sys.argv[1],sys.argv[2]

def openFiles(files):
	if os.path.isfile(files[0]) and os.path.isfile(files[1]):
		f = open(files[0])
		g = open(files[1])
		return f,g
	else:
		print("Can't open file: "+os.path.abspath(files[0]),file=sys.stderr)
		sys.exit()
		
		
def closeFiles(fobjects):
	fobjects[0].close()
	fobjects[1].close()

def createList(inFileObj):
	words=[]
	#mystr.replace('-', ' ').split(' ')
	for line in inFileObj[0]:
		#line = line.replace("'","-")
		for word in line.replace('-',' ').split(' '):
			word = word.strip()
			words.append(word)
			
	return words
	
def createDictionary(words):
	s =[]
	#print(words)
	#regex = re.compile('[^a-zA-Z]')
	for wor in words:
		sub = "'"
		subb= "\n"
		if sub in wor:
			wor = wor.split("'")
			#print(ge[0].lower())
			s.append(wor[0].lower())
		elif subb in wor:
			wor = wor.replace(" ","")
		else:	
			print(wor)
			result = re.sub('[^a-zA-Z]', "", wor)
			s.append(result.lower())
	dic = {}
	for w in s:
		dic[w] = s.count(w)
	
	for key in sorted(dic.keys()):
		#print ("%s: %s" % (key, dic[key]))
		print("",end='')
	print(len(dic))
	#print(sorted(dic))
	
def printDictionary():
	fileObj = openFiles(checkArgs())
	wordsList = createList(fileObj)
	createDictionary(wordsList)
	closeFiles(fileObj)
	
#createDictionary(createList(openFiles(checkArgs())))
printDictionary()			