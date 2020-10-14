import requests
import json
import re

from .result import QueryResult
from .errors import BadRequestError


def doi(doi: str):
    # using f-string
    an = re.search('10[.][0-9]{4,}[^\s"/<>]*/[^\s"<>]+', doi)

    if not an:
        raise BadRequestError("Wrong Doi format.")

    url = f"https://api.crossref.org/works/{doi}"
    request = requests.get(url)



    # you should handle error here, this is not enough
    if request.status_code == 404:
        raise BadRequestError("Get 404 from server.")

    result = json.loads(request.text)

    # the result is return as a class to store as many information as we can
    meta = QueryResult()
    meta.title = result['message']['title']
    meta.author = result['message']['author']
    meta.URL = result['message']['URL']
    meta.references_count = result['message']['references-count']



    return meta
