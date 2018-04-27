from collections_enum import Players
from graphic import Graphic

from game import Game

__author__ = 'gzhukova'


def main():
    g = Graphic()
    game = Game(g)
    game.display_instruct()
    enemy = game.ask_who_is_enemy()
    player1 = game.get_human_player()
    player2 = None
    if enemy == Players.human:
        player2 = game.get_human_player()
    elif enemy == Players.comp:
        player2 = game.get_computer_player()
    player1.setup_ships()
    player2.setup_ships()
    game.begin(player1, player2)


if __name__ == '__main__':
    main()
