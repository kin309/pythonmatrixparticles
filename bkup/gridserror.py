from config import screen, gray, pygame

class Grid:
    def __init__(self, lins, cols):
        self.x = 0
        self.y = 0
        self.lins = lins
        self.cols = cols
        self.cell_type = GridCell()
        self.cells = []
        self.counter = 0

        for ele in range(self.lins):
            self.cells.append([GridCell()]*self.cols)

        for i in range(self.lins):
            for j in range(self.cols):
                self.cells[i][j].x = self.x + i*10
                self.cells[i][j].y =  self.y + j*10


    def draw(self):
        for i in range(self.lins):
            for j in range(self.cols):
                # print(f"lin{i} col{j}")
                # print(f"{self.cells[i][j].x}")
                # print(f"{self.cells[i][j].y}")
                self.cells[i][j].draw()


class GridCell:
    def __init__(self, x = 0, y = 0,  width = 8, height = 8, color = gray):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)

    def draw(self):
        self.rect = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)