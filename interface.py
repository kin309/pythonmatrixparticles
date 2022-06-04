import sys
import pygame.event
from config import *
from grid import *

grids1 = Grid()




def color_test(x, y, color):
    pygame.draw.ellipse(screen, color,(x, y, 30, 30))


def interface():
    # grids1.paint_cell(random.randint(0, 29), random.randint(0, 40))
    while True:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for i in range(grids1.lins):
                for j in range(grids1.cols):
                    if grids1.cells[i][j].color != lightgray:
                        grids1.cells[i][j].b_clicker(event, gray)
                    else:
                        grids1.cells[i][j].b_clicker(event, nao5)


            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                    # grids1.paint_cell(random.randint(0, 29), random.randint(0, 40))

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    grids1.param = [(153, 255, 255), (0, 102, 204), (153, 255, 255), (0, 204, 204), (0, 102, 204), (0, 102, 204), (0, 204, 204), (0, 153, 153), (0, 153, 153)]

                if event.key == pygame.K_w:
                    grids1.param = [(0, 153, 153), (153, 255, 255), (0, 204, 204), (240, 240, 0), (0, 102, 204), (0, 102, 204), (240, 240, 0), (0, 153, 153), (153, 255, 255)]

                if event.key == pygame.K_e:
                    grids1.param = [(0, 153, 153), (0, 153, 153), (240, 240, 0), (0, 102, 204), (153, 255, 255), (153, 255, 255), (0, 153, 153), (0, 204, 204), (0, 153, 153)]


                if event.key == pygame.K_RETURN:
                    grids1.params1()

                if event.key == pygame.K_SPACE:
                    grids1.clear_screen()
                    grids1.paint_cell(random.randint(0, 29), random.randint(0, 40))
                    grids1.params1()

                if event.key == pygame.K_BACKSPACE:
                    grids1.clear_screen()


        # grids1.mecachins()

        for i in range(grids1.lins):
            for j in range(grids1.cols):
                if grids1.cells[i][j].color == nao6:
                    grids1.around_check(i, j)

        grids1.draw()
        grids1.mecachins1()
        mouse.set_mouse()
        pygame.display.update()
        timer.clock.tick(20)

interface()