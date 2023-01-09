empty_cell_sign = 'o'  # start symbol of the cell on the game board
ship_sign = '■'  # symbol where located the ship
shoot_sign = 'T'  # symbol where was the shot
hit_sign = 'X'  # symbol where was the hit
# the field size is larger to avoid IndexError when calculating the halos of ships
enemy_board = [[empty_cell_sign] * 10 for _ in range(10)]
player_board = [[empty_cell_sign] * 10 for _ in range(10)]
board_size = 6
board_row = ['a', 'b', 'c', 'd', 'e', 'f']  # symbols of the rows on the game board
board_col = ['1', '2', '3', '4', '5', '6']  # numbers of the cols on the game board
header = f"------------------------------------\n         STORM IN A GLASS\n------------------------------------\n"
command = 'Where to shoot? (e.g. a4): '
enemy_win_message = "Your navy has been destroyed.\nYou've lost the battle, Admiral.\nBut not the war.\n"
player_win_message = "Congratulations, Admiral!\nYou have destroyed the enemy navy\nand won the battle.\n"
