def create_board():
    row = list(range(0, 10))
    string = " "
    for a in range(0, 10):
        row[a] = string
    board = [row] * 10
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


def user_ship_setting():
    battleship = {"1": 4, "2": 3, "3": 2, "4": 1}
    print('your battleships \n',
          "size   units \n",
          " 1      ", battleship["1"], "\n",
          " 2      ", battleship["2"], "\n",
          " 3      ", battleship["3"], "\n",
          " 4      ", battleship["4"], "\n",
          )
    while True:
        try:
            user_input = input('please select your bettelship size: ',)
            if battleship[user_input] == 0:
                print('you do not have battleship of this size any more, please select other')
            else:
                battleship[user_input] -= 1
        except Exception as e:

            print('error')






c = create_board()
print_board(c)
user_ship_setting()