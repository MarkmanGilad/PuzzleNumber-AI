import numpy as np
from constants import *

class State:
    def __init__(self, board = None):
        if board is None:
            self.board = self.make_goal_state()
            self.blank_pos = 0, 0
            
        else:
            self.board = board # np.array
            self.blank_pos = self.find_blank_pos()
        
        self.rows, self.cols = board.shape

    def get_blank_pos (self):
        return self.blank_pos
    
    def find_blank_pos (self):
        pos = np.where(self.board == 0)
        row = pos[0].item()
        col = pos[1].item()
        return row, col

    def make_goal_state (self, rows=ROWS, cols=COLS):
        board = np.arange(rows*cols)
        board = board.reshape((rows, cols))
        return State(board)

    def __eq__(self, other):
        return np.equal(self.board, other.board).all()

    def copy (self):
        newBoard = np.copy(self.board)
        return State (newBoard)