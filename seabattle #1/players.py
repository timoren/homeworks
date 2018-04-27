import random
from board import Board

from collections_enum import Statuses, ShotResult

__author__ = 'gzhukova'


class Player(object):
    def __init__(self):
        self.board = Board()
        self.enemy = None

    def set_enemy(self, enemy):
        """
        Установка значения оппонента
        :param enemy: оппонент
        :return: None
        """
        self.enemy = enemy


class Human(Player):
    def __init__(self, name, graphic):
        super().__init__()
        self.name = name
        self.graphic = graphic

    def setup_ships(self):
        """
        Расстановка кораблей игроком
        :return: None
        """
        print("\n\n\t\tИгрок {0} расставляет свои корабли на доске: ".format(self.name))
        self.graphic.draw_board(self.board)
        for count_deck, count_ship in Board.SHIPS_COUNT.items():
            for i in range(count_ship):
                while True:
                    if count_deck == 1:
                        position = input("\n Введите позицию для {0}-палубного корабля(1a,4f...):\n".format(count_deck))
                        if self.validate_position_install(position):
                            direction = ""
                            break
                    else:
                        position_direction = input("\n Введите позицию для {0}-х палубного корабля и "\
                                                   "направление (n,s,w,e)(1an, 4fs ...):\n".format(count_deck))
                        if self.validate_position_direction(position_direction, count_deck):
                            position = position_direction[:-1]
                            direction = position_direction[-1]
                            break
                row_index, col_index = self.convert_position(position)
                self.board.add_ship(row_index, col_index, count_deck, direction)
                self.graphic.draw_board(self.board)

    @staticmethod
    def validate_position_shot(position):
        """
        Проверяется правильность формата введенных координат
        :param position: координаты на доске, заданные в формате строка-столбец
        :return: True - все введено верно, False - есть ошибка
        """
        row_index = position[:-1]
        col_index = position[-1]
        if not row_index.isdigit():
            print("Первым значением должно быть число - номер строки")
            return False
        row_index = int(row_index) - 1
        if row_index not in range(Board.N):
            print("Номер строки за границами доски")
            return False
        elif col_index not in Board.COLUMNS:
            print("Такого столбца нет")
            return False
        return True

    @staticmethod
    def convert_position(position):
        """
        Конвертирование координат, вводимых пользователем
        :param position: координаты на доске, заданные в формате строка-столбец
        :return: индексы указанной ячейки
        """
        row_index = int(position[:-1]) - 1
        col_index = Board.COLUMNS.index(position[-1])
        return row_index, col_index

    def validate_position_install(self, position):
        """
        Проверяется есть ли корабли в округе (для однопалубного корабля)
        :param position: координаты, заданные игроком
        :return: True или False
        """
        if not self.validate_position_shot(position):
            return False
        row_index, col_index = self.convert_position(position)
        if not self.board.is_surround_ok(self.board.cells[row_index][col_index]):
            print("Корабли не должны касаться друг друга")
            return False
        return True

    def validate_position_direction(self, position_direction, count_deck):
        """
        Проверка наличия кораблей в округе и правильности заданного направления (для многопалубных)
        :param position_direction:  координаты и направление
        :param count_deck: количество палуб
        :return: True, False
        """
        position = position_direction[:-1]
        if not self.validate_position_install(position):
            return False
        direction = position_direction[-1]
        if direction not in Board.DIRECTION:
            print("Укажите другое направление")
            return False
        step_row, step_col = Board.determine_direction(direction)
        row_index, col_index = self.convert_position(position)

        new_row_index = row_index + step_row * count_deck
        new_col_index = col_index + step_col * count_deck
        if not self.board.is_position_correct(new_row_index, new_col_index):
            print("Корабль не помещается на поле")
            return False
        for k in range(1, count_deck):
            cur_row = row_index + k * step_row
            cur_col = col_index + k * step_col
            for i in range(-1, 2):
                new_cur_row = cur_row + i
                for j in range(-1, 2):
                    new_cur_col = cur_col + j
                    if not Board.is_position_correct(new_cur_row, new_cur_col):
                        continue
                    if self.board.cells[new_cur_row][new_cur_col].status == Statuses.ship:
                        print("Корабли не должны касаться друг друга")
                        return False
        return True

    def shot(self):
        """
        Выстрелы игрока
        :return: None
        """
        is_enemy_shot = True
        while True:
            print("\n\n Ваш ход, {0} ".format(self.name))
            self.graphic.draw_board(self.enemy.board, True)
            position = input("\nВведите координаты выстрела (пример: 3b): \n")
            if not self.validate_position_shot(position):
                continue
            row_index, col_index = self.convert_position(position)
            c = self.enemy.board.cells[row_index][col_index]
            if c.status == Statuses.missed or c.status == Statuses.padded:
                print("Такие координаты уже вводились. Попробуйте еще раз.")
                continue
            res = (self.enemy.board.make_shot_by_position(row_index, col_index))[0]
            if res == ShotResult.miss:
                break
            if self.enemy.board.is_game_finished():
                self.graphic.draw_board(self.enemy.board)
                print("\nВы выиграли, {0}. Поздравляем!".format(self.name))
                is_enemy_shot = False
                break
        if is_enemy_shot:
            self.enemy.shot()


