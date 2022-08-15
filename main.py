import numpy as np
import os
from time import sleep


board = list()
SEED_ALIVE_PROBABILITY = 0.08
BOARD_X = 100
BOARD_Y = 30
EPOCHS = 1000

def print_board():
    print("|", end="")
    for _ in board:
        print("-", end="")
    print("|")
    for row in board:
        print("|", end="")
        for column in row:
            if column:
                print("█", end="")
            else:
                print(" ", end="")
        print("|")
    for _ in board:
        print("-", end="")


def get_neighbors_count(i: int, j: int) -> int:
    neighbors_count = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            try:
                if board[x][y]:
                    neighbors_count += 1
            except ValueError:
                continue
            except IndexError:
                continue
    return neighbors_count


def advance():
    for i in range(len(board)):
        for j in range(len(board[i])):
            try:
                neighbors_count = get_neighbors_count(i, j)
                if board[i][j]:
                    if neighbors_count < 2 or neighbors_count > 3:
                        board[i][j] = 0
                else:
                    if neighbors_count == 3:
                        board[i][j] = 1
            except ValueError:
                continue
    os.system("cls")
    print_board()


def main():
    for _ in range(BOARD_Y):
        board.append(
            np.random.choice(
                [0, 1],
                size=BOARD_X,
                p=[1 - SEED_ALIVE_PROBABILITY, SEED_ALIVE_PROBABILITY],
            )
        )
    for _ in range(EPOCHS):
        advance()
        sleep(0.2)


if __name__ == "__main__":
    main()
