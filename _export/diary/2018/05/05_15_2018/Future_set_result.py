import time
import uuid
from random import randint

from tornado import gen
from tornado.concurrent import Future

waiting_list = {}


@gen.coroutine
def main():
    req_id = uuid.uuid4().hex
    while True:
        future = Future()
        waiting_list.update({req_id: future})
        rand_sleep(req_id)
        try:
            result = yield gen.with_timeout(1, future)
            print(result)
        except gen.TimeoutError as e:
            waiting_list.pop(req_id, None)
            result = "timeout: {}".format(req_id)
        break
    print(result)


@gen.coroutine
def rand_sleep(req_id):
    # gen.sleep(randint(2, 3))
    time.sleep(randint(2, 3))
    future = waiting_list.pop(req_id, None)
    if future:
        future.set_result()


if __name__ == '__main__':
    main()
