# coding: utf8
"""
在8核 CPU 上，CUP 占用率仅有 150%，没有 800%。开再多线程，也不会有质的改观。
因为 python 的线程虽然是真正的线程，但解释器执行代码时，有一个 GIL 锁：Global Interpreter Lock，任何 python 线程执行前，必须先获得 GIL 锁，每执行 100 条字节码，解释器就自动释放 GIL 锁，让别的线程有机会执行。可以用多进程来解决这个问题，但是要注意多进程不能共享变量。
"""
import threading, multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(multiprocessing.cpu_count()):
    # t = threading.Thread(target=loop)
    t = multiprocessing.Process(target=loop)
    t.start()
