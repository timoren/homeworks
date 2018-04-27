from enum import Enum

__author__ = 'gzhukova'


class Players(Enum):
    human = 0
    comp = 1


class Statuses(Enum):
    free = 0
    missed = 1
    padded = 2
    ship = 3


class ShotResult(Enum):
    hit = 0
    miss = 1
    error = 2

if __name__ == "__main__":
    print("Вы запустили этот модуль напрямую")
