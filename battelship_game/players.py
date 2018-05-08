from board import Board

class Player(object):
    def __init__(self):
        self.board = Board()
        self.enemy = None

    def set_enemy(self, enemy):
        """
        set your enemy in the game
        :param enemy: enemy
        :return:
        """
        self.enemy = enemy


class Human(Player):
    def __init__(self, name, graphic):
        self.name = name
        self.graphic = graphic

