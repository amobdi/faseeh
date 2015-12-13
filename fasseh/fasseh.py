import logging
import logger

from textblob import TextBlob
import aiml
from Parser import *
import os

import chat, main
from PyQt4 import QtGui, QtCore
import sys

import socket
import thread
import time

class Faseeh(object) :
	def __init__(self) :
		
		self.log = logging.getLogger('fasseh.main')
		self.log.info('Faseeh Started')

		self.questions = ['What is upper ontology?', 'What is ontological engineering?', 'What is reification?']
		self.enemy_direction = 1
		self.my_direction = 0

		self.SERVER_PORT = 5678
		self.BUFFER_SIZE = 1024
		self.TIME_OUT = 10		# 10 seconds

		# Core
		self.kernel = aiml.Kernel()
		self.kernel.learn(os.getcwd() + '/fasseh/db/train.xml')
		self.parser = Parser()
		self.no_answer_string = 'I do not have an answer'

		self.blob = TextBlob('What is upper ontology')
		self.parser.get_all_question_combinations(self.blob.tags)

		# GUI
		self.app = QtGui.QApplication(sys.argv)
		self.MainWindow = QtGui.QMainWindow()
		self.ChatWindow = QtGui.QMainWindow()

		self.ui = main.Ui_MainWindow()
		self.ui.setupUi(self.MainWindow)
		self.ui2 = chat.Ui_MainWindow()
		self.ui2.setupUi(self.ChatWindow)

		self.ui2.pushButton_4.clicked.connect(lambda:self.goback()) 			# back_button
		self.ui.pushButton.clicked.connect(lambda:self.gochat('HTM'))    		# human_button
		self.ui.pushButton_2.clicked.connect(lambda:self.gochat('MTM'))  		# machine_button
		self.MainWindow.show()                             				# MAIN PAGE WINDOW    

		if len(sys.argv) == 2 :
			self.log.info('work as ' + sys.argv[1]) 
			self.gochatTest('MTM', '127.0.0.1', sys.argv[1])

		sys.exit(self.app.exec_())
	
	def answer_the_question(self, question) : 
		self.blob = TextBlob(question)
		question_combinations = self.parser.get_all_question_combinations(self.blob.tags)
		response = ''
		for sample_question in question_combinations :
			self.log.info('sample_question: ' + sample_question)
			response = self.kernel.respond(sample_question)
			if response != self.no_answer_string :
				break

		self.log.info('response: ' + response)
		self.log.info('---------------------------------------------------------------------')	
		return response

	def client_work(self, ServerIP) :
		try :
			self.log.info('client started')
			comm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			comm_socket.settimeout(self.TIME_OUT)
			comm_socket.connect((ServerIP, self.SERVER_PORT))
			self.log.info('client connected')
			for question in self.questions :
				self.log.info('question: ' + question)
				comm_socket.send( question + '#' )
				self.ui2.add_new_label(0, question)
				answer = str( comm_socket.recv(self.BUFFER_SIZE) )
				while not '#' in answer:
					answer = str( comm_socket.recv(BUFFER_SIZE) )
				self.log.info('answer: ' + answer)
				self.ui2.add_new_label(1, answer)

			comm_socket.close()	
		except Exception, e:
			print (str(e))

	def server_work(self, ServerIP) :
		try :
			self.log.info('server started')
			comm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			comm_socket.bind((ServerIP, self.SERVER_PORT))
			comm_socket.listen(1)
			conn, addr = comm_socket.accept()
			conn.settimeout(self.TIME_OUT)
			self.log.info('server connected')
			for i in range (len(self.questions)):
				question = str( conn.recv(self.BUFFER_SIZE) )
				while not '#' in question:
					question = str( conn.recv(self.BUFFER_SIZE) )

				self.ui2.add_new_label(self.enemy_direction, question)
				self.log.info('question: ' + question)
				answer = self.answer_the_question(question)
				self.log.info('answer: ' + answer)
				self.ui2.add_new_label(self.my_direction, answer)
				conn.send( answer + '#' )

			conn.close()
		except Exception, e:
			print (str(e))

	def human_work(self) :
		question = str( self.ui2.textEdit.toPlainText() )
		if question :
			self.ui2.add_new_label(self.enemy_direction, question)
			answer = self.answer_the_question(question)
			self.ui2.add_new_label(self.my_direction, answer)
		else :
			print 'Write your question first'

	def gochat(self, mode) :
		self.ChatWindow.show()
		self.MainWindow.hide()

		# Machine To Machine
		if mode == 'MTM' :
			ServerIP = self.ui.lineEdit.text()
			self.log.info('ServerIP: ' + ServerIP)

			if self.ui.radioButton.isChecked() :		# client
				self.client_work(ServerIP)
			elif self.ui.radioButton_2.isChecked() and ServerIP != '' :		# server	
				self.server_work(ServerIP)
			else :
				print 'Invalid Arguements, Please fill the required fields'
		else :
			# Human To Machine
			QtCore.QObject.connect(self.ui2.textEdit, QtCore.SIGNAL("sendMessage"), lambda:self.human_work())
			self.ui2.pushButton_3.clicked.connect(lambda:self.human_work())
		
	def gochatTest(self, mode, ServerIP, conn_mode) :
		# Machine To Machine
		if mode == 'MTM' :
			self.log.info('ServerIP: ' + ServerIP)

			if conn_mode == 'c' :		# client
				self.client_work(ServerIP)
			elif conn_mode == 's' and ServerIP != '' :		# server	
				self.server_work(ServerIP)
			else :
				print 'Invalid Arguements, Please fill the required fields'


	def goback(self) :
		MainWindow.show()
		ChatWindow.close()

if __name__ == '__main__':
	faseeh = Faseeh()