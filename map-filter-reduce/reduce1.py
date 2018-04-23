from functools import reduce

print('reduce result:', reduce(lambda a, b: a + b, list(len(x) for x in ['some', 'other', 'value'])))
