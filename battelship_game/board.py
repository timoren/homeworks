from collections_of_all_options import Players, Statuses, ShotResult

class Cell(object):
    def __init__(self, row_set, col_set):
        self.row_set = row_set
        self.col_set = col_set
        self._status_cell = Statuses.Free

    def get_status(self):
        """
        to get the status of a cell
        :return: Status
        """

        return self._status_cell

    def set_status(self, new_status):
        """
        setting new status of the cell 'self._status_cell'
        :param new_status:
        :return: None
        """
        if new_status not in Statuses.__dict__.values():
            raise ValueError ('wrong status type of the cell')
        else:
            self._status_cell = new_status
    status = property(get_status, set_status)

    @property
    def coord_cell(self):
        """
        to get the coordination of the cell
        :return: (row_set, col_set)
        """
        return (self.row_set, self.col_set)





class Board(object):
    N = 10
    COLUMNS = 'ABCDEFGHIJ'
    SHIPS_COUNT = {4: 1, 3: 2, 2: 3, 1: 4}
    DIRECTION = ["n", "s", "w", "e"]

    def __init__(self):
        self.ship = []
        self.cells = []
        for i in range(self.N):
            self.cells.append([Cell(i, j) for j in range(self.N)])
