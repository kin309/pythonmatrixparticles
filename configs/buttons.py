import pygame
from simpleasbreath.configs.colors import white, red
from simpleasbreath.configs.screens import screen
from simpleasbreath.configs.mouses import mouse

class Button:
    def __init__(self, text, x, y, font, color = white):
        self.color = color
        self.text = text
        self.text_len = len(self.text)
        self.font = font
        self.width = self.font.size*self.text_len/1.5
        self.height = self.font.size*1.5
        self.x = x - self.width/2
        self.y = y - self.height/2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        pygame.draw.rect(screen, red, self.rect)
        text = self.font.config.render(self.text, False, (255,255,255))
        screen.blit(text, ((0.1+0.15*self.text_len)*(0.3*self.font.size)+self.x, self.y))

    def b_clicker(self, event):
        if self.rect.collidepoint((mouse.x, mouse.y)) and mouse.clicker(event):
            return True
        else:
            return False