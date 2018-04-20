import random


empty_hole = " "

def add_table():
    table = []
    for i in range(9):
        table.append(empty_hole)
    return table


def print_table(table):
    print('\n\t', table[0], "|", table[1], "|",  table[2])
    print('\t', '---------')
    print('\t', table[3], '|', table[4], '|', table[5])
    print('\t', '---------')
    print('\t', table[6], '|', table[7], '|', table[8])


def start():
    ans = None
    while ans not in('y', 'n'):
        ans = input("do you want to start first: (y/n) ")
    if ans == "y":
        human = "X"
        comp = "O"
    else:
        human = "O"
        comp = "X"
    return human, comp


def user_input(table, human):
    user_choice = None
    rest = rest_move(table)
    print(rest, user_choice)
    while user_choice not in rest:
        try:
            user_choice = int(input('choose one number 0-8 which you want to set:'))
            print(user_choice)
            if user_choice in rest:
                table[user_choice] = human
                print(table)
                return table
            print(' here')
        except IndexError as e:
            print(e)
        except ValueError as e:
            print('wrong key: ', e)


def comp_input(table, comp_choice, comp):
    rest = rest_move(table)
    comp_choice = comp_comb(table, comp)
    if len(comp_choice) == 0:
        while comp_choice not in rest:
            if len(comp_choice) == 0:
                comp_choice = int(random.choice(rest))
                table[comp_choice] = comp
                return table, comp_choice
        # else:
        #     comp_choice = comp_comb(table)

        # elif empty_hole == table[comp_choice - 1] and table[comp_choice + 2] and table[comp_choice + 3]:


def comp_comb(table, comp):
    lst = list(range(9))
    new_list = []
    where_comp = []
    comp_pos = []
    for i in range(0, 8, 3):
        new_list.append(lst[i:i + 3])
        if i == 0:
            new_list.append(list([lst[i], lst[i + 3], lst[i + 6]]))
            new_list.append(list([lst[i + 1], lst[i + 4], lst[i + 7]]))
            new_list.append(list([lst[i + 2], lst[i + 5], lst[i + 8]]))
            new_list.append(list([lst[i], lst[i + 4], lst[i + 8]]))
            new_list.append(list([lst[i + 2], lst[i + 4], lst[i + 6]]))
    for i in range(0, 8, 3):
        comp_pos.append(table[i:i + 3])
        if i == 0:
            comp_pos.append(list([table[i], table[i + 3], table[i + 6]]))
            comp_pos.append(list([table[i + 1], table[i + 4], table[i + 7]]))
            comp_pos.append(list([table[i + 2], table[i + 5], table[i + 8]]))
            comp_pos.append(list([table[i], table[i + 4], table[i + 8]]))
            comp_pos.append(list([table[i + 2], table[i + 4], table[i + 6]]))
    for i in range(8):
        comp_comb1 = comp_pos[i]
        win_comb1 = new_list[i]

        count = -1
        lst_comp = []
        while True:
            try:
                lst_comp = comp_comb1.index(comp, count+1)
                print('here', lst_comp)
            except ValueError:
                print('here')
            else:
                lst_comp.append(lst_comp)
                count = lst_comp
    #     x = 'O'
    #     try:
    #         for i in range(0, 2):
    #             if comp_comb1[i] == x:
    #                 if win_comb1[i] not in where_comp:
    #                     where_comp.append(win_comb1[i])
    #             print('here', win_comb1, ":", where_comp, ":", comp_comb1, ":", comp_pos)
    #     except ValueError as e:
    #         print('eee', e)
    #     except IndexError as e:
    #         print(e)
    # print(where_comp)
    # comp_choice = comp_num(table, where_comp)
    return comp_choice


# def comp_num(table, where_comp):
#     rest = rest_move(table)

def win_combo(comp_choice):
    WAYS_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )



def rest_move(table):
    rest = []
    for i in range(9):
        if table[i] == empty_hole:
            rest.append(i)
    return rest


def main():
    print("""Игра крестики-нолики, противостояние с компьютером\n
        Чтобы сделать ход, необходимо ввести число от 0 до 8. Число однозначно соответствует
        полям доски, как показано на рисунке ниже:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        """)
    comp_choice = []
    human, comp = start()
    table = add_table()
    print_table(table)
    user_input(table, human)
    comp_input(table, comp_choice, comp)


main()


