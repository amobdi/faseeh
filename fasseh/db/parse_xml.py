import xml.etree.ElementTree as xe
import sys
from textblob import Word
from textblob.wordnet import VERB, NOUN
from collections import defaultdict

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

def represent_line(string) :
	line = ''
	words = string.split('*')
	for word in words :
		word = word.strip()
		if word :
			if line :
				line = line + ' * ' + word
			else :
				line = word
	return line


def get_synomyns(string) :
	dictionary = {}
	words = string.split('*')
	for word in words :
		word = word.strip()
		word = word.lower()
		if word :
			word_syn = Word(word)
			if len(word_syn.synsets) > 0 :
				synomyns = word_syn.synsets[0].lemma_names()
				for synomyn in synomyns :
					if synomyn and synomyn != word :
						synomyn.upper()
						if synomyn not in dictionary :
							# print synomyn, 'no int', dictionary.keys()
							dictionary[synomyn] = []
						if word not in dictionary[synomyn] :
							dictionary[synomyn].append(word)

	print dictionary.keys()
	# for key in dictionary :
	# 	print key, dictionary[key]
	# 	for item in dictionary[key] :
	# 		print '	<category>'
	# 		print '		<pattern>*', key , '*</pattern>'
	# 		print '		<template>'
	# 		print '			<srai><star index="1"/>', item ,'<star index="2"/></srai>'
	# 		print '		</template>'

sys.stdout = open('test.xml', 'w')

root = xe.parse('final.xml').getroot()
for child in root :
	get_synomyns(child[0].text)
