import random
import sys
import argparse
import pygame as pg

import agent
from sim import run_sim
from board import Board


def draw_board(screen, board):
    for i, row in enumerate(board.grid):
        for j, el in enumerate(row):
            if el == Board.PLAYER:
                colour = Board.RED
            elif el == Board.AGENT:
                colour = Board.YELLOW
            else:
                colour = Board.BLACK
            pg.draw.circle(screen, colour, (int((j+0.5)
                                                * Board.SQUARESIZE), int((i+0.5)*Board.SQUARESIZE)), Board.RADIUS)
    pg.display.update()


def display_message(screen, msg):
    font = pg.font.Font(None, 100)
    print(msg)
    label = font.render(msg, True, Board.BLACK)
    screen.blit(label, (200, Board.HEIGHT))


def run_game():
    pg.init()
    # Extra space at the bottom to display win/loss message
    size = (Board.WIDTH, Board.HEIGHT + Board.SQUARESIZE)
    screen = pg.display.set_mode(size=size)
    pg.draw.rect(screen, Board.BLUE, (0, 0, size[0], size[1]))

    board = Board()
    draw_board(screen, board)

    turn = random.randint(Board.PLAYER, Board.AGENT)
    game_over = False

    while not game_over:
        if turn == Board.PLAYER:
            event = pg.event.poll()
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                x = event.pos[0]
                col = x // Board.SQUARESIZE

                if col in board.valid_moves():
                    board = board.drop_piece(col, Board.PLAYER)
                    if board.is_win(Board.PLAYER):
                        display_message(screen, "You Won!")
                        game_over = True
                    if board.is_tie():
                        display_message(screen, "Tied Game!")
                        game_over = True
                    draw_board(screen, board)
                    turn = Board.AGENT

        if turn == Board.AGENT and not game_over:
            col = agent.move(board)
            board = board.drop_piece(col, Board.AGENT)
            if board.is_win(Board.AGENT):
                display_message(screen, "You Lost!")
                game_over = True
            if board.is_tie():
                display_message(screen, "Tied Game!")
                game_over = True
            draw_board(screen, board)
            turn = Board.PLAYER


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sim', nargs='?', type=int, const=10)

    args = parser.parse_args()
    if args.sim:
        run_sim(args.sim)
    else:
        run_game()


if __name__ == '__main__':
    main()
