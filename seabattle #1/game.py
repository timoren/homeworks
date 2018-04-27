import random
from players import Human, Computer

from collections_enum import Players

__author__ = 'gzhukova'


class Game(object):
    count_players = 1

    def __init__(self, graphic):
        self.graphic = graphic

    @staticmethod
    def display_instruct():
        """
        Выводится инструкция для игры
        :return: None
        """
        print("""
Добро пожаловать в игру 'МОРСКОЙ БОЙ'.
Играть можно в двух режимах:
1. Играют два человека друг против друга
2. Человек играет против компьютера
При игре с компьютером необходимо указать уровень сложности для компьютера:
1. Самое легкое
2. Средняя сложность
3. Высокий уровень сложности
У каждого игрока есть своя доска, на которой он расставляет корабли таким образом,
чтобы они не соприкасались друг с другом в том числе углами. Доска выглядит так:
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
        Добавление игрока - человека
        :return: новый игрок
        """
        name = ''
        while name == '':
            name = input("Введите имя игрока{0}: \n".format(self.count_players))
        self.count_players += 1
        return Human(name, self.graphic)

    def get_computer_player(self):
        """
        Добавление игрока - компьютера
        :return: новый игрок
        """
        return Computer(self.graphic)

    @staticmethod
    def ask_who_is_enemy():
        """
        Определение, против кого будем играть
        :return: игрок
        """
        correct_answers = ['1', '2']
        answer = ''
        while answer not in correct_answers:
            answer = input("Играть против человека или компьютера?(человек - 1, компьютер - 2): \n")
        return Players.human if answer == '1' else Players.comp

    def who_is_first(self):
        """
        Рандомное вычисление, кто из огроков будет ходить первым
        :return: кто ходит первым
        """
        return random.randint(1, self.count_players)

    def begin(self, player1, player2):
        """
        Первые выстрелы игроков
        :param player1: первый игрок
        :param player2: второй игрок
        :return:None
        """
        player1.enemy = player2
        player2.enemy = player1
        if self.who_is_first() == 1:
            player1.shot()
        else:
            player2.shot()

if __name__ == "__main__":
    print("Вы запустили этот модуль напрямую")
