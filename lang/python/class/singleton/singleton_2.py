# py2
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if '_instance' not in vars(cls):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class spam(Singleton):
    def __init__(self):
        print('creating spam')


a = spam()
b = spam()
print(a is b)
