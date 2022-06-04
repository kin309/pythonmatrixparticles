from simpleasbreath.configs.screens import screen
from simpleasbreath.configs.colors import white
import pygame


pygame.init()
class Font:
    def __init__(self, size):
        self.size = size
        self.config = pygame.font.SysFont("verdana", self.size)


font1 = Font(15)
font2 = Font(20)
font3 = Font(30)
font4 = Font(40)
font5 = Font(50)
font6 = Font(60)

def text_creator(text, x, y, color = white, fonts = font1):
    fontes = fonts.config.render(text, True, color)
    screen.blit(fontes, (x, y))

