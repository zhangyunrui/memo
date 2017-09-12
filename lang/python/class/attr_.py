# -*- coding: utf-8 -*-
"""
取值顺序：
  1. __attribute__
  2. attribute from property
  3. __attr__
__getitem__ = item['a']
item.a = getattr(item, 'a')，会优先去找子类中的 __getattribute__，再去找子类中的 __getattr__，再去找父类中的 __getattribute__
setattr(item, 'a', 'a') =  item.__dict__['a'] = ['a']
"""


class Item(object):
    def __getitem__(self, item):
        print 'getitem'

    # def __getattribute__(self, item):
    #     print 'father_getattribute'

    @property
    def father_getattribute(self):
        print "father_getattribute"

    def __getattr__(self, item):
        self.__dict__[item] = item
        print "{:=^50}".format(self.__getattribute__(item))

    def __get__(self, instance, owner):
        pass


item = Item()
item['a']
item.a
getattr(item, 'b')


class II(Item):
    def __getattribute__(self, item):
        print "child_real_getattribute"

    def __getattr__(self, item):
        print "child_getattr"

    @property
    def child_getattribute(self):
        print "child_getattribute"


ii = II()
ii.child_getattribute
ii.a
ii.father_getattribute


class Ts(object):
    def __getattr__(self, item):
        return item

    def __getattribute__(self, item):
        return item + '***'

    def __get__(self, instance, owner):
        print '__get__', instance, owner
        return self

    def __call__(self, *args, **kwargs):
        print '__call__', self
        return self


class TTs(object):
    t = Ts()  # t作为TTs的属性


t = Ts()
print t.y
print t.name

t.name = 'JJJ'
print t.name

print t()
print '*' * 30
tts = TTs()
print tts.t
