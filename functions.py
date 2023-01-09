from random import randint
from variables import *


def enemy_shoot(board):
    """
    enemy_shoot(board)
    Accepts the player's game board.
    Set one symbol if a hit or other symbol if a miss
    on player's game board
    """
    while True:
        x = randint(1, board_size)
        y = randint(1, board_size)
        if shoot_sign in board[x][y]:
            continue
        elif hit_sign in board[x][y]:
            continue
        elif ship_sign in board[x][y]:
            board[x][y] = hit_sign
            break
        elif empty_cell_sign in board[x][y]:
            board[x][y] = shoot_sign
            break


def player_shoot(board):
    """
    player_shoot(board)
    Accepts the enemy's board.
    Returns one symbol if a hit or other symbol if a miss
    Converts the 1st value from a letter to a digit.
    Converts the values from str to int.
    """
    while True:
        pos = list(input(command))
        if len(pos) == 2 and pos[0] in board_row and pos[1] in board_col and ship_sign in \
                board[ord(pos[0]) - 96][int(pos[1])]:
            pos[0] = ord(pos[0]) - 96  # converts the 1st value from a letter to a digit
            pos[1] = int(pos[1])  # converts the 2nd value from a letter to a digit
            board[pos[0]][pos[1]] = hit_sign
            break
        elif len(pos) == 2 and pos[0] in board_row and pos[1] in board_col and empty_cell_sign in \
                board[ord(pos[0]) - 96][int(pos[1])]:
            pos[0] = ord(pos[0]) - 96
            pos[1] = int(pos[1])
            board[pos[0]][pos[1]] = shoot_sign
            break
        else:
            continue


def win(board):
    if not any([ship_sign in board_cell for board_cell in board]):
        return True


def draw(field):
    """
    draw(field)
    Displays the game board in the console
    Accepts the game board.
    Returns nothing
    """
    f = field  # shortened the name for convenience
    print(f'      | 1 | 2 | 3 | 4 | 5 | 6 |\n'
          f'      -------------------------\n'
          f'    a | {f[1][1]} | {f[1][2]} | {f[1][3]} | {f[1][4]} | {f[1][5]} | {f[1][6]} |\n'
          f'    b | {f[2][1]} | {f[2][2]} | {f[2][3]} | {f[2][4]} | {f[2][5]} | {f[2][6]} |\n'
          f'    c | {f[3][1]} | {f[3][2]} | {f[3][3]} | {f[3][4]} | {f[3][5]} | {f[3][6]} |\n'
          f'    d | {f[4][1]} | {f[4][2]} | {f[4][3]} | {f[4][4]} | {f[4][5]} | {f[4][6]} |\n'
          f'    e | {f[5][1]} | {f[5][2]} | {f[5][3]} | {f[5][4]} | {f[5][5]} | {f[5][6]} |\n'
          f'    f | {f[6][1]} | {f[6][2]} | {f[6][3]} | {f[6][4]} | {f[6][5]} | {f[6][6]} |\n'
          f'      -------------------------\n')
