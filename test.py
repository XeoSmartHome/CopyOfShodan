import time
import asyncio
import requests
import aiohttp

from types import SimpleNamespace

durations = []


def timed(func):
    """
    records approximate durations of function calls
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'{func.__name__:<30} started')
        result = func(*args, **kwargs)
        duration = f'{func.__name__:<30} finished in {time.time() - start:.2f} seconds'
        print(duration)
        durations.append(duration)
        return result

    return wrapper


@timed
def async_requests_get_all(urls):
    """
    asynchronous wrapper around synchronous requests
    """
    loop = asyncio.get_event_loop()
    # use session to reduce network overhead
    session = requests.Session()

    async def async_get(url):
        return session.get(url)

    async_tasks = [loop.create_task(async_get(url)) for url in urls]
    return loop.run_until_complete(asyncio.gather(*async_tasks))


def test_speed(domain: str):
    urls = [domain] * 1
    async_requests_get_all(urls)
    print('----------------------')


test_speed('https://xeosmarthome.com')
test_speed('https://heimdallr.ro')
