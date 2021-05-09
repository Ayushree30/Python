from struct import *
import struct
import socket
import sys
import os
from uuid import getnode as get_mac
#from getmac import getmac
#from get_mac import get_mac_address
#dest_addr=get_mac_address(interface="eth0")
#print(dest_addr)
s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
#s=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(0X0800))
while True:
  packet=s.recvfrom(65565)
  packet=packet[0]
  ip_header=packet[0:20]
  iph = unpack('!BBHHHBBH4s4s' , ip_header)
  version_ihl = iph[0]
  version = version_ihl >> 4
  ihl = version_ihl & 0xF	
  iph_length = ihl * 4	
  ttl = iph[5]
  protocol = iph[6]
  s_addr = socket.inet_ntoa(iph[8])
  d_addr = socket.inet_ntoa(iph[9])
  print (' Version : ' + str(version) + ' IP Header length: ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
# data
  tcp
 	