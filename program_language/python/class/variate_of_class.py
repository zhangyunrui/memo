"""
py2
"""

class Person(object):
    name = 'a'

p1 = Person()
p2 = Person()
p1.name = 'b'
print(p1.name)
print(p2.name)
print(Person.name)