class Computer(Player):

    def __init__(self, graphic):
        super().__init__()
        self.name = 'intel core i5'
        self.graphic = graphic
        self.shot_count = 0
        self.last_padded_deck = None
        self.complexity = self.get_complexity()
        self.padded_ships = {
            1: 0,
            2: 0,
            3: 0,
            4: 0
        }

    @staticmethod
    def get_complexity():
        """
        Выбор уровня сложности для игры с компьютером
        :return: уровень сложности
        """
        l = [str(i) for i in range(1, 4)]
        compl = ""
        while compl not in l:
            compl = input("Введите уровень сложности для компьютера (1-3):")
        return int(compl)

    def setup_ships(self):
        """
        Расстановка кораблей компьютером
        :return: None
        """
        self.board.positioning_ships()

    def shot(self):
        """
        Алгоритм выстрелов компьютера
        :return: None
        """
        is_enemy_shot = True
        while True:
            print("\nХод компьютера: \n")
            res, shot_position = self.shot_comp()
            self.shot_count += 1
            self.graphic.draw_board(self.enemy.board)
            if res == ShotResult.miss:
                break
            elif res == ShotResult.hit:
                self.last_padded_deck = self.enemy.board.cells[shot_position[0]][shot_position[1]]
            if self.enemy.board.is_game_finished():
                print("\nВыиграл {0}!!!".format(self.name))
                is_enemy_shot = False
                break
        if is_enemy_shot:
            self.enemy.shot()

    def shot_comp(self):
        """
        Выстрел компьютера
        :return:значение, которое принимает клетка на доске
        """
        row_index = None
        col_index = None
        if self.complexity == 1:
            row_index, col_index = self.get_position_complexity_easy()
        elif self.complexity == 2:
            if self.shot_count % 3 == 0:
                row_index, col_index = self.get_position_complexity_easy()
            else:
                row_index, col_index = self.get_position_complexity_smart()
        elif self.complexity == 3:
            row_index, col_index = self.get_position_complexity_smart()

        return self.enemy.board.make_shot_by_position(row_index, col_index)

    def get_position_complexity_easy(self):
        """
        Вычисляет координаты для последующего выстрела рандомно
        :return: координаты в виде tuple
        """
        new_cells = []
        for i, row in enumerate(self.enemy.board.cells):
            for j, cell in enumerate(row):
                if cell.status != Statuses.missed and cell.status != Statuses.padded:
                    new_cells.append((i, j))
        return random.choice(new_cells)

    def get_position_complexity_smart(self):
        """
        Вычисляет координаты для последующего выстрела по алгоритму
        :return: координаты в виде tuple
        """
        if self.last_padded_deck is None:
            return self.get_position_complexity_easy()
        sp = self.retrieve_current_ship_to_sunk()
        coordinates = self.get_possible_coordinates_for_shot(sp)
        is_updated = self.update_padded_ships(sp, coordinates)
        if is_updated:
            return self.get_position_complexity_easy()
        coord_for_shot = random.choice(coordinates)
        return coord_for_shot

    def retrieve_current_ship_to_sunk(self):
        """
        Определение координат текущего потопляемого корабля
        :return: sp - список координат палуб текущего потопляемого корабля
        """
        sp = [self.last_padded_deck.coords]
        row_index, col_index = self.last_padded_deck.coords
        for item in self.last_padded_deck.neighbors_ortho:
            cell = self.enemy.board.cells[item[0]][item[1]]
            if cell.status == Statuses.padded:
                sp.append(cell.coords)
                step_row = cell.row_index - row_index
                step_col = cell.col_index - col_index
                new_row_index = cell.row_index
                new_col_index = cell.col_index
                while True:
                    new_row_index += step_row
                    new_col_index += step_col
                    if not Board.is_position_correct(new_row_index, new_col_index):
                        break
                    if self.enemy.board.cells[new_row_index][new_col_index].status == Statuses.padded:
                        sp.append((new_row_index, new_col_index))
                        if len(sp) == 4:
                            break
                    else:
                        break
                break
        return sp

    def update_padded_ships(self, sp, coordinates):
        """
        Обновление списка потопленных кораблей
        :param sp: список подбитых палуб
        :param coordinates: список возможных выстрелов
        :return: True - корабль полностью подбит и добавлен в список выбывших
        """
        count = 0
        ship_length = len(sp)
        if ship_length == 4:
            self.padded_ships[ship_length] += 1
            self.mark_cell_around_padded_ship(sp)
            return True
        for i in range(ship_length + 1, 5):
            if self.padded_ships[i] == Board.SHIPS_COUNT[i]:
                count += 1
        if count == 4 - ship_length:
            self.padded_ships[ship_length] += 1
            self.mark_cell_around_padded_ship(sp)
            return True
        if len(coordinates) == 0:
            self.padded_ships[ship_length] += 1
            self.mark_cell_around_padded_ship(sp)
            return True
        return False

    def mark_cell_around_padded_ship(self, sp):
        """
        Изменить все ячейки оставшиеся вокруг подбитого корабля, чтобы исключить их из вариантов выстрела
        :param sp:список координат палуб корабля
        :return:None
        """
        for s in sp:
            deck = self.enemy.board.cells[s[0]][s[1]]
            for i in deck.neighbors:
                cell = self.enemy.board.cells[i[0]][i[1]]
                if cell.status == Statuses.free:
                    cell.status = Statuses.missed

    def get_possible_coordinates_for_shot(self, sp):
        """
        Определяются возможные координаты для выстрела для текущего корабля, определенного в sp
        :param sp: список координат подбитых палуб корабля
        :return: список возможных координат для выстрела
        """
        possible_coordinates = []
        if len(sp) == 1:
            for item in self.last_padded_deck.neighbors_ortho:
                cell = self.enemy.board.cells[item[0]][item[1]]
                if cell.status != Statuses.missed:
                    possible_coordinates.append(cell.coords)
        elif len(sp) in (2, 3):
            p = []
            if abs(sp[0][1] - sp[-1][1]) == 0:   # вертикально
                top = (min(sp[0][0], sp[-1][0]) - 1, sp[0][1])
                bot = (max(sp[0][0], sp[-1][0]) + 1, sp[0][1])
                if Board.is_position_correct(top[0], top[1]):
                    p.append(top)
                if Board.is_position_correct(bot[0], top[1]):
                    p.append(bot)
            else:
                left = (sp[0][0], min(sp[0][1], sp[-1][1]) - 1)
                right = (sp[0][0], max(sp[0][1], sp[-1][1]) + 1)
                if Board.is_position_correct(left[0], left[1]):
                    p.append(left)
                if Board.is_position_correct(right[0], right[1]):
                    p.append(right)
            for item in p:
                cell = self.enemy.board.cells[item[0]][item[1]]
                if cell.status != Statuses.padded and cell.status != Statuses.missed:
                    possible_coordinates.append(item)
        return possible_coordinates


if __name__ == "__main__":
    print("Вы запустили этот модуль напрямую")
