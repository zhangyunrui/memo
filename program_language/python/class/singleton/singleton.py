"""
metaclass is the class of a class. Like a class defines how
an instance behaves, a metaclass defines how a class behaves.
A class is an instance of a metaclass.

py3
"""

class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print('creating Spam')

    @staticmethod
    def static_grok():
        print('Spam.static.grok')
        
    @classmethod
    def class_grok(cls):
        print('Spam.class.grok')

a = Spam()
b = Spam()
print(a is b)
