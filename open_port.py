import socket
import sys
import os
#hostname=socket.gethostname()
hostip=input('Enter the IPaddress:')
#ipaddress=socket.gethostbyname(hostname)
for port in range(0,65535):
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  sock_connect=s.connect_ex((hostip,port))
  if sock_connect==0:
    print('Port'+ str(port))
  port=port+1
  s.close()
    
	  
