# coding: utf8
"""
"balance += 5"在 cpu 中的计算过程是：
x = balance + 5
balance = x

而两个线程会随机交替执行，很有可能出现下列情况：
期望情况：
线程1：
x1 = balance + 5
balance = x1
线程2
x2 = balance + 8
balance = x2
意外情况：
线程2的两句被插入了线程1的两句中间

结论：需要用 lock.acquire() 和 lock.release() 获取和释放锁
"""
import threading

balance = 0
lock = threading.Lock()


def modify_balance(n):
    global balance
    balance += n
    balance -= n


# 无锁版本
# def run(n):
#     for i in range(1000000):
#         modify_balance(n)

def run(n):
    for i in range(1000000):
        lock.acquire()
        try:
            modify_balance(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run, args=(5,))
t2 = threading.Thread(target=run, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
