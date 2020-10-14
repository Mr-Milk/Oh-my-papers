import re
import requests
import json

from typing import Any

from .errors import RequestFailedError, DOIFormatIncorrect

DOI_REGEX = r'10.[0-9]{4,7}/.+'


# 这里我把处理request和验证DOI的逻辑分离了
# 可以思考一下这样子的好处

def request_parser(url: str) -> Any:
    # 这个地方出现的str和Any叫做类型注释type hint
    # 所有的函数都要标记好
    request = requests.get(url)

    if not request.ok:
        raise RequestFailedError(f"Request for {url} is failed.")

    result = json.loads(request.text)
    return result


def doi_validator(doi: str) -> str:
    result = re.search(DOI_REGEX, doi)
    if result is None:
        raise DOIFormatIncorrect("Please check your DOI")
    doi = result.group()

    return doi
