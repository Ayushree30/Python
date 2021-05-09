from tkinter import simpledialog
from tkinter import messagebox
import tkinter as tk
#import tkmessagebox
root=tk.Tk()
#root.wm_title("Window")
user_input=simpledialog.askstring(title="Encryption Software",prompt="Enter the text to be encrypted")
print_msg=messagebox.showinfo(user_input)
root.mainloop()
#print("Hello",user_input)
#print(print_msg)