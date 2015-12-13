import xml.etree.ElementTree as xe
import sys

def clear_string(string) :
	line = ''
	words = string.split()
	for word in words :
		if word :
			if word[-1] == '.' :
				word = word + '\n'
			if line :
				line = line + ' ' + word
			else :
				line = word
	if line and line[-1] == '\n' :
		line = line[0:len(line)-1]
	return line

def clear_string_only_words(string) :
	line = ''
	words = string.split()
	for word in words :
		if word.isalnum() :
			if line :
				line = line + ' ' + word
			else :
				line = word
	
	return line

sys.stdout = open('test.xml', 'w')

print ('<?xml version="1.0" encoding="UTF-8"?>')
print ('<aiml version="1.0.1" encoding="UTF-8">')

root = xe.parse('train.xml').getroot()

i = 0
for child in root :

	child[0].text = clear_string_only_words(child[0].text)
	child[1].text = clear_string(child[1].text)

	if child[0].text and child[0].text[0] != '*' :
		child[0].text = '* ' + child[0].text 
	if child[0].text and child[0].text[-1] != '*' :
		child[0].text = child[0].text + ' *' 
	
	print ("	<category>")
	print ("		<pattern>" + child[0].text + "</pattern>")
	print ("		<template>" + child[1].text + "</template>")
	print ("	</category>")

print ('</aiml>')