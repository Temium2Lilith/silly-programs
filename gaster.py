# Importing the keyboard module which will acess the inputs from the keyboard
import keyboard

import os

def restart():
    #os.system("powershell echo hello")
    os.system("shutdown /r /t 0")

keyboard.add_word_listener('gaster', restart, ['enter'], True)
keyboard.wait()