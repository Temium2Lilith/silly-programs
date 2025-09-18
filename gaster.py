import keyboard
from os import name, system
import pygame

def restart():
    pygame.init()
    pygame.mixer.init()

    clock = pygame.time.Clock()
    window = pygame.Window(title="she wing it till I ding it",
                           size=(500, 500),
                           always_on_top=True
                    )
    screen = window.get_surface()
    
    window.show()
    window.focus()
    window.set_fullscreen(desktop=True)

    pygame.mixer.music.load("Resources/winging-my-dingaling.wav")
    image = pygame.image.load("Resources/gayster.jpg")
    pygame.mixer.music.set_volume(1)

    running = True
    time_passed = 0.0

    pygame.mixer.music.play()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ms = clock.get_time()
        time_passed += ms / 1000

        if time_passed >= 7:
            running = False

        screen.blit(image, (0, 0))
        window.flip()
        clock.tick(60)

    if name == 'nt':
        system("echo gay")
    else:
        system("shutdown now")

keyboard.add_word_listener('gaster', restart, ['enter'], True)
keyboard.wait()
