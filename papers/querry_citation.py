import requests
import json
import re

from .result import CitationResult
from .errors import BadRequestError



def doi_2(doi: str):
    # using f-string
    an = re.search('10[.][0-9]{4,}[^\s"/<>]*/[^\s"<>]+', doi)

    if not an:
        raise BadRequestError("Wrong Doi format.")

    url = f"http://api.citeas.org/product/http://doi.org/{doi}"
    request = requests.get(url)

    if request.status_code == 404:
        raise BadRequestError("Get 404 from server.")

    result = json.loads(request.text)

    meta = CitationResult()

    meta.citation_apa = result['citations'][0]
    meta.citation_harvard = result['citations'][1]
    meta.citation_nature = result['citations'][2]
    meta.citation_modern = result['citations'][3]
    meta.citation_chicago = result['citations'][4]
    meta.citation_vancouver = result['citations'][5]

    return meta