import pygame

from config import *
import random

class Grid:
    def __init__(self, lins = 30, cols = 41):
        self.x = 60
        self.y = 20
        self.cols = cols
        self.lins = lins
        self.cell_type = GridCell()
        self.cell_size = 20
        self.cells = []
        self.counter = 0
        self.param = []

        self.params1()

        for ele in range(self.lins):
            self.cells.append([GridCell()]*self.cols)

        for i in range(self.lins):
            for j in range(self.cols):
                slot = GridCell(self.x + j * (self.cell_size+2), self.y + i * (self.cell_size+2), width=self.cell_size ,height=self.cell_size)
                self.cells[i][j] = slot
                slot.mPos = (i, j)


    def draw(self):
        for i in range(self.lins):
            for j in range(self.cols):
                self.cells[i][j].draw()

    def paint_cell(self, i, j, color = random.choice([nao1, nao2, nao3, nao4])):
            self.cells[i][j].color = color

    def params1(self):
        p1 = random.choice([nao2, nao3, nao4, nao6])
        p2 = random.choice([nao1, nao3, nao4, nao7])
        p3 = random.choice([nao1, nao3, nao4, nao7, nao6])
        p4 = random.choice([nao1, nao2, nao4, nao7])
        p5 = random.choice([nao1, nao2, nao4, nao7, nao6])
        p6 = random.choice([nao1, nao2, nao3, nao7])
        p7 = random.choice([nao1, nao2, nao3, nao7, nao6])
        p8 = random.choice([nao2, nao3, nao4, lightgray, nao6])
        p9 = random.choice([nao1, nao2, nao3, nao4, nao7, lightgray, nao5])
        p10 = random.choice([nao1, nao2, nao3, nao4, nao7, lightgray, nao5])
        p11 = random.choice([nao1, nao2, nao3, nao4, nao7, lightgray, nao5])
        p12 = random.choice([nao1, nao2, nao3, nao4, nao7, lightgray, nao5])
        p13 = random.choice([nao1, nao2, nao3, nao4, nao7, lightgray, nao5])
        p14 = random.choice([nao1, nao2, nao3, nao4, nao7, lightgray, nao5])
        p15 = random.choice([nao1, nao2, nao3, nao4, nao7, lightgray, nao5])
        p16 = random.choice([nao1, nao2, nao3, nao4, nao7, lightgray, nao5])
        self.param = [p1,p2,p3,p4,p5,p5,p6,p7, p8,p9,p10,p11,p12,p13,p14,p15,p16]
        print(self.param)

    def clear_screen(self):
        for i in range(self.lins):
            for j in range(self.cols):
                self.cells[i][j].color = lightgray



    def mecachins1(self):

        for i in range(self.lins):
            for j in range(self.cols):

                try:
                    if self.cells[i][j].color == nao5 and self.cells[i][j - 2].color != nao7 and self.cells[i][j-2] != nao6:
                        self.cells[i][j - 2].color = random.choice([nao1, nao2, nao3, nao4])

                    if self.cells[i][j].color == nao1:
                        self.cells[i][j - 1].color = self.param[0]

                    if self.cells[i][j].color == nao7:
                        self.cells[i][j + 1].color = self.param[7]

                    if self.cells[i][j].color == nao2:
                        self.cells[i+1][j].color = self.param[1]
                        self.cells[i-1][j].color = self.param[2]

                    if self.cells[i][j].color == nao3:
                        self.cells[i][j+1].color = self.param[3]
                        self.cells[i][j-1].color = self.param[4]

                    if self.cells[i][j].color == nao4:
                        if j > 0:
                            self.cells[i-1][j+1].color = self.param[6]
                        self.cells[i+1][j-1].color = self.param[5]


                except IndexError:
                    pass

    def around_check(self,posl, poscol):
        try:
            # abaixo
            self.cells[posl+1][poscol].color = self.param[8]

            # acima
            self.cells[posl-1][poscol].color = self.param[16]
            # esquerda
            self.cells[posl][poscol-1].color = self.param[10]

            # direita
            self.cells[posl][poscol+1].color = self.param[11]

            # esquerda baixo
            self.cells[posl+1][poscol-1].color = self.param[12]

            # esquerda cima
            self.cells[posl-1][poscol-1].color = self.param[13]

            # direita baixo
            self.cells[posl+1][poscol+1].color = self.param[14]

            # direita cima
            self.cells[posl-1][poscol+1].color = self.param[15]
        except IndexError:
            pass


class GridCell:
    def __init__(self, x = 0, y = 0,  width = 8, height = 8, color = lightgray):
        self.color = color
        self.width = width
        self.height = height
        self.mPos = (0,0)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)

    def draw(self):
        self.rect = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)

    def b_clicker(self, event, color):
        if self.rect.collidepoint((mouse.x,mouse.y)) and mouse.clicker(event):
            self.color = color