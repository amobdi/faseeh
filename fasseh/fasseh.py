import logging
import logger

from textblob import TextBlob
from textblob.classifiers import *
import aiml
from Parser import *
import os

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread, SIGNAL
import chat, main

import sys
import socket
import json
import time


sys.setrecursionlimit(1000000)

class Faseeh(QtGui.QMainWindow) :

	def __init__(self) :
		
		super(self.__class__, self).__init__()

		self.log = logging.getLogger('fasseh.main')
		self.log.info('Faseeh Started')

		self.questions = [
			'Hi', 
			'How are you?', 
			'what is justification-based truth maintenance system?',
			'why Situation calculus is limited in its applicability?',
			'what does "action" and "event" connotes?',
			'state one characteristic of Categories of composite objects?',
			'list 4 routes used to build existing ontologies.',
			'give some example of extrinsic properties?',
			'describe one approach to truth maintenance?',
			'mention the main tradeoff involved when taking decisions ?'
		]

		self.enemy_direction = 1
		self.my_direction = 0

		self.SERVER_PORT = 5678
		self.BUFFER_SIZE = 1024
		self.TIME_OUT = 50		# 50 seconds

		# Core
		self.kernel = aiml.Kernel()
		self.kernel.learn(os.getcwd() + '/fasseh/db/train.xml')
		self.parser = Parser()
		self.no_answer_string = 'I do not have an answer'

		self.blob = TextBlob('What is upper ontology')
		self.parser.get_all_question_combinations(self.blob.tags, 'What is upper ontology')

		# classifier
		self.classifier = NaiveBayesClassifier(open(os.getcwd() + '/fasseh/db/train.json', 'r'), format='json')

		# GUI
		self.MainWindow = QtGui.QMainWindow()
		self.ChatWindow = QtGui.QMainWindow()

		self.ui = main.Ui_MainWindow()
		self.ui.setupUi(self.MainWindow)
		self.ui2 = chat.Ui_MainWindow()
		self.ui2.setupUi(self.ChatWindow)

		self.ui2.pushButton_4.clicked.connect(lambda:self.goback()) 			# back_button
		self.ui.pushButton.clicked.connect(lambda:self.gochat('HTM'))    		# human_button
		self.ui.pushButton_2.clicked.connect(lambda:self.gochat('MTM'))  		# machine_button

		QtCore.QObject.connect(self.ui2.textEdit, QtCore.SIGNAL("sendMessage"), self.human_work)
		self.ui2.pushButton_3.clicked.connect(self.human_work)

		self.MainWindow.show()                             				# MAIN PAGE WINDOW    

		if len(sys.argv) == 2 :
			self.log.info('work as ' + sys.argv[1]) 
			self.gochatTest('MTM', '127.0.0.1', sys.argv[1])
	
	def answer_the_question(self, question) : 
		question = question.lower()
		# question = self.parser.replace_not(question)
		if self.parser.check_yes_ques(question) :
			prob = self.classifier.prob_classify(question)
			prob_yes = prob.prob('YES')
			prob_no = prob.prob('NO')
			if prob_yes > prob_no :
				return 'YES'
			else :
				return 'NO'
		else :
			self.blob = TextBlob(question)
			question_combinations = self.parser.get_all_question_combinations(self.blob.tags, question)
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
		self.client_worker = client_work_thread(self, ServerIP)
		self.connect(self.client_worker, SIGNAL("update_enemy(QString)"), self.client_enemy_work_callback)
		self.connect(self.client_worker, SIGNAL("update_my(QString)"), self.client_my_work_callback)
		self.client_worker.start()

	def client_enemy_work_callback(self, question) :
		self.ui2.add_new_label(self.enemy_direction, question)

	def client_my_work_callback(self, answer) :
		self.ui2.add_new_label(self.my_direction, answer)

	def server_work(self, ServerIP) :
		self.server_worker = server_work_thread(self, ServerIP)
		self.connect(self.server_worker, SIGNAL("update_enemy(QString)"), self.server_enemy_work_callback)
		self.connect(self.server_worker, SIGNAL("update_my(QString)"), self.server_my_work_callback)
		self.server_worker.start()

	def server_enemy_work_callback(self, question) :
		self.ui2.add_new_label(self.enemy_direction, question)

	def server_my_work_callback(self, answer) :
		self.ui2.add_new_label(self.my_direction, answer)

	def human_work(self) :
		question = self.ui2.textEdit.toPlainText()
		self.ui2.add_new_label(self.enemy_direction, question)
		self.human_worker = human_work_thread(self, question)
		self.connect(self.human_worker, SIGNAL("finished(QString)"), self.human_work_callback)
		self.human_worker.start()

	def human_work_callback(self, answer) :
		self.ui2.add_new_label(self.my_direction, answer)

	def gochat(self, mode) :
		# Machine To Machine
		if mode == 'MTM' :
			self.ChatWindow.show()
			self.MainWindow.hide()
			ServerIP = self.ui.lineEdit.text()
			self.log.info('ServerIP: ' + ServerIP)

			if self.ui.radioButton.isChecked() :		# client
				self.client_work(ServerIP)
			elif self.ui.radioButton_2.isChecked() and ServerIP != '' :		# server	
				self.server_work(ServerIP)
			else :
				print 'Invalid Arguements, Please fill the required fields'
		
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
		self.MainWindow.show()
		self.ChatWindow.close()

