import os
from functions import *
from classes import *
from variables import *

# =====================================================================================
enemy = Board(enemy_board, ship_sign)  # create game board object for enemy
enemy_navy = Ship(enemy.board, ship_sign)  # create enemy ships object
enemy.set_cruiser(enemy_navy.cruiser_pos)  # set cruiser on enemy game board
enemy.set_destroyer(enemy_navy.destroyer_pos)  # set 1st destroyer
enemy.set_destroyer(enemy_navy.destroyer_pos)  # set 2nd destroyer
enemy.set_torpedo_boat(enemy_navy.torpedo_ship_pos)  # set 1st torpedo boat
enemy.set_torpedo_boat(enemy_navy.torpedo_ship_pos)  # 2nd
enemy.set_torpedo_boat(enemy_navy.torpedo_ship_pos)  # 3rd
enemy.set_torpedo_boat(enemy_navy.torpedo_ship_pos)  # 4th
# =====================================================================================
player = Board(player_board, ship_sign)  # create game board object for player
player_navy = Ship(player.board, ship_sign)  # create player ships object
player.set_cruiser(player_navy.cruiser_pos)  # set cruiser on player game board
player.set_destroyer(player_navy.destroyer_pos)  # set 1st destroyer
player.set_destroyer(player_navy.destroyer_pos)  # set 2nd
player.set_torpedo_boat(player_navy.torpedo_ship_pos)  # set 1st torpedo boat
player.set_torpedo_boat(player_navy.torpedo_ship_pos)  # 2nd
player.set_torpedo_boat(player_navy.torpedo_ship_pos)  # 3rd
player.set_torpedo_boat(player_navy.torpedo_ship_pos)  # 4th
# =====================================================================================
if __name__ == "__main__":
    while True:
        os.system('cls||clear')
        print(header)
        print('    Enemy\n')
        draw(enemy.board)
        print('\n    You\n')
        draw(player.board)
        player_shoot(enemy.board)
        if win(enemy.board):
            os.system('cls||clear')
            print(header)
            print('    Enemy\n')
            draw(enemy.board)
            print('\n    You\n')
            draw(player.board)
            print(player_win_message)
            input('Press Enter to quit the game \n')
            os.system('cls||clear')
            quit()
        enemy_shoot(player.board)
        if win(player.board):
            os.system('cls||clear')
            print(header)
            print('    Enemy\n')
            draw(enemy.board)
            print('\n    You\n')
            draw(player.board)
            print(enemy_win_message)
            input('Press Enter to quit the game \n')
            os.system('cls||clear')
            quit()
