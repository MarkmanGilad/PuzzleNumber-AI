import pygame
import numpy as np
from constants import *
from State import State

class Graphics:
    def __init__(self):
        # self.board = state.board
        # self.rows, self.cols = self.board.shape
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Puzzle')
        
    def draw_all_pieces(self, state:State):
        board = state.board
        rows, cols = board.shape
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] !=0 :
                    self.draw_piece(state, (row, col))
            
    def draw_piece(self, state:State, row_col ):
        row, col = row_col
        board = state.board
        number = board[row][col]
        pos = self.calc_base_pos(row_col)
        color = self.calc_color(number)
        pygame.draw.rect(self.win, color, (*pos, SQUARE_SIZE-PADDING, SQUARE_SIZE-PADDING))
        if number != 0:
            font = pygame.font.SysFont('ariel', SQUARE_SIZE)
            text = font.render(str(number), 1, BLACK)
            textPos = self.calc_num_pos(row_col, font, number)
            self.win.blit(text, textPos)

    def calc_pos(self, row_col):
        row, col = row_col
        y = row * SQUARE_SIZE + SQUARE_SIZE//2 + FRAME
        x = col * SQUARE_SIZE + SQUARE_SIZE//2 + FRAME
        return x, y

    def calc_base_pos(self, row_col):
        row, col = row_col
        y = row * SQUARE_SIZE + FRAME
        x = col * SQUARE_SIZE + FRAME
        return x, y

    def calc_num_pos(self, row_col, font, number):
        row, col = row_col
        font_width, font_height = font.size(str(number))
        y = row * SQUARE_SIZE + FRAME + (SQUARE_SIZE - font_height)//2
        x = col * SQUARE_SIZE + FRAME + (SQUARE_SIZE - font_width)//2
        return x, y

    def calc_row_col(self, pos):
        x, y = pos
        col = x // SQUARE_SIZE
        row = y // SQUARE_SIZE
        return row, col

    def calc_color(self, number):
        if number == 0:
            return LIGHTGRAY
        elif number % 2 == 0:
            return BLUE
        else:
            return WHITE

    def draw(self, state):
        self.win.fill(LIGHTGRAY)
        self.draw_all_pieces(state)

    def draw_square(self, row_col, color):
        pos = self.calc_base_pos(row_col)
        pygame.draw.rect(self.win, color, (*pos, SQUARE_SIZE, SQUARE_SIZE))

    def blink(self, row_col, color):
        row, col = row_col
        player = self.board[row][col]
        for i in range (3):
            self.draw_square((row, col), color)
            pygame.display.update()
            time.sleep(0.2)
            self.draw_piece((row, col))
            pygame.display.update()
            time.sleep(0.2)

