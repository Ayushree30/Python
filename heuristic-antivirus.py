#Heuristic-based Antivirus detection
import os
import sys, glob, ntpath
import re
python_files=glob.glob('*.py')
l=[]
n=[]
#Create file.txt for comparison
if os.path.exists('file_size.txt'):
  pass
else:
  with open('file_size.txt','w') as f:
    for i in python_files:
      a=os.path.getsize(i)
      print(i,'\n',a,file=f)
#Read the lines in the file.txt for comparison and create a list
h = []
with open('file_size.txt', "r") as f1:
    for line in f1:
        h.append(line.strip('\n').strip(' ').strip(''))
#print(h)

#Find the current file size and create a list
for py in python_files:
  b=os.path.getsize(py)
  n.extend([py,b])
#print(n)

#Change the type of of odd element in 'h' list
#to make it compatible with 'n' lsit type
for i in range(len(n)):
  if i%2!=0:
    h[i]=int(h[i])

#Compare the two list
for i in range(len(n)):
  if n[i]!=h[i]:
    print('Virus is found!!!!!!!!!')
    print('The infected file is {} whose size is changed from {} to {}'.format(n[i-1],h[i],n[i]))