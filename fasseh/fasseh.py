import logging
import logger

from textblob import TextBlob
import sys
import aiml
from Parser import *
import os

# Setting log information.
log = logging.getLogger('fasseh.main')

def main():

	log.info('Fasseh started')
	print os.getcwd()
	kernel = aiml.Kernel()
	kernel.learn(os.getcwd() + '/fasseh/db/train.xml')
	parser = Parser()
	no_answer_string = 'I do not have an answer'

	while True :
		question = raw_input('Enter Your Question >> ')
		log.info('question: ' +  question)
		if question == 'exit' :
			break
		blob = TextBlob(question)
		question_combinations = parser.get_all_question_combinations(blob.tags)
		for sample_question in question_combinations :
			response = kernel.respond(sample_question)
			if response != no_answer_string :
				break
		print response
		log.info('response: ' + response)
		log.info('---------------------------------------------------------------------')

if __name__ == '__main__':
    main()