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

    def setup_ship(self):
        """
        setting ships on the board
        :return: None
        """

        print('\n\n\t\tplayer {} setting his ships on the board'.format(self.name))
        self.graphic.draw_board(self.board)
        for count_deck, count_ship in Board.SHIPS_COUNT.items():
            for i in range(count_ship):
                while True:
                    if count_deck == 1:
                        position = input('\n enter position for {} deck ship example (row,col) (1a or 4f...):\n'.format(count_deck))
                        if self.validate_position_install(position):
                            direction = ''
                            break
                        else:
                            position_direction = input('\n  enter position for {} deck ship example vector (n, s, w, e) (1a, 4f ...)'.format(count_deck))
                            if self.validation_position_direction((position_direction, count_deck))

