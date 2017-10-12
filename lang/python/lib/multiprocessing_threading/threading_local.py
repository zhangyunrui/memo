# coding: utf8
"""
拥有本线程独享的变量，可以通过 threading.local() 来实现
"""
import threading

local_school = threading.local()


def school_name():
    print("%s, %s" % (threading.currentThread().name, local_school.name))


def run(name):
    local_school.name = name
    school_name()


t1 = threading.Thread(target=run, name="Thread-A", args=("Alice",))
t2 = threading.Thread(target=run, name="Thread-B", args=("Bob",))
t1.start()
t2.start()
t1.join()
t2.join()
