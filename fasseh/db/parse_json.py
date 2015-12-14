import json
import sys

sys.stdout = open('train.json', 'w')

fil = open('yes-no_heba.txt', 'r')
lines = fil.read().split('\n')
i = 0
text = ''
label = ''
data = []
for line in lines :
	line = line.strip()
	if len(line) > 1 :
		if i % 2 == 0 :
			line = line[:-1]
			text = line.strip().lower() + '?'
		else :
			label = line.strip().upper()

		if text and label :
			data.append({'text': text, 'label': label})
			text = ''
			label = ''
		i = i + 1

print json.dumps(data)