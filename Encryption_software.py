from tkinter import *
from tkinter import messagebox
import tkinter
import tkinter as tk
from Crypto.Cipher import AES
import os,base64
import rsa

window=tk.Tk()
msg=tk.Label(text="Encryption Software",width=20,height=2)
label=tk.Label(text="Enter Plaintext")
entry=tk.Entry(width=40)

def encryption():
  #public and private Key generation
  RSA_key_length=512
  public_key, private_key=rsa.newkeys(RSA_key_length)

  #RSA encryption
  name=entry.get()
  ciphertext=rsa.encrypt(name.encode(),public_key)
  tkinter.messagebox.showinfo(title='Ciphertext',message=ciphertext)

def decryption():
  #RSA decryption
  RSA_key_length=512
  public_key, private_key=rsa.newkeys(RSA_key_length)
  name=entry.get()
  message_length=len(name)
  ciphertext=rsa.encrypt(name.encode(),public_key)
  decrypted_message=rsa.decrypt(ciphertext,private_key)
  decrypt=decrypted_message[0:message_length].decode("utf-8")
  tkinter.messagebox.showinfo(title='Plaintext',message=decrypt)

button_1=tk.Button(text="Encrypt",command=encryption)
button_2=tk.Button(text="Decrypt",command=decryption)

#text_box=tk.Text()
msg.pack()
label.pack()
entry.pack()
button_1.pack()
button_2.pack()

#text_box.pack()

window.mainloop()

