import pygame
import display
import ui

display = display.display
screen = display.screen
ui = ui.ui

pygame.init()
pygame.mixer.init()  ## For sound

all_sprites = pygame.sprite.Group()

def quit():
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            return False
    return True



while quit():

    
    display.clock.tick()

    all_sprites.update()

    screen.fill((255,255,255))

    ui.makeButon(display.WIDTH/2,display.HEIGHT/2,"""Exemple Text (this is an example text)""")

    all_sprites.draw(display)

    pygame.display.flip()     

    

pygame.quit()