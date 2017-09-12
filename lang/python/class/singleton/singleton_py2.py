# py2
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        # super(Singleton, self).__init__(*args, **kwargs)
        type.__init__(self, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            # self.__instance = super(Singleton, self).__call__(*args, **kwargs)
            self.__instance = type.__call__(self, *args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class spam():
    __metaclass__ = Singleton

    def __init__(self):
        print('creating spam')


a = spam()
b = spam()
print(a is b)
