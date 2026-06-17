"""
Tic-Tac-Toe CLI - Your favorite game at the distance of a command

This is a simple tic-tac-toe game to run inside the command-line.

Project elaborated by Rafael Ferreira
"""

# Constants

BOARD_SIZE = 3

# Board related functions

def board_init():
    board = [[" " for x in range(0,BOARD_SIZE)] for y in range(0, BOARD_SIZE)]
    return board

def board_to_str(board):
    boarders = f"+{"".join(['-' for x in range(0, BOARD_SIZE * 4 - 3)])}+"
    board_str = ""
    board_str += boarders + "\n"

    for i in range(0, BOARD_SIZE):
        if i != 0:
            board_str += "-" * (BOARD_SIZE * 4 - 1)
            board_str += "\n"
        for j in range(0, BOARD_SIZE):
            board_str += f"{board[i][j]:^3}"
            if j != (BOARD_SIZE-1):
                board_str += "|"
        if i != (BOARD_SIZE-1):
            board_str += "\n"
    board_str += "\n" + boarders
    return board_str

def convert_coordinates(house): # converts from 1-based to 0-based
    x  = house[0] - 1
    y = house[1] - 1
    return x, y

def change_value(board, house, value):
    x, y = convert_coordinates(house)
    board[x][y] = value
