# SINGLETON
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if getattr(cls, '_instance', None) is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class Base(object):
    pass
    
class M(six.with_metaclass(Singleton, Base)):
    pass

# TRANSACTION
class Transaction(object):
    def __init__(self, db_conn):
        self.conn = self.db_conn

    def __enter__(self):
        self.conn.excute("START TRANSACTION")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.excute("ROLLBACK")
            logger.exception("failed transaction (%s): %s", exc_val, exc_tb)
            return False
        else:
            self.conn.excute("COMMIT")
            return True

from contextlib import contextmanager
import torndb

class hykuConnection(torndb.Connection):
    @contextmanager
    def transaction(self):
        self._ensure_connected()
        self._db.begin()

        try:
            cursor = self._db.cursor()
            yield cursor
            cursor.commit()
        except Exception:
            self._db.rollback()
            _logger.exception("failed transaction")
            raise


################### metaclass conflict #####################
class MA(type):
    pass

class MB(type):
    pass

class A(object):
    __metaclass__=MA

class B(object):
    __metaclass__=MB

# metaclass occur
class C(A, B):
    pass
TypeError: Error when calling the metaclass bases
    metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases

# avoid metaclass
class MAMB(MA, MB):
    pass

class C(MAMB):
    pass


######################### ABCMeta ###########################
from abc import ABCMeta, abstractmethod

class Base(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

    # we forget to declare `bar`

Concrete()
TypeError: Can't instantiate abstract class Concrete with abstract methods bar
