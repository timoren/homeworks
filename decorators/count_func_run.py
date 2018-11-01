from functools import wraps

from time import time


#### test

class Counter(object):

    run_time_func = {}

    @staticmethod
    def call_counter(func):

        def counter_wrap(*args, **kwargs):

            if func.__name__ in Counter.run_time_func.keys():
                Counter.run_time_func[func.__name__] += 1
            else:
                Counter.run_time_func[func.__name__] = 1

            print('{} is called {} times'.format(func.__name__, Counter.run_time_func[func.__name__]))

            return func(*args, **kwargs)

        return counter_wrap

def print_func(func):
    def dec_func(value):
        print('---------')
        func(value)
        print('=========')
    return dec_func


def cancelled(func):
    """Cancels the execution of a function"""
    @wraps(func)
    def wrapped(*args, **kwargs):
        print(func.__name__, 'is cancelled!')
    return wrapped


@Counter.call_counter
@print_func
def print_vlaue(arg):
    print(arg)


print_vlaue('hello')

print_vlaue('hello1')