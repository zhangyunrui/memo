# -*- coding: utf-8 -*-
class Item(object):
    def __getitem__(self, item):
        print 'getitem'

    # def __getattribute__(self, item):
    #     print 'getattribute'

    def __getattr__(self, item):
        self.__dict__[item] = item
        print self.__getattribute__(item)

    def __get__(self, instance, owner):
        pass


item = Item()
item['a']
item.a
getattr(item, 'b')


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
