import requests
import aiohttp
import asyncio
from typing import List

from papers.errors import RequestFailedError

# try import ujson for faster json serialization
try:
    import ujson as json
except ImportError:
    import json


async def fetch(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            response.raise_for_status()
        text = await response.text()
        return json.loads(text)


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
    return results


def request_async(urls: List[str]) -> List[dict]:
    loop = asyncio.get_event_loop()
    if loop.is_running():
        results = await fetch_all(urls)
    else:
        results = loop.run_until_complete(fetch_all(urls))
    return results


def request(urls: List[str]) -> List[dict]:
    """

    """
    results = []
    for url in urls:
        r = requests.get(url)

        if not r.ok:
            raise RequestFailedError(f"Request for {url} is failed.")

        results.append(json.loads(r.text))
    return results
