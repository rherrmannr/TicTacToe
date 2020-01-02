import pygame
from ticTacToe import TicTacToe
from ticTacToeUi import TicTacToeUI

pygame.init()
window = pygame.display.set_mode((300, 350))


def loop():
    tictactoe = TicTacToe("X")
    ui = TicTacToeUI(pygame, tictactoe, window)
    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                return False
            if event.type is pygame.MOUSEBUTTONDOWN:
                if event.button is 1:
                    column = event.pos[0] // 100
                    row = event.pos[1] // 100
                    tictactoe.set_obj(row, column)
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_r:
                    tictactoe.restart()
        ui.update()


loop()
pygame.quit()
