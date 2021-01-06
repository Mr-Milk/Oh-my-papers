import re
from typing import Optional
from urllib.parse import urlparse
from pathlib import Path
from papers.errors import DOIFormatIncorrect

# This is a very board DOI regexp
# Crossref has a blog https://www.crossref.org/blog/dois-and-matching-regular-expressions/
DOI_REGEX = r'10.\d{4,7}/.+'


def doi_validator(doi: str) -> str:
    if isinstance(doi, str):
        raise TypeError(f"DOI should be a str, bad input: {doi}")
    result = re.search(DOI_REGEX, doi)
    if result is None:
        raise DOIFormatIncorrect("Please check your DOI format")
    doi = result.group()
    return doi


def crossref_doi_validator():
    pass


def download_url_guard(url: str) -> (str, str):
    p = urlparse(url)
    filename = Path(p.path).parts[-1]
    url = f"{p.scheme}://{p.netloc}/{p.path}"
    return url, filename
