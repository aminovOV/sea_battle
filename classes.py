from random import randint
from variables import board_size


class Board:  # responsible for placement of player's and enemy's ships
    def __init__(self, board=None, ship_sign=None):
        self.__board = board  # from variables.py
        self.__ship_sign = ship_sign  # from variables.py
        self.__pos = None  # accepts coordinates from ships

    @property
    def board(self):  # get game board
        return self.__board

    @board.setter
    def board(self, shot):  # accepts coordinates of shots on game board
        self.__board = shot

    def set_torpedo_boat(self, pos):  # set 1 symbol of ship on the game board
        self.__pos = pos
        self.__board[self.__pos[0]][self.__pos[1]] = self.__ship_sign

    def set_destroyer(self, pos):  # set 2 symbols of ship on the game board
        self.__pos = pos
        self.__board[self.__pos[0][0]][self.__pos[0][1]] = self.__ship_sign
        self.__board[self.__pos[1][0]][self.__pos[1][1]] = self.__ship_sign

    def set_cruiser(self, pos):  # set 3 symbols of ship on the game board
        self.__pos = pos
        self.__board[self.__pos[0][0]][self.__pos[0][1]] = self.__ship_sign
        self.__board[self.__pos[1][0]][self.__pos[1][1]] = self.__ship_sign
        self.__board[self.__pos[2][0]][self.__pos[2][1]] = self.__ship_sign


class Ship:  # responsible for calculating the positions of the possible placement of the player's and enemy's ships
    def __init__(self, board=None, ship_sign=None):
        self.__board = board
        self.__ship_sign = ship_sign

    @property
    def torpedo_ship_pos(self):  # get torpedo boat position
        b = self.__board
        while True:
            x = randint(1, board_size)  # random choice of row on game board
            y = randint(1, board_size)  # random choice of column on game board
            halo = [b[x][y], b[x + 1][y], b[x - 1][y], b[x][y + 1], b[x][y - 1]]  # kind of a halo around the ship
            if self.__ship_sign not in halo:
                return [x, y]

    @property
    def destroyer_pos(self):  # get destroyer position
        b = self.__board
        while True:
            x = randint(1, board_size)
            y = randint(1, board_size)
            orientation = randint(0, 1)  # choose vertical or horizontal orientation of the ship
            v_halo = [b[x][y], b[x + 1][y], b[x + 2][y], b[x - 1][y], b[x][y + 1],  # halo if vertical orientation
                      b[x][y - 1], b[x + 1][y + 1], b[x + 1][y - 1]]
            h_halo = [b[x][y], b[x + 1][y], b[x - 1][y], b[x][y + 1], b[x][y + 2],  # halo if horizontal orientation
                      b[x][y - 1], b[x + 1][y + 1], b[x - 1][y + 1]]
            if orientation == 0 and self.__ship_sign not in v_halo and x < board_size and y <= board_size:
                return [[x, y], [x + 1, y]]
            elif orientation == 1 and self.__ship_sign not in h_halo and x <= board_size and y < board_size:
                return [[x, y], [x, y + 1]]

    @property
    def cruiser_pos(self):  # the halo around this ship requires too many conditions (easy to set cruiser 1st)
        while True:
            x = randint(1, board_size)
            y = randint(1, board_size)
            orientation = randint(0, 1)
            if orientation == 0 and x < board_size - 1 and y <= board_size:
                return [[x, y], [x + 1, y], [x + 2, y]]
            elif orientation == 1 and x <= board_size and y < board_size - 1:
                return [[x, y], [x, y + 1], [x, y + 2]]
