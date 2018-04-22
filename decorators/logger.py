from functools import wraps



def logger_dec(func):
    print('decorator is started: \n')
    @wraps(func)
    def wrapped(*args, **kwargs):
        print(' \n function is started: {} \n'.format(func.__name__))
        func_return = func(*args, **kwargs)
        print('\n the function is end here: {} \n'.format(func.__name__))
        return func_return
    return wrapped

@logger_dec
def print_hello(value):
    print(value)


print_hello('hello')