import random
import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed

import agent
from board import Board


def sim_game():
    move_fns = {
        Board.PLAYER: agent.move,
        Board.AGENT: random_move
    }

    board = Board()
    turn = random.randint(Board.PLAYER, Board.AGENT)
    while True:
        col = move_fns[turn](board)
        board = board.drop_piece(col, turn)
        if board.is_win(turn):
            return turn
        if board.is_tie():
            return "tie"
        turn = turn % 2 + 1


def run_sim(n_games):
    # in the sim, agent is the player and the random agent is the agent
    wins = {
        Board.PLAYER: 0,
        Board.AGENT: 0,
        "tie": 0
    }

    print(f"Running {n_games} simulated games against random agent...")
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(sim_game) for _ in range(n_games)]
        for future in as_completed(futures):
            wins[future.result()] += 1

    print("Simulation Complete! Results:")
    print(f"Agent Wins: {wins[Board.PLAYER]}/{n_games}")
    print(f"Random Agent Wins: {wins[Board.AGENT]}/{n_games}")
    print(f"Ties: {wins['tie']}/{n_games}")


def random_move(board):
    return random.choice(board.valid_moves())
