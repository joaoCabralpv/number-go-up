from typing import Any
import pygame
import display
screen = display.display.screen



class Ui:
    font = None
    butons = []

    def __init__(self):
        self.font=pygame.font.Font("Buton.ttf",40)

    def makeButon(self,posx,posy,text):
        #checks the size of the text
        size = self.font.size(text)
        #renders the text
        text=self.font.render(text,False,(0,0,0))
        #translates the x and y positions
        #posx=(posx-size[0])/2
        posy=(posy-size[1])
        print(posy)
        #draws the rectangle that marks the buton
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(posx-10,posy-0,size[0]+20,size[1]+20),5)
        #draws the text
        screen.blit(text,(posx,posy))

    def update(self):
        for buton in self.butons:
            screen.blit(buton[0],buton[1])
pygame.init()
ui = Ui()

if __name__=="__main__":
    print("Usa o main.py")