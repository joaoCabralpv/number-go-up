import pygame
import display

pygame.init()

class Counter:
    counter = 0
    font=None

    def __init__(self) :
        self.font=pygame.font.Font("Font.ttf",60)
    
    def IncreceCounter(self,number):
        self.counter+=number
    
    def DisplayCounter(self):
      text = self.font.render(str(self.counter),False,(0,0,0))
      display.display.screen.blit(text,(100,100))

counter = Counter()

if __name__=="__main__":
    print("Usa o main.py")