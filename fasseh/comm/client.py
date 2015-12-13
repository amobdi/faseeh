import socket
import sys


def createMsg(msg):
	return msg + '#'

SERVER_IP = 'localhost'
SERVER_PORT = 5678
BUFFER_SIZE = 1024
TIME_OUT = 10		# 10 seconds

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('client started')

try:
	socket.settimeout(TIME_OUT)
	socket.connect((SERVER_IP, SERVER_PORT))
	
	for i in range (10):
		msg = input("Enter a question")
		socket.send(createMsg(msg))
		answer1 = str( socket.recv(BUFFER_SIZE) )
		while not '#' in answer1:
			answer1 = str( socket.recv(BUFFER_SIZE) )
		print(answer1)
	
	socket.close()	
except Exception as e:
	print (str(e))
	socket.close()
