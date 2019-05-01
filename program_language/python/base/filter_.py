print filter(lambda x: x if isinstance(x, int) else None, [1, 20, '1'])
print filter(lambda x: isinstance(x, int), [1, 20, '1'])
print map(lambda x: x if isinstance(x, int) else None, [1, 20, '1'])
print reduce(lambda x, y: x + y, [1, 20, 1])
