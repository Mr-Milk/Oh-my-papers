import requests
import aiohttp
import asyncio
from typing import List

from papers.errors import RequestFailedError
from .utils import JsonEncoder


async def fetch(session, url, **kwargs):
    async with session.get(url, **kwargs) as response:
        if response.status != 200:
            response.raise_for_status()
        text = await response.text()
        return JsonEncoder(text)


async def fetch_all(urls, **kwargs):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch(session, url, **kwargs))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
    return results


def request_async(urls: List[str], **kwargs) -> List[dict]:
    loop = asyncio.get_event_loop()
    if loop.is_running():
        results = await fetch_all(urls, **kwargs)
    else:
        results = loop.run_until_complete(fetch_all(urls, **kwargs))
    return results


def request_get(url, **kwargs) -> dict:
    r = requests.get(url, **kwargs)
    if not r.ok:
        raise RequestFailedError(f"Request for {url} failed.")
    return JsonEncoder(r.text)


def requests(urls: List[str], **kwargs) -> List[dict]:
    """

    """
    results = [request_get(url, **kwargs) for url in urls]
    return results
