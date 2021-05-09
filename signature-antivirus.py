#Signature-based Antivirus detection
import os
import sys, glob
import re
python_files=glob.glob('*.py')
print(python_files)
for i in python_files:
  read_files=open(i,'r')
  lines=read_files.readlines()
  virus_present=False
  for line in lines:
    if re.match("#Self-replicating virus",line) or re.match("#Worm development",line):
      virus_present=True
      print("The virus is present in the file {}".format(i))
