def create_board():
    row = list(range(0, 10))
    string = " "
    board = list(range(0, 10))
    for a in range(0, 10):
        row[a] = string
    for a in range(0, 10):
        board[a] = list(row)
    return board


def print_board(board):
    abc = 'ABCDEFGHJK'
    first_row = list(board[0])
    for a in range(0, 10):
        first_row[a] = abc[a]
    print("\n   ", first_row)
    for a in range(0, 10):
        if a < 9:
            print("\n", str(a + 1), "", board[a])
        else:
            print("\n", "10", board[a])


def battleship_set(board, ship_size, ship_h_v, ship_location1, ship_location2):
    board = list(board)
    sing = "O"
    row_set = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'J': 8, 'K': 9}
    ship_location1 = int(ship_location1) - 1
    ship_location2 = list(ship_location2)
    user_row = board[ship_location1]
    if ship_h_v == "H":
        for a in range(0, len(ship_location2)):
            ship_loc_index = row_set[ship_location2[a]]
            user_row[ship_loc_index] = sing
        print(user_row)
        print(ship_location1)
        board[ship_location1] = user_row
        print(board)
        return board


def user_ship_setting(board):
    user_board = board
    battleship = {"1": 4, "2": 3, "3": 2, "4": 1}
    ship_count = sum(battleship.values())
    print('your battleships \n',
          "size   units \n",
          " 1      ", battleship["1"], "\n",
          " 2      ", battleship["2"], "\n",
          " 3      ", battleship["3"], "\n",
          " 4      ", battleship["4"], "\n",
          )
    while True:
        try:
            user_ship_size = input('please select your bettelship size: ',)
            if ship_count != 0:
                if battleship[user_ship_size] == 0:
                    print('you do not have battleship of this size any more, please select other')
                else:
                    print_board(user_board)
                    user_ship_horizon_or_virtical = input('please select how you want your ship Horizontal or Virtical by ( H  or  V ): ', )
                    user_ship_location1, user_ship_location2 = input('please select location of bettelship size: for example  A 123 or  1 ABC ', ).split()
                    board = battleship_set(user_board, user_ship_size, user_ship_horizon_or_virtical, user_ship_location1, user_ship_location2)
                    ship_count -= 1
                    print_board(board)
                    battleship[user_ship_size] -= 1
        except Exception as e:

            print('error')






c = create_board()
print_board(c)
user_ship_setting(c)