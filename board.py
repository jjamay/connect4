import numpy as np
import pygame as pg


class Board:
    PLAYER = 1
    AGENT = 2

    ROWS = 6
    COLUMNS = 7

    WIN = 4

    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    SQUARESIZE = 100
    RADIUS = SQUARESIZE // 2 - 5

    def __init__(self, grid=None):
        if grid is None:
            self.grid = np.zeros((self.ROWS, self.COLUMNS))
        else:
            self.grid = grid

    def valid_moves(self):
        return [c for c in range(self.COLUMNS) if self.grid[0][c] == 0]

    def drop_piece(self, col, piece
                   ):
        next_grid = self.grid.copy()
        for row in range(self.ROWS-1, -1, -1):
            if next_grid[row][col] == 0:
                next_grid[row][col] = piece
                return Board(next_grid)

    def get_heuristic(self, piece):
        score = 0
        for window in self.get_windows():
            score += self.check_window(window, piece, 4) * 1000
            score += self.check_window(window, piece, 3) * 5
            score += self.check_window(window, piece, 2) * 1
            score += self.check_window(window, piece % 2+1, 2) * -1
            score += self.check_window(window, piece % 2+1, 3) * -5
        return score

    @classmethod
    def check_window(cls, window, piece, count):
        return (window.count(piece) == count and window.count(0) == cls.WIN-count)

    def get_windows(self):
        # horizontal
        for row in range(self.ROWS):
            for col in range(self.COLUMNS - (self.WIN-1)):
                yield list(self.grid[row, col:col+self.WIN])
        # vertical
        for row in range(self.ROWS - (self.WIN-1)):
            for col in range(self.COLUMNS):
                yield list(self.grid[row:row+self.ROWS, col])
        # down-right diagonal
        for row in range(self.ROWS - (self.WIN-1)):
            for col in range(self.COLUMNS - (self.WIN-1)):
                yield list(self.grid[range(row, row+self.WIN), range(col, col+self.WIN)])
        # up-right diagonal
        for row in range(self.WIN-1, self.ROWS):
            for col in range(self.COLUMNS - (self.WIN-1)):
                yield list(self.grid[range(row, row-self.WIN, -1), range(col, col+self.WIN)])

    @property
    def is_terminal(self):
        if list(self.grid[0, :]).count(0) == 0:
            return True

        if self.is_win(self.PLAYER) or self.is_win(self.AGENT):
            return True

        return False

    def is_win(self, piece):
        for window in self.get_windows():
            if self.check_window(window, piece, 4):
                return True
        return False
