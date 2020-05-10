import random
import numpy as np


class Agent:
    def move(self, board):
        valid_moves = board.valid_moves()
        scores = dict(zip(valid_moves, [self.score_move(
            board, col) for col in valid_moves]))
        # Get a list of columns (moves) that maximize the heuristic
        max_cols = [key for key in scores.keys() if scores[key] ==
                    max(scores.values())]
        # Select at random from the maximizing columns
        return random.choice(max_cols)

    def score_move(self, board, col):
        next_board = board.drop_piece(col, board.AGENT)
        return self.minimax(next_board, 3, False, board.AGENT)

    def minimax(self, board, depth, maximizing_agent, piece):
        if depth == 0 or board.is_terminal():
            # reward/penalize quicker wins/losses more heavily
            return (depth + 1) * board.get_heuristic(piece)

        valid_moves = board.valid_moves()
        if maximizing_agent:
            value = -np.Inf
            for col in valid_moves:
                next_board = board.drop_piece(col, piece)
                value = max(value, self.minimax(
                    next_board, depth-1, False, piece))
        else:
            value = np.Inf
            for col in valid_moves:
                next_board = board.drop_piece(col, piece % 2+1)
                value = min(value, self.minimax(
                    next_board, depth-1, True, piece))
        return value
