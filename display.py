import pygame

class Display:
    screen = None
    WIDTH = 1280
    HEIGHT = 720
    SCALE_FACTOR_X = 1
    SCALE_FACTOR_Y = 1
    FPS = 30
    clock = None

    def __init__(self):
        self.SCALE_FACTOR_X = self.WIDTH/1280
        self.SCALE_FACTOR_Y = self.HEIGHT/720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Number go up")
        self.clock = pygame.time.Clock()
    def tick(self):
        self.clock.tick(self.FPS)

display = Display()

if __name__=="__main__":
    print("Usa o main.py")