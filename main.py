import random
import sys
import pygame as pg
from board import Board
from agent import Agent


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


def display_message(screen, player_win):
    font = pg.font.Font(None, 100)
    message = "You Won!" if player_win else "You Lost!"
    print(message)
    label = font.render(message, True, Board.RED)
    screen.blit(label, (200, Board.HEIGHT))


def main():
    pg.init()
    # Extra space at the bottom to display win/loss message
    size = (Board.WIDTH, Board.HEIGHT + Board.SQUARESIZE)
    screen = pg.display.set_mode(size=size)
    pg.draw.rect(screen, Board.BLUE, (0, 0, size[0], size[1]))

    board = Board()
    draw_board(screen, board)

    turn = random.randint(Board.PLAYER, Board.AGENT)
    game_over = False
    agent = Agent()

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
                        display_message(screen, True)
                        game_over = True
                    draw_board(screen, board)
                    turn = turn % 2 + 1

        if turn == Board.AGENT and not game_over:
            col = agent.move(board)
            board = board.drop_piece(col, Board.AGENT)
            if board.is_win(Board.AGENT):
                display_message(screen, False)
                game_over = True
            draw_board(screen, board)
            turn = turn % 2 + 1

    pg.time.wait(5000)


if __name__ == '__main__':
    main()
