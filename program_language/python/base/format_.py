# coding: utf-8
"""
"!": 后接预设值
e.g. '{!s}{!r}'.format(Data())

":":
1. 后接格式规定串，格式串也可以是用"{}"指代，并在 format 中显式的指出
e.g.
"{:{dt}}".format(datetime.datetime.now(), dt="%Y-%m-%d"),
"{:{oc}^10}".format("a", oc="=")
2. 后接 __format__ 预设
e.g.
class Wu(object):
    def __format__(self, format_spec):
        return format_spec * 2
'{:aa}'.format(Wu())

".": 后接属性
e.g.
class Plant(object):
    tree = 't'
"{0.tree}".format(Plant())

"[]": 与字典及列表中的"[]"用法一致
"""

import datetime


class Data(object):
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


dd = dict(f='ffff', d='dddd', )

ll = [1, 2, 3, 4]


class Wu(object):
    def __format__(self, format_spec):
        return format_spec * 2


class Plant(object):
    tree = 't'


l = [
    '{2}{0}'.format(1, 2, 3),
    '{0!s}{0!r}{1!s}{1!r}'.format(Data, Data()),
    '{!s}'.format(Data()),

    '{0:10}|{0:_<10}|{0:=>10.3}|{0:^10}'.format('test'),

    '{0:f}'.format(3.1415926),
    '{0:<10d}|{0:_<10d}|{0:=>10d}|{0:^10d}'.format(1234),
    '{0:<10.2f}|{0:0<10.3f}|{0:+>10.30f}|{0:^10f}'.format(3.1415926),
    '{0:+d}|{0:->5d}|{0: d}'.format(1234),
    '{:-d}'.format(-1234),

    '{f} {d}'.format(**dd),
    '{f} {d}'.format(f='ffff', d='dddd', ),
    '{a[f]} {a[d]}'.format(a=dd),
    '{0[f]} {0[d]}'.format(dd),
    '{0[1]} {0[2]}'.format(ll),

    '{:{dt} {mt}}'.format(datetime.datetime.now(), dt='%Y-%m-%d', mt='%H-%m'),
    '{:%Y-%m-%d %H-%M}'.format(datetime.datetime.now(), dt='%Y-%m-%d', mt='%H-%m'),
    '{0:.{b}f}|{0:{c}{d}}'.format(12.123456, a=10, b=5, c=10, d='.7'),
    '{0:.5f}|{0:10.7}'.format(12.123456),
    '{:aa}'.format(Wu()),

    '{p1.tree} {p2.tree}'.format(p1=Plant(), p2=Plant()),
    '{0.tree} {1.tree}'.format(Plant(), Plant()),

    "{:{dt}}".format(datetime.datetime.now(), dt="%Y-%m-%d"),
    "{:{oc}^10}".format("a", oc="=")
]

for i in l:
    print(i)
