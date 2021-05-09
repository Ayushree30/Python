import hashlib
#create the password hash
password=input('Enter the password : ')
password_h=hashlib.sha1(password.encode())
password_hash=password_h.hexdigest()
print('The password hash is {}'.format(password_hash))

#crack the password hash
pass_found=False
pass_hash_input= password_hash
all_password=['qwerty','password','Pdchotiayu30$$','Ayushjiansh']
for i in all_password:
  i_hash=hashlib.sha1(i.encode())
  password_hash_i=i_hash.hexdigest()
  if password_hash_i == password_hash:
    pass_found=True
    final_pass=i
    
if pass_found==False:
  print('Hash is not found')
else:
  print('The hash is present and the password is {}'.format(final_pass))
  
