import multiprocessing
import time


def request_url(query_url):
    time.sleep(3)


if __name__ == '__main__':
    url_list = ["abc.com", "xyz.com"]
    task_list = [multiprocessing.Process(target=request_url, args=(url,)) for url in url_list]
    [task.start() for task in task_list]
    [task.join() for task in task_list]
