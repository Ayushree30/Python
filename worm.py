#Worm development
import sys
import os
import shutil
directory="/home/kali/Desktop/Antivirus/hello"
if os.path.isdir(directory):
  pass
else:
  os.mkdir(directory)
print('Directory Created')
shutil.copy('/home/kali/Desktop/Antivirus/worm','/home/kali/Desktop/Antivirus/hello/')
for i in range(10):
  shutil.copytree('/home/kali/Desktop/Antivirus/hello/','/home/kali/Desktop/Antivirus/hello{}'.format(i))
print('The folders are replicated')
#Worm end