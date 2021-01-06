from .base import doi_validator, request_get, request_async, CrossrefHeader
from .paper import Paper, Papers
from .config import Config
from typing import Union, Optional, List, Tuple

from .base import CrossrefDOIRecord
from .paper import Papers

CROSSREF_WORKS_URL = "https://api.crossref.org/works/"


def search(
        doi: Union[List[str], str, None] = None,
        keywords: Union[List[str], str, None] = None,
        year: Union[Tuple[int], int, None] = None,
        publisher: Union[List[str], str, None] = None,
        author: Union[List[str], str, None] = None,
        people: Union[List[str], str, None] = None,
        affiliation: Union[List[str], str, None] = None,
        my_email: Optional[str] = None,
        token: Optional[str] = None
) -> Union[Paper, Papers]:
    if my_email is None:
        my_email = Config.email
    if token is None:
        token = Config.token
    headers = CrossrefHeader(email=my_email, token=token).header


def search_doi(doi: Union[List[str], str]):
    if isinstance(doi, str):
        doi = doi_validator(doi)
        url = f"{CROSSREF_WORKS_URL}{doi}"
        p = CrossrefDOIRecord.to_paper(request_get(url)['message'])
        return p
    else:
        doi = [doi_validator(i) for i in doi]
        urls = [f"{CROSSREF_WORKS_URL}{i}" for i in doi]
        results = request_async(urls)
        papers = [CrossrefDOIRecord.to_paper(obj['message']) for obj in results]
        return Papers(papers)


def search_keywords(
        keywords: Union[List[str], str],
):
    pass
