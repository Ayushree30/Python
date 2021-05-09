from Crypto.Cipher import AES
import os,base64
from Crypto import Random
import random
import string
from base64 import b64encode,b64decode

msg=input('Enter the message to be encrypted:')
msg_e=msg.encode()
msg_len=len(msg)
N=32
key=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)for i in range(N))
key_e=key.encode()

iv=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)for i in range(16))
iv_e=iv.encode()

#def pad(s):
#    return s + ((16 - len(s) % 16) * '{')
#encrypt
cipher=AES.new(key_e,AES.MODE_EAX,iv_e)
encd=cipher.encrypt(msg.encode('utf-8'))

#Decrypt
cipher=AES.new(key_e,AES.MODE_EAX,iv_e)
decd=cipher.decrypt(encd[0:msg_len]).decode('utf-8')
print('The Decrypted message is:', decd)