#!/usr/bin/python3
import sys
import re
import os
def checkArgs():
	if len(sys.argv)<3 or len(sys.argv)>3:
		sys.stderr.write("\tUsage: ./prog2.py inFile outFile\n\n")
		sys.exit()
	else:
		return sys.argv[1],sys.argv[2]

def openFiles(files):
	try:
		inputFile = open(files[0])
		outputFile = open(files[1],'w')
		outputFile.write("Output Values for Data: "+os.path.abspath(files[0])+"\n")
		return inputFile,outputFile
	except (OSError, IOError) as e:
		sys.stderr.write("Can't open file: "+os.path.abspath(files[0])+"\n\n")
		sys.exit()			
		
def closeFiles(fobjects):
	fobjects[0].close()
	fobjects[1].close()
	if not (fobjects[0].closed or fobjects[1].closed):
		sys.stderr.write("File cannot be closed")
		sys.exit()

def createList(inFileObj):
	words=[]
	wo=""
	for line in inFileObj[0]:
		for word in line.replace('-',' ').split(' '):
			word = word.strip()
			words.append(word)								
	return words
	
def createDictionary(words):
	newWords =[]
	for element in words:
		quote = "'"
		questionmark= "?"
		if quote in element:
			element = element.split("'")
			if element[0].isalpha():
				newWords.append(element[0].lower())
		elif questionmark in element:
			element = element.split("?")
			if element[0].isalpha():
				newWords.append(element[0].lower())
		else:		
			result = re.sub('[^a-zA-Z]', "", element)
			if result.isalpha():
				newWords.append(result.lower())
			
	dic = {}
	for key in newWords:
		dic[key] = newWords.count(key)
	return dic
	
def printDictionary():
	fileObj = openFiles(checkArgs())
	wordsList = createList(fileObj)
	dic = createDictionary(wordsList)
	i=0
	fileObj[1].write("---------------------------------------------------------\n")
	fileObj[1].write("size = "+str(len(dic)))
	fileObj[1].write("\n\n")
	for key in sorted(dic.keys()):
		if i<3:
			fileObj[1].write ("%-14s: %3s" % (key, dic[key])+"    ")
			i=i+1
		else:
			fileObj[1].write("\n")
			fileObj[1].write ("%-14s: %3s" % (key, dic[key])+"    ")
			i=1
	
	closeFiles(fileObj)
	

printDictionary()			