from .base import doi_validator, request, request_async
from papers.result import Paper

# 这是一个常量，所以我们把他移出来，方便以后修改
# 常量的变量名全大写字母
CROSSREF_WORKS_URL = "https://api.crossref.org/works/"


def doi(DOI: str):
    """Get metadata of an article by doi

    Args:
        DOI: a doi string
    """
    DOI = doi_validator(DOI)

    url = f"{CROSSREF_WORKS_URL}{DOI}"

    result = request(url)

    meta = Paper()
    meta.raw = result
    meta.doi = DOI
    meta.title = result['message']['title']
    meta.author = result['message']['author']
    meta.URL = result['message']['URL']
    meta.references_count = result['message']['references-count']

    return meta
