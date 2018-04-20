def my_function():
    print('i am a function')

print(my_function)
print('function are objects', isinstance(my_function, object))

test = my_function
test()

my_list = []
my_list.append(my_function)
print(my_list)

def call_passed_function(incoming):
    print('calling')
    incoming()
    print('called')


call_passed_function(my_function)
try:
    d = 2
    d()
except TypeError as e:
    print('it is not a function', e)

print(callable(len), callable(45), callable(callable))


def return_min_function():
    return min


test = return_min_function()
print(test)
min_value = test(4, 5, -9, 12)
print('min value is: ', min_value)