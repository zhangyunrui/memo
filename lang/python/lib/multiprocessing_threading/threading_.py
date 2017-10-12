# coding: utf8
"""
关键点：当前线程 join 之后的代码要等此线程执行完之后再执行
"""
import time, threading


def loop(a):
    print("%s is running ..." % threading.currentThread().name)
    for i in range(5):
        print("%s -> %s -> %s" % (threading.currentThread().name, i, a))
        time.sleep(0.5)
    print("%s is end." % threading.currentThread().name)


if __name__ == '__main__':
    print("%s is running ..." % threading.currentThread().name)
    t = threading.Thread(target=loop, name='LoopThread', args=('a',))
    t.start()
    print("%s is stated." % t.getName())
    t.join()
    print("%s is end." % threading.currentThread().name)
