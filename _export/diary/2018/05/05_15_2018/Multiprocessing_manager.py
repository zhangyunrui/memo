import multiprocessing
import time


def request_url(query_url, result_dict):
    time.sleep(3)
    result_dict[query_url] = {}


if __name__ == '__main__':
    process_manager = multiprocessing.Manager()
    result_dict = process_manager.dict()
    url_list = ["baidu.com", "bing.com"]
    task_list = [multiprocessing.Process(target=request_url, args=(url, result_dict)) for url in url_list]
    [task.start() for task in task_list]
    [task.join() for task in task_list]
    print(result_dict)
