import keyboard
import os
import pygame
import time

def restart():
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("🕈︎☟︎✡︎ ❄︎☞︎ 👎︎✋︎👎︎ 🕆︎ ❄︎☼︎✌︎☠︎💧︎☹︎✌︎❄︎☜︎ ❄︎☟︎✋︎💧︎ 🖳︎🕿︎🕿︎🕿︎🕿︎")

    image = pygame.image.load("gayster.jpg")
    screen.blit(image, (0, 0))

    pygame.display.flip()
    time.sleep(7) # added a second more to have some silence after the recoding. It's funny lol

    if os.name == 'nt':
        os.system("shutdown /r /t 0")
    else:
        os.system("shutdown now")

keyboard.add_word_listener('gaster', restart, ['enter'], True)
keyboard.wait()
