from functools import wraps
from time import time


def count_time(func):

    @wraps(func)
    def print_time(value):
        start = time()
        func(value)
        end = time()
        return print(end - start)
    return print_time


@count_time
def print_value(arg):
    print(arg)


print_value('hello')


@count_time
def print_range(arg):
    for a in arg:
        print(a)


print_range('range')