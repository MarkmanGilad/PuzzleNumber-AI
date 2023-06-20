import numpy as np

class State:
    def __init__(self, board):
        self.board = board # np.array
        self.rows, self.cols = board.shape

    def get_blank_pos (self):
        pos = np.where(self.board == 0)
        row = pos[0].item()
        col = pos[1].item()
        return row, col

    def __eq__(self, other):
        return np.equal(self.board, other.board).all()

    def copy (self):
        newBoard = np.copy(self.board)
        return State (newBoard)