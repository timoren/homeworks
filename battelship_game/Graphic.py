from collections_of_all_options import Statuses


class Graphic(object):

    def draw_board(self, board, hide_ship=False):
        """
        drawing the board game
        :param board: board of the player
        :param hide_ship: hided ship of the enemy
        :return: None
        """
        print('\n')
        print('   ', end='')
        for s in board.COLUMNS:
            print(s, end=' ')
        for i, row in enumerate(board.cells):
            print('')
            gap = ' ' if i >= 9 else '  '
            print(str(i + 1), end=gap)
            for cell in row:
                if cell.status == Statuses.ship and hide_ship:
                    print(self.sym_from_status(Statuses.free), end=' ')
                else:
                    print(self.sym_from_status(cell.status), end=' ')

    @staticmethod
    def sym_from_status(status):
        """
        setting the right sign for cell status for printing
        :param status: cell status
        :return: sign for cell status
        """
        if status == Statuses.free:
            return '-'
        elif status == Statuses.ship:
            return 'S'
        elif status == Statuses.missed:
            return '*'
        elif status == Statuses.padded:
            return 'X'


if __name__ == '__main__':
    print('you are running this model locally')



