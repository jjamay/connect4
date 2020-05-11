import random
import numpy as np

import agent
from board import Board


def run_sim():
    # in the sim, agent is the player and rand_agent is the agent
    wins = {
        Board.PLAYER: 0,
        Board.AGENT: 0
    }

    move_fns = {
        Board.PLAYER: agent.move,
        Board.AGENT: random_move
    }

    print("Running Simulation...")
    # simulate 100 games
    for _ in range(100):
        board = Board()
        turn = random.randint(Board.PLAYER, Board.AGENT)
        while True:
            col = move_fns[turn](board)
            board = board.drop_piece(col, turn)
            if board.is_win(turn):
                wins[turn] += 1
                break
            if board.is_tie():
                break
            turn = turn % 2 + 1

    print("Agent Wins: {}/100".format(wins[Board.PLAYER]))
    print("Random Agent Wins: {}/100".format(wins[Board.AGENT]))
    print("Ties: {}/100".format(100 - sum(wins.values())))


def random_move(board):
    return random.choice(board.valid_moves())
