import pygame
import display
import counter
screen = display.display.screen


class Buton:
    font = None
    butons = []
    WasAButonPressed = False
    counter = None

    def __init__(self):
        self.font=pygame.font.Font("Font.ttf",40)
        self.counter=counter.counter

    def makeButon(self,posx,posy,text):
        #checks the size of the text
        size = self.font.size(text)
        #saves the buton variables to the butons list
        self.butons.append(((posx-size[0],posy),size,text))
        
        
    
    def updateButons(self):
        for buton in self.butons:
            #saves the values of the buton to the variables
            posx=buton[0][0]
            posy=buton[0][1]
            size=buton[1]
            text=buton[2]
            
            self.ButonInteraction(buton,text)

            #renders the text
            text=self.font.render(text,False,(0,0,0))
            #draws the rectangle
            pygame.draw.rect(screen,(0,0,0),pygame.Rect(posx-10,posy-10,size[0]+20,size[1]+20),5)
            #draws the text
            screen.blit(text,(posx,posy))

            
    
    def CheckMouseIsOnTheButon(self,mousex,mousey,posx,posy,width,height):
        return mousex>=posx and mousex<=posx+width and mousey>=posy and mousey<=posy+height

    def ButonInteraction(self,buton,text):
        mouse= pygame.mouse.get_pos()
            #Checks if the mouse is on top of the buton
        if self.CheckMouseIsOnTheButon(mouse[0],mouse[1],buton[0][0],buton[0][1],buton[1][0],buton[1][1]):
            #Draws a gray rectangle on top of the buton that has the mouse on top
            pygame.draw.rect(screen,(150,150,150),pygame.Rect(buton[0][0]-10,buton[0][1]-10,buton[1][0]+20,buton[1][1]+20))
            #Checks if the mouse buton is pressed
            if pygame.mouse.get_pressed()[0]:
                if not not "self.WasAButonPressed":
                    self.WasAButonPressed = True
                    self.counter.IncreceCounter(1)
                    return
            else:   
                self.WasAButonPressed = False


            

pygame.init()
buton = Buton()

if __name__=="__main__":
    print("Usa o main.py")