import pygame
import display
import buton
import counter

display = display.display
screen = display.screen
Buton = buton.buton
Counter = counter.counter

pygame.init()
pygame.mixer.init()  ## For sound

all_sprites = pygame.sprite.Group()

def quit():
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            return False
    return True

Buton.makeButon(display.WIDTH-60,display.HEIGHT/2,"Increce number")


while quit():
  
    display.tick()

    all_sprites.update()

    screen.fill((255,255,255))

    Buton.updateButons()

    Counter.DisplayCounter()

    all_sprites.draw(display)

    pygame.display.flip()     

pygame.quit()