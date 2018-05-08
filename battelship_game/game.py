import random

class Game(object):
    count_player = 1

    def __init__(self, graphic):
           self.graphic = graphic

    @staticmethod
    def display_instruct():
        """
        print the game instruction.
        :return:
        """

    print("""
        Wellcome to game seabattle ship
        play you can in 2 stages
        1. play with other player
        2. play with computer
        in stage playing with computer you have to select the level of the computer
        1. easy
        2. med
        3. hard
        each player have board of the game on which hi setting his ships
           a b c d e f g h i j 
           1  - - - - - - - - - -
           2  - - - - - - - - - -
           3  - - - - - - - - - -
4  - - - - - - - - - -
5  - - - - - - - - - -
6  - - - - - - - - - -
7  - - - - - - - - - -
8  - - - - - - - - - -
9  - - - - - - - - - -
10 - - - - - - - - - -
Классы и количество кораблей:
4 палубы - 1
3 палубы - 2
2 палубы - 3
1 палуба - 4
Для выстрела по доске противника необходимо указать координаты ячейки
в формате номер строки-буква столбца.
Побеждает тот, кто первым подобъет все корабли противника.
\n\n """)

    def get_human_player(self):
        """
        add player - human
        :return: new player
        """

        name = ''
        while name == '':
            name = input('Please enter name of player {}'.format(self.count_player))
        self.count_player += 1
        return Human(name, self.graphic)


