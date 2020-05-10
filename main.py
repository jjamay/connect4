import random
import sys
import pygame as pg
from board import Board
from agent import Agent


def draw_board(screen, board):
    for i, row in enumerate(board.grid):
        for j, el in enumerate(row):
            pg.draw.rect(screen, Board.BLUE, (j*Board.SQUARESIZE,
                                              i*Board.SQUARESIZE, Board.SQUARESIZE, Board.SQUARESIZE))

            if el == Board.PLAYER:
                colour = Board.RED
            elif el == Board.AGENT:
                colour = Board.YELLOW
            else:
                colour = Board.BLACK
            pg.draw.circle(screen, colour, (int((j+0.5)
                                                * Board.SQUARESIZE), int((i+0.5)*Board.SQUARESIZE)), Board.RADIUS)
    pg.display.update()


def main():
    width = Board.COLUMNS * Board.SQUARESIZE
    height = Board.ROWS * Board.SQUARESIZE
    size = (width, height)
    pg.init()
    screen = pg.display.set_mode(size=size)
    pg.draw.rect(screen, Board.BLUE, (0, 0, size[0], size[1]))

    myfont = pg.font.SysFont("monospace", 75)

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
                        print("Player wins!")
                        # label = myfont.render("Player wins!!", 1, Board.RED)
                        # screen.blit(label, (40, 10))
                        game_over = True
                    draw_board(screen, board)
                    turn = turn % 2 + 1

        if turn == Board.AGENT and not game_over:
            col = agent.move(board)
            board = board.drop_piece(col, Board.AGENT)
            if board.is_win(Board.AGENT):
                print("Agent wins!")
                # label = myfont.render("Player wins!!", 1, Board.RED)
                # screen.blit(label, (40, 10))
                game_over = True
            draw_board(screen, board)
            turn = turn % 2 + 1

    pg.time.wait(3000)


if __name__ == '__main__':
    main()
