import sys
import keyboard
import pyperclip
import win32gui as win
import os
data=[]


def copy():
    d=pyperclip.paste()
    data.append(d)

def infront():
    for it in data:
        print(f'{data.index(it)+1} {it}')
    try:
##        q=win.FindWindow(None,os.path.join(os.getcwd(), __file__))
        q=win.FindWindow(None,sys.executable)
        print(q)
        
        
        
##        win.SetActiveWindow(q)
        win.ShowWindow(q,2)
        win.BringWindowToTop(q)
        
        win.SetForegroundWindow(q)
        
        
        select = int(input("Enter a number (0 to cancel): "))-1
        if select==-1:
            return
        pyperclip.copy(data[select])

    except Exception as e:
        print(e)


##print(__name__)
##print(__file__)
##print(sys.executable)

keyboard.register_hotkey('Ctrl+c',copy)
keyboard.register_hotkey('Ctrl+.',infront)
try:
    while True:
        continue
except Exception as e:
    print(e)