class human_work_thread(QThread):
    def __init__(self, faseeh, question):
        QThread.__init__(self)
        self.faseeh = faseeh
        self.question = str(question)

    def __del__(self):
        self.wait()

    def run(self):
		print 'in thread'
		if self.question :
			answer = self.faseeh.answer_the_question(self.question)
		else :
			print 'Write your question first'
		self.emit(SIGNAL('finished(QString)'), answer)

class client_work_thread(QThread):
    def __init__(self, faseeh, ServerIP):
        QThread.__init__(self)
        self.faseeh = faseeh
        self.ServerIP = ServerIP

    def __del__(self):
        self.wait()

    def run(self):
		try :
			print 'ServerIP', self.ServerIP, 'port', self.faseeh.SERVER_PORT
			self.faseeh.log.info('client started')
			self.comm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.comm_socket.settimeout(self.faseeh.TIME_OUT)
			self.comm_socket.connect((self.ServerIP, self.faseeh.SERVER_PORT))
			self.faseeh.log.info('client connected')
			for question in self.faseeh.questions :
				self.faseeh.log.info('question: ' + question)
				print 'question', question
				self.comm_socket.send( question + '#' )
				self.emit(SIGNAL('update_my(QString)'), question)
				answer = str( self.comm_socket.recv(self.faseeh.BUFFER_SIZE) )
				while not '#' in answer:
					answer = str( self.comm_socket.recv(self.faseeh.BUFFER_SIZE) )
				self.faseeh.log.info('answer: ' + answer)
				print 'answer', answer
				answer = answer[:-1]
				self.emit(SIGNAL('update_enemy(QString)'), answer)
				self.sleep(1)

			self.comm_socket.close()	
		except Exception, e:
			print (str(e))

class server_work_thread(QThread):
    def __init__(self, faseeh, ServerIP):
        QThread.__init__(self)
        self.faseeh = faseeh
        self.ServerIP = ServerIP

    def __del__(self):
        self.wait()

    def run(self):
		try :
			self.faseeh.log.info('server started')
			print 'ServerIP', self.ServerIP, 'port', self.faseeh.SERVER_PORT
			self.comm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.comm_socket.bind((self.ServerIP, self.faseeh.SERVER_PORT))
			self.comm_socket.listen(1)
			self.conn, addr = self.comm_socket.accept()
			self.conn.settimeout(self.faseeh.TIME_OUT)
			self.faseeh.log.info('server connected')
			for i in range (len(self.faseeh.questions)):
				question = str( self.conn.recv(self.faseeh.BUFFER_SIZE) )
				while not '#' in question:
					question = str( self.conn.recv(self.faseeh.BUFFER_SIZE) )

				question = question[:-1]
				self.emit(SIGNAL('update_enemy(QString)'), question)
				self.sleep(1)
				print 'question', question
				self.faseeh.log.info('question: ' + question)
				answer = self.faseeh.answer_the_question(question)
				self.faseeh.log.info('answer: ' + answer)
				print 'answer', answer
				self.conn.send( answer + '#' )
				self.emit(SIGNAL('update_my(QString)'), answer)
				self.sleep(1)

			self.conn.close()
		except Exception, e:
			print (str(e))

if __name__ == '__main__':
	
	app = QtGui.QApplication(sys.argv)	
	faseeh = Faseeh()
	sys.exit(app.exec_())
