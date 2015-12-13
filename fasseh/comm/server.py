import socket
import sys


def createMsg(msg):
	return msg + '#'

SERVER_IP = 'localhost'
SERVER_PORT = 5678
BUFFER_SIZE = 1024
TIME_OUT = 10		# 10 seconds
ans = "answer"

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((SERVER_IP, SERVER_PORT))
print ('server started')

while True:
	try:
		socket.listen(1)
		conn, addr = socket.accept()
		
		conn.settimeout(TIME_OUT)
		question1 = ''
		
		for i in range (10):
			print("connection accepted3")
			question1 = str( conn.recv(BUFFER_SIZE) )
			print("connection accepted4")
			while not '#' in question1:
				question1 = str( conn.recv(BUFFER_SIZE) )
			print(question1)
			conn.send(createMsg(ans))

		break

	except Exception as e:
		print ( str(e) )
		break

socket.close()