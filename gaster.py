# Importing the keyboard module which will acess the inputs from the keyboard
import keyboard
import os
import pygame

def restart():
    if os.name == 'nt':
        os.system("shutdown /r /t 0")
    else:
        os.system("shutdown now")

keyboard.add_word_listener('gaster', restart, ['enter'], True)
keyboard.wait()
