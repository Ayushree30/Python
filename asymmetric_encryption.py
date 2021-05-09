import os,base64
import rsa

message=input('Enter the message to be encrypted:')
message_length=len(message)

#public and private Key generation
RSA_key_length=512
public_key, private_key=rsa.newkeys(RSA_key_length)
#print(private_key)
#print(public_key)

#RSA encryption
ciphertext=rsa.encrypt(message.encode(),public_key)

#RSA decryption
decrypted_message=rsa.decrypt(ciphertext,private_key)
decrypt=decrypted_message[0:message_length].decode("utf-8")
print('The decrypted message is:',decrypt)