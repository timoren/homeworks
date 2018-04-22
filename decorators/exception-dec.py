from functools import wraps


def exception_dec(func):

    @wraps(func)
    def wrapped(*value, **kwargs):
        try:
            func_return = func(*value, **kwargs)
        except Exception as e:
            return 'exception \'{}\' occured while running \'{}\''.format(e, func.__name__)
        return func_return
    return wrapped

@exception_dec
def add_2_value(*args):
    arg = []
    for a in args:
        arg.append(a + 2)
    return arg



new_value = add_2_value(1, 4, 7)
print(new_value)
