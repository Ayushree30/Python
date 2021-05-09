from Crypto.Cipher import AES
import os,base64
from Crypto import Random
import random
import string
from Crypto.Util.Padding import pad,unpad

msg=input('Enter the message to be encrypted:')
msg_len=len(msg)
padded='{'
N=32
B=16
key=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)for i in range(N))
key_e=key.encode()
iv=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)for i in range(16))
iv_e=iv.encode()

cipher=AES.new(key_e,AES.MODE_CBC,iv_e)
msg_pvt=msg + (((16 - msg_len) % 16) * padded)
m=msg_pvt.encode()
#encrypt
encd=cipher.encrypt(m)

#Decrypt
cipher2=AES.new(key_e,AES.MODE_CBC,iv_e)
decd=cipher2.decrypt(encd)
n=decd.decode('utf-8').rstrip(padded)
print('The Decrypted message is:',n)