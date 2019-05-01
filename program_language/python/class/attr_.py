# class B(object):
#     def c(self):
#         return "class_method"
#
# b = B()
# print(b.c)
# b.c = "instance_method"
# print(b.c)
# print(b.__dict__["c"])
# print(type(b).__dict__["c"])
#
#
#
# class D(property):
#     def c(self):
#         return "class_method"
#
# d = D()
# # d.c = 't'
# print(d.__get__(D))
#
# dict

class RevealAccess(object):
    """
    A data descriptor that sets and returns values
    normally and prints a message logging their access.
    """
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, instance, value):
        print 'Updating', self.name
        self.val = value

class MyClass(object):
    x = RevealAccess(10, "var 'x'")
    y = 5

m = MyClass()
print(m.x)
m.x = 20
print(m.x)
print(m.y)

