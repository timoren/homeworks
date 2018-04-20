import random

moves = {'w': -4, 's': 4, 'a': -1, 'd': 1}
right_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']

def build_table():
    table = list(range(1, 16))
    table.append('x')
    random.shuffle(table)
    print('This is the perfect table and you need to build the same: ', '\n')
    for i in range(0, 16, 4):
        print(right_table[i:i + 4])
    print('\n')
    return table


def print_table(table):
    print('\n You need to fix this table to be the same like perfect one \n')
    for i in range(0, 16, 4):
        print(table[i:i + 4])
    print('\n')


def all_option(current_empty, table):
    mid_left = [4, 8]
    mid_right = [7, 11]
    if current_empty >= 12:
        if current_empty == 15:
            option_list = (table[current_empty -1], table[current_empty - 4])
            return option_list

        elif current_empty == 12:
            option_list = (table[current_empty +1], table[current_empty - 4])
            return option_list
        else:
            option_list = (table[current_empty - 4], table[current_empty - 1], table[current_empty + 1])
            return option_list

    if 3 < current_empty < 12:
        if current_empty in mid_left:
            option_list = (table[current_empty -4], table[current_empty + 1], table[current_empty + 4])
            return option_list
        elif current_empty in mid_right:
            option_list = (table[current_empty - 4], table[current_empty - 1], table[current_empty + 4])
            return option_list
        else:
            option_list = (table[current_empty - 4], table[current_empty -1], table[current_empty + 1], table[current_empty + 4])
            return option_list
    if current_empty <= 3:
        if current_empty == 0:
            option_list = (table[current_empty + 1], table[current_empty + 4])
            return option_list
        elif current_empty == 3:
            option_list = (table[current_empty - 1], table[current_empty + 4])
            return option_list
        else:
            option_list = (table[current_empty - 1], table[current_empty + 1], table[current_empty + 4])
            return option_list


def user_input(table):
    index_empty = table.index('x')
    available_option = all_option(index_empty, table)
    while True:
        print('you can move now only this number: ', available_option)
        user_num = input('choose your number: ')
        try:
            user_num = int(user_num)
            if user_num in available_option:
                user_index = table.index(user_num)
                table[index_empty], table[user_index] = table[user_index], table[index_empty]
                return table
        except ValueError as e:
            print('you pushed wrong key', e)


def is_game_finished(table, count):
    print('you finished the game and number of movements that you did is: ', count)
    return right_table == table


def main():
    """
    build table with 16 parts.
    :return:
    """
    table = build_table()
    count = 0
    while not is_game_finished(table, count):
        print_table(table)
        table = user_input(table)
        count += 1


if __name__ == '__main__':
    main()