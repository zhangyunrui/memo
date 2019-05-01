from tornado.concurrent import futures
import requests

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

def load_url(url, timeout):
    return requests.get(url, timeout=timeout).text

def main():
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = dict(
            (executor.submit(load_url, url, 60), url)
             for url in URLS)

        for future in futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                print('%r page is %d bytes' % (
                          url, len(future.result())))
            except Exception as e:
                print('%r generated an exception: %s' % (
                          url, e))

if __name__ == '__main__':
    main()