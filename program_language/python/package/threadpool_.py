# coding: utf-8
"""
threadpool 是线程池，可以方便的在线程间共享数据
"""
import time
from threadpool import makeRequests, ThreadPool, NoResultsPending

_list = []


def func(a):
    print(a)
    _list.append(a)


def main():
    main = ThreadPool(3)
    requests = makeRequests(func, range(8))
    for r in requests:
        main.putRequest(r)
    while True:
        try:
            time.sleep(0.5)
            print('main poll ...')
            main.poll()
        except KeyboardInterrupt:
            break
        except NoResultsPending:
            print("NoResultsPending")
            break
    if main.dismissedWorkers:
        main.joinAllDismissedWorkers()
    print(_list)


if __name__ == '__main__':
    main()
