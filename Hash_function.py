import hashlib
#to keep password hidden
import getpass
#to get random number for salting
import os
#md5 hash
hash=hashlib.md5(b'I LOVE CYBERSECURITY')
print(hash.hexdigest())

#SHA1 string hash
st=input('Enter the string to hash:')
hash_st=hashlib.sha1(st.encode())
print(hash_st.hexdigest())

#sha512 string hash
hash_string=input('Enter another string to be hashed:')
hashing=hashlib.sha512(hash_string.encode())
print(hashing.hexdigest())

#sha1 file hash
print('file')
file="/Users/missayushree/Desktop/Python_security/check.txt"
hash_file=hashlib.sha1()
print(len(file))
with open(file,'rb') as f:
    fb=f.read()
    if len(fb)>0:
        hash_file.update(file.encode('utf-8'))
print(hash_file.hexdigest())

#salting
#not to display password
password=getpass.getpass('Password:')
salt='5fg'
pass_salt=password+salt
hash_func=hashlib.sha1(pass_salt.encode())
print(hash_func.hexdigest())

#with password-based key derivation function 2
pass_salt_pbkdf2=hashlib.pbkdf2_hmac('sha1',password.encode(),os.urandom(16),100000)
print(pass_salt_pbkdf2.hex())