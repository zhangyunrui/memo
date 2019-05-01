import Queue

import MySQLdb


class PooledConnection(object):
    def __init__(self, pool, conn):
        self._pool = pool
        self._conn = conn

    def __getattr__(self, item):
        return getattr(self, item)

    def release(self):
        return self._pool.release()

    def __enter__(self):
        if self.autocommit():
            self.begin()
        return self.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                self.rollback()
            else:
                self.commit()
        finally:
            self.release()


class Pool(object):
    def __init__(self, creator, max_size=1, **kwargs):
        assert callable(creator)
        self._creator = creator
        self._pool = Queue.Queue(maxsize=max_size)
        self.__kwargs = kwargs
        for _ in range(max_size):
            conn = PooledConnection(self, self._creator(**self.__kwargs))
            self._pool.put(conn)

    def connection(self):
        conn = self._pool.get(timeout=3)
        try:
            try:
                conn.ping()
            except:
                conn.ping(True)
        except:
            conn = self._creator(**self.__kwargs)
        return conn

    def release(self, conn):
        self._pool.put(conn)


class MysqlDBPool(Pool):
    def __init__(self, **kwargs):
        kwargs.setdefault("cursorclass", MySQLdb.cursors.DictCursor)
        kwargs.setdefault("charset", "utf8")
        super(MysqlDBPool, self).__init__(MySQLdb.connect, **kwargs)
