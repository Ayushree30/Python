from urllib.request import urlopen, hashlib
import os
import getpass
#Common password list
guessed_password=False
LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
#Enter password and create the sha1 hash of it
enter_password=getpass.getpass('Enter the password:')
password_hash=hashlib.sha1(enter_password.encode()).hexdigest()
print(password_hash)
for i in LIST_OF_COMMON_PASSWORDS.split('\n'):
  i_hash=hashlib.sha1(i.encode()).hexdigest()
  if i_hash==password_hash:
    guessed_password=True
    final_guess=i

if guessed_password==True:
  print('The guessed is correct and the password is',final_guess)
else:
  print('The password is not guessed correctly')
