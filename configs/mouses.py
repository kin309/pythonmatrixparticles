import pygame

class Mouse:
    def __init__(self):
        self.click_counters = 0
        self.x = int()
        self.y = int()
        self.click = False

    def set_mouse(self):
        self.x, self.y = pygame.mouse.get_pos()

    def clicker(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            return True
        if event.type == pygame.MOUSEBUTTONUP:
            self.click = False
            return False

mouse = Mouse()