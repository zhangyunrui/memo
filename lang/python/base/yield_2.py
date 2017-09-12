# coding: utf-8
"""
调用函数的时候，函数里的代码并没有运行，函数仅仅返回生成器对象。
每当用for语句迭代生成器的时候，代码才开始运转，直到碰到yield，
然后会返回本次循环的第一个返回值，以此类推，直到没有返回值。
"""

import itertools

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)
print(list(races))
