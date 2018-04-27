import random

from collections_enum import Statuses, ShotResult

__author__ = 'gzhukova'


class Cell(object):
    ortho_steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, row_index, col_index):
        self.row_index = row_index
        self.col_index = col_index
        self._status = Statuses.free

    def get_status(self):
        """
        Получение статуса ячейки
        :return: статус
        """
        return self._status

    def set_status(self, new_status):
        """
        Изменение статуса ячейки
        :param new_status: новый статус
        :return: None
        """
        if new_status not in Statuses.__dict__.values():
            raise ValueError("Неверный статус ячейки")
        self._status = new_status
    status = property(get_status, set_status)

    @property
    def coords(self):
        """
        Свойство для получения индексов ячейки
        :return: tuple(индекс строкиб индкс столбца)
        """
        return (self.row_index, self.col_index)

    @property
    def neighbors_ortho(self):
        """
        Создается список ячеек, которые окружают текущую по вертикали и горизонтали
        :return: список ячеек окружения
        """
        s = []
        for i, j in self.ortho_steps:
            if Board.is_position_correct(self.row_index + i, self.col_index + j):
                s.append((self.row_index + i, self.col_index + j))
        return s

    @property
    def neighbors(self):
        """
        Создается список ячеек, которые окружают текущую со всех сторон, включая углы
        :return: список ячеек окружения
        """
        s = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if Board.is_position_correct(self.row_index + i, self.col_index + j):
                    s.append((self.row_index + i, self.col_index + j))
        return s

    def __str__(self):
        """
        Изменение метода отображения элементов
        :return: формат строки вывода
        """
        return str.format("row={0} col={1} status={2}", self.row_index,
                          self.col_index, self.status)


class Ship(object):

    def __init__(self, count_deck):
        self.decks = []
        self.count_deck = count_deck

    def set_status(self):
        """
        Устанавливается статус для корабля
        :return: None
        """
        for deck in self.decks:
            deck.status = Statuses.ship

    def is_sunk(self):
        """
        Проверяется, подбит ли корабль
        :return: False - корабль еще на плаву, True - корабль потоплен
        """
        for deck in self.decks:
            if deck.status == Statuses.ship:
                return False
        return True

    def __str__(self):
        s = []
        for deck in self.decks:
            s.append(str(deck))
        return " ".join(s)


class Board(object):
    N = 10
    COLUMNS = "abcdefghij"
    SHIPS_COUNT = {4: 1, 3: 2, 2: 3, 1: 4}
    DIRECTION = ["n", "s", "w", "e"]

    def __init__(self):
        self.ships = []
        self.cells = []
        for i in range(self.N):
            self.cells.append([Cell(i, j) for j in range(self.N)])

    def positioning_ships(self):
        """
        Расположение кораблей компьютером
        :return: None
        """
        for count_deck, count_ship in self.SHIPS_COUNT.items():
            for i in range(count_ship):
                ship = self.create_ship(count_deck)
                ship.set_status()

    def create_ship(self, count_deck):
        """
        Компьютером создается корабль и помещается на доске
        :param count_deck: количество палуб
        :return: корабль
        """
        self.ships.append(Ship(count_deck))
        cells_index = []
        for i in range(self.N):
            cells_index.append([j for j in range(self.N)])
        while True:
            first_deck_cell = self.get_random_cell(cells_index)
            res = self.is_surround_ok(first_deck_cell)
            if res is False:
                cells_index[first_deck_cell.row_index].remove(first_deck_cell.col_index)
                if len(cells_index[first_deck_cell.row_index]) == 0:
                    cells_index.remove(cells_index[first_deck_cell.row_index])
                continue
            self.ships[-1].decks.append(first_deck_cell)
            if count_deck == 1:
                return self.ships[-1]
            else:
                direction = self.DIRECTION[:]
                random.shuffle(direction)
                for d in direction:
                    step_row, step_col = self.determine_direction(d)
                    count_good = 1
                    for i in range(1, count_deck):
                        row_index = first_deck_cell.row_index + i * step_row
                        col_index = first_deck_cell.col_index + i * step_col
                        if not (0 <= row_index < self.N) or not(0 <= col_index < self.N):
                            break
                        test_cell = self.cells[row_index][col_index]
                        res = self.is_surround_ok(test_cell)
                        if res is False:
                            break
                        count_good += 1
                    if count_good == count_deck:
                        for i in range(1, count_deck):
                            row_index = first_deck_cell.row_index + i * step_row
                            col_index = first_deck_cell.col_index + i * step_col
                            self.ships[-1].decks.append(self.cells[row_index][col_index])
                        return self.ships[-1]

    def add_ship(self, row_index, col_index, count_deck, direction):
        """
        Добавление корабля на доску игрока
        :param row_index: координаты строки
        :param col_index: координаты столбца
        :param count_deck: количество палуб
        :param direction: напраление
        :return:None
        """
        ship = Ship(count_deck)
        step_row, step_col = self.determine_direction(direction)
        for i in range(count_deck):
            ship.decks.append(self.cells[row_index][col_index])
            col_index += step_col
            row_index += step_row
        ship.set_status()
        self.ships.append(ship)

    @staticmethod
    def determine_direction(direct):
        """
        Определяется шаг для указанного направления
        :param direct: направление
        :return: размер шага по горизонтали и вертикали
        """
        step_row = 0
        step_col = 0
        if direct == "n":
            step_row = - 1
        elif direct == "s":
            step_row = 1
        elif direct == "w":
            step_col = - 1
        elif direct == "e":
            step_col = 1
        return step_row, step_col

    def get_random_cell(self, cells_index):
        """
        Выбирает случайным образом ячейку из списка
        :param cells_index: список ячеек
        :return: случайную ячейку
        """
        row = random.choice(cells_index)
        row_index = cells_index.index(row)
        col_index = random.choice(row)
        return self.cells[row_index][col_index]

    def is_surround_ok(self, cell):
        """
        Проверка пустого места вокруг ячейки
        :param cell: ячейка
        :return: True - вокруг ячейки пусто или False - места нет
        """
        for item in cell.neighbors:
            if self.cells[item[0]][item[1]].status != Statuses.free:
                return False
        return True

    @staticmethod
    def is_position_correct(row, col):
        """
        Ячейка находится на доске
        :param row: координата строки
        :param col: координата столбца
        :return: True - ячейка на доске, False - ячейка не на доске
        """
        if row < 0 or col < 0 or row > Board.N - 1 or col > Board.N - 1:
            return False
        return True

    def make_shot_by_position(self, row_index, col_index):
        """
        Выстрел одного из игроков (человек или компьютер)
        :param row_index: индекс строки
        :param col_index: индекс столбца
        :return: значение, которое принимает клетка на доске
        """
        cell = self.cells[row_index][col_index]
        res = ''
        if cell.status == Statuses.free:
            cell.status = Statuses.missed
            res = ShotResult.miss
        elif cell.status == Statuses.missed:
            res = ShotResult.error
        elif cell.status == Statuses.padded:
            res = ShotResult.error
        elif cell.status == Statuses.ship:
            cell.status = Statuses.padded
            res = ShotResult.hit
        return res, (row_index, col_index)

    def is_game_finished(self):
        """
        Определяет, закончена ли игра
        :return: True - игра закончена, False - игра еще не закончена
        """
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True


if __name__ == "__main__":
    print("Вы запустили этот модуль напрямую")
