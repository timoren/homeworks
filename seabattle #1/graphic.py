from collections_enum import Statuses

__author__ = 'gzhukova'


class Graphic(object):

    def draw_board(self, board, hide_ship=False):
        """
        Отрисовывает игральную доску
        :param board: доска
        :param hide_ship: скрыть корабль
        :return: None
        """
        print("\n")
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
        Определение символов выведения состояния ячеек на экран
        :param status: статус ячейки
        :return: символ отображения ячейки
        """
        if status == Statuses.free:
            return "-"
        elif status == Statuses.ship:
            return "S"
        elif status == Statuses.missed:
            return "*"
        elif status == Statuses.padded:
            return "X"

if __name__ == "__main__":
    print("Вы запустили этот модуль напрямую")
