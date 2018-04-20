from functools import wraps
from time import time


def cancelled(func):
    """Cancels the execution of a function"""
    @wraps(func)
    def wrapped(*args, **kwargs):
        print(func.__name__, 'is cancelled!')
    return wrapped


@cancelled
def echo_value(arg):
    print(arg)